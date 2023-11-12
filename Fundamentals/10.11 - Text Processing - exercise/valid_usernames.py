# Write a program that reads usernames on a single line (separated by ", ")
#   and prints all valid usernames on separate lines.
# A valid username:
# has length between 3 and 16 characters inclusive
# can contain only letters, numbers, hyphens, and underscores
# has no redundant symbols before, after, or in between

usernames = input().split(", ")

for valid_username in usernames:
    if 3 <= len(valid_username) <= 16:
        if valid_username.isalnum() or "-" in valid_username or "_" in valid_username:
            print(valid_username)
