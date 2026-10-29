import json

with open("student.json","r",encoding="utf-8") as f:
 data=json.load(f)
 top_student=None
 top_scores=float("-inf")
 for student in data["students"]:
  names=student["name"]
  scores=student["scores"]["python"]
  if scores>top_scores:
   top_scores=scores
   top_student=names
 print(f"Top Scorer = {top_student}\nHeight Score = {top_scores}")

result={
 "name":top_student,
 "python_score":top_scores
 
}

with open("top_student.json","w",encoding="utf-8") as f:
 json.dump(result,f,indent=4)