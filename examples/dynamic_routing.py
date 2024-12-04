from lmnr_flow import Flow, TaskOutput, NextTask, Context

def router(context: Context) -> TaskOutput:
    task_type = context.get("type")
    routes = {
        "process": [NextTask("process_task")],
        "analyze": [NextTask("analyze_task")],
        "report": [NextTask("report_task")]
    }
    return TaskOutput(f"routing to {task_type}", next_tasks=routes.get(task_type, []))

def process_task(context: Context) -> TaskOutput:
    return TaskOutput(output="processed data")

flow = Flow()
flow.add_task("router", router)
flow.add_task("process_task", process_task)
result = flow.run("router", inputs={"type": "process"})
# Returns {"process_task": "processed data"}
