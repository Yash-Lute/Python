import psutil
import sys
import os
import time
import schedule
Border="-"*50
def CreateLog(FolderName):
    Ret=False
    Ret=os.path.exists(FolderName)
    if Ret==True:
        Ret=os.path.isdir(FolderName)
        if Ret==False:
            print("Unable to create the folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created sucessfully ")
        
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name :",FileName)
    fobj=open(FileName,"w")
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System-----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")
    fobj.write("----------------System report-----------------------\n")
    #print("CPU usage :",psutil.cpu_percent())
    fobj.write("CPU usage: %s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")
    mem=psutil.virtual_memory()
    #print("Ram usage : ",mem.percent)
    fobj.write("Ram usage : %s %%\n"%mem.percent)
    fobj.write(Border+"\n")
    
    fobj.write("\n Disk usage report\n")
    fobj.write(Border+"\n")
    for part in psutil.disk_partitions():
        try:
            usage=psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s ->%s %% used\n"%(part.mountpoint,usage.percent))
        except:
            pass
    fobj.write(Border+"\n")
    net=psutil.net_io_counters()
    fobj.write("\n Network Usage report")
    fobj.write("Sent : %.2f MB\n"%(net.bytes_sent/(1024*1024)))
    fobj.write("Recv : %.2f MB\n"%(net.bytes_recv/(1024*1024)))
    fobj.write(Border+"\n")
    #process log
    fobj.write(Border+"\n")
    fobj.write("-----end of file----------------")
    fobj.write(Border+"\n")
    

        
        
def main():
    
    print(Border)
    print("------Marvellous Platform Surveillance System-----")
    print(Border)
    
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Exceute periodically")
            print("3 : Senads mail with log")
            print("4 : Store information about processs")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName :  Name of directory to create auto logs ")
        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    # python Demo.py 5 Marvellous
    elif    (len(sys.argv)==3):
        print("Inside project logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])
        print("Platform Surveillance System started successfully")
        print("Directory creadted with name : ",sys.argv[2])
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
    