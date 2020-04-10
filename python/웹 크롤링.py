## 파이썬 관련 직업을 찾는 경우의 크롤링 예시
##크롤링한 자료는 엑셀 시트에 입력되게 할 것
##1. 먼저 파이썬으로 웹사이트에 들어간다
##2. 크롤링할 자료가 몇 페이지 인지 확인해야한다(하나하나 들어가야 한다)
##3. 고급 검색을 들어가 한페이지당 몇개의 내용을 보여둘 것인지도 확인한다
##4. 페이지를 번갈아 접속하지 않고 한곳씩 모든 자료를 가져올 것이다
## https://stackoverflow.com/jobs?q=python , https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50

import requests
# 파이썬에서 요청을 모아둔 모듈  urllib보다 좋다.
from bs4 import BeautifulSoup
# 파서

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50")

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
#print(range(last_page))  range함수는 ()안의 숫자만크 배열을 만들어준다.

for n in range(last_page):
    print(f'start={n*50}')
