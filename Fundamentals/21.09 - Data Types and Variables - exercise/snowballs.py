number_of_snowballs = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_score = 0

for i in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    if (weight / time) ** quality > best_score:
        best_weight = weight
        best_time = time
        best_quality = quality
        best_score = int(best_weight / best_time) ** best_quality

print(f"{best_weight} : {best_time} = {best_score} ({best_quality})")
