import os
import sys
import time
import schedule

def DirectoryScanner(dirName="Marvellous"):
    border="-"*50
    timestamp=time.ctime()
    
    logfileName="Marvellous%s.log" %(timestamp)
    logfileName=logfileName.replace(" ","_")
    logfileName=logfileName.replace(":","_")
    fobj=open(logfileName,"w")
    
    fobj.write(border+"\n")
    fobj.write("this ia  a log file created by Marvellous Automation\n")
    fobj.write("This is a Directory Clearner script\n")
    fobj.write(border+"\n")
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
           
            if os.path.getsize(fname)==0:  #Empty file
                EmptyFileCount=EmptyFileCount+1 
                os.remove(fname)
    
    
    
    
    fobj.write("Toatl files scanned : "+str(filecount)+"\n")
    fobj.write("Toatl empty  files found : "+str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(border+"\n")
    fobj.close()
                
                
        
def main():
    border="-"*50
    print(border)
    print("-----------Marvellous Directory  Automation -------")
    print(border)
    
    if (len(sys.argv)!=2):
        print("Invaild No of arguments")
        print("Please specifiy the name of directory")
        return
    
    schedule.every(1).minute.do(DirectoryScanner)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
    #DirectoryScanner(sys.argv[1])
    
    print(border)
    print("-----------Marvellous Directory  Automation -------")
    print(border)
    
    
if __name__=="__main__":
    main()