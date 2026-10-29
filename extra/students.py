with open("students.txt","r",encoding="utf-8") as f:
    text=f.read().splitlines()
    max_score=float("-inf")
    top_name=None
    for line in text:
        name,score = line.split(",")
        if int(score)>max_score:
            max_score=int(score)
            top_name=name
    print(top_name,max_score)

        