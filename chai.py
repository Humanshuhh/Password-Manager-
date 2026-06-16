import streamlit as st
import pdfplumber


st.title("Resume Praser")
file = st.file_uploader("paste yor Resume", type =["pdf"])

# text extraction function

def text_extractor(sample_text):
    all_text =""
   # with pdfplumber.open(file) as pdf:
    for text in sample_text:
        text = 
         if text:
                all_text += text + "\n"

    return all_text

required_skills = [" Python"," machine learning ","aws","flask"]

def calculate_ats_score(all_text,required_skills):

    found_skills = []
    missing_skills = []

    for skills in required_skills:
        if skills.lower() == all_text.lower():
            found_skills.append(skills)
        else:
            missing_skills.append(skills)

    found_skills_score = len(found_skills)
    score = (len(found_skills) / len(required_skills))*100
    return {
        "overall_score": round(score),
        "found_skills": found_skills,
        "missing_skills": missing_skills
    }
sample_text = "I am a pyhton engineer with flask"


if file:
    st.success("file uploaded succesfully")

    resume_text = text_extractor(sample_text)

    ats_results = calculate_ats_score(resume_text,required_skills)

    
    st.json(ats_results)




