# Write a program that receives a single string and extracts all email addresses from it.
#   Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:
# {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
# Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
# Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"
# {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".".
#   Each word consists of only letters and can have hyphens "-" between the letters.
# Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
# Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"

import re

text_sentence = input()

pattern = r" (([a-z0-9]+[\.\-\_])?([a-z0-9]+)@([a-z\-]+)(\.\w+)+)"

match = re.findall(pattern, text_sentence)

for mail in match:
    print(mail[0])
