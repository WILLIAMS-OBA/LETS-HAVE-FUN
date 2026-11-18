average = 0
sum_of_all = 0
for counter in range(10):
    score = int(input("Enter a score: "))
    if score > 0 and score < 100:
        sum_of_all += score
    
average = sum_of_all / counter
print(sum_of_all)
