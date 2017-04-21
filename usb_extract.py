import sys
import os
from os.path import isfile,join,isdir
import subprocess as sp
import shutil
import webbrowser
#import mtTkinter as tk
import Tkinter as tk
import tkMessageBox



def pull_operation(deviceid):
	file_name='log.txt'
	src='//sdcard//'+ file_name
	dest=os.path.join(os.getcwd(),'extracted')
	if (isdir(dest)):
		shutil.rmtree(dest)
	os.makedirs(dest)
	os.chdir(dest)
	cmd = 'adb -s ' + deviceid +' pull ' + src
	try:
		adb = sp.Popen(cmd,shell=True)
		adb.wait()
		webbrowser.open(file_name)
	except:
		tkMessageBox.showinfo("ERROR!", "unexpected error, try again")			
		return

def list_devices():
	for ele in root.winfo_children():
		ele.destroy()
	refreshbutton = tk.Button(root,text ="refresh device list",command = list_devices)
	refreshbutton.pack()

	devices = check_devices()
	if devices == -1:
		return #error!!

	for i in range(0,len(devices)):
			deviceid = devices[i]
			displaytext = 'fetch '+ deviceid
			devicelist = tk.Button(	root,text =displaytext,command = lambda: pull_operation(devices[i]))
			devicelist.pack()

def check_devices():
	device_list = sp.check_output("adb devices",shell=True)
	device_list = device_list.split()
	if len(device_list)>4: #List of devices attached is 4
		device_list=device_list[4:] #removes above elements
		device_list = device_list[::2]
		return device_list

	else:
		tkMessageBox.showinfo("ERROR!", "no device connected")
		return -1

root = tk.Tk()
root.title("root file copy")
root.geometry('500x400')

listdevices = tk.Button(root,text ="list devices",command = list_devices)
listdevices.pack()

tk.mainloop()