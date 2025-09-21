# smart study.py

# Corrected import statement
import google.generativeai as genai
import os

# --- Example of how to use it ---
# It's a good practice to use environment variables for your API key
# from dotenv import load_dotenv
# load_dotenv()
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Or configure it directly (less secure)
# genai.configure(api_key="YOUR_API_KEY")

# Now you can use the library, for example:
# model = genai.GenerativeModel('gemini-pro')
# response = model.generate_content("Explain what a large language model is.")
# print(response.text)

print("Google Generative AI library imported successfully!")
