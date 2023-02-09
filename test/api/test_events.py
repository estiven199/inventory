import os
import pytest
from api.api_v1.endpoints.events import router
from fastapi.testclient import TestClient
from fastapi import HTTPException

client = TestClient(router)


@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_create_event_good(env_vars) -> any:
    os.environ.update(env_vars)

    response = client.post("/events/", 
        headers={
            'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwidXNlcl9pZCI6ImdBQUFBQUJqNF9Qbl9UR3llOVYzWVdUUmZKbzFIWkFHRVdWSHk5OEJmMVhpaERZN29yYWh0Z3I0dXY4WFZXVHA3S2l3U0hHSnhWRTVKeV9hUHp6ZHM4OEVZa3hfeUg1dFhnPT0iLCJleHAiOjE2NzY2NTUxNzR9.my31Vq4g3YzmvlGsr9ImwyTtsXMuqwl_Jng0aOZqxtc"},
        json={
            "name": "string",
            "type": "solicitud",
            "description": "string"
        })
    assert response.status_code == 200


@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_create_event(env_vars) -> any:
    os.environ.update(env_vars)
    with pytest.raises(HTTPException) as excinfo:
        client.post(
            f"/events/")
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Token field required."


@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_create_event_token(env_vars) -> any:
    os.environ.update(env_vars)
    with pytest.raises(HTTPException) as excinfo:
        client.post(f"/events/", headers={'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwidXNlcl9pZCI6ImdBQUFBQUJqNF9Qbl9UR3llOVYzWVdUUmZKbzFIWkFHRVdWSHk5OEJmMVhpaERZN29yYWh0Z3I0dXY4WFZXVHA3S2l3U0hHSnhWRTVKeV9hUHp6ZHM4OEVZa3hfeUg1dFhnPT0iLCJleHAiOjE2NzY2NDc0Nzh9.Hbr3k_s8qJ0EUTIQXnkYqLuystWGu5xwSqnP4g5kWEo"})
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "The json is required."


@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_create_event_bad_token(env_vars) -> any:
    os.environ.update(env_vars)
    with pytest.raises(HTTPException) as excinfo:
        client.post(f"/events/", headers={
            'token': "JhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ4X3Rva2VuIjoiZ0FBQUFBQmptMTFrYThLaDVBZ3hXeEIxMkF3d2gzMWZlODNxR3MxVExHNWF0SUhGQkJabWFiakZ1ZkozLUoxU0lSa3YybjJpM1Z3TlhncWszdGJmelV6bmxRT0YweEtFckE9PSIsInhfYXBpX2tleSI6ImdBQUFBQUJqbTRZTHNDd1dIcVpYU05acjZQQ0V1QlNJR0Noem5KaldHV0pTQkpjd2tDQkVOTk01Z2kwdTc5MUQ3NzNSeW5vdjRUMTBMd3dmQWZNMmNFQ3pPSmxrU0s4YmdlaHRtbWRVQWxTQnk1YThOM0hJbDB3PSIsInhfc2VjcmV0X2lkIjoiZ0FBQUFBQmptMTIwTjdjamVFYlBtNDh0STFrY2ZheFc5ZnVLMksxTzU2eWxMQmlYRnlNUWtLRVNuWGdzS0NtRXMycWczdDJBQ3RtanRuYXZtZzhLX3Q1OFBsc0tmSFoyYXpXdDVscnBxZDBtbEtrUi1vRkxCVjQ9IiwidXNlcl9pZCI6ImdBQUFBQUJqNF9Qbl9UR3llOVYzWVdUUmZKbzFIWkFHRVdWSHk5OEJmMVhpaERZN29yYWh0Z3I0dXY4WFZXVHA3S2l3U0hHSnhWRTVKeV9hUHp6ZHM4OEVZa3hfeUg1dFhnPT0iLCJleHAiOjE2NzY2NDc0Nzh9.Hbr3k_s8qJ0EUTIQXnkYqLuystWGu5xwSqnP4g5kWEo"},
            json={
            "name": "string",
            "type": "solicitud",
            "description": "string"
        })
    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "Invalid token."
