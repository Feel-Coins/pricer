number = int(input('input the number: '))
len_numb = len(str(number))
math = []
for i in str(number):
    len_numb -= 1
    i += "0" * len_numb
    math.append(i)

count = ''
for i in math:
    count += i
    if math.index(i) != len(str(number))-1:
        count += ' + '

print(count)


