from lmnr_flow import Flow, TaskOutput, Context

def parameterized_task(context: Context) -> TaskOutput:
    name = context.get("user_name")
    return TaskOutput(output=f"Hello {name}!")

flow = Flow()
flow.add_task("greet", parameterized_task)
result = flow.run("greet", inputs={"user_name": "Alice"})
# Returns {"greet": "Hello Alice!"}
