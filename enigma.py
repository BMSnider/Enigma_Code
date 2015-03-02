def setting(num, list):
	times = 0
	while num > times:
		times += 1
		q = list.pop(0)
		list.append(q)
	return list
	
def switch(list):
	z = raw_input('Do you want to switch to letters? ')
	while z == 'yes':
		let1 = raw_input('What\'s the first letter? ')
		let2 = raw_input('What\'s the second letter? ')
		x = list.index(let1)
		y = list.index(let2)
		list[x], list[y] = let2, let1
		z = raw_input('Do you want to switch another pair? ')
	return list
		
def enigma():
	cho = raw_input('Do you want to encrypt or decrypt a message? ')
	alpha = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
			'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
			'w', 'x', 'y', 'z', ' ', '.']
	rotor1 = [9, 17, 6, 16, 19, 27, 10, 0, 2, 7, 22, 3, 26, 14, 1, 4, 
			24, 20, 18, 11, 21, 8, 15, 25, 5, 13, 12, 23]
	rotor2 = [22, 6, 8, 16, 25, 7, 2, 14, 20, 18, 10, 4, 23, 24, 
			26, 17, 27, 13, 19, 3, 9, 11, 15, 0, 5, 1, 12, 21]
	rotor3 = [7, 10, 11, 19, 0, 22, 9, 24, 27, 18, 20, 6, 15, 14, 8, 
			1, 13, 2, 3, 16, 12, 5, 23, 17, 25, 4, 21, 26]
	turn = [21, 13, 26, 25, 11, 24, 22, 14, 15, 10, 9, 4, 23, 1, 7, 
			8, 19, 27, 20, 16, 18, 0, 6, 12, 5, 3, 2, 17]
	check = []
	code = ''
	count1 = 0
	count2 = 0
	switch(alpha)
	setting(int(raw_input('What is the setting for the first rotor? ')), rotor1)
	setting(int(raw_input('What is the setting for the second rotor? ')), rotor2)
	setting(int(raw_input('What is the setting for the third rotor? ')), rotor3)
	#string = raw_input('What is the secret code? ')
	file = open('c:/users/bert/desktop/input.txt','r+')
	string = file.read()
	file.close()
	if cho == 'encrypt':
		for x in string:
			x = str.lower(x)
			letter = alpha.index(x)
			change1 = rotor1[letter]
			change2 = rotor2[change1]
			change3 = rotor3[change2]
			change4 = turn[change3]
			change5 = turn[change4]
			change6 = rotor3[change5]
			change7 = rotor2[change6]
			change8 = rotor1[change7]
			code = code + alpha[change8]
			count1 = count1 + 1
			y = rotor1.pop(0)
			rotor1.append(y)
			if count1 == len(alpha) + 1:
				count2 = count2 + 1
				z = rotor2.pop(0)
				rotor2.append(z)
				count1 = 0
				if count2 == len(alpha):
					t = rotor3.pop(0)
					rotor3.append(t)
					count2 = 0
		myfile = open('c:/users/bert/desktop/input.txt','w')
		myfile.write(str(code))
		myfile.close()
		print code

	if cho == 'decrypt':
		for x in string:
			letter = alpha.index(x)
			change1 = rotor1.index(letter)
			change2 = rotor2.index(change1)		
			change3 = rotor3.index(change2)
			change4 = turn.index(change3)
			change5 = turn.index(change4)
			change6 = rotor3.index(change5)
			change7 = rotor2.index(change6)
			change8 = rotor1.index(change7)
			code = code + alpha[change8]
			count1 = count1 + 1
			y = rotor1.pop(0)
			rotor1.append(y)
			if count1 == len(alpha) + 1:
				count2 = count2 + 1
				z = rotor2.pop(0)
				rotor2.append(z)
				count1 = 0
				if count2 == len(alpha):
					t = rotor3.pop(0)
					rotor3.append(t)
					count2 = 0
		myfile = open('c:/users/bert/desktop/input.txt','w')
		myfile.write(str(code))
		myfile.close()
		print code

enigma()d


