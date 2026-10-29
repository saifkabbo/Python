paragraph = 'I love teaching. If you do not love teaching what else can you love I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'

import re

prag=re.split(r" ",paragraph)
prag_dict={}
for item in prag:
    if item in prag_dict:
        prag_dict[item]+=1
    else:
        prag_dict[item]=1

result=sorted(prag_dict.items(),key=lambda x:x[1],reverse=True)

print(result)