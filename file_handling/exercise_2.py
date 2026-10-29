with open("file_handling/michelle.txt","r",encoding="utf-8") as f:
 michele=f.read()

with open("file_handling/melina.txt","r",encoding="utf-8") as f:
 melina=f.read()


def clean_text(x):
 import re
 x=re.sub(r"[;'.,-]","",x)
 x=x.lower()
 return x

ct_michele=clean_text(michele)
ct_melina=clean_text(melina)
  
def remove_support_words(x):
 new_words=[]
 from stop_words import stop_words
 words=x.split()
 for word in words:
  if word not in stop_words:
    new_words.append(word)
 return new_words

rev_michele=remove_support_words(ct_michele)
rev_melina=remove_support_words(ct_melina)

def check_text_similarity(x,y):
 x=set(x)
 y=set(y)
 result=x&y
 total_word=len(x|y)
 average=len(result)/total_word
 return average*100

print(check_text_similarity(rev_melina,rev_michele))