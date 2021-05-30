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
print("강의 리스트")
for course in courses:
    print(course.get_text())
print("------------------------------------")
# 강의 세부페이지 링크 긁어오기
id = 0
for link in courselist.find_all('a'):
    id += 1
    print("id : ", id)
    url = link.get('href') #링크 긁어오기
    response=session.get(url)   #링크로 넘어가기
    response.raise_for_status()
    soup=BeautifulSoup(response.text,"html.parser")
    currentweek = soup.find("div", {"class": "course_box course_box_current"})  #해당주차
    section = currentweek.find("ul", {"class": "section img-text"}) 
    
    if section != None:
        #li class activity assign modtype_assign (과제)
        if section.find("li", {"class": "activity assign modtype_assign "}) != None:
            instance = section.find("li", {"class": "activity assign modtype_assign "})
            assignment_link = instance.find('a').get('href')
            assignment_name = instance.find("span", {"class": "instancename"})
            print("과제명 : ", assignment_name.get_text())
            print("과제링크 : ", assignment_link)
            response=session.get(assignment_link)   #링크로 넘어가기
            response.raise_for_status()
            soup=BeautifulSoup(response.text,"html.parser")
            submissionstatus = soup.find("div", {"class": "submissionstatustable"})
            alltr = submissionstatus.find_all("tr")
            duedate = alltr[2].find("td", {"class": "cell c1 lastcol"})
            print("duedate : ", duedate)

        #li class activity vod modtype_vod (강의VOD)
        if section.find("li", {"class": "activity vod modtype_vod "}) != None:
            instance = section.find("li", {"class": "activity vod modtype_vod "})
            vod_name = instance.find("span", {"class": "instancename"})
            vod_link = instance.find('a').get('onclick')
            vod_duedate = instance.find("span", {"class":"text-ubstrap"})
            print("vod 명 : ",vod_name.get_text())
            print("vod 링크 : ",vod_link)
            print("duedate : ",vod_duedate.get_text())

        #li class activity url modtype_url (강의 link)
        if section.find("li", {"class": "activity url modtype_url "}) != None:
            instance = section.find("li", {"class": "activity url modtype_url "})
            link_name = instance.find("span", {"class": "instancename"})
            vod_link = instance.find('a').get('onclick')
            print("강의 명 : ", link_name.get_text())
            print("강의 링크 : ",vod_link)

        #li class activity quiz modtype_quiz (퀴즈)
        if section.find("li", {"class": "activity quiz modtype_quiz "}) != None:
            instance = section.find("li", {"class": "activity quiz modtype_quiz "})
            quiz_name = instance.find("span", {"class": "instancename"})
            print("퀴즈 명 : ",quiz_name.get_text())
            if instance.find('a') != None:
                quiz_link = instance.find('a').get('href')
                print("퀴즈 링크 : ",quiz_link)
            else:
                print("no link")
    else:
        print("No Assginment / Lecture / Quiz")
            
    print("------------------------------------")
        
    
    
    
    