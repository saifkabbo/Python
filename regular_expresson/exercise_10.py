text = """
Contact: john@gmail.com
Contact: jane@yahoo.com
Contact: bob@hotmail.com
Invalid: alice@gmail
"""
import re

print(re.findall(r"[a-z0-9]+@[a-z]+\.[a-z]{2,}",text))