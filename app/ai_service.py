#---------------------------------------------------------------------------------------
# AI service implementation to utilize OPENAI API
#---------------------------------------------------------------------------------------

# from openai import OpenAI
# from app.config import OPENAI_API_KEY

# client = OpenAI(api_key=OPENAI_API_KEY)


# def generate_summary(prompt: str):

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ],
#         temperature=0.2
#     )

#     return response.choices[0].message.content


#---------------------------------------------------------------------------------------
# AI service implementation to utilize GEMINI API
#---------------------------------------------------------------------------------------

from google import genai

from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_summary(prompt: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text