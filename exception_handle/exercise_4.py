def show_person_info(**kwargs):
 for k,v in kwargs.items():
  print(f"{k} = {v}")
 

show_person_info(
    name="Saif",
    age=25,
    country="Bangladesh",
    city="Dhaka"
)