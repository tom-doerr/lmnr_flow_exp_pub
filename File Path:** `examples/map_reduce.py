from lmnr_flow import Flow, TaskOutput, NextTask, Context

def task1(ctx):
    ctx.set("collector", [])

    return TaskOutput("result1", [
        NextTask("task2", spawn_another=True),
        NextTask("task2", spawn_another=True),
        NextTask("task2", spawn_another=True)
    ])

def task2(ctx):
    collector = ctx.get("collector")
    collector.append("result2")
    ctx.set("collector", collector)

    return TaskOutput("", [NextTask("task3")])

def task3(ctx):
    collector = ctx.get("collector")
    return TaskOutput(collector)

flow = Flow()
flow.add_task("task1", task1)
flow.add_task("task2", task2)
flow.add_task("task3", task3)

result = flow.run("task1")
assert result == {"task3": ["result2", "result2", "result2"]}
