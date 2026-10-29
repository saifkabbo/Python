text = """
Call: 01712345678
Call: +8801712345678
Call: +880 1712-345678
Call: 01912345678
Invalid: 123456789
"""
import re

print(re.findall(r"(\+880)?(01\d{3}-?\d{6})",text))