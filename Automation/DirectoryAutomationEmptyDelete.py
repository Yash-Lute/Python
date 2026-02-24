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
    
    for FolderName,SubFolder,FileName in os.walk(dirName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            print("File Name : ",fname)
            print("File size : ",os.path.getsize(fname))
            if os.path.getsize(fname)==0:    #Empty file 
                os.remove(fname)
                
        
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
        
    
    
if __name__=="__main__":
    main()