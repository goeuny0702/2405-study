# 23년 8월 부동산 실거래가 데이터(apt2308.cv) 전처리 및 분석
# 강원도에 120m2이상 3억원 이하인 아파트만 검색한 결과를 임의의 csv파일로 저장

import os, re
import usecsv

os.chdir(r'd:\goeun\python-practice1\240626')

total = usecsv.opencsv("apt2308.csv")

