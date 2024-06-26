# -*- coding: utf-8 -*-
"""Gokul || Numerical Programming in Python - Web Scraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1psy3YEl0fI2nV08EpVbumrLLZtrA4_Dm

# **Web Scraping & Data Handling Challenge**

### **Website:**
JustWatch -  https://www.justwatch.com/in/movies?release_year_from=2000


### **Description:**

JustWatch is a popular platform that allows users to search for movies and TV shows across multiple streaming services like Netflix, Amazon Prime, Hulu, etc. For this assignment, you will be required to scrape movie and TV show data from JustWatch using Selenium, Python, and BeautifulSoup. Extract data from HTML, not by directly calling their APIs. Then, perform data filtering and analysis using Pandas, and finally, save the results to a CSV file.

### **Tasks:**

**1. Web Scraping:**

Use BeautifulSoup to scrape the following data from JustWatch:

   **a. Movie Information:**

      - Movie title
      - Release year
      - Genre
      - IMDb rating
      - Streaming services available (Netflix, Amazon Prime, Hulu, etc.)
      - URL to the movie page on JustWatch

   **b. TV Show Information:**

      - TV show title
      - Release year
      - Genre
      - IMDb rating
      - Streaming services available (Netflix, Amazon Prime, Hulu, etc.)
      - URL to the TV show page on JustWatch

  **c. Scope:**

```
 ` - Scrape data for at least 50 movies and 50 TV shows.
   - You can choose the entry point (e.g., starting with popular movies,
     or a specific genre, etc.) to ensure a diverse dataset.`

```


**2. Data Filtering & Analysis:**

   After scraping the data, use Pandas to perform the following tasks:

   **a. Filter movies and TV shows based on specific criteria:**

   ```
      - Only include movies and TV shows released in the last 2 years (from the current date).
      - Only include movies and TV shows with an IMDb rating of 7 or higher.
```

   **b. Data Analysis:**

   ```
      - Calculate the average IMDb rating for the scraped movies and TV shows.
      - Identify the top 5 genres that have the highest number of available movies and TV shows.
      - Determine the streaming service with the most significant number of offerings.
      
   ```   

**3. Data Export:**

```
   - Dump the filtered and analysed data into a CSV file for further processing and reporting.

   - Keep the CSV file in your Drive Folder and Share the Drive link on the colab while keeping view access with anyone.
```

**Submission:**
```
- Submit a link to your Colab made for the assignment.

- The Colab should contain your Python script (.py format only) with clear
  comments explaining the scraping, filtering, and analysis process.

- Your Code shouldn't have any errors and should be executable at a one go.

- Before Conclusion, Keep your Dataset Drive Link in the Notebook.
```



**Note:**

1. Properly handle errors and exceptions during web scraping to ensure a robust script.

2. Make sure your code is well-structured, easy to understand, and follows Python best practices.

3. The assignment will be evaluated based on the correctness of the scraped data, accuracy of data filtering and analysis, and the overall quality of the Python code.

# **Start The Project**

## **Task 1:- Web Scrapping**
"""

#Installing all necessary labraries
!pip install bs4
!pip install requests
!pip install wordcloud

#import all necessary labraries
import requests
from bs4 import BeautifulSoup
import time
import re
import pandas as pd
import numpy as np
import csv
from datetime import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt

"""## **Scrapping Movies Data**"""

# Specifying the URL from which movies related data will be fetched
url = 'https://www.justwatch.com/in/movies?release_year_from=2000'

# Sending an HTTP GET request to the URL
page = requests.get(url)
# Parsing the HTML content using BeautifulSoup with the 'html.parser'
soup = BeautifulSoup(page.text,'html.parser')
# Printing the prettified HTML content
print(soup.prettify())

"""## **Fetching Movie URL's**"""

# Write Your Code here
# Initialize an empty list to store complete movie URLs
movies_link_list = []

# Set the main website URL
main_website_url = r'https://www.justwatch.com'

