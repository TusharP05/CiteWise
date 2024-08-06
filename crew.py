import json
from crewai import Crew, Process
from tasks import research_task, write_task, link_finder,paper_write
from agents import news_researcher, news_writer, linker, paper_writer

from bs4 import BeautifulSoup



# Forming the tech-focused crew with some enhanced configuration
crew = Crew(
    agents=[linker],
    tasks=[link_finder],
    process=Process.sequential,
)

def gather_results(topic):
    try:
        # Kick off the crew task
        result = crew.kickoff(inputs={'topic': topic})

        # Debugging statement to print raw result
        print(result)

        # Ensure the result is properly encoded and decoded
        result_str = str(result).encode('utf-8', 'ignore').decode('utf-8')

        return result_str
        
    
    except Exception as e:
        print(f"Error in gather_results: {e}")  # Debugging print statement
        return {'error': str(e)}
