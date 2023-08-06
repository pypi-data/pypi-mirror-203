import copy
from typing import Optional, List, Tuple

from data_watch.api.service.group.view.model import GroupViewResponse
from data_watch.api.service.group.view.synchronous import (
    get_group_view_by_name,
    get_group_view,
)
from data_watch.api.service.job import create_job, update_job
from data_watch.api.service.job.model import JobRequest, JobResponse
from data_watch.common.enum import Status


def get_group(
    group_name: Optional[str] = None, group_id: Optional[str] = None
) -> GroupViewResponse:
    """
    Helper method for getting the group of rules from the group_id or group_name.

    NOTE: You must provide the group_name or group_id but not both.

    Args:
        group_name (Optional[str]): The name of rule group
        group_id (Optional[str]): The id of the rule group

    Returns:
        GroupViewResponse: The view of the group associated with the group_id/group_name
    """
    if not ((group_name is None) ^ (group_id is None)):
        raise ValueError(f"You must supply group_id or group_name and only one of them")

    if group_id is not None and group_name is None:
        response = get_group_view(group_id)
    else:
        response = get_group_view_by_name(group_name)
    return GroupViewResponse(**response)


def start_job(
    job_name: str,
    *,
    group_name: Optional[str] = None,
    group_id: Optional[str] = None,
    metadata: Optional[dict] = None,
    tags: Optional[List[str]] = None,
) -> Tuple[JobResponse, GroupViewResponse]:
    """
    Creates the job with the starting information.

    NOTE: You must provide the group_name or group_id but not both.

    Args:
        job_name (str): Name assigned to the job created from running this pipeline
        group_name (Optional[str]): The name of rule group run on the pipeline
        group_id (Optional[str]): The id of the rule group run on the pipeline
        metadata (Optional[dict]): Metadata added to the job information
        tags (Optional[List[str]]): Tags added to the job

    Returns:
        Tuple[JobResponse, GroupViewResponse]: The created job and the group used in the job
    """
    group = get_group(group_name=group_name, group_id=group_id)
    request = JobRequest(
        name=job_name,
        status=Status.IN_PROGRESS,
        group_id=group.id,
        metadata=metadata,
        tags=tags,
    )
    response = create_job(request)
    job = JobResponse(**response)
    return job, group


def stop_job(
    job: JobResponse,
    status: Status,
    *,
    start_time: int,
    end_time: int,
    metadata: Optional[dict] = None,
    tags: Optional[List[str]] = None,
) -> JobResponse:
    """
    Stops the job and updates it with all the results.

    Args:
        job (JobResponse): The job being updated
        status (Status): The status of the job
        start_time (int): The timestamp from when the job started
        end_time (int): The timestamp from when the job ended
        metadata (Optional[dict]): Metadata added to the job information
        tags (Optional[List[str]]): Tags added to the job

    Returns:
        JobResponse: The updated job
    """
    combined_metadata = copy.deepcopy(job.metadata)
    combined_metadata.update(metadata)
    request = JobRequest(
        name=job.name,
        status=status,
        group_id=job.group_id,
        start_time=start_time,
        end_time=end_time,
        metadata=combined_metadata,
        tags=tags or job.tags,
    )
    response = update_job(job.id, request)
    job = JobResponse(**response)
    return job
