#Starting the Login script

#Basic
#Will let you create and account and save the data in a file.
#It will ask you for a username and password.
#It will let you in only if the username exists and 
#   it matchs the password.
#Give me the option to login OR create an account
#Don't end the program if something goes wrong, just go to the start
# make that a function
#Make the username match ONLY the FULL username
#Separate Username and Password prompts
#Allow Attempts to insert pw alone
#Chance to change password if you chage ur username when creating an acc.

#Password Shanenugans
##limited tries to insert password.


#comment ur sh1t

#switch open() to with open
#implement dict comprehension




import os

os.chdir('C:\\Users\\Nestico\\Documents\\Python\\Mini_projects\\Login_system')

def CreateAccountFromInput():
	name = input('Insert username.')

	#Checking if the username already exists
	check = False
	while check == False:

		if CheckUsername(name):
			print('That username already exists.')
			if choose('Wanna try another name? 1.Y 2.N'):
				name = input('Insert username.')
				if CheckUsername(name):
					#this name also exists, go again with the loop.
					continue
				else:
					#lets you continue with the account creation
					check = True 
			
			else:
				Exitprompt()
				return
		else: check = True

	password = input('Insert password.')
	#Checking if password meets requirements (WIP?)
	PasswordReqs(password)

	CreateAccount(name,password)
	#Stores the access data in a file
	

def CreateAccount(name,password):
	with open('Database.txt','a') as accounts:
		accounts.write(name+'	'+password+'\n')
	print('Succesfully created the account.')


def Login():
	
	name = input('Insert username.')
	password = input('Insert password')

	#Checking if the username exists.
	if not CheckUsername(name):
		print("username does exist'n.")
		Exitprompt()
		return
		
	#Checks if the password is correct and acts accordingly... 
	CheckPw(name, password)

def CheckUsername(name): 
	namefound = False

	if name in accdic:
		namefound = True

	return namefound

def CheckPw(user, password):
		#Checking if the password is correct
	
	print(accdic[user])
	if accdic[user] == password:
		print('The data matched so i guess you are logged in... where tho?')
		return True
	else:
		print('Incorrect password.')
		return False

		#NewPw(accdic[user])

def NewPw(correctpw):
		counter = 3
		#gives counter tries to get the right password. Everytime the password is wrong but there are tries left, gives you the option to quit.
		while counter > 0:
			print('You have %i tries left to insert a password.'%counter)
			if choose('Yo wanna try the password again? 1. yes 2.no'):

				print(counter)	
				newpw = input('Insert password.')
				if newpw == correctpw:
					LoggedIn()
					return
				else: counter = counter-1
			else:
				Exitprompt()
				return
		print('You have used all your chances. Prepare to dye.')
		Exitprompt()

def PasswordReqs(password):
	pass


def LoggedIn():
	print('Succesfully logged in.')
	return

def Exitprompt():
	
	if choose("try again? 1 yes. 2 no."):
		main()
	else: 
			return

def main():
	
	LoadAccountDictionary()

	if choose("1 to log in, 2 to create an account."):
		print('Log in into your account.')
		Login()
	else:
		print('Insert the data for the new account')
		CreateAccount()


def choose(prompt):
	option = 0

	while option != '1' and option != '2':
		option = input(prompt)
	if option == '1': return True
	else: return False

def LoadAccountDictionary():

	global accdic


	with open('Database.txt') as accounts:
		#take each line in the file, split it to obtain username and password as elements of a dictionary
		accdic = {username:password for line in accounts for (username,password) in [line.strip().split('	',1)]}


accdic = {}

if __name__ == "__main__":
	main()




