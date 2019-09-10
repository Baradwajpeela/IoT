from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)
from time import sleep,time

while True:

	with open("/home/baradwaj/Desktop/firstupload.txt", "r")as file:
		file_drive = drive.CreateFile({'title': os.path.basename(file.name)})
		print(time())
		file_drive.SetContentString(file.read() + str(time())) 
	file_drive.Upload()
	print("#########")
	sleep(600)