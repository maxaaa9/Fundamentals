import re
text = input()
title = r"<title>([A-Za-z0-9 ]+)<\/title>"
extract_text = r"<body>(.+)<\/body>"
clear_tags = r"<.*?>"

match_title = "".join(re.findall(title, text))

content = "".join(re.findall(extract_text, text))
cleaned_text = re.sub(clear_tags, "", content).replace("\\n", "")

print(f"Title: {match_title}")
print(f"Content: {cleaned_text}")



