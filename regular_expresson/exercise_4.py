sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

import re

def clean_text(x):
    return re.sub(r"[$%@#&;!.?,]+","",x)

# print(clean_text(sentence))

def most_frequent_words(y):
    z=re.split(" ",y)
    count={}
    for i in z:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return sorted(count.items(),key=lambda x:x[1],reverse=True)[:3]
    
print(most_frequent_words(clean_text(sentence)))




