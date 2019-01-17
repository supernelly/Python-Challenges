class Palindrome():

	@staticmethod
	def is_palindrome(word):
		letters = [x for x in word.lower()]
		
		y = len(letters) - 1
		for x in letters:
			if x == letters[y]:
				y = y - 1
			else:
				return False
		return True
		
print(Palindrome.is_palindrome('Deleveled'))