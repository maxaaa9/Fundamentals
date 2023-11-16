# Every valid date has the following characteristics:
# ⦁	It always starts with two digits, followed by a separator
# ⦁	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
# ⦁	After that, it has a separator and exactly 4 digits (for the year).
# ⦁	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
# ⦁	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT).
#   Use a group backreference to check for this.

import re

input_text = input()
patters = r"([0-9]{2})([/.-])([A-Z][a-z]{2})\2([0-9]{4})\b"

search = re.findall(patters, input_text)
for match in search:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")