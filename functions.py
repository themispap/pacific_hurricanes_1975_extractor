# Import required packages
import requests  # To make HTTP requests to the Wikipedia page
from bs4 import BeautifulSoup  # To parse HTML content
from openai import OpenAI  # To interact with the OpenAI GPT model
from dotenv import load_dotenv  # To load environment variables, such as API keys
from datetime import datetime  # To handle date formatting and conversion

# Load environment variables (such as OpenAI API keys)
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Function to extract specific information from the text using GPT
def extract_info_from_text(text):
    # Prompt for GPT-3.5 turbo to extract the number of deaths and affected areas
    prompt = f"""Extract from the text the following information in python dictionary format:
    1. The number of deaths (dictionary key='number_of_deaths') as an integer (if no deaths, return 0).
    2. A list of areas affected (dictionary key='areas_affected') (mention locations only).

    Text: {text}

    * No need to use ```Python ```
    * Use only double quotes (")
    """
    
    # Make a request to OpenAI GPT to process the prompt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert assistant who extracts useful information from text."},
            {"role": "user", "content": prompt}
        ]
    )
    # Return the GPT-processed response
    return response


# Function to get and parse the HTML content of a given URL
def get_url_content(url):
    # Fetch the content of the webpage
    response = requests.get(url)
    # If the request is successful (status code 200)
    if response.status_code == 200:
        page_content = response.content
        soup = BeautifulSoup(page_content, 'html.parser')  # Parse the HTML content using BeautifulSoup
        print("Successfully fetched the requested page.")
        return soup
    else:
        # If the request fails, print an error message
        print("Failed to retrieve the requested page.")

# Function to convert a given date (string format) to 'YYYY-MM-DD' format
def convert_date(date_string):
    # Parse the given date (add year 1975 as part of the date)
    date_object = datetime.strptime(date_string + ' 1975', '%B %d %Y')
    # Return the formatted date in 'YYYY-MM-DD' format
    return date_object.strftime('%Y-%m-%d')