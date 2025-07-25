# StreamlitAPP.py

import streamlit as st
import json
import os
import traceback
import pandas as pd
from dotenv import load_dotenv

from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.pipeline import generate_evaluate_chain
from langchain_community.callbacks.manager import get_openai_callback
from src.mcqgenerator.logger import logging

# ✅ Load Response.json safely
try:
    with open("Response.json", 'r') as f:
        RESPONSE_JSON = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    st.error("❌ 'Response.json' is missing or not a valid JSON.")
    RESPONSE_JSON = {}

# ✅ Title
st.title("MCQs Creator Application with LangChain ✍️")

# ✅ Input Form
with st.form("user_inputs"):
    uploaded_file = st.file_uploader("📄 Upload a PDF or TXT file")
    mcq_count = st.number_input("🔢 No. of MCQs", min_value=3, max_value=50)
    subject = st.text_input("📘 Subject", max_chars=20)
    tone = st.text_input("🧠 Complexity Level of Questions", max_chars=20, placeholder="Simple")
    button = st.form_submit_button("🚀 Create MCQs")

# ✅ Main Logic
if button and uploaded_file is not None and mcq_count and subject and tone:
    with st.spinner("Generating questions..."):
        try:
            # Step 1: Read uploaded file
            text = read_file(uploaded_file)

            # Step 2: Generate MCQs using LangChain and OpenAI
            with get_openai_callback() as cb:
                response = generate_evaluate_chain({
                    "text": text,
                    "number": mcq_count,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                })

        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            st.error("Something went wrong while generating the quiz.")

        else:
            print(f"Total Tokens: {cb.total_tokens}")
            print(f"Prompt Tokens: {cb.prompt_tokens}")
            print(f"Completion Tokens: {cb.completion_tokens}")
            print(f"Total Cost: ${cb.total_cost:.4f}")

            # Step 3: Display results
            if isinstance(response, dict):
                quiz = response.get("quiz", None)

                if quiz is not None:
                    table_data = get_table_data(quiz)
                    print("DEBUG: Quiz from response:", quiz)
                    print("DEBUG: Table Data from get_table_data:", table_data)

                    if table_data and isinstance(table_data, list):
                        df = pd.DataFrame(table_data)
                        df.index = df.index + 1
                        st.table(df)

                        # Show review (if any)
                        st.text_area(label="Review", value=response.get("review", ""))
                    else:
                        st.error("Could not format quiz data into table.")
                else:
                    st.error("No quiz data found in the response.")
            else:
                st.write(response)
