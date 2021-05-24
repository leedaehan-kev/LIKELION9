import requests
from bs4 import BeautifulSoup
      
#세션만들기
session=requests.session()
#로그인 하는 페이지의 general-requestURL에서 url 가져옴
url="https://lms.kau.ac.kr/login/index.php"
      
#가져오고 싶은 데이터 (form data)
data={
    "username":"2017125028",
    "password":"westlangley23!!"  
}
response=session.post(url, data=data ) #요청을 모방하면됨 (get, post, put 등)
      
#로그인 실행
response.raise_for_status()
      
      
#LMS 접근
url="http://lms.kau.ac.kr"
response=session.get(url)
response.raise_for_status()

#Crawling 시작 
soup=BeautifulSoup(response.text,"html.parser")
#강의명 긁어오기
courselist = soup.find("div", {"class": "course_lists"})
courses = courselist.find_all('h3')
for course in courses:
    print(course.get_text())

# 강의 세부페이지 링크 긁어오기
for link in courselist.find_all('a'):
    url = link.get('href') #링크 긁어오기
    response=session.get(url)   #링크로 넘어가기
    response.raise_for_status()
    soup=BeautifulSoup(response.text,"html.parser")
    currentweek = soup.find("div", {"class": "course_box course_box_current"})  #해당주차 과제
    content = currentweek.find("div", {"class": "content"})
    print(content)