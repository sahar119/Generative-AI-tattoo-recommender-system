import os
import openai

import streamlit as st
from PIL import Image
import webbrowser

import pandas as pd
import random

df = pd.read_csv('SelectionTitles.csv')

text = df['Title'].to_list()
random_row = random.sample(text,5)

bott = st.button("recommend it")
if bott:
    st.write(random_row)

#print(random_row)

### Load your API key 
openai.api_key = os.getenv("OPENAI_API_KEY")

import requests

QUERY_URL = "https://api.openai.com/v1/images/generations"

def generate_image(prompt, model, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    model = "image-alpha-001"
    data = """
    {
        """
    data += f'"model": "{model}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"1024x1024",
        "response_format":"url"
    }
    """

    resp = requests.post(QUERY_URL, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_text = resp.json()
    return response_text['data'][0]['url']


if __name__ == '__main__':
    #prompt = input("Please enter your sentence:")                                                                                                    
    #prompt = "a dragon tattoo design"
    prompt = st.text_input("Please enter your sentence:", 'a tattoo design with')
    api_key = "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"
    model = "image-alpha-001"
    image_url = generate_image(prompt, model, api_key)
    result = st.button("Generate")
    if result :
        st.markdown(image_url)                                                                       
        #print(f"Image URL: {image_url}")




   
   
