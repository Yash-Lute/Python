import os
import sys

def DirectoryScanner(dirName="Marvellous"):
    Ret=False
    
    Ret= os.path.exists(dirName)
    if Ret==False:
        print("There is no such directory")
        return
        
    Ret=os.path.isdir(dirName)
    
    if Ret==False:
        print("It is not a directory")
        return
    
    filecount=0
    EmptyFileCount=0
    
    for FolderName,SubFolder,FileName in os.walk(dirName):
        
        for fname in FileName:
            filecount=filecount+1
            fname=os.path.join(FolderName,fname)
            print("File Name : ",fname)
            print("File size : ",os.path.getsize(fname))
            if os.path.getsize(fname)==0:  #Empty file
                EmptyFileCount=EmptyFileCount+1 
                os.remove(fname)
    
    border="-"*50
    print(border)
    print("---------------Automation Report -----------------")
    print("Toatl files scanned : ",filecount)
    print("Toatl empty  files found : ",EmptyFileCount)
                
                
        
def main():
    border="-"*50
    print(border)
    print("-----------Marvellous Diectory  Automation -------")
    print(border)
    
    if (len(sys.argv)!=2):
        print("Invaild No of arguments")
        print("Please specifiy the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])
    print(border)
    print("-----------Marvellous Diectory  Automation -------")
    print(border)
    
    
if __name__=="__main__":
    main()