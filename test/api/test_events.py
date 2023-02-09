import os
import pytest
from  api.api_v1.endpoints.events import router
from fastapi.testclient import TestClient
from fastapi import HTTPException

client  = TestClient(router)

@pytest.mark.parametrize("env_vars", [{"SECRET": "ZQeOwY6pNusL_xnUV_2i2g5F6BhYFaoL4mt9pB5ANw8="}])
def test_create_event(env_vars) -> any:
    os.environ.update(env_vars)
    response = client.post(
        f"/events", headers={
                }
    )
    assert response.status_code == 400