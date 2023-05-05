#importing necessary libraries for this project
import os   # This library is used for read & check the files/folders
import shutil    #This library is used for move files to nesssary locations
import time

#reading in all the files inside given folder path
path=r"C:/Users/tuanminhaj/Desktop/files/"    

#list of files,folders contains in the directory
file_name=os.listdir(path)

def move_file():
    #creating required folders according to file types
    folder_names=['csv files','image files','text files']
    for folder in range(3):
        if not os.path.exists(path+folder_names[folder]):
            os.makedirs(path+folder_names[folder])
        
        

    #searching file types and moving those into nessary folders
    for file in file_name:
        if ".csv" in file and not os.path.exists(path+"csv files/"+file):
                shutil.move(path+file,path+"csv files/"+file)
        elif ".jpg" in file and not os.path.exists(path+"image files/"+file):
                shutil.move(path+file,path+"image files/"+file)
        elif ".txt" in file and not os.path.exists(path+"text files/"+file):
                shutil.move(path+file,path+"text files/"+file) 

while True:
    move_file()
    time.sleep(5)   
 
        