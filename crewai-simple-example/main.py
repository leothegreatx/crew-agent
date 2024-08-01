import sys
from crewai import Agent, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from MarkdownTools import markdown_validation_tool

load_dotenv()

llm = ChatOpenAI(
    model="crewai-llama2",
    base_url="http://localhost:11434/v1",
    openai_api_key="na"
)

# Define research agent
research_agent = Agent(
    role='Researcher',
    goal="""Develop comprehensive ideas for teaching a beginner about a specific subject.
            Provide a structured plan with topics to cover, suggested resources, and a
            step-by-step guide to ensure a solid understanding of the subject.""",
    backstory="""You are an experienced educator and researcher. Your task is to create
                 an effective and engaging teaching plan that introduces a new learner
                 to a subject in a clear and structured manner.""",
    allow_delegation=False,
    verbose=True,
    tools=[markdown_validation_tool],
    llm=llm,
    stop=["Final Answer:", "Thought:"]
)

# Define writer agent
writer_agent = Agent(
    role='Writer',
    goal="""Write a clear and engaging piece of text explaining a specific subject based on
            the provided teaching plan. The explanation should be understandable to a beginner and
            provide a concise overview of the subject.""",
    backstory="""You are a skilled writer with expertise in creating clear and engaging content.
                 Your task is to use the provided teaching plan to write a piece that explains
                 the subject in a way that is easy for a beginner to understand.""",
    allow_delegation=False,
    verbose=True,
    llm=llm,
    stop=["Final Answer:", "Thought:"]
)

# Define examiner agent
examiner_agent = Agent(
    role='Examiner',
    goal="""Craft 2-3 questions to evaluate a person's understanding of a specific subject based
            on the provided explanation. The questions should assess comprehension and retention of
            the key concepts presented in the explanation.""",
    backstory="""You are an experienced examiner with expertise in creating questions that effectively
                 evaluate understanding and retention of educational material. Your task is to create
                 questions that help gauge a learner's grasp of the subject matter.""",
    allow_delegation=False,
    verbose=True,
    llm=llm,
    stop=["Final Answer:", "Thought:"]
)

def develop_teaching_plan(subject):
    task_description = f"""
        Develop a teaching plan for a beginner on the subject: {subject}.
        Include a structured plan with topics to cover, suggested resources,
        and a step-by-step guide to ensure a solid understanding of the subject.
    """
    teaching_plan_task = Task(
        description=task_description,
        agent=research_agent
    )
    teaching_plan = teaching_plan_task.execute()
    return teaching_plan

def write_explanation(subject, teaching_plan):
    task_description = f"""
        Based on the following teaching plan, write a clear and engaging piece of text
        explaining the subject: {subject}. The explanation should be suitable for a beginner
        and provide a concise overview.
        
        Teaching Plan:
        {teaching_plan}
    """
    write_task = Task(
        description=task_description,
        agent=writer_agent
    )
    explanation = write_task.execute()
    return explanation

def craft_questions(subject, explanation):
    task_description = f"""
        Based on the following explanation, craft 2-3 questions to evaluate a person's understanding
        of the subject: {subject}. The questions should assess comprehension and retention of the
        key concepts presented in the explanation.
        
        Explanation:
        {explanation}
    """
    question_task = Task(
        description=task_description,
        agent=examiner_agent
    )
    questions = question_task.execute()
    return questions

# If called directly from the command line
if __name__ == "__main__":
    if len(sys.argv) > 1:
        subject = sys.argv[1]
        teaching_plan = develop_teaching_plan(subject)
        explanation = write_explanation(subject, teaching_plan)
        questions = craft_questions(subject, explanation)
        print("Explanation:\n", explanation)
        print("\nQuestions:\n", questions)

