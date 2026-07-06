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

import logging

from google import genai

from app.config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash"


def generate_summary(prompt: str):
    logger.info("Generating summary with model %s", MODEL_NAME)
    logger.debug("Prompt length: %d characters", len(prompt))

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    logger.info("Summary generated (%d characters)", len(response.text))
    return response.text
