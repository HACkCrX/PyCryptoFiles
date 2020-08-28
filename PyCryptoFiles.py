import pyAesCrypt
import getpass
from os import system as cmd
from os import popen
from time import sleep
import os
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import hashlib
from cryptography.fernet import Fernet
import random
import platform
from clear_screen import clear





def Banner():
	print(Fore.CYAN+"""
   _   _   _   _   _   _   _   _     _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ 
 ( P | y | C | r | y | p | t | o ) ( F | i | l | e | s )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ 

[==>] Created by: NoOAYe   [<==]                                             
[==>]    Version: 0.2      [<==]
[==>] 010101010101010101   [<==]  
     
\____________________________________________________/  

		""")
	

	print(Style.RESET_ALL)


def encryption():
	GCWD = os.getcwd()

	clear()
	Mrak = Fore.RED+"[-]"+Style.RESET_ALL
	username = getpass.getuser()
	bufferSize = 64 * 1024
	Banner()
	print()
	Folder = input('[=>] Insert Folder Path [<=]: ')
	if os.path.isdir(Folder)==True:
		pass

	else:
		print(Mrak+ ' Error Exception: Path Not [exists] Press Enter To Continue [<=]')
		input()
		encryption()

	print()
	print(Fore.CYAN+'++++++++++++++++++++++++++++++++++++++')
	print(Style.RESET_ALL)
	print("[=>] Insert Password [<=]: ")
	print()
	Passwd  = getpass.getpass('[~]:{}@Shell => '.format(username)) 
	clear()
	Mrakp = Fore.GREEN+"[+]"+Style.RESET_ALL
	print(Fore.CYAN+'***************************************'+Style.RESET_ALL)
	print(Mrakp+' Start Encryption [=>] Files [<=] 010101 ')
	print(Fore.CYAN+'***************************************'+Style.RESET_ALL)
	sleep(0.40)
	clear()
	
	result = hashlib.sha512(Passwd.encode()).hexdigest() 
	with open('key.txt', 'w+') as out:
		out.write(result)
	

	os.chdir(Folder)
	listFiles = os.listdir()
	Mrakp = Fore.GREEN+"[+]"+Style.RESET_ALL
	for i in listFiles:
		outputfile=i+".aes"
		pyAesCrypt.encryptFile(i, outputfile, Passwd, bufferSize)
		Check_IMG_Ex = i.split('.')
		Mrak = Fore.RED+"[-]"+Style.RESET_ALL
		IMG_EX = Check_IMG_Ex[-1]
		extensions = [
		'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES [danger]
		'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
	    'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
	    'yml', 'yaml', 'json', 'xml', 'csv', # structured data
	    'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images
	    'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
	    'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
	    'java', 'class', 'jar', # java source code
	    'ps', 'bat', 'vb', # windows based scripts
	    'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
	    'go', 'pyc', 'bf', 'coffee', # other source code files
		'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw','jpeg','webp', # images
		'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
		'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp','ts', # Video and movies
		'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak' 
		] 
		if IMG_EX in extensions :
			print(Mrakp,"Encrypt => {}".format(i))
		else:
			print(Mrak,'Faild To Encrypt => {} Extension Not Supported'.format(i))


		System = platform.platform().split("-")[0]
		if System=="Windows":
			cmd('del {}'.format(i))
		elif System=="Linux":
			cmd('rm {}'.format(i))
	print(Style.RESET_ALL)
	os.chdir(GCWD)
	input('[=>] PRESS [ENTER] TO CONTINUE [<=]')




