a = int(input('a = '))
b = int(input('b = '))
c = input('| + | × | ÷ | - |_')
if c == '+':
	an = a + b
elif c == '×':
	an = a * b
elif c == '÷':
	an = a / b
elif c == '-':
	an = a - b
else:
	an = Error
print('Answer = ', an)

from time import sleep
sleep(999)
