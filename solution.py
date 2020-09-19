   #Folder Management System
   #vivek kumar singh

#importing os module
import os

#function to create folders
def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
#function to move files         
def move(fname,files):
    for file in files:
        os.replace(file,f"{fname}/{file}")

files =os.listdir()
files.remove("solution.py")
print(files)

#call create function to create folders 
create("Media")
create("Docs")
create("Img")
create("Others")

#describe the extention for each files for folder
medext=[".mp4",".mp3",".flv"]
docext=[".pdf",".txt",".docx",".doc"]
imgext=[".png",".jpg",".jpeg"]

#image 
img=[]
for file in files:
    if os.path.splitext(file)[1].lower() in imgext:
        img.append(file)
print(img)

#document
docs=[]
for file in files:
    if os.path.splitext(file)[1].lower() in docext:
        docs.append(file)
print(docs)

#media
media=[]
for file in files:
    if os.path.splitext(file)[1].lower() in medext:
        media.append(file)
print(media)

#other
others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in medext) and(ext not in docext ) and(ext not in imgext) and os.path.isfile(file):
        others.append(file)
print(others)

#call move function to move the files in respective folder 
move("Media",media)
move("Img",img)
move("Docs",docs)
move("Others",others)
