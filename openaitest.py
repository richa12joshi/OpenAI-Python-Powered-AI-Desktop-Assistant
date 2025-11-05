import os
import openai
from config import apikey  # Make sure config.py is in the same directory and contains: apikey = "YOUR_OPENAI_API_KEY"

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")
# Create a completion request
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write an email to my boss for resignation.",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)