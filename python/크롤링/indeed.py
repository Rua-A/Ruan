import requests
# 파이썬에서 요청을 모아둔 모듈  urllib보다 좋다.
from bs4 import BeautifulSoup
# 파서
LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

def get_indeed_pages():
    indeed_result = requests.get(INDEED_URL)
    indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

    #print(indeed_soup.title)
    #각 링크에서 페이지 함수를 가져오고 거기서 페이지 숫자만을 뜻하는 것을 다져온다.
    pagination = indeed_soup.find("div", {"class" : "pagination"})
    pages = pagination.find_all('a')
    spans = []
    for page in pages[0:-1]:
        spans.append(int(page.find("span").string))


    last_page = spans[-1] +1
    return int(last_page)
    #print(last_page) #마지막 숫자를 출력
    #print(spans)
    #print(range(last_page))  range함수는 ()안의 숫자만크 배열을 만들어준다

def extract_job(html):
    title = html.find("div",{"class" : "title"}).find('a')["title"]
    company = html.find("span",{"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else :
        company = str(company.string)
    company = company.strip()
    location = html.find("div",{"class" : "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {
        'title' : title,
        'company' : company, 
        'location': location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
        }


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div",{"class" : "jobsearch-SerpJobCard"})
        print(f"현재 페이지 출력 {page+1}")
        for result in results : 
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_indeed_pages()
    jobs = extract_indeed_jobs(last_page)
    return jobs


