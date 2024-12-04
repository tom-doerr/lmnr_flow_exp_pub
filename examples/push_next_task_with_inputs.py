from lmnr_flow import Flow, TaskOutput, NextTask, Context

def task1(ctx):
    return TaskOutput("result1", [NextTask("task2", inputs={"input1": "value1"})])

# task2 will be called with inputs={"input1": "value1"}
def task2(ctx, inputs):
    assert inputs == {"input1": "value1"}
    return TaskOutput("result2")

flow = Flow()
flow.add_task("task1", task1)
flow.add_task("task2", task2)
result = flow.run("task1")
# Returns {"task2": "result2"}
