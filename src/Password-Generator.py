import mechanicalsoup
import json
from random import randrange
from random import randint

def random_case(string):
	password = ''
	for char in string:
		case = randint(0, 1)
		if case == 0:
			password += char.upper()
		else:
			password += char.lower()			
	return password

def password_generator():
	password_lst = []
	while True:
		try:
			number_keywords = int(input("How many keywords would you like your " 
										"password to be comprised of? "))
			break
		except ValueError:
			print("Input invalid, try again.")
	i = 0	
	while (i < number_keywords):
		try:
			userinput = input("Enter keyword number {}: ".format(i+1)).rstrip()
			url = 'https://api.datamuse.com/words?rel_trg={}'.format(userinput)
			browser = mechanicalsoup.Browser()
			response = browser.get(url)
			data = json.loads(response.text)
			random_num = randrange(len(data)) # randrange throws ValueError is data = 0
			password_lst.append(data[random_num]['word'])
			i += 1
		except ValueError:
			print("Got nothing for that, try again.")

	print("Your randomly generated words were {}.".format('/'.join(password_lst)))
	password = random_case(''.join(password_lst))
	print("Generated password: {}\n".format(password))

def main():
	while True:
		password_generator()

if __name__ == '__main__':
	main()