##install package: pip install google-genai
from google import genai


client = genai.Client(api_key="AIzaSyDOvaCm5_I6DGP8AEvy62sPHZMwUbtQQX0")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)