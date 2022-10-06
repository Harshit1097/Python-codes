# the user will have in his head a number between 0 and 100. The program will guess a number, and the user will say whether it is too high,
# too low, or your number. At the end of this exchange, the program printa out how many guesses it took to guess the number.

# Method : using binary search and narrowing down based on response

alist = range(101)
n = len(alist)
ig = alist[n//2]           # initial guess
start_index = 0
end_index = n
counter = 0

while True:
    counter += 1
    print(f'my guess: {ig}')
    user = input('> ')
    if user.lower() == 'high':
        end_index = alist.index(ig)
        ig = alist[(start_index + end_index)//2]
    elif user.lower() == 'low':
        start_index = alist.index(ig)
        ig = alist[(start_index + end_index)//2]
    elif user.lower() == 'correct':
        break

print(f'I took {counter} attempts to guess that the correct number is {ig}')
