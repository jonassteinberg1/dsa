""""
Problem:
Design and implement a job scheduler that supports:

Delayed execution: jobs can be scheduled to run N seconds in the future.

Recurring execution: jobs can be scheduled to repeat every N seconds.

Cancellation: jobs can be cancelled before they run.

Concurrency-safe: supports multiple workers processing jobs in memory safely.

Constraints:

Jobs are in-memory only (no persistence needed).

Each job is a function (e.g., () => void) passed to the scheduler.

You should provide an API to schedule, cancel, and list jobs.

Recurring jobs should continue running until explicitly cancelled.

Example Usage:

python
Copy
Edit
scheduler.schedule(job_id="foo", fn=print_hello, delay=10)         # Runs once in 10s  
scheduler.schedule(job_id="bar", fn=check_status, interval=5)      # Runs every 5s  
scheduler.cancel(job_id="bar")                                     # Stops recurring job  
Implement this in a single-threaded or multi-threaded model—your choice.
"""

import asyncio
import heapq
import sys

# imagine as an api call
async def job(name: str, interval: int = 0, delay: int = 0) -> tuple
    """
    name: name of the job
    interval: job repeats every "interval" seconds; conflicts with "delay"
    delay: job runs "delay" seconds in the future; conflicts with "interval"
    """

    if not isinstance(name, str):
        print("name must be a string")
        sys.exit(7)
        if len(name) > 32:
            print("name must be 32 characters or less")
            sys.exit(8)
    
    if (interval > 0) and (delay > 0):
        print("interval and delay cannot be used together")
        sys.exit(9)
    
    if interval < 0:
        print("interval must be greater than 0")
        sys.exit(10)
    
    if delay < 0:
        print("delay must be greater than 0")
        sys.exit(11)
    
    heapq.heappush(job_queue, (name, interval, delay))
    



    

job_queue = []

async def main():


