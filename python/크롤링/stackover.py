import requests
from bs4 import BeautifulSoup

STO_URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_stack_page():
    stack_result = requests.get(STO_URL)
    stack_soup = BeautifulSoup(stack_result.text, "html.parser")

    pag = stack_soup.find("div",{"class":"s-pagination"})
    pages = pag.find_all("a")
    spans =[]
    for page in pages[0:-1]:
       spans.append(page.find("span"))
    last_page = spans[-1]
    last = last_page.get_text(strip=True).strip("<span>")
    return int(last)
    #아래 range 함수는 int형이어야 하므로 그냥 last_page는 str이어서 int로 변경한다.

def extract_job(html):
    titles = html.find("div",{"class":"grid--cell fl1"}).find("h2").find("a")["title"]
    company,location = html.find("div",{"class":"grid--cell fl1"}).find("h3").find_all("span",recursive=False)
    #recursive=False는 더 깊게 들어있는 span을 가져오는 것을 막는다.
    # 찾은 내용이 두가지 일 경어 첫번째를 comany에 넣고 두번째 내용이 location에 들어간다.
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")#둘다 줄바꿈
    job_id = html['data-jobid']

    return {"title":titles, "company":company,"location":location,"link":f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page): 
        print(f"Scrapping SO : Page:{page}")
        result = requests.get(f"{STO_URL}&pg={page+1}")
        stack_soup = BeautifulSoup(result.text,"html.parser")
        results = stack_soup.find_all("div",{"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_stack_page()
    jobs = extract_jobs(last_page)
    return jobs
