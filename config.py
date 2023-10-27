# 설정 관련
from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")

API_KEY = config("API_KEY", default="")