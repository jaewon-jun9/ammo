# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:46:41 2019

@author: upnell
"""
class MyCalendar:
    def __init__(self,y,m): #초기 생성에서 연과 월을 지정
        self.year=y
        self.month=m
        self.data()
    def setYM(self,y,m): #중간에 바꾸고 싶을 때 사용
        self.year=y
        self.month=m
    def data(self): #계산을 위해서 미리 준비한 데이터
        self.monthdays1=[31,28,31,30,31,30,31,31,30,31,30,31] #각 월의 일 수
        self.monthdays2=[31,29,31,30,31,30,31,31,30,31,30,31] #윤년
        self.monthdays3=[31,30,31,30,31,31,30,31,30,31,28,31] #과거 달력 계산을 위해 1을 뒤집음
        self.monthdays4=[31,30,31,30,31,31,30,31,30,31,29,31] #과거 달력 계산을 위해 2를 뒤집음
        self.iniday1=6 #2018.12.1 의 요일(6은 토요일)  2019년 이후의 각 월별 1일의 요일을 판정하기 위한 기초값
        self.iniday2=2 #2019.1.1 의 요일(2는 화요일)  2019년 이전의 각 월별 1일의 요일을 판정하기 위한 기초값
    def mycalendar(self):
        if self.year >= 2019: #2019년 이후의 달력을 위한 요일 위치 계산
            dis=self.year-2019 #기준인 2019년 과의 차이
            iniday=self.iniday1 #요일 계산을 위한 기초값
            for i in range(dis+1): #평년 윤년을 판정하여 요일 계산시에 다른 날짜를 삽입
                weekdays=[] #각 월의 1일의 요일을 저장. 누적하지 않고
                #루프의 마지막에 목적하는 연도의 요일 데이터가 생성된다
                if (i+3)%4==0: #윤년을 판정에 따라 일수를 조정한 값을 사용하기 위함
                    monthdays=self.monthdays2 #윤년기준 사용
                    pass
                else:
                    monthdays=self.monthdays1 #평년기준 사용
                    pass
                for i in range(12): #2019년 1월 1일의 요일위치를 바탕으로
                    #1년치 각월의 시작요일 데이터를 생성
                    weekday=iniday+monthdays[i-1]%7 #월의 일수를 
                    if weekday>=7: #7로 나눈 나머지를 이용
                        weekday=weekday-7 #6이 넘는 경우 7을 빼줌
                        pass
                    weekdays.append(weekday)
                    iniday=weekday #다음 달의 계산을 위해 사용
                    pass
                pass
            pass
        if self.year < 2019: #2018년 이전의 각 월의 시작점을 계산하여 역순으로 저장
            dis=2019-self.year
            iniday=self.iniday2
            for i in range(dis): #목적년도와의 차이
                weekdays=[]#각 월의 1일의 요일을 저장. 누적하지 않고
                #루프의 마지막에 목적하는 연도의 요일 데이터가 생성된다
                if (i+2)%4==0: #윤년판정
                    monthdays=self.monthdays4 #과거로 역산하므로 뒤집어진 배열사용
                    pass#윤념임
                else: #평년
                    monthdays=self.monthdays3 #뒤집어진 평년배열
                    pass
                for i in monthdays: #계산방식은 역순인거 제외하면 편년과 같음
                    weekday=iniday-i%7
                    if weekday<0:
                        weekday=weekday+7
                        pass
                    weekdays.append(weekday)
                    iniday=weekday
                    pass
                pass
            temp=[] #역순인 배열을 뒤집기
            for i in reversed(weekdays):
                temp.append(i)
                pass
            weekdays=temp
            pass
        #여기서부터는 출력부
        if self.year%4==0: #윤년판정
            monthdays=self.monthdays2
            pass
        else:
            monthdays=self.monthdays1
            pass
        print("\t\t",self.year,"년",self.month,"월 달력\n\n일\t월\t화\t수\t목\t금\t토\n") #달력의 헤더
        for i in range(weekdays[self.month-1]): #미리 선언한 배열에서 시작 요일의 위치를 가져와 공백 삽입
            print("\t",end="")
            pass
        for i in range(0,monthdays[self.month-1]): #미리 선언한 배열에서 날짜 수를 가져와서 반복
            print("{:>2}".format(i+1),end="\t")
            if ((i+weekdays[self.month-1])+1)%7 == 0: #시작 요일위치+반복시행수의 합이 7이 될때마다 개행
                print("\n")
                pass
            pass
        print("\n")
        pass