import requests 
from bs4 import BeautifulSoup

#configurações
url_base ="https://br.indeed.com/empregos?"
results_per_pages = 50

def search_keyword(keyword):
  #faz a busca e de scobre a quantidade de pags
  r_indeed = requests.get(f'{url_base}q={keyword}&limit=50&start=0')
  html_indeed = r_indeed.text
  soup = BeautifulSoup(html_indeed, 'html.parser')

  #descobrindo quantas pags analisando o código
  pages_link = soup.find('ul', class_='pagination-list').find_all('a')

  #lista que armazena pags
  number_of_pages = [0,1]
  for link in pages_link:
    n_page=link.string
    if n_page == None:
      continue
    number_of_pages.append(int(n_page))


  urls=[]
  for pages in number_of_pages[:-1]:
    url = f"{url_base}q={keyword}&limit=50&start={results_per_pages * pages}"
    urls.append(url)
  return scrapping_indeed(urls)
  



def scrapping_indeed(urls):
  all_jobs=[]
  for url in urls:
    #url+request
    r_indeed = requests.get(url)
    #salva html em html_indeed
    html_indeed = r_indeed.text
    #faz a sopa
    soup = BeautifulSoup(html_indeed, 'html.parser')
    #filtrar os cards
    cards = soup.find_all('div', class_="jobsearch-SerpJobCard")
    for card in cards:
      company = card.find('span', class_='company')
      if company == None:
        company = "Não encontrada"
      else:
        company=company.get_text().strip()
      job = {
        'title': card.find('a').get('title'),
        'company': company,
        'location':card.find('span', class_='location').string,
        'how_old': card.find('span', class_='date').string,
        'link_job': f"https://br.indeed.com{card.find('a').get('href')}"
      }
      all_jobs.append(job)
     
  return all_jobs
