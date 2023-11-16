# You will receive lines of input:
# On the first line, you will receive a title of an article
# On the second line, you will receive the content of that article
# On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
# The title should be in "h1" tag (<h1></h1>)
# The content in article tag (<article></article>)
# Each comment should be in div tag (<div></div>)
# For more clarification see the example below.

title = input()
content = input()

content_list = []

while True:
    command = input()
    if command == "end of comments":
        break
    content_list.append(command)

print(f"<h1>\n"
      f"    {title}\n"
      f"</h1>")
print(f"<article>\n"
      f"    {content}\n"
      f"</article>")
for div in content_list:
    print(f"<div>\n"
          f"    {div}\n"
          f"</div>")
