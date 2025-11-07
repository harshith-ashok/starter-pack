# Simple Script to start with a project

import os

choice = int(
    input("Language/Framework:\n1.Flask\n2.Angular\n3.Svelte\n4.Express API\n5.Ollama Chat-Bot:"))

if choice == 1:
    os.system("cp -r ~/Dev/Templates/flask-skele .")
    f_name = input("Name of project: ")
    os.system(f"mv ./flask-skele {f_name}")
elif choice == 2:
    os.system("cp -r ~/Dev/Templates/angular-skele .")
    f_name = input("Name of project: ")
    os.system(f"mv ./angular-skele {f_name}")
    os.system(f"cd ./{f_name} && npm install")
elif choice == 3:
    os.system("cp -r ~/Dev/Templates/svelte-skele .")
    f_name = input("Name of project: ")
    os.system(f"mv ./svelte-skele {f_name}")
    os.system(f"cd ./{f_name} && npm install")
elif choice == 4:
    os.system("cp -r ~/Dev/Templates/express-skele .")
    f_name = input("Name of project: ")
    os.system(f"mv ./express-skele {f_name}")
    os.system(f"cd ./{f_name} && npm install")
elif choice == 5:
    os.system("cp -r ~/Dev/Templates/chat-bot-skele/ .")
    f_name = input("Name of project: ")
    os.system(f"mv ./chat-bot-skele/ {f_name}")
    os.system(f"cd ./{f_name}/frontend && npm install")
else:
    print("Bubye")
