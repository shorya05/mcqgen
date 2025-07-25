# 🧠 MCQ Generator with LangChain

This is a Streamlit-based application that generates **Multiple Choice Questions (MCQs)** from uploaded `.pdf` or `.txt` documents using **LangChain** and **OpenAI's LLMs**. It simplifies quiz creation by automating the generation process, making it useful for teachers, students, and training organizations.

---

## 🚀 Features

- 📄 Upload PDF or TXT files as input
- 🔢 Choose number of MCQs (3–50)
- 📘 Add subject and tone (e.g., "simple", "complex")
- 🧠 Generates MCQs with options and correct answers
- 📊 Displays questions in a clean table format
- 📋 Includes a review/summary section
- ⚙️ Powered by LangChain, OpenAI, Streamlit, Pandas

---

## 🛠️ Tech Stack

| Tool          | Purpose                           |
|---------------|-----------------------------------|
| Python        | Backend logic                     |
| Streamlit     | Frontend Web App                  |
| LangChain     | Prompt chaining & OpenAI interface|
| OpenAI API    | Language model for MCQs           |
| Pandas        | Data handling and tabular output  |
| dotenv        | Load API keys securely            |

---

## 📂 Folder Structure

mcqgen/
│
├── StreamlitAPP.py # Main app
├── Response.json # JSON structure for parsing response
├── .env # Stores OpenAI API Key
│
├── src/
│ └── mcqgenerator/
│ ├── init.py
│ ├── utils.py # File reading and table formatting
│ ├── pipeline.py # LangChain chain setup
│ ├── logger.py # Logging utility



2. Create virtual environment (optional but recommended)
bash
Copy
Edit
conda create -n mcqgenv python=3.10
conda activate mcqgenv

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt


4. Add your .env file
Create a .env file in the root folder with your OpenAI API key:

env
Copy
Edit
OPENAI_API_KEY=your-openai-key-here


5. Run the Streamlit app
bash
Copy
Edit
streamlit run StreamlitAPP.py



