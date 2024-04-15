from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import re

#importing files
import db as db
import textextract as txt


llm = ChatGoogleGenerativeAI(
        google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
        model="gemini-pro",
        convert_system_message_to_human=True
        
    )


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
    model="models/embedding-001",


)

def navigator(Query):
    template = f"""
Categorize the given query and select the appropriate repository to retrieve data from. 

Repositories:
1. Database: Contains information that can be easily converted from a query to PostgreSQL query.
2. Text File: The text provides information about various banking services, procedures, and FAQs, which are typically stored as textual information. if the user ask question related to below question then fetch from the vector database
if it is not related to banking content then display "I'm Sorry, Provided context does not related to banking so i cannot answer you".

Query:
{Query}

Provide your response in the below format:
Reason: <Provide your Reason here>
Answer: <Provide Database or Text File>

"""
    
    result = llm.invoke(template)
    result = result.content

    match = re.search(r"Answer:\s*(.*)", result, flags= re.DOTALL)
    if match:
        navigator_match = match.group(1)
        if navigator_match == 'Database':
            return db.sqlquery_retriever(Query)
        elif navigator_match == 'Text File':
            return txt.text_retriever(Query)
        else:
            return "The requested information not found"




"""Repositories:
1. Database: Contains information that can be easily converted from a query to PostgreSQL query.
2. Text file: The text provides information about various banking services, procedures, and FAQs, which are typically stored as textual information. if the user ask question related to below question then fetch from the vector database
if it is not related to banking content then display "I'm Sorry, Provided context does not related to banking so i cannot answer you".
"""