sum_of_all = 0
for counter in range(10):
    score = int(input("Enter a score: "))
    while score < 0 or score > 100:
        print("Enter a valid score: ")
        score = int(input("Enter a score: "))
    sum_of_all += score  
    
print(sum_of_all)
