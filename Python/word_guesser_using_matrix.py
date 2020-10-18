'''

Using some counting tricks and matrices, successfully guesses any word of any length.

'''

def main():

	a = ''
	b = ''
	final = ''
	count = 0
	first_matrix = [['A','B','C','D','E','F'],
			['G','H','I','J','K','L'],
			['M','N','O','P','Q','R'],
			['S','T','U','V','W','X'],
			['Y','Z']]
	second_matrix = [['A','G','M','S','Y'],
				['B','H','N','T','Z'],
				['C','I','O','U'],
				['D','J','P','V'],
				['E','K','Q','W'],
				['F','L','R','X']]
	n = input('whats the length of the word you want me to guess?:- ')

	if not n.isdigit():
		print('please enter a number.')
		exit()

	print('  1,   2,   3,   4,   5,   6\n')

	for i in first_matrix:
		print(i)

	for i in range(int(n)):
		x = input('enter the column number which contains the %dth word of the word:- '%(i+1))
		a+=x

	print('  1,   2,   3,   4,   5,   6\n')

	for i in a:
		print(second_matrix[int(i)-1],'\n')

	print('\nDO IT ONE MORE TIME:\n')

	for i in range(int(n)):
		x = input('enter the column number which contains the %dth word of the word:- '%(i+1))
		b+=x

	for i in range(int(n)):
		final += first_matrix[int(b[count])-1][int(a[count])-1]
		count+=1
		
	print('\nThe word is:- ' + final)
main()
