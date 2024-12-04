from lmnr_flow import Flow, TaskOutput, NextTask, Context

def conditional_task(context: Context) -> TaskOutput:
    count = context.get("count", 0)
    
    if count >= 3:
        return TaskOutput(output="done")
    
    context.set("count", count + 1)
    return TaskOutput(f"iteration_{count}", next_tasks=[NextTask("conditional_task")])

flow = Flow()
flow.add_task("conditional_task", conditional_task)
flow.add_task("finish", lambda ctx: TaskOutput("completed", None))
flow.run("conditional_task")
