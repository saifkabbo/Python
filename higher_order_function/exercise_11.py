items = [10, "hello", 3.5, True, "Python", 20]
# def get_string_lists(items):
#     result = []

#     for item in items:
#         if isinstance(item, str):
#             result.append(item)

#     return result

result=filter(lambda x: isinstance(x, str), items)

print(list(result))

