from crewai_tools import SerperDevTool

# Initialize the tool for internet searching
# It automatically looks for SERPER_API_KEY in your .env
search_tool = SerperDevTool()