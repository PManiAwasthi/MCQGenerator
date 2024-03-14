import os
import PyPDF2
import json
import traceback


def read_file(file):
    #to check if the file is pdf
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            #getting the content in pagewise manner
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading the PDF file")     

    #to check if the file is text
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception(
            "unsupported file format only pdf and text file supported"
        ) 


def get_table_data(quiz_str):
    try:
        #quiz_str is the response we will get from the api call to OpenAI
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        
        for key, value in quiz_dict.items():
            mcq=value['mcq']
            options=" | ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                ]
            )
            correct=value["correct"]
            quiz_table_data.append({'MCQ':mcq, "Choices":options, "Correct":correct})
        return quiz_table_data
    
    except Exception as e:
        raise e