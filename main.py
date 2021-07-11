import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

if __name__ == '__main__':
    files = os.listdir()
    files.remove("main.py")


    createIfNotExist("Images")
    createIfNotExist("Docs")
    createIfNotExist("Media")
    createIfNotExist("Python Files")
    createIfNotExist("Others")

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".docx", ".doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp3", ".mp4", ".flv", ".wav"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    pythonExt = [".py"]
    pythonCodes = [file for file in files if os.path.splitext(file)[1].lower() in pythonExt]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in pythonExt) and os.path.isfile(file):
            others.append(file)



    move("Docs", docs)
    move("Images", images)
    move("Media", medias)
    move("Others", others)
    move("Python Files", pythonCodes)





