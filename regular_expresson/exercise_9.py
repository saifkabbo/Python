text = """
Call me at 01712345678.
Office: +880 1712-345678.
Wrong: 12345.
Another: +1-202-555-0198.
"""
import re

print(re.findall(r"01\d{9}|\+880 \d{4}-\d{6}",text))