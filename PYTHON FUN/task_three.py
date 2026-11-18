average = 0
sum_of_all = 0
for counter in range(10):
    score = int(input('Enter a score: '))
    sum_of_all += score
    
average = sum_of_all / counter
print('The average is: ', average)
print("The sum is: ", sum_of_all)
