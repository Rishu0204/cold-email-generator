import os
from langchain_groq import ChatGroq
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            

            ###INSTRUCTION
            the scraped text is from the career page's website.
            your job is to extract the job postings and return them in JSON format containing
            the following keys:'role','experience','skills' and description'.
            make sure the experience and skills are concise and to the point do not add unnecessary details.
            make each skills in list format i.e the skills key has a list value with the skills
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

             ### INSTRUCTION:
            You are Mohan, a business development executive at "XYZ". XYZ is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of XYZ
            in fulfilling their needs.
            make sure to also read the title and include a portfolio relatred to the title example if it's and al/ml posting make sure to have an al/ml portfolio.
            Also read the skills required carefully and match it with job description to find the most revelevant portfolios
            add them from the following links to showcase XYZ's portfolio: {link_list}
            Remember you are Mohan, BDE at XYZ. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))




 
            