average = 0
sum_of_all = 0
for counter in range(1,11):
    score = int(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Enter a valid score: ")
        score = int(input("Enter a score: "))
    sum_of_all += score  
    average = sum_of_all / counter
    
print(sum_of_all)
print(average)

