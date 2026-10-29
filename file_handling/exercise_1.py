with open("file_handling/tramp.txt","r",encoding="utf-8") as f:
    text=f.read()



def most_frequest_words(x,n=10):
    import re
    x=re.sub(r"[:.]","",x)
    count_word={}
    for i in x.split():
        if i in count_word:
            count_word[i]+=1
        else:
            count_word[i]=1
    return sorted(count_word.items(),key=lambda x:x[1],reverse=True)[:n]
print(most_frequest_words(text))

