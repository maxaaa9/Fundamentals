import re


def mirror_validator(string):
    middle_of_string = len(string) // 2
    left_part = string[:middle_of_string]
    right_part = string[middle_of_string:]
    right_part = right_part[::-1]
    if left_part == right_part:
        return True
    return False


def cleaner(validated_string):
    validated_string = validated_string.replace("##", " <=> ")
    validated_string = validated_string.replace("@@", " <=> ")
    validated_string = validated_string.replace("@", "")
    validated_string = validated_string.replace("#", "")
    return validated_string


text = input()
pattern = r"((@|#)[A-Za-z]{3,}\2)((@|#)[A-Za-z]{3,}\4)"

match = re.finditer(pattern, text)
pairs_counter = 0
mirror_list = []
for objects in match:
    object_string = objects.group()
    pairs_counter += 1
    if mirror_validator(object_string):
        mirror_list.append((cleaner(object_string)))


if pairs_counter == 0:
    print("No word pairs found!")
else:
    print(f"{pairs_counter} word pairs found!")

if len(mirror_list) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_list))
