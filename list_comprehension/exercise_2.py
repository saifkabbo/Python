list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_list=[num for row in list_of_lists for num in row]

print(flatten_list)