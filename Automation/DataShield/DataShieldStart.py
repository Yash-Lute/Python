import sys
import os
import time
import schedule
import shutil


def BackupFiles(Source,Destination):
    copied_files=list();
    print("Create the backup folder for backup process")
    os.makedirs(Destination,exist_ok=True) #if folder already present still continue 
    
    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path=os.path.join(root,file)
            relative=os.path.relpath(src_path,Source)
            des_path=os.path.join(Destination,relative)
            
            os.makedirs(os.path.dirname(des_path),exist_ok=True)
            
            #Copy the files if its new 
            shutil.copy2(src_path,des_path) # its copies the files with their metadata (inode no,date modified)
            copied_files.append(relative)
    return copied_files
             
def MarvellousDataShieldStart(Source="Data"):
    BackupName="MarvellousBackup"
    
    print("Backup process staarted successfully at :",time.ctime())
    
    BackupFiles(Source,BackupName)
        

        
        
def main():
    Border="-"*50
    print(Border)
    print("------Marvellous Data Shield System--------")
    print(Border)
    
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to :")
            print("1: Takes auto backup at given time")
            print("2: backup only new and updated files")
            print("3: Create an archive of backup periodically")
            
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to back up")
           
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    # python Demo.py 5 Data
    elif    (len(sys.argv)==3):
        print("Inside project logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])
        print("Data Shield  System started successfully")
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl+C to stop the execution")
        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
        
        
    else:
        print("Inavild no of command line arguments ")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")
        
    
        
        
        
        
        
    
    print(Border)
    print("------------Thank You for using our script--------")
    print(Border)
    
if __name__ == '__main__':
    main()
    