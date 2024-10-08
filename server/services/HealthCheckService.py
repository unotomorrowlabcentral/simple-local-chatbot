import http
from fastapi import FastAPI


class HealthCheckService:

    @staticmethod
    async def healthCheck() -> dict:
        return {"status": http.HTTPStatus.OK}