# Find all <a> tags with the specified class
movies_link = soup.find_all('a', class_="title-list-grid__item--link")

# Iterate through each <a> tag in the list
for link in movies_link:
    # Extract the value of the href attribute (movie URL)
    movie_url = link.get('href')

    # Combine the main website URL with the movie URL and append to the list
    movies_link_list.append(main_website_url + movie_url)

# Print the list of complete movie URLs
print(movies_link_list)

"""## **Scrapping Movie Title**"""

# Write Your Code here
# Initialize an empty list to store movie titles
movie_title_list = []

# Loop through each link in the movies_link_list
for link in movies_link_list:
    # Assign the current link to a variable
    url_from_list = link

    # Send a GET request to the URL
    page = requests.get(url_from_list)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the <h1> tag in the parsed HTML
    h1_tag = soup.find('h1')

    # Check if <h1> tag is found
    if h1_tag:
        # Extract the text of the <h1> tag and remove leading/trailing spaces
        movie_title = h1_tag.text.strip()
        # Append the extracted movie title to the movie_title_list
        movie_title_list.append(movie_title)
    else:
        # If <h1> tag is not found, append a message indicating the title was not found
        movie_title_list.append(f"Movie title not found for {url_from_list}")

    # Pause the execution for 3 seconds before processing the next link
    time.sleep(3)

# Print the list of extracted movie titles
print(movie_title_list)

"""## **Scrapping release Year**"""

# Write Your Code here
# Initialize an empty list to store movie release year
release_year_list = []

# Iterate through each movie link in the list (list_of_movies_links)
for link in movies_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the movie release year
    release_span = soup.find('span', class_='text-muted')

    # Check if the release year is found
    if release_span:
        release_year = release_span.text.strip('() ').replace('(', '').replace(')', '')  # Remove leading/trailing parentheses and whitespace
        release_year_list.append(release_year)
    else:
        release_year_list.append(f"Release year not found for {link}")

    # Pause the execution for 3 seconds before processing the next link
    time.sleep(3)

# Print the list of extracted release year
print(release_year_list)

"""## **Scrapping Genres**"""

# Write Your Code here
# Initialize an empty list to store genres
genres_list = []

# Loop through each link in the movies_link_list
for link in movies_link_list:
    # Get the URL from the current link in the list
    url_from_list = link

    # Send a GET request to the URL
    page = requests.get(url_from_list)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the genre heading in the HTML with class 'detail-infos__subheading' and text 'Genres'
    genre_heading = soup.find('h3', class_='detail-infos__subheading', string='Genres')

    # Check if genre heading is found
    if genre_heading:
        # Find the next div with class 'detail-infos__value' after the heading
        genre_div = genre_heading.find_next('div', class_='detail-infos__value')

        # Check if genre_div is found
        if genre_div:
            # Get the text inside the div and strip any leading/trailing whitespace
            genres = genre_div.get_text(strip=True)
            # Append the genres to the genres_list
            genres_list.append(genres)
        else:
            # If genre_div is not found, append a message indicating genres were not found for the URL
            genres_list.append(f"Genres not found for {url}")
    else:
        # If genre_heading is not found, append a message indicating genres were not found for the URL
        genres_list.append(f"Genres not found for {url}")

    # Pause execution for 3 seconds
    time.sleep(3)

# Print the list of genres
print(genres_list)

"""## **Scrapping IMBD Rating**"""

# Write Your Code here
# Initialize an empty list to store IMDb ratings
imdb_rating_list = []

