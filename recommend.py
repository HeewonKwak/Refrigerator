import openai
from config import API_KEY



def chatGPT(message):
    # set api key
    openai.api_key = API_KEY 

    # Call the chat GPT API
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"I'll tell you the ingredients in my refrigerator. Recommend good one food to cook without any explanation in Korean. Let me know if there are any additional ingredients I need to buy."},
            {"role": "system", "content": f"Use only ingredients less than 5 in my refrigerator"},
            {"role": "assistant", "content": f"Examples like: Food name / Refrigerator_ingredient1, Refrigerator_ingredient2 / Additional_required_ingredient1"},
            {"role": "user", "content": message}
        ],
        temperature=0,
        max_tokens=100
    )
    return completion['choices'][0]['message']['content']