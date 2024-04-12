# Project Overview

## Description

This project utilizes Python to scrape information from the web, implementing Google's Gemini API and Generative AI. Additionally, it applies BeautifulSoup, a Python library for parsing HTML and XML documents, to extract data from web pages.  

## Features

1. **Web Scraping**: Python's BeautifulSoup library is used for scraping data from web pages. This allows the extraction of specific information from HTML or XML documents.

2. **Google's Gemini API**: The project integrates Google's Gemini API, which provides access to a range of machine learning models including Generative AI. This allows for the generation of creative content, text, images, etc., based on trained models.

## Detailed Description

In this project, I copied the HTML code directly from https://www.nlschools.ca/schools/schooldirectory.jsp into an HTML file (websiteone.html). This was because the BeauifulSoup library inaccurately pasrsed the HTML code. Using this code, I scraped information from the given table, getting the School Names, Grades, and direct website pages to each individual school site. Using requests, and BeautifulSoup again, I parsed the HTML code from these individual websites to get further information on the school such as Principle Emails, Guidance Emails, School Emails, School Phone Numbers, and Addresses, and stored it into an excel file. This project was made to automate the process of researching schools for U+ Education.  

## Comments
**websiteone.html**: A copy of https://www.nlschools.ca/schools/schooldirectory.jsp's site's HTML code (The card would inaccurately be parsed through BeautifulSoup) 

**main.py**: The main code, parses HTML and scrapes the information. Stores the information into excel file

**Newfoundlandschools.xlsx**: The result of main.py, all the information on hundreds of newfoundland schools  

