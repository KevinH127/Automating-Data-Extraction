from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook
import google.generativeai as genai
from dotenv import load_dotenv
import os 

load_dotenv()
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)

geminiModel = genai.GenerativeModel('gemini-pro')

def gemeni_response(message):
  return geminiModel.generate_content(message).text

wb= load_workbook('Newfoundlandschools.xlsx')
sheet = wb.active

html_text = open('websiteone.html').read()
page = BeautifulSoup(html_text, 'lxml')
table = page.find('table', class_='schoolDirectoryTable table table-sm responsive nowrap dataTable no-footer dtr-inline')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')

for data in table_row:
  school = data.find('td', class_='dtr-control sorting_1').text 
  grade = data.find('td', class_=None).text
  web = data.find('a', class_="btn btn-xs btn-danger", href=True)
  url = f'https://www.nlschools.ca/schools/{web["href"]}'
  html_text2 = requests.get(url).text
  soup = BeautifulSoup(html_text2, 'lxml')
  
  #Card with CONTACT INFORMATION
  contact_information_card_div = soup.find_all('div')
  text = 'CONTACT INFORMATION'
  for div in contact_information_card_div:
    if div.string == text:
      contact_information_card_body = div.paren 
  
  #Card with EMAIL INFORMATION
  email_information_card_div = soup.find_all('b') 
  text = 'Security Camera(s):'
  for b in email_information_card_div:
    if b.string == text:
      email_information_card_body = b.parent
  
  guidance = gemeni_response(f'What is the the guidance name in this text: {email_information_card_body}? Print the name together (ex. GeminiBot) and If none, print N/A')
  if guidance != 'N/A':
    guidance_email = f'{guidance}@nlesd.ca'
  else:
    guidance_email = 'N/A'

  address = gemeni_response(f'What is the address given this text: {str(contact_information_card_body)}')
  phones = gemeni_response(f'What are the phone numbers given in this text: {str(contact_information_card_body)}? State which one is TEL and which one is FAX (TEL: , FAX:)')
  school_email = gemeni_response(f'What is the email given in this text: {contact_information_card_body}? If none, print N/A')
  principle = gemeni_response(f'Who is the principle given in this text: {email_information_card_body}?')
  principle_email = gemeni_response(f'What is the {principle}s email given in this text: {email_information_card_body}?')
  
  sheet.append([school, address, phones, school_email, principle, principle_email, grade, guidance_email])
  wb.save(filename='Newfoundlandschools.xlsx')