def Decryption():
	GCWD = os.getcwd()
	os.chdir(GCWD)
	clear()
	username = getpass.getuser()
	bufferSize = 64 * 1024
	Banner()
	print()
	Folder = input('[=>] Insert Folder Path [<=]: ')
	if os.path.isdir(Folder)==True:
		pass

	else:
		Mrak = Fore.RED+"[-]"+Style.RESET_ALL
		print(Mrak+ ' Error Exception: Path Not [exists] Press Enter To Continue [<=]')
		input()
		Decryption()
	print()
	print(Fore.CYAN+'++++++++++++++++++++++++++++++++++++++')
	print(Style.RESET_ALL)
	print("[*] Insert Password")
	print()
	Mrakp = Fore.GREEN+"[+]"+Style.RESET_ALL
	Passwd  = getpass.getpass('[~]:{}@Shell => '.format(username)) 
	result = hashlib.sha512(Passwd.encode()).hexdigest() 
	clear()
	
	System = platform.platform().split("-")[0]
	if System=="Windows":
		KEY_PATH =  GCWD+"\\"+'key.txt'
		
	elif System=="Linux":
		KEY_PATH =  GCWD+"/"+'key.txt'
	
	Mrak = Fore.RED+"[-]"+Style.RESET_ALL
	with open(KEY_PATH, 'r') as out:
		READ_HASH_PASS = out.read()

	if result == READ_HASH_PASS:
		print(Fore.CYAN+'***************************************'+Style.RESET_ALL)
		print(Mrakp+' Start Decryption [=>] Files [<=] 010101 ')
		print(Fore.CYAN+'***************************************'+Style.RESET_ALL)
		sleep(0.40)
		clear()
		os.chdir(Folder)
		listFiles = os.listdir()
		for i in listFiles:
			outputfile=i.split('.')
			GetFileNameEx = outputfile[0]+"."+outputfile[-2]
			try:
				pyAesCrypt.decryptFile(i, GetFileNameEx, Passwd, bufferSize)
			except ValueError:
				pass
				print(Mrak+' Not Encrypted File => {} '.format(i))
			else:
				print(Mrakp,"Decrypt => {} ".format(i))

			System = platform.platform().split("-")[0]
			if System=="Windows":
				cmd('del {}'.format(i))
			elif System=="Linux":
				cmd('rm {}'.format(i))
		print(Style.RESET_ALL)

		input('[=>] PRESS [ENTER] TO CONTINUE [<=]')

	else:
		Mrak = Fore.RED+"[-]"+Style.RESET_ALL
		print(Mrak,' Exception: [=>] [WorngPassword]:',end="")
		input('[=>] PRESS [ENTER] TO CONTINUE [<=]')
		sys.exit()
		




def Banners():
	B1 = """
 __, , _  _, __, , _ __, ___  _,   __, _ _,  __,  _,
 |_) \ | / ` |_) \ | |_)  |  / \   |_  | |   |_  (_ 
 |    \| \ , | \  \| |    |  \ /   |   | | , |   , )
 ~     )  ~  ~ ~   ) ~    ~   ~    ~   ~ ~~~ ~~~  ~ 
      ~'          ~'                                
[==>]  Created by: NoOAYe    [<==]                                             
[==>]    Version -> 0.2      [<==]
[==>] 010101010101010101     [<==]

\____________________________________________________/  
	"""

	B2 = """
 ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ 
||P |||y |||C |||r |||y |||p |||t |||o |||       |||F |||i |||l |||e |||s ||
||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|

[==>]  Created by: NoOAYe    [<==]                                             
[==>]    Version -> 0.2      [<==]
[==>] 010101010101010101     [<==]

\____________________________________________________/  
	"""

	B3 = """
  ^    ^    ^    ^    ^    ^    ^    ^       ^    ^    ^    ^    ^  
 /P\  /y\  /C\  /r\  /y\  /p\  /t\  /o\     /F\  /i\  /l\  /e\  /s\ 
<___><___><___><___><___><___><___><___>   <___><___><___><___><___>

[==>]  Created by: NoOAYe    [<==]                                             
[==>]    Version -> 0.2      [<==]
[==>] 010101010101010101     [<==]

\____________________________________________________/  
	"""
	
	B4 = """
___  _   _ ____ ____ _   _ ___  ___ ____    ____ _ _    ____ ____ 
|__]  \_/  |    |__/  \_/  |__]  |  |  |    |___ | |    |___ [__  
|      |   |___ |  \   |   |     |  |__|    |    | |___ |___ ___] 
                                                                                  
[==>]  Created by: NoOAYe    [<==]                                             
[==>]    Version -> 0.2      [<==]
[==>] 010101010101010101     [<==] 
   
\____________________________________________________/  
""" 
	Banners = [Fore.CYAN+B1,Fore.BLUE+B2,Fore.GREEN+B3,Fore.RED+B4]
	print(random.choice(Banners))
	print(Style.RESET_ALL)
	
#main 
while True:
	clear()
	Banners()
	
	print()
	print('[1] Encryption')
	print("[2] Decryption")
	print()
	
	try:
		ch = int(input("[=>]:PyCryptoFiles@Shell[<=]: "))
	except KeyboardInterrupt:
		print()
		print("[+] Detecting [CTRL+C] Quiting.... ", end="")
		sleep(0.25)
		clear()
		sys.exit()
	except ValueError:
		continue

	if ch==1:
		encryption()

	elif ch==2:
		Decryption()



	else:
		continue


