import sys
import os
import subprocess as sp
import webbrowser
import Tkinter as tk
import tkMessageBox



def pull_operation():
	file_name='log.txt'
	src='//sdcard//'+file_name
	dest=os.path.join(os.getcwd(),'extracted')
	if not os.path.exists(dest):
		os.makedirs(dest)
	os.chdir(dest)
	cmd = 'adb pull ' + src 
	a = sp.Popen(cmd,shell=True)
	webbrowser.open('log.txt')

def detect_callback():
	for ele in root.winfo_children():
		ele.destroy()
	w = tk.Button(root,text ="refresh device list",command = detect_callback)
	w.pack()
	devices = check_devices()
	if devices == 1:
		return #error!!

	for i in range(len(devices)):
			w = tk.Button(root,text =devices[i],command = pull_operation)
			w.pack()
	#populate buttons with device name		
	#pull_operation()	

def check_devices():
	device_list = sp.check_output("adb devices",shell=True)
	device_list = device_list.split()
	if len(device_list)>4: #List of devices attached is 4
		device_list=device_list[4:] #removes above elements
		c = 'device'
		if c in device_list:
			device_list.remove(c)
		return device_list	
		'''count = 1
		for i in range(count,len(a)):
			print len(a)
			if count%2==0:
				del a[count-1]
			count+=1
		print a'''
	else:
		tkMessageBox.showinfo("ERROR!", "no device connected")
		return 1

root = tk.Tk()
root.title("root file copy")
root.geometry('500x400')
w = tk.Button(root,text ="list devices",command = detect_callback)
w.pack()

tk.mainloop()