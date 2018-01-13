import os
print('The current directory is：',os.getcwd())
DirListName='dirlist.txt'
#Get the directory list in current directory
currentFileList=os.listdir()
#Test wether there is a dirlist.txt file
if DirListName in currentFileList:
    f=open(DirListName,'r')
    dirliststr=f.read()
    f.close()
    dirlist=dirliststr.split("\n")
    for i in dirlist:
        os.mkdir(i)
    print("success creating directories in dirlist")
# no dirlist.txt file is found
else:
    noteWords="please create a 'dirlist.txt' which contains directory name, each name should be in one line"
    print(noteWords)