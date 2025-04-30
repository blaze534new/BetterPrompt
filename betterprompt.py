import os
import requests
from dotenv import load_dotenv

# === Load API key from .env ===
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama3-70b-8192"  # valid Groq model

DEBUG = False  # disables debug messages, only final output is shown


def call_groq(messages):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 2048
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def detect_italian(prompt):
    italian_keywords = ["che", "come", "perché", "voglio", "lista", "migliori", "cosa", "spiegami", "elenca", "dettagli",
                        "includi", "scrivi"]
    return any(word in prompt.lower() for word in italian_keywords)


def main():
    user_prompt = input("Enter your base prompt: ").strip()
    is_italian = detect_italian(user_prompt)

    # STEP 1 – Initial response (not shown in final version)
    initial_response_msg = [
        {"role": "system",
         "content": "If the prompt is in Italian, respond in Italian. Otherwise, respond in the original language."},
        {"role": "user", "content": user_prompt}
    ]
    _ = call_groq(initial_response_msg)  # Generated but not shown

    # STEP 2 – Generate the "Perfect Prompt"
    perfect_prompt_msg = [
        {
            "role": "system",
            "content": (
                "You are an expert prompt engineer. Transform the following request into a 'Perfect Prompt' with these sections:\n"
                "GOAL, FORMAT, WARNINGS, CONTEXT DUMP.\n"
                "Be precise and detailed. If the input is in Italian, keep the entire prompt in Italian."
            )
        },
        {"role": "user", "content": user_prompt}
    ]
    perfect_prompt = call_groq(perfect_prompt_msg)

    # STEP 3 – Strip headers and further optimize the prompt
    cleaned_prompt = perfect_prompt.replace("GOAL", "").replace("FORMAT", "").replace("WARNINGS", "").replace(
        "CONTEXT DUMP", "").replace("-----", "")

    refined_prompt_msg = [
        {
            "role": "system",
            "content": (
                "You are a world-class prompt optimizer. Here is a very detailed prompt.\n"
                "Now rewrite it even better, using maximum clarity, precision, and structure. "
                "Use as reference this example in English:\n\n"
                "I want a list of the best medium-length hikes within two hours of San Francisco...\n\n"
                "Keep the language of the input (Italian or English)."
            )
        },
        {"role": "user", "content": cleaned_prompt}
    ]
    final_prompt = call_groq(refined_prompt_msg)

    # STEP 4 – Final response to the optimized prompt
    final_response_msg = [
        {"role": "system", "content": "You are a helpful assistant. Respect the user's language (Italian or English)."},
        {"role": "user", "content": final_prompt}
    ]
    final_response = call_groq(final_response_msg)

    print("\n--- FINAL RESPONSE ---")
    print(final_response)


if __name__ == "__main__":
    main()
