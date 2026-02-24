import hashlib
import os
def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb")
    
    
    hobj=hashlib.md5()
    
    Buffer=fobj.read(1000)
    while (len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)
        
    fobj.close()
    return hobj.hexdigest()
        
def DirectoryWatcher(DirectoryName="Marvellous"):
    Ret=False
    
    Ret=os.path.exists(DirectoryName)
    if Ret==False:
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirectoryName)
    
    if Ret==False:
        print("it is not directory")
        return
    
    for FolderName,SubFloderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            Checksum=CalculateCheckSum(os.path.join(fname))
            
            print(f"File Name : {fname}  Checksum : {Checksum}")
            
            
        
        
        
        
    
def main():
    DirectoryWatcher()

    
    
if __name__=="__main__":
    main()
    
    