# Loop through each movie link in the movies_link_list
for link in movies_link_list:
    url_from_list = link

    # Send a GET request to the movie URL
    page = requests.get(url_from_list)

    # Parse the HTML content of the page
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all span elements on the page
    rating_spans = soup.find_all('span', class_='')

    # Initialize IMDb rating variable
    imdb_rating = None

    # Loop through the rating spans to find the IMDb rating
    for span in rating_spans:
        # Check if the previous sibling of the span has an img with the alt text "IMDB"
        previous_sibling = span.find_previous_sibling('img')
        if previous_sibling and 'IMDB' in previous_sibling['alt']:
            # Use regex to extract the numeric IMDb rating
            match = re.search(r'\d+\.\d+', span.get_text(strip=True))
            if match:
                imdb_rating = match.group(0)
                break

    # Append the IMDb rating to the list, or a not found message if no rating was found
    if imdb_rating:
        imdb_rating_list.append(imdb_rating)
    else:
        imdb_rating_list.append(f"IMDb rating not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of IMDb ratings
print(imdb_rating_list)

"""## **Scrapping Runtime/Duration**"""

# Write Your Code here
# Initialize an empty list to store the durations
duration_list = []

# Iterate through each movie link in the list (movies_link_list)
for link in movies_link_list:
    # Set the current URL to the movie link
    url_from_list = link

    # Sending an HTTP GET request to the URL to fetch the webpage content
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the h3 element containing the text 'Runtime'
    runtime_heading = soup.find('h3', string='Runtime')

    # Initialize runtime as None in case the element is not found
    runtime = None

    # Check if the 'Runtime' heading is found
    if runtime_heading:
        # Find the next sibling div containing the runtime information
        runtime_div = runtime_heading.find_next_sibling('div')

        # Check if the sibling div is found
        if runtime_div:
            # Extract the text value of the runtime
            runtime = runtime_div.get_text(strip=True)

    # If runtime information is found, append it to the duration list
    if runtime:
        duration_list.append(runtime)
    else:
        # If runtime information is not found, append a not found message
        duration_list.append(f"Duration not found for {url_from_list}")

    # Pause for 3 seconds before making the next request to avoid overloading the server
    time.sleep(3)

# Print the final list of durations
print(duration_list)

"""## **Scrapping Age Rating**"""

# Write Your Code here
# Initialize an empty list to store age ratings
age_rating_list = []

# Iterate through each movie link in the list (movies_link_list)
for link in movies_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the h3 element containing the text 'Age rating'
    age_rating_heading = soup.find('h3', string='Age rating')

    # Initialize age_rating as None in case the element is not found
    age_rating = None

    # If the age rating heading is found, proceed to find the age rating value
    if age_rating_heading:
        # Find the next sibling div containing the age rating information
        age_rating_div = age_rating_heading.find_next_sibling('div')

        # If the sibling div is found, extract the text value of the age rating
        if age_rating_div:
            age_rating = age_rating_div.get_text(strip=True)

    # If age rating is found, add it to the list and print it
    if age_rating:
        age_rating_list.append(age_rating)
    else:
        # If age rating is not found, add a message to the list
        age_rating_list.append(f"Age rating not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of age ratings
print(age_rating_list)

"""## **Fetching Production Countries Details**"""

# Write Your Code here
# Initialize an empty list to store production countries
production_country_list = []

# Iterate through each movie link in the list (movies_link_list)
for link in movies_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all div elements with class 'detail-infos'
    detail_infos_divs = soup.find_all('div', class_='detail-infos')

    # Initialize production_country as None
    production_country = None

    # Loop through each detail-infos div to find the production country
    for div in detail_infos_divs:
        # Find the h3 element inside the detail-infos div
        h3_element = div.find('h3')

        # Check if the h3 element exists and contains the text 'Production country'
        if h3_element and 'Production country' in h3_element.get_text():
            # Find the div containing the production country information
            production_country_div = div.find('div', class_='detail-infos__value')

            # Check if the production country div is found
            if production_country_div:
                # Extract the text value of the production country
                production_country = production_country_div.get_text(strip=True)
                break  # Stop searching if production country is found

    # Add the production country to the list or add a message if not found
    if production_country:
        production_country_list.append(production_country)
    else:
        production_country_list.append(f"Production country not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of production countries
print(production_country_list)

"""## **Fetching Streaming Service Details**"""

# Write Your Code here
# Initialize an empty list to store streaming services
streaming_service_list = []

# Iterate through each movie link in the list (movies_link_list)
for link in movies_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the div containing the streaming service information
    stream_div = soup.find('div', class_='buybox-row stream')

    # Initialize streaming_service as None
    streaming_service = None

    # If the stream div is found, extract the streaming service name
    if stream_div:
        # Find the anchor tag within the stream div
        stream_anchor = stream_div.find('img')['alt']

        # Check if the anchor tag exists and extract the text value (streaming service name)
        if stream_anchor:
            streaming_service = stream_anchor

    # Add the streaming service to the list or add a message if not found
    if streaming_service:
        streaming_service_list.append(streaming_service)
    else:
        streaming_service_list.append(f"Streaming service not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of streaming services
print(streaming_service_list)

"""## **Now Creating Movies DataFrame**"""

# Write Your Code here
# Creating the dictinary of movies data
movies_data = {
    'movies_titles'     : movie_title_list,
    'release_year'      : release_year_list,
    'genre'             : genres_list,
    'imdb_rating'       : imdb_rating_list,
    'duration'          : duration_list,
    'age_rating'        : age_rating_list,
    'production_country': production_country_list,
    'streaming_service' : streaming_service_list,
    'movie_url'         : movies_link_list,
}

# Creating the DataFrame from the dictinary
movies_df = pd.DataFrame(movies_data)

# Display the first 5 rows of the movies_df DataFrame
movies_df.head(5)

# Display the last 5 rows of the movies_df DataFrame
movies_df.tail(5)

"""## **Scraping TV  Show Data**"""

# Specifying the URL from which tv show related data will be fetched
tv_url='https://www.justwatch.com/in/tv-shows?release_year_from=2000'
# Sending an HTTP GET request to the URL
page=requests.get(tv_url)
# Parsing the HTML content using BeautifulSoup with the 'html.parser'
soup=BeautifulSoup(page.text,'html.parser')
# Printing the prettified HTML content
print(soup.prettify())

"""## **Fetching Tv shows Url details**"""

# Write Your Code here
# Initialize an empty list to store complete movie URLs
tvshows_link_list = []

# Set the main website URL
main_website_url = r'https://www.justwatch.com'

# Find all <a> tags with the specified class
tvshows_link = soup.find_all('a', class_="title-list-grid__item--link")

# Iterate through each <a> tag in the list
for link in tvshows_link:
    # Extract the value of the href attribute (tv shows URL)
    tvshows_url = link.get('href')

    # Combine the main website URL with the tv shows URL and append to the list
    tvshows_link_list.append(main_website_url + tvshows_url)

# Print the list of tv shows URLs
print(tvshows_link_list)

"""## **Fetching Tv Show Title details**"""

# Write Your Code here
# Initialize an empty list to store tv shows titles
tv_title_list = []

# Loop through each link in the tvshows_link_list
for link in tvshows_link_list:
    # Assign the current link to a variable
    url_from_list = link

    # Send a GET request to the URL
    page = requests.get(url_from_list)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the <h1> tag in the parsed HTML
    h1_tag = soup.find('h1')

    # Check if <h1> tag is found
    if h1_tag:
        # Extract the text of the <h1> tag and remove leading/trailing spaces
        tvshows_title = h1_tag.text.strip()
        # Append the extracted movie title to the tvshows_title_list
        tv_title_list.append(tvshows_title)
    else:
        # If <h1> tag is not found, append a message indicating the title was not found
        tv_title_list.append(f"Tv show title not found for {url_from_list}")

    # Pause the execution for 3 seconds before processing the next link
    time.sleep(3)

print(tv_title_list)

"""## **Fetching Release Year**"""

# Write Your Code here
# Initialize an empty list to store tv shows release year
tv_release_year_list = []

# Iterate through each tv show link in the list (list_of_tv_shows_links)
for link in tvshows_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the tv shows release year
    release_span = soup.find('span', class_='text-muted')

    # Check if the release year is found
    if release_span:
        release_year = release_span.text.strip('() ').replace('(', '').replace(')', '')  # Remove leading/trailing parentheses and whitespace
        tv_release_year_list.append(release_year)
    else:
        tv_release_year_list.append(f"Release year not found for {link}")

    # Pause the execution for 3 seconds before processing the next link
    time.sleep(3)

# Print the list of extracted release year
print(tv_release_year_list)

"""## **Fetching TV Show Genre Details**"""

# Write Your Code here
# Initialize an empty list to store genres
tv_genres_list = []

# Loop through each link in the tvshows_link_list
for link in tvshows_link_list:
    # Get the URL from the current link in the list
    url_from_list = link

    # Send a GET request to the URL
    page = requests.get(url_from_list)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the genre heading in the HTML with class 'detail-infos__subheading' and text 'Genres'
    genre_heading = soup.find('h3', class_='detail-infos__subheading', string='Genres')

    # Check if genre heading is found
    if genre_heading:
        # Find the next div with class 'detail-infos__value' after the heading
        genre_div = genre_heading.find_next('div', class_='detail-infos__value')

        # Check if genre_div is found
        if genre_div:
            # Get the text inside the div and strip any leading/trailing whitespace
            genres = genre_div.get_text(strip=True)
            # Append the genres to the genres_list
            tv_genres_list.append(genres)
        else:
            # If genre_div is not found, append a message indicating genres were not found for the URL
            tv_genres_list.append(f"Genres not found for {url}")
    else:
        # If genre_heading is not found, append a message indicating genres were not found for the URL
        tv_genres_list.append(f"Genres not found for {url}")

    # Pause execution for 3 seconds
    time.sleep(3)

# Print the list of genres
print(tv_genres_list)

"""## **Fetching IMDB Rating Details**"""

# Write Your Code here
# Initialize an empty list to store IMDb ratings
tv_imdb_rating_list = []

# Loop through each movie link in the tvshows_link_list
for link in tvshows_link_list:
    url_from_list = link

    # Send a GET request to the movie URL
    page = requests.get(url_from_list)

    # Parse the HTML content of the page
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all span elements on the page
    rating_spans = soup.find_all('span', class_='')

    # Initialize IMDb rating variable
    imdb_rating = None

    # Loop through the rating spans to find the IMDb rating
    for span in rating_spans:
        # Check if the previous sibling of the span has an img with the alt text "IMDB"
        previous_sibling = span.find_previous_sibling('img')
        if previous_sibling and 'IMDB' in previous_sibling['alt']:
            # Use regex to extract the numeric IMDb rating
            match = re.search(r'\d+\.\d+', span.get_text(strip=True))
            if match:
                imdb_rating = match.group(0)
                break

    # Append the IMDb rating to the list, or a not found message if no rating was found
    if imdb_rating:
        tv_imdb_rating_list.append(imdb_rating)
    else:
        tv_imdb_rating_list.append(f"IMDb rating not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of IMDb ratings
print(tv_imdb_rating_list)

"""## **Fetching Age Rating Details**"""

# Write Your Code here
# Initialize an empty list to store age ratings
tv_age_rating_list = []

# Iterate through each movie link in the list (tvshows_link_list)
for link in tvshows_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the h3 element containing the text 'Age rating'
    age_rating_heading = soup.find('h3', string='Age rating')

    # Initialize age_rating as None in case the element is not found
    age_rating = None

    # If the age rating heading is found, proceed to find the age rating value
    if age_rating_heading:
        # Find the next sibling div containing the age rating information
        age_rating_div = age_rating_heading.find_next_sibling('div')

        # If the sibling div is found, extract the text value of the age rating
        if age_rating_div:
            age_rating = age_rating_div.get_text(strip=True)

    # If age rating is found, add it to the list and print it
    if age_rating:
        tv_age_rating_list.append(age_rating)
    else:
        # If age rating is not found, add a message to the list
        tv_age_rating_list.append(f"Age rating not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of age ratings
print(tv_age_rating_list)

"""## **Fetching Production Country details**"""

# Write Your Code here
# Initialize an empty list to store production countries
tv_production_country_list = []

# Iterate through each movie link in the list (tvshows_link_list)
for link in tvshows_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find all div elements with class 'detail-infos'
    detail_infos_divs = soup.find_all('div', class_='detail-infos')

    # Initialize production_country as None
    production_country = None

    # Loop through each detail-infos div to find the production country
    for div in detail_infos_divs:
        # Find the h3 element inside the detail-infos div
        h3_element = div.find('h3')

        # Check if the h3 element exists and contains the text 'Production country'
        if h3_element and 'Production country' in h3_element.get_text():
            # Find the div containing the production country information
            production_country_div = div.find('div', class_='detail-infos__value')

            # Check if the production country div is found
            if production_country_div:
                # Extract the text value of the production country
                production_country = production_country_div.get_text(strip=True)
                break  # Stop searching if production country is found

    # Add the production country to the list or add a message if not found
    if production_country:
        tv_production_country_list.append(production_country)
    else:
        tv_production_country_list.append(f"Production country not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of production countries
print(tv_production_country_list)

"""## **Fetching Streaming Service details**"""

# Write Your Code here
# Initialize an empty list to store streaming services
tv_streaming_service_list = []

# Iterate through each movie link in the list (tvshows_link_list)
for link in tvshows_link_list:
    # Set the current URL
    url_from_list = link

    # Sending an HTTP GET request to the URL
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the div containing the streaming service information
    stream_div = soup.find('div', class_='buybox-row stream')

    # Initialize streaming_service as None
    streaming_service = None

    # If the stream div is found, extract the streaming service name
    if stream_div:
        # Find the anchor tag within the stream div
        stream_anchor = stream_div.find('img')['alt']

        # Check if the anchor tag exists and extract the text value (streaming service name)
        if stream_anchor:
            streaming_service = stream_anchor

    # Add the streaming service to the list or add a message if not found
    if streaming_service:
        tv_streaming_service_list.append(streaming_service)
    else:
        tv_streaming_service_list.append(f"Streaming service not found for {url_from_list}")

    # Pause for 3 seconds before making the next request
    time.sleep(3)

# Print the list of streaming services
print(tv_streaming_service_list)

"""## **Fetching Duration Details**"""

# Write Your Code here
# Initialize an empty list to store the durations
tv_duration_list = []

# Iterate through each movie link in the list (tvshows_link_list)
for link in tvshows_link_list:
    # Set the current URL to the tvshow link
    url_from_list = link

    # Sending an HTTP GET request to the URL to fetch the webpage content
    page = requests.get(url_from_list)

    # Parsing the HTML content using BeautifulSoup with the 'html.parser'
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find the h3 element containing the text 'Runtime'
    runtime_heading = soup.find('h3', string='Runtime')

    # Initialize runtime as None in case the element is not found
    runtime = None

    # Check if the 'Runtime' heading is found
    if runtime_heading:
        # Find the next sibling div containing the runtime information
        runtime_div = runtime_heading.find_next_sibling('div')

        # Check if the sibling div is found
        if runtime_div:
            # Extract the text value of the runtime
            runtime = runtime_div.get_text(strip=True)

    # If runtime information is found, append it to the duration list
    if runtime:
        tv_duration_list.append(runtime)
    else:
        # If runtime information is not found, append a not found message
        tv_duration_list.append(f"Duration not found for {url_from_list}")

    # Pause for 3 seconds before making the next request to avoid overloading the server
    time.sleep(3)

# Print the final list of durations
print(tv_duration_list)

"""## **Creating TV Show DataFrame**"""

# Write Your Code here
# Creating the dictinary of tv shows data
tvshows_data = {
    'tv_shows_titles'   : tv_title_list,
    'tv_release_year'      : tv_release_year_list,
    'tv_genre'             : tv_genres_list,
    'tv_imdb_rating'       : tv_imdb_rating_list,
    'tv_duration'          : tv_duration_list,
    'tv_age_rating'        : tv_age_rating_list,
    'tv_production_country': tv_production_country_list,
    'tv_streaming_service' : tv_streaming_service_list,
    'tv_show_url'       : tvshows_link_list,
}

# Creating the DataFrame from the dictinary
tvshows_df = pd.DataFrame(tvshows_data)

# Display the first 5 rows of the tvshows_df DataFrame
tvshows_df.head(5)

# Display the last 5 rows of the tvshows_df DataFrame
tvshows_df.tail(5)

"""## **Task 2 :- Data Filtering & Analysis**

- Only include movies and TV shows released in the last 2 years (from the current date).
      - Only include movies and TV shows with an IMDb rating of 7 or higher.
"""

# Write Your Code here
# Get the current date
current_date = datetime.now()

# Extract the year from the current date
current_year = current_date.year

# Convert 'movies_release_years' column to numeric
movies_df['release_year'] = pd.to_numeric(movies_df['release_year'], errors='coerce')
tvshows_df['tv_release_year'] = pd.to_numeric(tvshows_df['tv_release_year'], errors='coerce')
movies_df['imdb_rating'] = pd.to_numeric(movies_df['imdb_rating'], errors='coerce')
tvshows_df['tv_imdb_rating'] = pd.to_numeric(tvshows_df['tv_imdb_rating'], errors='coerce')

# Function to filter movies based on release year
def filter_movies(movies_df, current_year):
    filterd_movies = movies_df[
        (movies_df['release_year'].between(current_year - 2, current_year)) &
        (movies_df['imdb_rating'] >= 7)
        ]
    return filterd_movies

# Function to filter TV shows based on release year
def filter_tv_shows(tvshows_df, current_year):
    filterd_tv_shows = tvshows_df[
        (tvshows_df['tv_release_year'].between(current_year - 2, current_year)) &
        (tvshows_df['tv_imdb_rating'] >= 7)
        ]
    return filterd_tv_shows

# Filter and sort movies and TV shows
filterd_movies = filter_movies(movies_df, current_year)
filterd_tv_shows = filter_tv_shows(tvshows_df, current_year)

# Display the filtered movies first 3 rows
filterd_movies.head(3)

# Display the filtered movies last 3 rows
filterd_movies.tail(3)

# Display the filtered tv shows first 3 rows
filterd_tv_shows.head(3)

# Display the filtered tv shows last 3 rows
filterd_tv_shows.tail(3)

"""## **Calculating Mean IMDB Ratings for both Movies and Tv Shows**"""

# Write Your Code here
# Calculate the mean IMDb rating for movies
mean_imdb_rating_movies = movies_df['imdb_rating'].astype(float).mean()

# Calculate the mean IMDb rating for TV shows
mean_imdb_rating_tv_shows = tvshows_df['tv_imdb_rating'].astype(float).mean()

# Printing the Mean IMDb Rating for Movies and Tv Shows
print(f"Mean IMDb Rating for Movies: {mean_imdb_rating_movies:.2f}")
print(f"Mean IMDb Rating for TV Shows: {mean_imdb_rating_tv_shows:.2f}")

"""## **Analyzing Top Genres**"""

# Write Your Code here
# Analyze top genres for movies
top_genres_movies = movies_df['genre'].str.split(', ', expand=True).stack().value_counts().head(5)

top_genres_movies_data = {
    'Genre': top_genres_movies.index,
    'Count': top_genres_movies.values
}

# Create DataFrame
top_genres_movies_df = pd.DataFrame(top_genres_movies_data)

# Displaying top genres tv DataFrame
top_genres_movies_df

# Analyze top genres for TV shows
top_genres_tv = tvshows_df['tv_genre'].str.split(', ', expand=True).stack().value_counts().head(5)

top_genres_tv_data = {
    'Genre': top_genres_tv.index,
    'Count': top_genres_tv.values

}

# Create DataFrame
top_genres_tv_df = pd.DataFrame(top_genres_tv_data)

# Displaying top genres tv DataFrame
top_genres_tv_df

#Let's Visvalize it using word cloud
# Generate a word cloud for movies
wordcloud_movies = WordCloud(
    width=800,
    height=400,
    background_color='lightgrey',
    colormap='viridis',
    max_words=100,
    contour_width=3,
    contour_color='steelblue',
).generate_from_frequencies(top_genres_movies)

# Plot the word cloud for movies
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud_movies, interpolation='bilinear')
plt.title('Top Genres for Movies', fontsize=16, color='black')
plt.axis('off')
plt.show()

# Generate a word cloud for TV shows
wordcloud_tv_shows = WordCloud(
    width=800,
    height=400,
    background_color='lightgrey',
    colormap='viridis',
    max_words=100,
    contour_width=3,
    contour_color='steelblue',
).generate_from_frequencies(top_genres_tv)

# Plot the word cloud for TV shows
plt.figure(figsize=(20, 6))
plt.imshow(wordcloud_tv_shows, interpolation='bilinear')
plt.title('Top Genres for TV Shows', fontsize=16, color='black')
plt.axis('off')
plt.show()

"""## **Finding Predominant Streaming Service**"""

# Write Your Code here
# Streaning services movies
streaming_services_movies = movies_df['streaming_service'].str.split(', ', expand=True).stack().value_counts()

# Filter the series to include only services with a count greater than 2
streaming_services_movies = streaming_services_movies[streaming_services_movies >= 2]

# Streaming services tv shows
streaming_services_tv_shows = tvshows_df['tv_streaming_service'].str.split(', ', expand=True).stack().value_counts()

# Filter the series to include only services with a count greater than 2
streaming_services_tv_shows = streaming_services_tv_shows[streaming_services_tv_shows >= 2]

#Let's Visvalize it using word cloud
# Generate a word cloud for streaming services in movies
wordcloud_movies_services = WordCloud(
    width=800,
    height=400,
    background_color='lightgrey',
    colormap='plasma',
    max_words=100,
    contour_width=3,
    contour_color='orange',
).generate_from_frequencies(streaming_services_movies)

# Plot the word cloud for streaming services in movies
plt.figure(figsize=(16, 6))
plt.imshow(wordcloud_movies_services, interpolation='bilinear')
plt.title('Predominant Streaming Services for Movies', fontsize=16, color='black')
plt.axis('off')
plt.show()

# Generate a word cloud for streaming services in TV shows
wordcloud_tv_shows_services = WordCloud(
    width=800,
    height=400,
    background_color='lightgrey',
    colormap='plasma',
    max_words=100,
    contour_width=3,
    contour_color='orange',
).generate_from_frequencies(streaming_services_tv_shows)

# Plot the word cloud for streaming services in TV shows
plt.figure(figsize=(16, 6))
plt.imshow(wordcloud_tv_shows_services, interpolation='bilinear')
plt.title('Predominant Streaming Services for TV Shows', fontsize=16, color='black')
plt.axis('off')
plt.show()

"""## **Task 3 :- Data Export**"""

#saving final dataframe as Final Data in csv format

# Save filtered movies dataframe to CSV
movies_df.to_csv('Final_movies_data.csv', index=False)

# Save filtered TV shows dataframe to CSV
tvshows_df.to_csv('Final_tv_shows_data.csv', index=False)

#saving filter data as Filter Data in csv format

# Save filtered movies dataframe to CSV
filterd_movies.to_csv('filtered_movies_data.csv', index=False)

# Save filtered TV shows dataframe to CSV
filterd_tv_shows.to_csv('filtered_tv_shows_data.csv', index=False)

"""# **Dataset Drive Link (View Access with Anyone) -**

https://drive.google.com/drive/folders/1_3bEG7L5ASdjs5OIT0Lojk5eSzbEokq3?usp=sharing

# ***Congratulations!!! You have completed your Assignment.***
"""
