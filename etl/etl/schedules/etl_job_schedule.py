from dagster import schedule

from etl.jobs.run_etl import etl


@schedule(cron_schedule="0 10 * * *", job=etl, execution_timezone="US/Central")
def etl_job_schedule(_context):
    run_config = {}
    return run_config
