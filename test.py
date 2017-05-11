import subprocess as sp
import selenium

#sp.Popen(cmd, shell=True)
# sp.call["start strings.exe", shell=True]
# sp.call["start strings64.exe", shell=True]
sp.call("strings gmm_storage.db-journal > file.txt", shell=True)
f = open('file.txt', 'r')
data = f.read()
print data
a = data.find("lat")
b = data.find('https', a)
print a
print b

