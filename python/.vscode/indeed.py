import requests
# 파이썬에서 요청을 모아둔 모듈  urllib보다 좋다.
from bs4 import BeautifulSoup
# 파서
INDEED_URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50"

def extract_indeed_pages():
    indeed_result = requests.get(INDEED_URL)

    indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

    #print(indeed_soup.title)
    #각 링크에서 페이지 함수를 가져오고 거기서 페이지 숫자만을 뜻하는 것을 다져온다.
    pagination = indeed_soup.find("div", {"class" : "pagination"})
    pages = pagination.find_all('a')
    print(pages)
    spans = []
    for page in pages[0:-1]:
        spans.append(int(page.find("span").string))
    #spans = spans[0:-1]

    last_page = spans[-1]
    #print(last_page) 마지막 숫자를 출력
    #print(spans)
    #print(range(last_page))  range함수는 ()안의 숫자만크 배열을 만들어준다