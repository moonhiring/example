from dotenv import main
import os
main.load_dotenv()
import openai
openai.api_key= os.environ.get("OPENAI_API_KEY")
print("야 이자식아")