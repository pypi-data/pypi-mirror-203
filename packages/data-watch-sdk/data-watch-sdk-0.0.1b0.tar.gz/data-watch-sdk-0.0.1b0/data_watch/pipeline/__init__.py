import logging
from typing import Any, Optional, List
from data_watch.api.service.job.model import JobResponse
from data_watch.common.date.function import current_timestamp
from data_watch.pipeline.execution.synchronously import run_pipeline
from data_watch.pipeline.utils import (
    start_job,
    stop_job,
    async_start_job,
    async_stop_job,
)


logger = logging.getLogger(__name__)


def data_quality_pipeline(
    data: Any,
    job_name: str,
    *,
    group_name: Optional[str] = None,
    group_id: Optional[str] = None,
    metadata: Optional[dict] = None,
    tags: Optional[List[str]] = None,
    multi_processing: bool = False,
    processes: int = 5,
) -> JobResponse:
    """
    Runs data through a data quality pipeline.

    NOTE: You must provide the group name or group id for this method to run.
    NOTE: The number of rules run in parallel is dependent on the number of processes.

    Args:
        data (Any): Data that is run through the pipeline
        job_name (str): Name assigned to the job created from running this pipeline
        group_name (Optional[str]): The name of group run on the pipeline
        group_id (Optional[str]): The id of the group run on the pipeline
        metadata (Optional[dict]): Metadata added to the job information
        tags (Optional[List[str]]): Tags added to the job
        multi_processing (bool): Optional flag to run the rules over the data concurrently
        processes (int): Optional number of process to spin up when running the rules concurrently

    Returns:
        JobResponse: The job response with all the information from the run
    """
    job, group = start_job(
        job_name=job_name,
        group_name=group_name,
        group_id=group_id,
        metadata=metadata,
        tags=tags,
    )

    start_time = current_timestamp()
    logger.info(f"Starting data quality pipeline [{job_name=}, {start_time=}]")
    result = run_pipeline(
        data, group, multi_processing=multi_processing, processes=processes
    )
    end_time = current_timestamp()
    logger.debug(f"Data quality pipeline result: {result}")
    logger.info(
        f"Data quality pipeline finished [{job_name=}, {end_time=}]: {result.status}"
    )

    job = stop_job(
        job=job,
        status=result.status,
        start_time=start_time,
        end_time=end_time,
        metadata=result.metadata.request_dict(),
        tags=tags,
    )
    return job


async def async_data_quality_pipeline(
    data: Any,
    job_name: str,
    *,
    group_name: Optional[str] = None,
    group_id: Optional[str] = None,
    metadata: Optional[dict] = None,
    tags: Optional[List[str]] = None,
    multi_processing: bool = False,
    processes: int = 5,
) -> JobResponse:
    """
    Asynchronously runs data through a data quality pipeline.

    NOTE: You must provide the group name or group id for this method to run.
    NOTE: The number of rules run in parallel is dependent on the number of processes.

    Args:
        data (Any): Data that is run through the pipeline
        job_name (str): Name assigned to the job created from running this pipeline
        group_name (Optional[str]): The name of rule group run on the pipeline
        group_id (Optional[str]): The id of the rule group run on the pipeline
        metadata (Optional[dict]): Metadata added to the job information
        tags (Optional[List[str]]): Tags added to the job
        multi_processing (bool): Optional flag to run the rules over the data concurrently
        processes (int): Optional number of process to spin up when running the rules concurrently

    Returns:
        JobResponse: The job response with all the information from the run
    """
    job, group = await async_start_job(
        job_name=job_name,
        group_name=group_name,
        group_id=group_id,
        metadata=metadata,
        tags=tags,
    )

    start_time = current_timestamp()
    logger.info(f"Starting data quality pipeline [{job_name=}, {start_time=}]")
    result = run_pipeline(
        data, group, multi_processing=multi_processing, processes=processes
    )
    end_time = current_timestamp()
    logger.debug(f"Data quality pipeline result: {result}")
    logger.info(
        f"Data quality pipeline finished [{job_name=}, {end_time=}]: {result.status}"
    )

    job = await async_stop_job(
        job=job,
        status=result.status,
        start_time=start_time,
        end_time=end_time,
        metadata=result.metadata.request_dict(),
        tags=tags,
    )
    return job
