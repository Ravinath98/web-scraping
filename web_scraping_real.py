from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/jobskill/python-jobs').text
#print(html_text)
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_='clearfix joblistli')
#print(job)
for job in jobs:
    company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
    skills=job.find('span',class_='srp-skills').text
    #print(skills)
    print(f'''
    Company Name: {company_name.split()[0]}
    Required Skills: {skills}
    ''')
    #print(company_name.split()[0])
