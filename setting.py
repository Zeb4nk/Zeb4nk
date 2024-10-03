import os
print("""
\033[37m  ░█████╗░████████╗██╗  ░█████╗░██████╗░
\033[37m  ██╔══██╗╚══██╔══╝██║  ██╔══██╗╚════██╗
\033[37m  ██║░░╚═╝░░░██║░░░██║  ██║░░╚═╝░░███╔═╝
\033[37m  ██║░░██╗░░░██║░░░██║  ██║░░██╗██╔══╝░░
\033[37m   █████╔ ░░░██║░░░██║  ╚█████╔╝███████╗
\033[37m  ░╚════╝░░░░╚═╝░░░╚═╝  ░╚════╝░╚══════╝

""")

print("""\33[0;32m[1] TERMUX\n[2] VPS\n[3] CANCEL\nWhich one do you use?""")

c = input(">>>: ")
if c == "1":
    os.system("pkg install nodejs")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("npm i header-generator")
    os.system("npm i nik-parse -g")
    os.system("npm i crypto")
    os.system("npm i cluster")
    os.system("npm i user-agents")
    os.system("npm i axios")
    os.system("npm i fake-useragent")
    os.system("pkg install golang")
    os.system("python3 cnc.py")

elif c == "3":
    os.system("clear")

c = input(">>>: ")
if c == "2":
    os.system("sudo apt install nodejs")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("npm i header-generator")
    os.system("npm i nik-parse -g")
    os.system("npm i crypto")
    os.system("npm i cluster")
    os.system("npm i user-agents")
    os.system("npm i fake-useragent")
    os.system("npm i axios")
    os.system("sudo apt install golang")
    os.system("python3 cnc.py")


print("\33[0;32m[ √ ] S U C C E S S F U L L Y")
  
