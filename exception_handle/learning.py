

# # try:
# #     year=int(input("Enter your birth year: "))
# #     age=2026-year
    
# # except Exception as e:
# #     print(e)
# # else:
# #     print(age)



# person = {
#     "name": "John",
#     "country": "USA",
#     "city": "New York",
#     "age": 25
# }

#                    PYTHON
#                         │
#         ┌───────────────┼───────────────┐
#         ↓               ↓               ↓
#    Exceptions      Arguments        Iteration
#         │               │               │
#    try/except      Packing/           enumerate
#    else            Unpacking           zip
#    finally         Spreading
#         │               │
#         │          ┌────┴────┐
#         │          ↓         ↓
#         │        *args    **kwargs
#         │          ↓         ↓
#         │        tuple     dict
#         │
#         └── handle errors safely