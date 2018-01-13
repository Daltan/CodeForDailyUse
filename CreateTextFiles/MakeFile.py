import os
print('The current directory is：',os.getcwd())
fileListName='filelist.txt'
#Get the file list in current directory
currentFileList=os.listdir()
#Test wether there is a filelist.txt file
if fileListName in currentFileList:
    f=open(fileListName,'r')
    fileliststr=f.readline()
    filelist=fileliststr.split(" ")
    for i in filelist:
        # Create a file whose name is from 'filelist.txt'
        f1=open(i,'w+')
        f1.close()
    print("success creating files in 'filelist.txt'")
# no filelist.txt file is found
else:
    noteWords="please create a 'filelist.txt' which contains filename.suffix and space"
    print(noteWords)
    #os.chdir("")
    #print(os.listdir())

