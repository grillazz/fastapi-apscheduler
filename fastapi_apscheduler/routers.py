from fastapi import APIRouter, Request, status
from .utils import get_logger
from .schemas import Job

logger = get_logger(__name__)


class JobNotFoundError(Exception):
    pass


def get_jobs_router() -> APIRouter:
    """
    Generate a router with the scheduler routes.

    Returns:
        APIRouter: The router with the defined routes for job scheduling.
    """
    router = APIRouter()

    @router.post("", name="scheduler:add_job", status_code=status.HTTP_201_CREATED)
    async def add_job(request: Request, job: Job):
        """
        Add a new job to the scheduler.

        Args:
            request (Request): The request object.
            job (Job): The job data to be added.

        Returns:
            dict: A dictionary containing the job ID.
        """
        job = request.app.scheduler.add_job(**job.model_dump())
        return {"job": f"{job.id}"}

    @router.get("", name="scheduler:get_jobs", response_model=list)
    async def get_jobs(request: Request):
        """
        Retrieve all jobs from the scheduler.

        Args:
            request (Request): The request object.

        Returns:
            list: A list of dictionaries representing the jobs.
        """
        jobs = request.state.scheduler.get_jobs()
        jobs = [{k: v for k, v in job.__getstate__().items() if k != "trigger"} for job in jobs]
        return jobs

    @router.delete("/{job_id}", name="scheduler:remove_job")
    async def remove_job(request: Request, job_id: str):
        """
        Remove a job from the scheduler by job ID.

        Args:
            request (Request): The request object.
            job_id (str): The ID of the job to be removed.

        Returns:
            dict: A dictionary containing the job ID of the removed job.

        Raises:
            JobNotFoundError: If no job with the given ID is found.
        """
        try:
            deleted = request.state.scheduler.remove_job(job_id=job_id)
            logger.debug(f"Job {job_id} deleted: {deleted}")
            return {"job": f"{job_id}"}
        except AttributeError as err:
            raise JobNotFoundError(f"No job by the id of {job_id} was found") from err

    return router
