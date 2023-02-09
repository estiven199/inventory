import os
import pytest
from  api.api_v1.endpoints.events import router
from fastapi.testclient import TestClient
from fastapi import HTTPException

