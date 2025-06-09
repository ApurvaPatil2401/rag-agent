import json
import re
from openai import AsyncOpenAI
from agent.prompts import system_prompt
from agent.tools import query_documents

client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")  # Ollama-compatible

# 🧠 Simple parser to extract CALL_TOOL-style instruction from LLM output
def extract_tool_call(response_text: str):
    match = re.search(r'CALL_TOOL:\s*(\w+)\((.*?)\)', response_text)
    if not match:
        return None, {}

    func_name = match.group(1)
    args_str = match.group(2)
    args = {}

    for arg in args_str.split(","):
        if "=" in arg:
            key, val = arg.split("=")
            args[key.strip()] = val.strip().strip('"')

    return func_name, args

# 🔁 Main chat function
async def chat_with_agent(user_query: str):
    messages = [
        {"role": "system", "content": system_prompt + "\nUse CALL_TOOL if data lookup is required."},
        {"role": "user", "content": user_query}
    ]

    # 🔍 Query Ollama model
    response = await client.chat.completions.create(
        model="qwen:0.5b",  # Replace if using a different local model
        messages=messages,
        temperature=0.7,
    )

    msg = response.choices[0].message.content
    print("💬 LLM response:", msg)

    # 🛠 Detect and handle tool call
    func_name, args = extract_tool_call(msg)

    if func_name == "query_documents":
        result = await query_documents(**args)
        print("📄 Tool call result:", result)

        # 🤖 Ask model to summarize the result
        messages.append({"role": "assistant", "content": msg})
        messages.append({"role": "user", "content": f"Summarize these results:\n{result}"})

        final = await client.chat.completions.create(
            model="qwen:0.5b",
            messages=messages,
        )
        return final.choices[0].message.content

    # No tool call, return original message
    return msg
