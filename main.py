import functions as f

# URL for the 1975 Pacific hurricane season Wikipedia page
url = 'https://en.wikipedia.org/wiki/1975_Pacific_hurricane_season'
# Parse the HTML
soup=f.get_url_content(url)

div_element=soup.find_all('div', {'class':'mw-heading mw-heading3'})
hurricane_storm_name=[]
for h3 in div_element:
    striped_h3=h3.find('h3').text.strip()
    hurricane_storm_name.append(striped_h3)

table_element=soup.find_all('table', {'class':'infobox'})
exact_class_tables = [table for table in table_element if table['class'] == ['infobox']]
start_date=[]
end_date=[]
for td in exact_class_tables:
    striped_date=td.find('td',{'class':'infobox-data'}).text.strip().split('\xa0– ')
    start_date.append(striped_date[0])
    end_date.append(striped_date[1])

# extract the text of each hurricane/storm paragraph
all_h3 = soup.find_all('div',{'class':'mw-heading mw-heading3'})
info_text=[]
for h3 in all_h3:
    content_between_h3 = []
    # Loop through the siblings after the <div> tag
    for sibling in h3.find_next_siblings():
        # Stop when reaching the next <div> tag
        if sibling.name == 'div':
            break
        # Append the content of <p> to the list
        if sibling.name == 'p':
            text=sibling.text.strip()
            content_between_h3.append(text)
    # Join the list into a single string
    info_text.append(''.join(content_between_h3))

deaths=[]
affected_areas=[]
for text in info_text:
    info=f.extract_info_from_text(text)
    deaths.append(info['number_of_deaths'])
    affected_areas.append(info['areas_affected'])