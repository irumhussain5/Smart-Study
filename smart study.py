# Install first:
# pip install google-generativeai

import os
import google.generativeai as genai

# 1. Configure Gemini with your API key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def generate():
    # 2. Choose a model (fast + good for Q&A)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # 3. Create a Study Mode prompt
    prompt = """
    You are Study Mode, a teaching assistant.
    - Always explain step by step.
    - Then return JSON with:
      "solution": detailed explanation
      "quiz": 3 short quiz questions
      "flashcard": { "front": "question", "back": "answer" }

    User question: Explain Newton's Second Law.
    """

    # 4. Generate response
    response = model.generate_content(prompt)

    # 5. Print text output
    print(response.text)

if __name__ == "__main__":
    generate()
