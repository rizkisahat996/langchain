# Menggunakan Hugging FaceHub
import os
from langchain_community.llms import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUG_API")
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
text = "Beritahu fakta menarik tentang kentang!"
result = llm.invoke(text)
print(result)

