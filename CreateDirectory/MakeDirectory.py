import os
print('The current directory is：',os.getcwd())
DirListName='dirlist.txt'
#Get the file list in current directory
currentFileList=os.listdir()
#Test wether there is a filelist.txt file
if DirListName in currentFileList:
    f=open(DirListName,'r')
    fileliststr=f.read()
    f.close()
    filelist=fileliststr.split("\n")
    for i in filelist:
        os.mkdir(i)
    print("success creating directories in dirlist")
# no filelist.txt file is found
else:
    noteWords="please create a 'dirlist.txt' which contains directory name, each name should be in one line"
    print(noteWords)