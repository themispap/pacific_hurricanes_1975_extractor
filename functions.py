# Import required packages
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
import json
import pandas as pd
from datetime import datetime

load_dotenv()
client = OpenAI()

def extract_info_from_text(text):
    prompt = f"""Extract from the text the following information in python dictionary format:
    1. The number of deaths (dictionary key='number_of_deaths') as an integer (if no deaths, return 0).
    2. A list of areas affected (dictionary key='areas_affected') (mention locations only).

    Text: {text}
    """
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are an expert assistant who extracts useful information from text."},
            {"role": "user", "content": prompt}
    ]
    # max_tokens=15  # Maximum number of tokens to generate
    )
    # Extract the response content
    text_response = response.choices[0].message.content
    # Convert the JSON string to a Python dictionary
    result = json.loads(text_response)
    return result


# Get the content of the page
def get_url_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')
        print("Successfully fetched the requested page.")
        return soup
    else:
        print("Failed to retrieve the requested page.")

def convert_date(date_string):
    # Parse the date string of the year 1975
    date_object = datetime.strptime(date_string + ' 1975', '%B %d %Y')
    # Convert it to the format 'YYYY-MM-DD'
    return date_object.strftime('%Y-%m-%d')