import os 
# text = os.environ.get('MESSAGE', None)
is_ascii = lambda s: len(s) == len(s.encode())

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
