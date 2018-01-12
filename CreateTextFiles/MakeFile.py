import os
print('The current directory is：',os.getcwd())
fileListName='filelist.txt'
currentFileList=os.listdir()
if fileListName in currentFileList:
    f=open(fileListName,'r')
    fileliststr=f.readline()
    filelist=fileliststr.split(" ")
    for i in filelist:
        f1=open(i,'w+')
        f1.close()
    print("success creating files in 'filelist.txt'")
else:
    noteWords="please create a 'filelist.txt' which contains filename.suffix and space"
    print(noteWords)
    #os.chdir("")
    #print(os.listdir())

