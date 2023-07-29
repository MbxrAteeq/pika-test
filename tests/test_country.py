import json

import pytest
from fastapi import status
import responses

from helpers.constants import rest_countries_url
from tests.database import get_test_db
from tests.fake_data import countries_data


@pytest.fixture
def db_session():
    yield from get_test_db()


@responses.activate
def test_save_countries(db_session, client):
    responses.add(
        responses.POST,
        url=rest_countries_url,
        body=json.dumps(countries_data),
        status=200
    )

    response = client.post("/api/v1/country")

    assert response.status_code == status.HTTP_200_OK
