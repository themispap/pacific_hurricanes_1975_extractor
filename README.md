# 1975 Pacific Hurricane Season Data Scraper

This project scrapes data from the Wikipedia page on the **1975 Pacific hurricane season** and structures the data into a CSV file. The project uses Python along with web scraping and language model processing tools like **BeautifulSoup** and **OpenAI GPT**.

## Features

- Scrapes hurricane data (name, dates, number of deaths, and affected areas) from Wikipedia.
- Cleans and extracts the relevant data using an AI model.
- Outputs the data into a structured CSV file.
- Provides methodology for data extraction and quality assessment.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Methodology](#methodology)
- [License](#license)

## Prerequisites

- Python 3.9 or later
- An OpenAI API key (for GPT-based text extraction)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/themispap/pacific_hurricanes_1975_extractor.git
cd pacific_hurricanes_1975_extractor

```

### Step 2: Set Up the Python Environment

You can set up the Python environment using either **Conda** or **virtualenv**.

#### Using Conda:

```bash
conda create --name hurricane_scraper python=3.9
conda activate hurricane_scraper
```

#### Using virtualenv:

```bash
python -m venv hurricane_scraper
source hurricane_scraper/bin/activate  # On Windows use env\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up OpenAI API Key

Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the Python script to scrape data and generate the CSV file:

```bash
python main.py
```

The script will:

1. Scrape data from the Wikipedia page for the 1975 Pacific hurricane season.
2. Clean the data and use OpenAI GPT to help parse and structure it.
3. Output the data to a CSV file (`hurricanes_1975.csv`).

### CSV Output Format

The CSV file will contain the following columns:

- `hurricane_storm_name`: Name of the hurricane or storm.
- `date_start`: The start date of the hurricane or storm.
- `date_end`: The end date of the hurricane or storm.
- `number_of_deaths`: Total number of deaths attributed to the hurricane or storm.
- `list_of_areas_affected`: Areas affected by the hurricane or storm.

## Files

- **main.py**: The main Python script for scraping and generating the CSV file.
- **notebook.ipynb**: The jupyter notebook describing the main Python script.
- **requirements.txt**: Lists the Python libraries required for the project.
- **hurricanes_1975.csv**: The output CSV file with the extracted hurricane data.
- **methodology.md**: A brief explanation of the approach used for scraping and processing the data.
- **.env**: Contains the OpenAI API key (this should not be committed to version control).

## Methodology

The data extraction process involves scraping Wikipedia data using BeautifulSoup and then utilizing OpenAI's language model (GPT) to parse unstructured text into a structured format. The extracted data is cleaned and written into a CSV file. The methodology includes data validation to ensure that missing values, dates, and names are handled appropriately, and duplicate data is removed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.