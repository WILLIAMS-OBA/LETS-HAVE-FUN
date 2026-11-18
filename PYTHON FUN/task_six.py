average = 0
sum_of_all = 0
for counter in range(10):
    score = int(input('Enter a score: '))
    if score % 2 ==0:
        sum_of_all += score
        counter+1

average = sum_of_all // counter
print("The average is: ", average)
