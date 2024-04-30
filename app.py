from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import sqlite3
import google.generativeai as genai

##Configure API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load the Google Gemini model and provide sql query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

##Function to retrieve 

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall() 
    conn.commit()
    conn.close()
    for row in rows:
        print(row)  
    return rows


## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App
st.set_page_config(page_title="I can retrieve Any SQL Query",page_icon="🔍",layout="centered")

st.header("Gemini App to retriecve SQL Data")

question=st.text_input("input:",key="input")

submit=st.button("Ask the question")

## If the submit button is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is:")
    for row in data:
        st.header(row)
            

