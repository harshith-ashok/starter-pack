# Simple Script to start with a project

import os

choice = int(input("Language/Framework:\n1.Flask\n2.Angular\n3.Svelte\n:"))

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
else:
    print("Bubye")
