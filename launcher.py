import minecraft_launcher_lib
import subprocess
import os
import config

options = config.options

while True:
	print(f"┌──────────┐\n-PYLAUNCHER-\n└──────────┘\n\nMain menu:\n1. Run instance\n2. Create instance\n3. Exit\n\nFolder: {options['gameDirectory']}\nNickname: {options['username']}\nJVM arguments: {options['jvmArguments']}\nDefault java path: {options['defaultExecutablePath']}")

	s = input("\nSelect (number): ")

	if s == '3':
		exit()
	if s == '2':
		ver = input('Version to install (ex. 1.12.2): ')
		if ver == None:
			pass
		else:
			minecraft_launcher_lib.install.install_minecraft_version(ver, options['gameDirectory'])

	if s == '1':
		ver = input('Version to run (ex. 1.12.2): ')
		if ver == None:
			pass
		else:
			subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(ver, options['gameDirectory'], options))
