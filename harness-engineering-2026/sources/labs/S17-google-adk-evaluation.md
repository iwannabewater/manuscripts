---
source_url: https://google.github.io/adk-docs/evaluate/
fetched_for: learn/canonical-article
source_check_date: 2026-06-20
---

[fetch] tier=local status=ok extractor=stdlib hint="install readability-lxml + html2text for cleaner output"
# Why evaluate agents - Agent Development Kit (ADK)Agent Development Kit (ADK)

> Source: https://google.github.io/adk-docs/evaluate/

Skip to content

Why evaluate agents¶

Supported in ADKPython

In traditional software development, unit tests and integration tests provide confidence that code functions as expected and remains stable through changes. These tests provide a clear "pass/fail" signal, guiding further development. However, LLM agents introduce a level of variability that makes traditional testing approaches insufficient.

Due to the probabilistic nature of models, deterministic "pass/fail" assertions are often unsuitable for evaluating agent performance. Instead, we need qualitative evaluations of both the final output and the agent's trajectory - the sequence of steps taken to reach the solution. This involves assessing the quality of the agent's decisions, its reasoning process, and the final result.

This may seem like a lot of extra work to set up, but the investment of automating evaluations pays off quickly. If you intend to progress beyond prototype, this is a highly recommended best practice.

Prepare for agent evaluations¶

Before automating agent evaluations, define clear objectives and success criteria:

Define Success: What constitutes a successful outcome for your agent?

Identify Critical Tasks: What are the essential tasks your agent must accomplish?

Choose Relevant Metrics: What metrics will you track to measure performance?

These considerations will guide the creation of evaluation scenarios and enable effective monitoring of agent behavior in real-world deployments.

What to evaluate?¶

To bridge the gap between a proof-of-concept and a production-ready AI agent, a robust and automated evaluation framework is essential. Unlike evaluating generative models, where the focus is primarily on the final output, agent evaluation requires a deeper understanding of the decision-making process. Agent evaluation can be broken down into two components:

Evaluate Trajectory and Tool Use: Analyzing the steps an agent takes to reach a solution, including its choice of tools, strategies, and the efficiency of its approach.

Evaluate the Final Response: Assessing the quality, relevance, and correctness of the agent's final output.

The trajectory is just a list of steps the agent took before it returned to the user. We can compare that against the list of steps we expect the agent to have taken.

Evaluate trajectory and tool use¶

Before responding to a user, an agent typically performs a series of actions, which we refer to as a 'trajectory.' It might compare the user input with session history to disambiguate a term, or lookup a policy document, search a knowledge base or invoke an API to save a ticket. We call this a ‘trajectory’ of actions. Evaluating an agent's performance requires comparing its actual trajectory to an expected, or ideal, one. This comparison can reveal errors and inefficiencies in the agent's process. The expected trajectory represents the ground truth -- the list of steps we anticipate the agent should take.

For example:

# Trajectory evaluation will compare
expected_steps = ["determine_intent", "use_tool", "review_results", "report_generation"]
actual_steps = ["determine_intent", "use_tool", "review_results", "report_generation"]

ADK provides both groundtruth based and rubric based tool use evaluation metrics. To select the appropriate metric for your agent's specific requirements and goals, please refer to our recommendations.

How evaluation works with ADK¶

ADK offers two methods for evaluating agent performance against predefined datasets and evaluation criteria. While conceptually similar, they differ in the amount of data they can process, which typically dictates the appropriate use case for each.

Evaluate with test files¶

This approach involves creating individual test files, each representing a single, simple agent-model interaction (a session). It's most effective during active agent development, serving as a form of unit testing. These tests are designed for rapid execution and should focus on simple session complexity. Each test file contains a single session, which may consist of multiple turns. A turn represents a single interaction between the user and the agent. Each turn includes

User Content: The user issued query.

Expected Intermediate Tool Use Trajectory: The tool calls we expect the
agent to make in order to respond correctly to the user query.

Expected Intermediate Agent Responses: These are the natural language
responses that the agent (or sub-agents) generates as it moves towards
generating a final answer. These natural language responses are usually an
artifact of an multi-agent system, where your root agent depends on sub-agents to achieve a goal. These intermediate responses, may or may not be of
interest to the end user, but for a developer/owner of the system, are of
critical importance, as they give you the confidence that the agent went
through the right path to generate final response.

Final Response: The expected final response from the agent.

You can give the file any name for example evaluation.test.json. The framework only checks for the .test.json suffix, and the preceding part of the filename is not constrained. The test files are backed by a formal Pydantic data model. The two key schema files are
Eval Set and
Eval Case.
Here is a test file with a few examples:

Note

Comments are included for explanatory purposes and should be removed for the JSON to be valid.

