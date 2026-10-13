print("Golf Score Tracker")
scores = []
score_input = input("Enter a score (q to quit): ")

while score_input.lower() != "q":
    scores.append(int(score_input))
    score_input = input("Enter a score (q to quit): ")

print(f"Scores: {scores}")
print(f"Rounds played: {len(scores)}")

if len(scores) > 0:
    average = sum(scores) / len(scores)
    print(f"Average score: {average:.1f}")
    # Challenge: the lowest score is the best score.
    print(f"Best score: {min(scores)}")
else:
    print("No rounds played yet!")