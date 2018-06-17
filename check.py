import os 
import sys

# text = os.environ.get('MESSAGE', None)
is_ascii = lambda s: len(s) == len(s.encode())
main = lambda: print('yes done')

if len(sys.argv) >1:
	text = sys.argv[1]
else:
	text = input('Enter the MESSAGE: \n')

def can_send(text):
	if type(text) != type(''):
		return False, 'Not text'
	if len(text) <= 5:
		return False, 'Text too small'
	if len(text) >=141:
		return False, 'Text too large'
	else:
		return is_ascii(text), text

print(can_send(text))
finish = input('Now do i send the message?')
if finish == 'y':
	main()
else:
	print('fail')
