text = "Contact me at saif@gmail.com or test123@yahoo.com. Don't use abc@ or hello.com."

import re

print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text))