code = input().strip()
n = len(code)

numbers = list()

result = ''
for i in range(len(code) + 1):
    numbers.append(i + 1)
    if i == len(code) or code[i] == 'I':
                # run till stack is empty
                while numbers:
                    # remove top element from the stack and add it to solution
                    result += str(numbers.pop())

print(result)