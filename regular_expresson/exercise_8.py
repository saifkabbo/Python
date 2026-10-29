import re

text = """
Important dates:
2026-10-06
1999-01-25
2026-2-5
25-12-2026
2026-13-40
2020-02-29
"""

print(re.findall(r"\d{4}-\d{2}-\d{2}",text))
