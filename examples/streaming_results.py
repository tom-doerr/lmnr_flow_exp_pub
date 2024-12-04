from lmnr_flow import Flow, TaskOutput, Context, StreamChunk

def streaming_task(context: Context) -> TaskOutput:
    # Stream intermediate results
    stream = context.get_stream()
    for i in range(3):
        # (task_id, chunk_value)
        stream.put(StreamChunk("streaming_task", f"interim_{i}"))
    return TaskOutput(output="final")

flow = Flow()
flow.add_task("streaming_task", streaming_task)

# Get results as they arrive
for task_id, output in flow.stream("streaming_task"):
    print(f"{task_id}: {output}")
    # Prints:
    # streaming_task: interim_0
    # streaming_task: interim_1
    # streaming_task: interim_2
    # streaming_task: final
