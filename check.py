import os 
text = os.environ.get('MESSAGE', None)
# text = "ctpoka"

is_ascii = lambda s: len(s) == len(s.encode())
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
