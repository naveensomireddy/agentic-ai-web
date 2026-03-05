import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load your API key from .env
load_dotenv()

# Initialize Gemini 1.5 Pro
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

class WebsiteAgents:
    def researcher_agent(self):
        return Agent(
            role='Market Researcher',
            goal='Analyze {topic} trends in 2026',
            backstory='Expert at deep-web analysis and trend forecasting.',
            llm=gemini_llm,  # <--- This connects the agent to Gemini
            verbose=True
        )

    def writer_agent(self):
        return Agent(
            role='Content Strategist',
            goal='Create a viral post about {topic}',
            backstory='A master wordsmith who optimizes for engagement.',
            llm=gemini_llm,  # <--- Both agents use the same LLM
            verbose=True
        )