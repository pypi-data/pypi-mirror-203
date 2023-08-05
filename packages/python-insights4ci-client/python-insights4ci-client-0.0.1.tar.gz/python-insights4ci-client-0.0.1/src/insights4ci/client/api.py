# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; specifically version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Authors: Beraldo Leal <bleal@redhat.com>

import requests
import logging

LOG = logging.getLogger('insights4ci.client.api')


class Insights4CIClient:
    def __init__(self, url, auth=None):
        self.url = url.strip('/')
        self.auth = auth

    def _request(self, method, endpoint, params=None, data=None, json=None):
        url = self.url + endpoint
        response = method(url, params=params, data=data, json=json)
        # pylint: disable=no-member
        if response.status_code != requests.codes.ok:
            LOG.error(f"Failed requesting {endpoint}:")
            LOG.error(response)
            response.raise_for_status()
        return response.json()

    def get(self, endpoint, params=None, data=None):
        return self._request(requests.get,
                             endpoint,
                             params=params,
                             data=data)

    def post(self, endpoint, params=None, data=None, json=None):
        return self._request(requests.post, endpoint,
                             params=params, data=data, json=json)


class I4CBaseEndpoint:
    ENDPOINT = None

    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.data.get('id')

    @classmethod
    def get_all(cls, client, skip=0, limit=100):
        """List all objects."""
        params = {'skip': skip,
                  'limit': limit}
        endpoint = f"{cls.ENDPOINT}/"
        return [cls(data) for data in client.get(endpoint, params=params)]

    @classmethod
    def get_by_id(cls, client, object_id):
        """Get details about the object.

        TODO: Currently it is showing all runners, but should be limited to
        runners that user has access.
        """
        LOG.info(f"Getting object by id {object_id}...")
        data = client.get(f"{cls.ENDPOINT}/{object_id}")
        return cls(data)

    def post(self, client):
        """Register current data as a new object (POST).

        Please make sure your self.data has the right values for the object
        your posting. If you got any result from this API, most likely your
        post will fail because this object already exists.
        """
        LOG.info(f"Sending a new object ({self})...")
        self.data = client.post(f"{self.ENDPOINT}/", json=self.data)
        return self

    def as_dict(self):
        return {key: value for key, value in self.data.items()}


class Project(I4CBaseEndpoint):
    ENDPOINT = "/projects"

    def __str__(self):
        return f"Project: {self.id}"

    def get_pipelines(self, client, dt_from=None, dt_to=None, in_groups=None):
        """List the pipelines for this project."""
        endpoint = f"{self.ENDPOINT}/{self.id}/pipelines"
        params = {'dt_from': dt_from,
                  'dt_to': dt_to,
                  'in_groups': in_groups}
        return [Pipeline(self, data) for data in client.get(endpoint,
                                                            params=params)]

    def create_pipeline(self, client, pipeline):
        endpoint = f"{self.ENDPOINT}/{self.id}/pipelines"
        assert pipeline.project == self
        pipeline.data = client.post(endpoint, json=pipeline.data)
        return pipeline

    def get_pipeline_by_id(self, client, pipeline_id):
        """Get details about a specific pipeline."""
        endpoint = f"{self.ENDPOINT}/{self.id}/pipelines/{pipeline_id}"
        return Pipeline(self, client.get(endpoint))

    def get_latest_pipeline(self, client):
        """Get details about the latest pipeline."""
        endpoint = f"{self.ENDPOINT}/{self.id}/pipelines?limit=1"
        try:
            data = client.get(endpoint)[0]
        except IndexError:
            return None
        return Pipeline(self, data)

    def create_job(self, client, pipeline, job):
        endpoint = f"{self.ENDPOINT}/{self.id}/pipelines/{pipeline.id}/jobs"
        assert pipeline.project == self
        return client.post(endpoint, json=job.data)

    def create_test_result(self, client, test_result):
        job = test_result.job
        assert job.pipeline.project == self
        endpoint = f"{self.ENDPOINT}/{self.id}/jobs/{job.id}/testresult"
        return client.post(endpoint, jsob=test_result.data)


class Runner(I4CBaseEndpoint):
    ENDPOINT = "/runners"

    def __str__(self):
        return f"Runner: {self.id}"


class Pipeline:
    """Just a dummy Pipeline object.

    This is not an I4CBaseEndpoint, since it is part of a project.
    """

    def __init__(self, project, data):
        self.project = project
        self.data = data

    def __str__(self):
        return f"Pipeline: {self.id}"

    @property
    def id(self):
        return self.data.get('id')

    @property
    def external_id(self):
        return self.data.get('external_id')

    @property
    def created_at(self):
        return self.data.get('created_at')

    def post(self, client):
        LOG.info(f"Creating pipeline for {self.project}...")
        return self.project.create_pipeline(client, self)

    def create_job(self, client, job):
        assert job.pipeline == self
        return self.project.create_job(client, self, job)

    def create_test_result(self, client, test_result):
        assert test_result.job.pipeline == self
        return self.project.create_test_result(client, test_result)


class Job:
    def __init__(self, pipeline, data):
        self.pipeline = pipeline
        self.data = data

    def __str__(self):
        return f"Job: {self.id}"

    @property
    def id(self):
        return self.data.get('id')

    def post(self, client):
        LOG.info(f"Creating job for {self.pipeline}...")
        return self.pipeline.create_job(client, self)

    def create_test_result(self, client, test_result):
        assert test_result.job == self
        return self.pipeline.create_test_result(client, test_result)


class TestResult:
    def __init__(self, job, data):
        self.job = job
        self.data = data

    def __str__(self):
        return f"TestResult: {self.id}"

    @property
    def id(self):
        return self.data.get('id')

    def post(self, client):
        LOG.info(f"Creating test result for {self.job}...")
        self.job.create_test_result(client, self)
