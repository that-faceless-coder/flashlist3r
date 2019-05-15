import os,sys,random,requests
from re import findall
from requests.exceptions import ConnectionError

colour=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m']
color=('\033[0;92m')
colo=('\033[0;96m')
normal=('\033[1;m')

try:
	def top():
		print('#'*71)

	def topspace():
		for x in range(2):
			print('#'+' '*69+'#')
	
	def msg():
		print('#'+' '*15+random.choice(colour)+'Flashlist3r for researchers,pentesters'+normal+' '*15+' #')
		print('#'+' '*22+random.choice(colour)+'IG: @that_faceless_coder'+normal+' '*23+'#')
		print('#'+' '*26+random.choice(colour)+'Flashlist3r v0.9'+normal+' '*27+'#')
		
	#banner
	def banner():
		top()
		topspace()
		msg()
		topspace()	
		top()
	#find subdomins
	def sub_find(site):
		print(random.choice(colour)+"[*] Subdomain Scan Started\n"+normal)
		response = requests.get('https://findsubdomains.com/subdomains-of/' + site).text
		sub = findall(r'(?s)<div class="domains js-domain-name">(.*?)</div>', response)
		print(random.choice(colour)+'[+] Subdomain Results:\n'+normal)
		for i in range (len(sub)):
			subdo =  [str(sub[i])]
			subdom=map(str.strip,subdo)
			subdomain=''.join(subdom)
			subdomain[1:-1]
			print (str((i+1))+' '+subdomain)
			fiLe=open('output.txt','a')
			fiLe.write(subdomain+'\n')
			fiLe.close()
		print(random.choice(colour)+'[+] Data has be saved to /flashlist3r/output.txt'+normal)
		
		

	banner()
	site=raw_input(random.choice(colour)+"Enter Url:"+normal)
	sub_find(site)
except KeyboardInterrupt:
	os.system('clear')
	sys.exit()

except ConnectionError as e:
	print('Please check your internet connection...')


