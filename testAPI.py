import os, sys
import openai
# Initialize client
openai.api_key = os.getenv("OPENAI_API_KEY")
model="gpt-4.1"

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4.1",  # or "gpt-3.5-turbo"
            messages=[          
                {"role": "system", "content": "Read the following text and identify any potential misinformation or false claims. List any parts that may be misleading, unsupported, or factually incorrect. SUMARIZE the points into bullet form and provide explanations and reliable sources if possible"},
                {"role": "user", "content": prompt}
            ],
        
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error calling GPT]: {str(e)}"


def main():
    text: str = sys.stdin.read()
    if not text.strip():
        print("Invalid input: No text recieved")
        exit()
    reply = chat_with_gpt(text)
    print(f"ChatGPT {model}" + '\n' + reply)

if __name__ == "__main__":
    #print("ENTER PROMPT: ")
    main()
   
