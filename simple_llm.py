import os
from langchain_openai import ChatOpenAI
import gradio as gr

from dotenv import load_dotenv

load_dotenv()
# Memasukkan API key
os.environ["OPENAI_API_KEY"] = os.getenv("GPT_API")
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )
def chatbot(prompt):
    return gpt3.invoke(prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)