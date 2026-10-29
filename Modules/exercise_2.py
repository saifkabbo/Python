import exercise_1



def user_id_gen_by_user(character=16,id=5):
 for _ in range(id):
  print(exercise_1.random_user_id(character))

user_id_gen_by_user(5,5)

