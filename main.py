# Import custom utility functions from the 'functions.py' file as 'f'
import functions as f

# URL for the 1975 Pacific hurricane season Wikipedia page
url = 'https://en.wikipedia.org/wiki/1975_Pacific_hurricane_season'

# Call function to get and parse the HTML content of the URL
soup = f.get_url_content(url)

# Find all <div> elements containing class 'mw-heading mw-heading3' (hurricane/storm names)
div_element = soup.find_all('div', {'class': 'mw-heading mw-heading3'})

# Initialize a list to hold storm/hurricane names
hurricane_storm_name = []

# Loop through each div element to extract storm names
for h3 in div_element:
    striped_h3 = h3.find('h3').text.strip()  # Extract and clean text of the storm name
    hurricane_storm_name.append(striped_h3)  # Append the cleaned name to the list

# Find all <table> elements with class 'infobox' (information boxes)
table_element = soup.find_all('table', {'class': 'infobox'})

# Filter tables that have exactly 'infobox' class (ignore other table types)
exact_class_tables = [table for table in table_element if table['class'] == ['infobox']]

# Initialize lists to hold start and end dates
start_date = []
end_date = []

# Loop through the filtered infobox tables to extract storm dates
for td in exact_class_tables:
    # Extract the start and end dates of the storm (strip extra characters like '\xa0–')
    striped_date = td.find('td', {'class': 'infobox-data'}).text.strip().split('\xa0– ')
    start_date.append(striped_date[0])  # Append start date
    end_date.append(striped_date[1])    # Append end date

# Initialize a list to hold storm/hurricane descriptions
info_text = []

# Find all <div> elements with class 'mw-heading mw-heading3' for each storm's description
all_h3 = soup.find_all('div', {'class': 'mw-heading mw-heading3'})

# Loop through each heading and extract its corresponding paragraphs
for h3 in all_h3:
    content_between_h3 = []
    
    # Loop through sibling tags after each <div> tag until another <div> tag is found
    for sibling in h3.find_next_siblings(recursive=False):
        # Break the loop if another heading <div> is found
        if sibling.name == 'div' and sibling.attrs == {'class': ['mw-heading', 'mw-heading3']}:
            break
        # Collect text from <p> (paragraphs)
        if sibling.name == 'p':
            text = sibling.text.strip()  # Clean and extract paragraph text
            content_between_h3.append(text)
    
    # Join paragraphs into a single string
    info_text.append(''.join(content_between_h3))

# Remove the last element from the info_text list (not needed)
info_text = info_text[:-1]

# Initialize a list to hold extracted information and token counts
result = []
tokens_used = 0
prompt_tokens = 0
completion_tokens = 0

# Loop through each hurricane description and extract information using the GPT function
for text in info_text:
    response = f.extract_info_from_text(text)  # Extract data using OpenAI GPT
    text_response = response.choices[0].message.content  # Get GPT response
    result.append(text_response)  # Append extracted data to the result list
    
    # Track usage statistics for OpenAI API tokens
    tokens_used += response.usage.total_tokens
    prompt_tokens += response.usage.prompt_tokens
    completion_tokens += response.usage.completion_tokens

# Import JSON to handle the response data
import json

# Initialize lists to hold extracted deaths and affected areas data
deaths = []
affected_areas = []

# Loop through each GPT response and convert it to a Python dictionary
for item in result:
    # Replace single quotes with double quotes to ensure valid JSON format
    item_n = item.replace("'", '"')
    info = json.loads(item_n)  # Convert string to dictionary
    
    # Extract deaths and affected areas from the dictionary
    deaths.append(info['number_of_deaths'])
    affected_areas.append(info['areas_affected'])

# Import pandas to handle dataframes
import pandas as pd

# Create a dictionary with all columns (storm names, dates, deaths, areas)
columns = {
    'hurricane_storm_name': hurricane_storm_name[:-1],  # Exclude the last entry
    'date_start': start_date,
    'date_end': end_date,
    'number_of_deaths': deaths,
    'list_of_areas_affected': affected_areas
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(columns)

# Apply the date conversion function to start and end dates
df['date_start'] = df['date_start'].apply(f.convert_date)
df['date_end'] = df['date_end'].apply(f.convert_date)

# Join the list of areas affected into a single string for each storm
df['list_of_areas_affected'] = df['list_of_areas_affected'].apply(lambda x: ', '.join(x))

# Export the DataFrame to a CSV file
df.to_csv('hurricanes_1975.csv', index=False)

# Write the token usage information to a log file
with open('log.txt', 'w') as file:
    file.write('tokens_used: ' + str(tokens_used) + '\n')
    file.write('prompt_tokens: ' + str(prompt_tokens) + '\n')
    file.write('completion_tokens: ' + str(completion_tokens))
