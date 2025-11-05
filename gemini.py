key="AIzaSyD8I1UViqZFEOfMpF1XNRA2p5Ak3U1ne5I"
from google import genai

client = genai.Client(api_key=key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="write a email to boss"
)
print(response.text)