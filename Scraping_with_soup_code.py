Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>> import csv
>>> from itertools import zip_longest
>>> url = 'https://wuzzuf.net/search/jobs/?q=python&a=hpb'
>>> src = requests.get(url).content
>>> soup = BeautifulSoup (src, 'lxml')
>>> job_titles = soup.find_all('h2',{'class':'css-m604qf'})
>>> company_names = soup.find_all('a',{'class':'css-17s97q8'})
>>> location_names = soup.find_all('span',{'class':'css-5wys0k'})
>>> job_skills = soup.find_all("div",{'class':'css-y4udm8'})
>>> job_title = []
>>> company_name = []
>>> location_name = []
>>> skills = []
>>> for i in range(len(job_titles)):
	job_title.append(job_titles[i].text)
	company_name.append(company_names[i].text)
	location_name.append(location_names[i].text)
	skills.append(job_skills[i].text)

	
>>> print (job_title, location_name, company_name)
['Python Django Developer', 'Python Developer (FinTech)', 'Python Django Developer', 'Junior Python Developer', 'Senior Backend Engineer - Python', 'Python Developer - Internship', 'Senior Python (Django) Engineer', 'Python Developer', 'Senior Python Backend Engineer- Core API.', 'Senior Python Backend Engineer Core DB', 'Lead Python Developer', 'Python Or Electron Framework Developer (Knowledge Survivor - Desktop Application)', 'Senior Python Developer', 'Flask Python Developer', 'Senior DevOps Engineer'] ['Dubai, United Arab Emirates ', 'Smart Village, Giza, Egypt ', 'New Cairo, Cairo, Egypt ', 'Dokki, Giza, Egypt ', 'Heliopolis, Cairo, Egypt ', 'Maadi, Cairo, Egypt ', 'Cairo, Egypt ', 'New Cairo, Cairo, Egypt ', 'Cairo, Egypt ', 'Cairo, Egypt ', 'Cairo, Egypt ', 'Oakville, Canada ', 'Sofia, Bulgaria ', 'Cairo, Egypt ', 'Heliopolis, Cairo, Egypt '] ['Confidential -', 'Bright Creations -', 'Mentor Seven -', 'RDI -', 'Trufla -', 'TMentors -', 'GetTechForce.com -', 'Bydotpy -', 'Twerlo -', 'Twerlo -', 'Twerlo -', 'ItsTime -', 'CLOUDSIGMA AG -', 'Cyber security  Company -', 'Luftborn -']
>>> file_list = [job_title,company_name,location_name,skills]
>>> exported = zip_longest(*file_list)
>>> with open ('D:\data\Wuzzuf.csv','w') as myfile:
	wr = csv.writer(myfile)
	wr.writerow(['job title', 'Company', 'location', 'skills' ])
	wr.writerows(exported)

	
35
>>> 