
#Vamo a ber como integramos esto de Tktinter en el login que ya tenemoh.
#Vamo a implementar el resto de weas de loops y condiciones ---

from tkinter import *
import Login
import os

#Creating a hopefullly fancy window
def StartWindow():
	global main_window #Makes sense to be global, right?
	button_clr="DarkGrey"
	window_dimensions= "300x250"
	window_title="My First Login O"
	#set window properties
	main_window=Tk() #ITS HAPPENING :O
	main_window.geometry(window_dimensions)
	main_window.title(window_title)
	
	#build the window (list the elements)
	Label(text="Escoja su opcion",bg="LightGreen",width="300",height="2",font=("Calibri",13)).pack()
	Label(text="").pack()

	Button(text="Acceder", height="2", width="30", bg=button_clr,command=login).pack()
	Label(text="").pack()
	Button(text="Registrarse", height="2", width="30", bg=button_clr,command=registro).pack()
	Label(text="").pack()
	
	#set this as the main window...?
	main_window.mainloop()

def login():
	global login_window
	#This window spawns over the main window
	login_window=Toplevel(main_window)
	#window variables and properties
	button_clr="DarkGrey"
	window_dimensions= "300x250"
	window_title="Put your data in the box B|"

	login_window.geometry(window_dimensions)
	login_window.title(window_title)

	#number of tries
	global password_counter
	global username_counter
	password_counter = 3
	username_counter = 3 

	#vars to store login data
	global check_user
	global check_password

	check_user = StringVar()
	check_password = StringVar()

	global entry_user_login
	global entry_password_login

	#building the window
	Label(login_window, text="DAME LOS DATOS", font = ("Calibri",42)).pack()
	Label(login_window, text="").pack()

	Label(login_window, text="Usuario:").pack()

	entry_user_login = Entry(login_window, textvariable = check_user)
	entry_user_login.pack()
	Label(login_window, text="").pack()

	Label(login_window, text="Contraseña:").pack()
	
	entry_password_login = Entry(login_window, textvariable = check_password, show='*')
	entry_password_login.pack()
	Label(login_window, text="").pack()

	Button(login_window, text="Acceder", height="2", width="30", bg=button_clr,command=verifica_login).pack()


def verifica_login():
	#Almacena lo que se ingreso en las cajas
	usuario1 = check_user.get()
	clave1 = check_password.get()

	global password_counter
	global username_counter

	entry_user_login.delete(0,END)
	entry_password_login.delete(0,END)

		#CHECK USERNAME AND PASSWORD AND DEPENDING ON THE OUTPUT DO:
	#AND TO FINISH, CREATE A WINDOW WITH THE MESSAGE

	#The windows already close without killing the program. what you need is a counter and a function capable to saying "Fk u" when the chances run out.

	
	if Login.CheckUsername(usuario1): #the username exists
		if Login.CheckPw(usuario1, clave1): #the password is correct
			message_window("Todo bien master")
		else:
			password_counter = password_counter -1
			if password_counter == 0:
				message_window("Se acabaron los intentos.")
				close_window(login_window)
			else:
				message_window("La contraseña esta mal master. Tienes %i intentos restantes."%password_counter)
			
	else:
		username_counter = username_counter -1
		if username_counter == 0:
				message_window("Se acabaron los intentos.")
				close_window(login_window)
		else:
			message_window("El usuario no existe master. Tienes %i intentos restantes."%username_counter)







def message_window(window_text):
	global msg_window
	try: 
		login_window
	except NameError:
		msg_window = Toplevel(signup_window)
	else:
		msg_window = Toplevel(login_window)
		
	msg_window.title("Aviso")
	msg_window.geometry("150x100")

	Label(msg_window, text=window_text).pack()
	Button(msg_window, text="OK",command= lambda: close_window(msg_window)).pack()

def close_window(window):
	window.destroy( )

def registro():
	global signup_window #Makes sense to be global, right?
	signup_window = Toplevel(main_window)
	button_clr="DarkGrey"
	window_dimensions= "300x250"
	window_title="Put your data in the box B|"
	
	signup_window.geometry(window_dimensions)
	signup_window.title(window_title)
	
	global username
	global password
	global entry_name
	global entry_password

	global username_counter
	username_counter = 3

	username = StringVar()
	password = StringVar()
	
	 #ITS HAPPENING :O

	
	Label(signup_window, text="Introduzca datos",bg="LightGreen").pack()
	Label(text="").pack()

	tag_name = Label(signup_window, text="Nuevo usuario:")
	tag_name.pack()

	entry_name = Entry(signup_window, textvariable = username)
	entry_name.pack()

	tag_password = Label(signup_window, text="Contraseña:")
	tag_password.pack()

	entry_password = Entry(signup_window, textvariable = password, show='*')
	entry_password.pack()

	Label(signup_window, text="").pack()

	Button(signup_window, text="Registrarse", width="10", height="1", bg="LightGreen",command=registro_usuario).pack()

def registro_usuario(): #AQUI DEBO EMPEZAR A INTEGRAR CON LO QUE HICE ANTES
	
	global username_counter
	exists = False


	user_info = username.get()
	password_info = password.get()

	entry_name.delete(0,END)
	entry_password.delete(0,END)

	for name in Login.accdic:
		if user_info == name:
			username_counter = username_counter -1
			if username_counter == 0:
				message_window("Se acabaron los intentos.")
				close_window(signup_window)
				return
			else:
				message_window("That name already exists. You have %i tries left."%username_counter)
				exists = True 
				break

	#(OPEN THE FILE AND WRITE THE STUFF).exe
	if not exists:
		Login.CreateAccount(user_info,password_info)
		Login.accdic[user_info] = password_info
		Label(signup_window, text="Registro completado! ",fg="Green", font=("Calibri", 11)).pack()

		exists = False


if __name__ == "__main__":
	
	Login.LoadAccountDictionary()
	StartWindow()