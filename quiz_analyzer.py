
scores = []

for i in range(1, 6):
    score = float(input())
    scores.append(score)

print(scores)
total_score = sum(scores)
average_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)
print(total_score)
print(average_score)
print(highest_score)
print(lowest_score)

print("========QUIZ SCORE REPORT========")
