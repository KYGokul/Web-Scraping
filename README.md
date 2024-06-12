# JustWatch Web Scraping Project

## Overview
This project involves scraping movie and TV show data from JustWatch, a popular platform for searching content across various streaming services like Netflix, Amazon Prime, Hulu, etc. The scraping is done using Python with BeautifulSoup for HTML parsing. The extracted data is then filtered and analyzed using Pandas, followed by saving the results to a CSV file for further processing.

## Project Steps
### 1. Web Scraping
   - Scraping movie and TV show information including title, release year, genre, IMDb rating, streaming services available, and URL to the respective pages on JustWatch.
   - Scoping: Scraping data for a minimum of 50 movies and 50 TV shows, ensuring diversity by choosing different entry points such as popular movies, specific genres, etc.

### 2. Data Filtering & Analysis
   - Filtering movies and TV shows based on specific criteria like release year (last 2 years), IMDb rating (7 or higher).
   - Data analysis tasks include calculating the average IMDb rating, identifying top 5 genres with the highest number of available content, and determining the streaming service with the most significant offerings.

### 3. Data Export
   - Exporting the filtered and analyzed data into a CSV file for further processing and reporting.
   - Keeping the CSV file in a Drive Folder and sharing the Drive link on colab with view access for anyone.

## Acknowledgments
Thanks to the open-source community for tools and libraries used in this project.
