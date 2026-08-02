from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from app.tools.resume_tool import get_resume_content
import os

class AgentState(TypedDict):
    messages: list
    resume_context: str

def call_model(state: AgentState):
    prompt = f"""You are Prakashsinh Rajput's professional AI agent. 
    Your goal is to provide high-quality, well-formatted, and concise answers based on his resume.
    
    GUIDELINES:
    - Use Markdown formatting for readability.
    - Use bullet points or numbered lists for skills and project features.
    - Use tables when comparing technologies or listing structured experience.
    - Use bold text to highlight key achievements or technologies.
    - If the answer is not in the context, politely state that the information is not available in the provided resume.
    
    Resume Context:
    {state['resume_context']}
    
    User Question: {state['messages'][-1]}
    """
    
    llm = ChatOpenAI(model="gpt-4o")
    response = llm.invoke(prompt)
    return {"messages": state['messages'] + [response.content]}

def create_agent():
    resume_context = get_resume_content()
    
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", call_model)
    workflow.set_entry_point("agent")
    workflow.add_edge("agent", END)
    
    return workflow.compile(), resume_context
