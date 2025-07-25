import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported file format. Only PDF and text files are supported.")

def get_table_data(quiz_data):
    try:
        # Skip json.loads if already list/dict
        if isinstance(quiz_data, str):
            import json
            quiz_data = json.loads(quiz_data)

        print("DEBUG: quiz_data =", quiz_data)

        table = []
        for item in quiz_data:
            mcq = item.get("question", "")
            options = " || ".join(item.get("options", []))
            correct = item.get("answer", "")

            table.append({
                "MCQ": mcq,
                "Choices": options,
                "Correct": correct
            })

        return table

    except Exception as e:
        print("ERROR in get_table_data:", e)
        return []


