import os
import pytest
from api.api_v1.endpoints.login import router
from fastapi.testclient import TestClient
from fastapi import HTTPException

client = TestClient(router)


@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_login_access_token(env_vars) -> any:
    os.environ.update(env_vars)
    response = client.post(
        f"/login/access-token/", headers={
            'x-token': "gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
            'x-api-key': "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
            'x-secret-id': "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4=",
            'user-id': "gAAAAABj4_Pn_TGye9V3YWTRfJo1HZAGEWVHy98Bf1XihDY7orahtgr4uv8XVWTp7KiwSHGJxVE5Jy_aPzzds88EYkx_yH5tXg=="
        }
    )
    assert response.status_code == 200


def test_login_access_token_not_headers_x_token() -> any:
    with pytest.raises(HTTPException) as excinfo:
        client.post(
            f"/login/access-token/", headers={
                'x-api-key': "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
                'x-secret-id': "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4=",
                'user-id': "gAAAAABj4_Pn_TGye9V3YWTRfJo1HZAGEWVHy98Bf1XihDY7orahtgr4uv8XVWTp7KiwSHGJxVE5Jy_aPzzds88EYkx_yH5tXg=="
            })
    assert excinfo.value.status_code == 400


def test_generate_token_not_headers_x_api_key() -> any:
    with pytest.raises(HTTPException) as excinfo:
        client.post(
            f"/login/access-token/", headers={
                'x-token': "gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
                'x-secret-id': "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4=",
                'user-id': "gAAAAABj4_Pn_TGye9V3YWTRfJo1HZAGEWVHy98Bf1XihDY7orahtgr4uv8XVWTp7KiwSHGJxVE5Jy_aPzzds88EYkx_yH5tXg=="
            })
    assert excinfo.value.status_code == 400


def test_generate_token_not_headers_x_secret_id() -> any:
    with pytest.raises(HTTPException) as excinfo:
        client.post(
            f"/login/access-token/", headers={
                'x-token': "gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
                'x-api-key': "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
                'user-id': "gAAAAABj4_Pn_TGye9V3YWTRfJo1HZAGEWVHy98Bf1XihDY7orahtgr4uv8XVWTp7KiwSHGJxVE5Jy_aPzzds88EYkx_yH5tXg=="
            })
    assert excinfo.value.status_code == 400


def test_generate_token_not_headers_user_id() -> any:
    with pytest.raises(HTTPException) as excinfo:
        client.post(
            f"/login/access-token/", headers={
                'x-token': "gAAAAABjm11ka8Kh5AgxWxB12Awwh31fe83qGs1TLG5atIHFBBZmabjFufJ3-J1SIRkv2n2i3VwNXgqk3tbfzUznlQOF0xKErA==",
                'x-api-key': "gAAAAABjm4YLsCwWHqZXSNZr6PCEuBSIGChznJjWGWJSBJcwkCBENNM5gi0u791D773Rynov4T10LwwfAfM2cECzOJlkSK8bgehtmmdUAlSBy5a8N3HIl0w=",
                'x-secret-id': "gAAAAABjm120N7cjeEbPm48tI1kcfaxW9fuK2K1O56ylLBiXFyMQkKESnXgsKCmEs2qg3t2ACtmjtnavmg8K_t58PlsKfHZ2azWt5lrpqd0mlKkR-oFLBV4=",
            })
    assert excinfo.value.status_code == 400
