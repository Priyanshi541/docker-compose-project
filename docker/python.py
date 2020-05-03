import os

while True:
	os.system("clear")
	print(" ")
	print("\t\t\t\t    Welcome")   
	print("================================================================================")	
	print(" ")
	print("Press 1: Start Services")
	print("Press 2: Stop Services")
	print("Press 3: Exit")
	print(" " )

	x=input("ENTER YOUR CHOICE : ")

	if int(x)==1:
		os.system("clear")
		print(" " )
		print("WHICH SERVICE DO YOU WANT TO START")
		print(" ")
		print("Press 1: Wordpress")
		print("Press 2: Joomla")
		print("Press 3: Drupal")
		print("Press 4: Own HTML Site")
		print(" " )

		y=input("ENTER YOUR CHOICE : ")

		if int(y)==1:
			os.chdir("/wpcompose")
			os.system("docker-compose up -d")

		elif int(y)==2:
			os.chdir("/joomcompose")
			os.system("docker-compose up -d")
		elif int(y)==3:
			os.chdir("/drupcompose")
			os.system("docker-compose up -d")
		elif int(y)==4:
			os.chdir("/dockcomp")
			os.system("docker-compose up -d --build")
		else:
			print("Wrong Choice")
		input("Press Any Key to Continue...")
		os.system("clear")
	elif int(x)==2:
		os.system("clear")
		print(" " )
		print("WHICH SERVICE DO YOU WANT TO STOP")
		print(" ")
		print("Press 1: Wordpress")
		print("Press 2: Joomla")
		print("Press 3: Drupal")
		print("Press 4: Own HTML Site")
		print( " ")

		z=input("ENTER YOUR CHOICE : ")

		if int(z)==1:
			os.chdir("/wpcompose")
			os.system("docker-compose stop")

		elif int(z)==2:
			os.chdir("/joomcompose")
			os.system("docker-compose stop")
		elif int(z)==3:
			os.chdir("/drupcompose")
			os.system("docker-compose stop")
		elif int(z)==4:
			os.chdir("/dockcomp")
			os.system("docker-compose stop")
		else:
			print("Wrong Choice")
		input("Press Any Key to Continue...")
		os.system("clear")
	elif int(x)==3:
		os.system(exit())
	else:
		print("WRONG CHOICE")
		input("Press Any key to continue...")
