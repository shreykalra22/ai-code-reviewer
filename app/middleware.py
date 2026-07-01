import time

from fastapi import Request

from app.logger import logger


async def log_requests(request: Request, call_next):

    start_time = time.time()

    logger.info(
        f"Started {request.method} {request.url.path}"
    )

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"Completed {request.method} {request.url.path} "
        f"Status={response.status_code} "
        f"Time={process_time:.4f}s"
    )

    return response