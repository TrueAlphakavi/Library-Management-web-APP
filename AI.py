import google.generativeai as genai
import os


os.environ['GOOGLE_API_KEY'] = "AIzaSyCterFUXWjcdxnUpnTweyxGueUjmfcjx00"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])



def Ask_AI(query:str)->str:

    model = genai.GenerativeModel('gemini-pro')

    prompt = "Answer the following question, question : " + query

    response = model.generate_content([prompt], stream=True)

    response.resolve()

    output_gemini_text = response.text

    return output_gemini_text