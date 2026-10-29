text = """
Users: @saif123 @john_doe @alice99
Invalid: @123 @ab @john-123
"""
import re
print(re.findall(r"@[A-Za-z0-9_]{3,12}(?=\s|$)",text))