# Averages three numbers using a list and a loop

# from cs50 import get_int

# Get scores
scores = []
for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

# Print average
average = sum(scores) / len(scores)
print(f"Average: {average}")

print("average {},scores{}".format(average,scores))