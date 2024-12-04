from concurrent.futures import ThreadPoolExecutor
from lmnr_flow import Flow, TaskOutput, NextTask, Context, StreamChunk

# thread pool executor is optional, defaults to 4 workers
flow = Flow(thread_pool_executor=ThreadPoolExecutor(max_workers=4))

# Simple task that returns a result
def my_task(context: Context) -> TaskOutput:
    return TaskOutput(output="Hello World!")

flow.add_task("greet", my_task)
result = flow.run("greet")  # Returns {"greet": "Hello World!"}
