import csv

with open("file_handling/hacker_news.csv","r",encoding="utf-8") as f:
 count=0
 for line in f:
#   if "javascript" in line.lower():
  if "java" in line.lower():
   count+=1
 print(count)