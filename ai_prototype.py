import openai
import OpenaiAPI

openai.api_key = OpenaiAPI.apikey()

def ai_assistant_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message['content'].strip()

def prompt1():
    with open('database.txt', 'r') as file:
        file_content = file.read()
    user_prompt_1 = input("Give a basic prompt: ")
    user_prompt_1 += "\n" + file_content
    response_1 = ai_assistant_response(user_prompt_1)
    print("Response:", response_1)

def prompt2():
    with open('database.txt', 'r') as file:
        file_content = file.read()
    user_prompt_2 = input("Give a specific prompt: ")
    user_prompt_2 += "\n" + file_content
    response_2 = ai_assistant_response(user_prompt_2)
    print("Response:", response_2)

def main():
    prompt1()
    prompt2()

if __name__ == "__main__":
    main()
