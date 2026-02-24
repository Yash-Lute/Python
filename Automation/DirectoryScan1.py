import os
def main():
    DirectoryName=input("enter the name of directory")
    print("Contests of the directory are : ")
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName) :
        print("Folder name : ",FolderName)
        
        for subf in SubFolderName:
            print("SubFolder name : ",subf)
        for fname in FileName:
            print("File Name : ",fname)
        
    
if __name__ =="__main__":
    main()