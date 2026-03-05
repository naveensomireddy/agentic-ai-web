from fastapi import FastAPI
from agents import WebsiteAgents, WebsiteTasks
from crewai import Crew

app = FastAPI()

@app.get("/generate")
async def generate_content(topic: str):
    agents = WebsiteAgents()
    tasks = WebsiteTasks()

    # Initialize Agents
    researcher = agents.researcher_agent()
    writer = agents.writer_agent()

    # Form the Crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[tasks.research_task(researcher, topic), tasks.write_task(writer, topic)],
        process=Process.sequential
    )

    result = crew.kickoff()
    return {"status": "success", "output": result}
