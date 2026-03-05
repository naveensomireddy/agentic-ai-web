from crewai import Agent, Task, Crew, Process

class WebsiteAgents:
    def researcher_agent(self):
        return Agent(
            role='Market Researcher',
            goal='Analyze the latest trends in {topic} for 2026',
            backstory='You are an expert analyst with a knack for spotting emerging tech.',
            allow_delegation=False,
            verbose=True
        )

    def writer_agent(self):
        return Agent(
            role='Content Strategist',
            goal='Write a compelling blog post about {topic}',
            backstory='You transform complex data into engaging, easy-to-read web content.',
            allow_delegation=False,
            verbose=True
        )

class WebsiteTasks:
    def research_task(self, agent, topic):
        return Task(description=f'Search for 3 major breakthroughs in {topic}.', agent=agent)

    def write_task(self, agent, topic):
        return Task(description=f'Compose a 500-word article on {topic} based on research.', agent=agent)
