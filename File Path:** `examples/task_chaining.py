from lmnr_flow import Flow, TaskOutput, NextTask, Context

# Tasks can trigger other tasks
def task1(context: Context) -> TaskOutput:
    return TaskOutput(output="result1", [NextTask("task2")])

def task2(context: Context) -> TaskOutput:
    # Access results from previous tasks
    t1_result = context.get("task1")  # waits for task1 to complete
    return TaskOutput(output="result2")

flow = Flow()
flow.add_task("task1", task1)
flow.add_task("task2", task2)
flow.run("task1")  # Returns {"task2": "result2"}
