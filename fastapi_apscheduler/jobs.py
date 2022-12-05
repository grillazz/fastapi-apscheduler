from fastapi import APIRouter, Request, status


def get_users_router() -> APIRouter:
    """Generate a router with the scheduler routes."""
    router = APIRouter()

    @router.post("", name="scheduler:add_job", status_code=status.HTTP_201_CREATED)
    async def add_job(request: Request, job: dict):
        job = request.app.state.scheduler.add_job(**job)
        return {"job": f"{job.id}"}

    @router.get("", name="scheduler:get_jobs", response_model=list)
    async def get_jobs(request: Request):
        jobs = request.app.state.scheduler.get_jobs()
        jobs = [
            dict((k, v) for k, v in job.__getstate__().items() if k != "trigger")
            for job in jobs
        ]
        return jobs

    return router