# Do note that some fields are removed for sake of making this doc readable.
{
"eval_set_id": "home_automation_agent_light_on_off_set",
"name": "",
"description": "This is an eval set that is used for unit testing `x` behavior of the Agent",
"eval_cases": [
{
"eval_id": "eval_case_id",
"conversation": [
{
"invocation_id": "b7982664-0ab6-47cc-ab13-326656afdf75", # Unique identifier for the invocation.
"user_content": { # Content provided by the user in this invocation. This is the query.
"parts": [
{
"text": "Turn off device_2 in the Bedroom."
}
],
"role": "user"
},
"final_response": { # Final response from the agent that acts as a reference of benchmark.
"parts": [
{
"text": "I have set the device_2 status to off."
}
],
"role": "model"
},
"intermediate_data": {
"tool_uses": [ # Tool use trajectory in chronological order.
{
"args": {
"location": "Bedroom",
"device_id": "device_2",
"status": "OFF"
},
"name": "set_device_info"
}
],
"intermediate_responses": [] # Any intermediate sub-agent responses.
}
}
],
"session_input": { # Initial session input.
"app_name": "home_automation_agent",
"user_id": "test_user",
"state": {}
}
}
]
}

Test files can be organized into folders. Optionally, a folder can also include a test_config.json file that specifies the evaluation criteria.

How to migrate test files not backed by the Pydantic schema?¶

Note

If your test files don't adhere to EvalSet schema file, then this section is relevant to you.

Please use AgentEvaluator.migrate_eval_data_to_new_schema to migrate your
existing *.test.json files to the Pydantic backed schema.

The utility takes your current test data file and an optional initial session
file, and generates a single output json file with data serialized in the new
format. Given that the new schema is more cohesive, both the old test data file
and initial session file can be ignored (or removed.)

Evaluate with an Evalset File¶

The evalset approach utilizes a dedicated dataset called an "evalset" for evaluating agent-model interactions. Similar to a test file, the evalset contains example interactions. However, an evalset can contain multiple, potentially lengthy sessions, making it ideal for simulating complex, multi-turn conversations. Due to its ability to represent complex sessions, the evalset is well-suited for integration tests. These tests are typically run less frequently than unit tests due to their more extensive nature.

An evalset file contains multiple "evals," each representing a distinct session. Each eval consists of one or more "turns," which include the user query, expected tool use, expected intermediate agent responses, and a reference response. These fields have the same meaning as they do in the test file approach. Alternatively, an eval can define a conversation scenario which is used to dynamically simulate a user interaction with the agent. Each eval is identified by a unique name. Furthermore, each eval includes an associated initial session state.

Creating evalsets manually can be complex, therefore UI tools are provided to help capture relevant sessions and easily convert them into evals within your evalset. Learn more about using the web UI for evaluation below. Here is an example evalset containing two sessions. The eval set files are  backed by a formal Pydantic data model. The two key schema files are
Eval Set and
Eval Case.

Warning

This evalset evaluation method requires the use of a paid service,
Vertex Gen AI Evaluation Service API.

Note

Comments are included for explanatory purposes and should be removed for the JSON to be valid.

# Do note that some fields are removed for sake of making this doc readable.
{
"eval_set_id": "eval_set_example_with_multiple_sessions",
"name": "Eval set with multiple sessions",
"description": "This eval set is an example that shows that an eval set can have more than one session.",
"eval_cases": [
{
"eval_id": "session_01",
"conversation": [
{
"invocation_id": "e-0067f6c4-ac27-4f24-81d7-3ab994c28768",
"user_content": {
"parts": [
{
"text": "What can you do?"
}
],
"role": "user"
},
"final_response": {
"parts": [
{

"text": "I can roll dice of different sizes and check if numbers are prime."
}
],
"role": null
},
"intermediate_data": {
"tool_uses": [],
"intermediate_responses": []
}
}
],
"session_input": {
"app_name": "hello_world",
"user_id": "user",
"state": {}
}
},
{
"eval_id": "session_02",
"conversation": [
{
"invocation_id": "e-92d34c6d-0a1b-452a-ba90-33af2838647a",
"user_content": {
"parts": [
{
"text": "Roll a 19 sided dice"
}
],
"role": "user"
},
"final_response": {
"parts": [
{
"text": "I rolled a 17."
}
],
"role": null
},
"intermediate_data": {
"tool_uses": [],
"intermediate_responses": []
}
},
{
"invocation_id": "e-bf8549a1-2a61-4ecc-a4ee-4efbbf25a8ea",
"user_content": {
"parts": [
{
"text": "Roll a 10 sided dice twice and then check if 9 is a prime or not"
}
],
"role": "user"
},
"final_response": {
"parts": [
{
"text": "I got 4 and 7 from the dice roll, and 9 is not a prime number.\n"
}
],
"role": null
},
"intermediate_data": {
"tool_uses": [
{
"id": "adk-1a3f5a01-1782-4530-949f-07cf53fc6f05",
"args": {
"sides": 10
},
"name": "roll_die"
},
{
"id": "adk-52fc3269-caaf-41c3-833d-511e454c7058",
"args": {
"sides": 10
},
"name": "roll_die"
},
{
"id": "adk-5274768e-9ec5-4915-b6cf-f5d7f0387056",
"args": {
"nums": [
9
]
},
"name": "check_prime"
}
],
"intermediate_responses": [
[
"data_processing_agent",
[
{
"text": "I have rolled a 10 sided die twice. The first roll is 5 and the second roll is 3.\n"
}
]
]
]
}
}
],
"session_input": {
"app_name": "hello_world",
"user_id": "user",
"state": {}
}
}
]
}
