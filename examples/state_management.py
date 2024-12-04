from lmnr_flow import Flow, TaskOutput, Context

context = Context()
context.from_dict({"task1": "result1"})

flow = Flow(context=context)
flow.add_task("task2", lambda ctx: TaskOutput("result2"))
flow.run("task2")

assert flow.context.get("task1") == "result1" # True, because it was set in the context
assert flow.context.get("task2") == "result2"

# Serialize the context to a dictionary
flow.get_context().to_dict()
# Returns {"task1": "result1", "task2": "result2"}
