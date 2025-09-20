# pip install streamlit google-genai

import google.generativeai as genai
# Initialize Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Streamlit app
st.title("📘 Study Mode Clone")
st.write("Ask any question and get explanation + quiz + flashcards.")

# Input box
user_question = st.text_input("Enter your question:")

if st.button("Generate Study Mode Answer"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        # Create structured prompt
        prompt = f"""
        You are Study Mode, a teaching assistant.

        Rules:
        - Always explain step by step.
        - Then generate JSON output with:
          "solution": detailed explanation
          "quiz": 3 short quiz questions
          "flashcard": {{ "front": "question", "back": "answer" }}
        - Answer ONLY in JSON.

        User question: {user_question}
        """

        # Request Gemini
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            )],
        )

        # Display raw output
        st.subheader("📜 Raw Output (JSON)")
        st.code(response.text, language="json")

        # Try parsing JSON
        try:
            data = json.loads(response.text)

            st.subheader("✅ Solution")
            st.write(data.get("solution", ""))

            st.subheader("📝 Quiz Questions")
            for q in data.get("quiz", []):
                st.write(f"- {q}")

            st.subheader("📇 Flashcard")
            st.write("**Front:**", data.get("flashcard", {}).get("front", ""))
            st.write("**Back:**", data.get("flashcard", {}).get("back", ""))

        except Exception as e:
            st.error(f"Could not parse JSON: {e}")
