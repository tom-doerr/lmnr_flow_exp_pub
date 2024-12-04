from typing import List
import json
from lmnr_flow import Flow, TaskOutput, NextTask, Context

def llm_agent(context: Context) -> TaskOutput:
    # Simulated LLM response that determines which tools to use
    prompt = context.get("user_input")
    llm_response = {
        "reasoning": "Need to search database and format results",
        "tools": ["search_db", "format_results"]
    }
    
    # Schedule the selected tools in sequence
    next_tasks: List[NextTask] = []
    for tool in llm_response["tools"]:
        next_tasks.append(NextTask(tool))
    
    return TaskOutput(output=llm_response["reasoning"], next_tasks)

def search_db(context: Context) -> TaskOutput:
    # Simulate database search
    results = ["result1", "result2"]
    return TaskOutput(output=results)

def format_results(context: Context) -> TaskOutput:
    # Format results from previous task
    search_results = context.get("search_db")
    formatted = json.dumps(search_results, indent=2)
    return TaskOutput(output=formatted)

# Set up the agent
flow = Flow()
flow.add_task("llm_agent", llm_agent)
flow.add_tool("search_db", search_db)
flow.add_tool("format_results", format_results)

# Run the agent
result = flow.run("llm_agent", inputs={"user_input": "Find and format data"})
# Returns the final formatted results
