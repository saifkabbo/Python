text = "The prices are $25, $100 and $7."
import re

print(re.findall(r"[$]\d+",text))