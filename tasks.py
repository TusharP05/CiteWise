from crewai import Task
from tools import tool, paper_tool,scrape
from agents import news_researcher, news_writer, linker, paper_writer

# Research task
research_task = Task(
    description=(
        "Go through only 5 or 6 (by search engine results) peer-reviewed journals and papers in {topic}. Analyze the content and summarize the key findings, methodologies, and conclusions do not make more than 5 requests Dont bush around stay on topic."
    ),
    expected_output='A detailed summary of key points, methodologies, and conclusions in a 3-page document.',
    tools=[tool, paper_tool],
    agent=news_researcher,
    allow_delegation= True
)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Provide students researching a new topic with important details such as a summary of key findings, relevant research papers along with their links, and useful video links.Do not busha around much as it can overload the model. "
        "Divide the writing into the following sections with proper formatting: "
        "1) Review of Research Done Till Now (include citations with hyperlinks for quoted lines), "
        "2) Future Scope, "
        "3) Literature Review, "
        "4) Useful Paper Links, "
        "5) Video References, "
        "6) A comprehensive guide on how to write your own research papers on the topic, including detailed descriptions of each segment, and new ideas or improvements. "
        "Ensure that headings and subheadings are properly spaced and formatted, with newlines after headings for better readability. "
        "List items should be correctly formatted with a newline before starting the list. Provide the output in markdown format with appropriate citations and hyperlinks."
    ),
    expected_output=(
        'A comprehensive markdown document that includes the following: '
        '1) Review of Research Done Till Now with citations hyperlinked to the original papers, '
        '2) Future Scope, '
        '3) Literature Review, '
        '4) Useful Paper Links, '
        '5) Video References, '
        '6) A detailed guide on writing research papers, with each section clearly formatted and cited properly.'
    ),
    tools=[tool, paper_tool],
    agent=news_writer,
    async_execution=False,
    output_file='final.md'
)


link_finder= Task(
    description=(
        "search internet for the papers and journals related to {topic} and provide a list of 10 of them, along with their heading links(mostly of google scholar and springer and ieee and other reputed ones like nature) and authors and date laong with them, please do not provide broken links check the links if they have some data or not. Make sure no broken links are given verify them please, the article should be there when I click the link."),
    
     expected_output=' a file with 10 research papers, with author names and date and links',
    tools=[tool,paper_tool],
    agent=linker,
    async_execution=False,
    output_file= 'papers.md'

)
paper_write = Task(
    description=(
        "Write a well-structured, detailed, and publication-ready formatted review paper on the given {topic}. Do not bush around as the model may get overloaded.Whatever is available on the top searches use those. "
        "The paper should be organized into the following sections: "
        "1) **Abstract** (150-250 words): Provide a concise summary of the main findings and scope of the review. "
        "2) **Introduction** (500-1,000 words): Introduce the topic, explain its relevance, and outline the objectives of the review. "
        "3) **Literature Review** (3,000-5,000 words): Analyze key research papers and findings related to the topic. Ensure to include hyperlinks to original sources for each quoted statement or data point. "
        "4) **Discussion** (1,000-2,000 words): Discuss the implications of the reviewed literature, identify gaps, and suggest future research directions. "
        "5) **Conclusion** (500-1,000 words): Summarize the key insights and findings of the review. "
        "6) **References**: List all cited papers with proper formatting and hyperlinks. "
        "Ensure the paper is formatted in markdown with clear headings and subheadings. "
        "Include proper spacing between sections and ensure all hyperlinks are functional. Use a professional tone and maintain clarity throughout the document."
    ),
    expected_output=(
        "A well-structured, complete review paper markdown document containing: "
        "1) **Abstract** (150-250 words): A concise summary of the review paper. "
        "2) **Introduction** (500-1,000 words): An introduction to the topic and objectives of the review. "
        "3) **Literature Review** (3,000-5,000 words): A detailed analysis of key research papers with citations hyperlinked to the original sources. "
        "4) **Discussion** (1,000-2,000 words): Analysis of implications and future research directions. "
        "5) **Conclusion** (500-1,000 words): Summary of key findings. "
        "6) **References**: A list of all cited papers with hyperlinks. Ensure all links are functional and do not provide broken links. "
        "The paper should be formatted for readability, with proper headings, subheadings, and spacing."
    ),
    tools=[tool, paper_tool, scrape],
    agent=paper_writer,
    async_execution=False,
    output_file='review_paper.md'
)

