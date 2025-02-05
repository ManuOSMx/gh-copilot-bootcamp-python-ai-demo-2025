import os  
import json
from openai import AzureOpenAI  
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")  
deployment = os.getenv("DEPLOYMENT_NAME")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")  

def send_prompt_to_AzureOpenAI(prompt_message, translate=False):
    client = AzureOpenAI(  
        azure_endpoint=endpoint,  
        api_key=subscription_key,  
        api_version="2024-05-01-preview",
    )
    #Prepare the chat prompt
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": f"{prompt_message}"
                }
            ]
        }
    ] 

    # Generate the completion  
    completion = client.chat.completions.create(  
        model=deployment,
        messages=chat_prompt,
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,
        stop=None,  
        stream=False
    )
    response = json.loads(completion.to_json())
    # print(response)
    return response["choices"][0]["message"]["content"] 