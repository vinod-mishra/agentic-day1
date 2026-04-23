 # System Message - Set the Agent Personality
 # Human Message - User Query
 # AI Message - model's response

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 1. Project Setup
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", seed=6)

# 2. Context Break Demonstration (Naïve Invocation)
resp1 = llm.invoke("We are building an AI system for processing medical insurance claims.")
print(f"Response 1: {resp1.content}\n")

resp2 = llm.invoke("What are the main risks in this system?")
print(f"Response 2: {resp2.content}\n")

# Comment explaining the failure:
# The second question fails because LLMs are stateless. Each .invoke() call 
# is a brand new session. Without sending resp1 back in the next call, 
# the model has no idea what "this system" refers to.

# 3. Context Fix Using Messages API
messages = [
    SystemMessage(content="You are a senior AI architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

resp3 = llm.invoke(messages)
print(f"Fixed Context Response: {resp3.content}")

# 4. Reflection Block (Mandatory)
"""
Reflection:

1. Why did string-based invocation fail?
String-based invocation failed because it only sends the current prompt. 
Since LLMs do not store memory of previous calls locally, the second prompt 
lacked the context of what system was being discussed.

2. Why does message-based invocation work?
Message-based invocation works because we pass an array of the entire 
conversation history. This allows the model to look back at previous 
messages to resolve pronouns like "this system."

3. What would break in a production AI system if we ignore message history?
In production, ignoring history would break chatbots, multi-step workflows, 
and troubleshooting agents. Users would have to repeat their entire 
problem in every single message, leading to a frustrating and unusable experience.
"""


