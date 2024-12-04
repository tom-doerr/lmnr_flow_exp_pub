import time
from lmnr_flow import Flow, TaskOutput, NextTask, Context

def starter(context: Context) -> TaskOutput:
    # Launch multiple tasks in parallel by simply adding them to the next_tasks list
    return TaskOutput(output="started", [NextTask("slow_task1"), NextTask("slow_task2")])

def slow_task1(context: Context) -> TaskOutput:
    time.sleep(1)
    return TaskOutput(output="result1")

def slow_task2(context: Context) -> TaskOutput:
    time.sleep(1)
    return TaskOutput(output="result2")

flow = Flow()
flow.add_task("starter", starter)
flow.add_task("slow_task1", slow_task1)
flow.add_task("slow_task2", slow_task2)
flow.run("starter")
