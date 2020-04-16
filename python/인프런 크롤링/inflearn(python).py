import requests
from bs4 import BeautifulSoup
from save import save_to_file

URL = f"https://www.inflearn.com/courses?s=python&view=list&order=search&page="
LINK = "https://www.inflearn.com"
inflearn_result = requests.get(URL)
#URL에 접속
inflearn_soup = BeautifulSoup(inflearn_result.text,'html.parser')
#URL에 있는 홈페이지 정보를 모두 가져와 저장

pagination = inflearn_soup.find("ul",{"class":"pagination-list"})
pages = pagination.find_all('a',{'class':'pagination-link'})
#하나씩 리스트에 넣어준다.
last_page = pages[-1].get_text(strip=True).strip("<a>")

def extract_job(html):
    tag_py = []
    inflearn_im = html.find("div",{"class":"content_container"})

    name = inflearn_im.find("a").find("h2")
    name_in = name.get_text(strip=True).strip("h2")
    

    tag = inflearn_im.find("a").find("div",{"class":"tags"})
    tags = tag.find_all("span")
    for num in tags:
        tags_py = str(num.string)
        tag_py.append(tags_py)
    tag_in = ", ".join(tag_py)


    rating = inflearn_im.find("div",{"class":"star_solid"})['style'].strip("%").strip("width:").strip(" ")
    ratings = float(rating)
    rating_in = round(ratings)

    price = html["fxd-data"]
    prices = price.split(':')[2]
    price_in = prices[:-1]

    link_in = inflearn_im.find("a").find("h2")["href"]
    
    return {"강의명":name_in, "범주":tag_in, "평점":f"{rating_in}""점", "가격":price_in, "링크":f"{LINK+link_in}"}

jobs = []
prince = []
for page in range(int(last_page)):
    print(f"인프런 페이지 스크랩핑 중 : {page+1}")
    result = requests.get(f"{URL}{page+1}")
    inflearn_py_soup = BeautifulSoup(result.text,"html.parser")
    results = inflearn_py_soup.find_all("div",{"class":"box"})

    for result in results:
        job = extract_job(result)
        extract_job(result)
        jobs.append(job)

    

save_to_file(jobs)

