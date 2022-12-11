from fastapi import APIRouter, Request, status
from .utils import get_logger
from .schemas import Job

logger = get_logger(__name__)


class JobNotFound(Exception):
    pass


def get_jobs_router() -> APIRouter:
    """Generate a router with the scheduler routes."""
    router = APIRouter()

    @router.post("", name="scheduler:add_job", status_code=status.HTTP_201_CREATED)
    async def add_job(request: Request, job: Job):
        job = request.app.state.scheduler.add_job(**job.dict())
        return {"job": f"{job.id}"}

    @router.get("", name="scheduler:get_jobs", response_model=list)
    async def get_jobs(request: Request):
        jobs = request.app.state.scheduler.get_jobs()
        jobs = [
            dict((k, v) for k, v in job.__getstate__().items() if k != "trigger")
            for job in jobs
        ]
        return jobs

    @router.delete("/{job_id}", name="scheduler:remove_job")
    async def remove_job(request: Request, job_id: str):
        try:
            deleted = request.app.state.scheduler.remove_job(job_id=job_id)
            logger.debug(f"Job {job_id} deleted: {deleted}")
            return {"job": f"{job_id}"}
        except AttributeError:
            raise JobNotFound(f"No job by the id of {job_id} was found")

    return router
