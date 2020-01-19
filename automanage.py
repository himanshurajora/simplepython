import os
import matplotlib
import shutil


folderpath = '/home/himanshu/Downloads/Manager'
if not os.path.exists(folderpath):
    os.mkdir(folderpath)
else:
    print("folder already exsists")
docpath = '/home/himanshu/Downloads/Manager/Docs'
vidpath = '/home/himanshu/Downloads/Manager/Videos'
musicpath = '/home/himanshu/Downloads/Manager/Audio'
codepath = '/home/himanshu/Downloads/Manager/Codes'
commonpath = '/home/himanshu/Downloads/Manager/Common'
imgpath = '/home/himanshu/Downloads/Manager/Images'
zippath = '/home/himanshu/Downloads/Manager/Zip'
debpath = '/home/himanshu/Downloads/Manager/Deb'
if not os.path.exists(docpath):
    os.mkdir(docpath)
else:
    print("folder already exsists")
if not os.path.exists(vidpath):
    os.mkdir(vidpath)
else:
    print("folder already exsists")
if not os.path.exists(musicpath):
    os.mkdir(musicpath)
else:
    print("folder already exsists")
if not os.path.exists(codepath):
    os.mkdir(codepath)
else:
    print("folder already exsists")
if not os.path.exists(commonpath):
    os.mkdir(commonpath)
else:
    print("folder already exsists")
if not os.path.exists(imgpath):
    os.mkdir(imgpath)
else:
    print("folder already exsists")
if not os.path.exists(zippath):
    os.mkdir(zippath)
else:
    print("folder already exsists")
if not os.path.exists(debpath):
    os.mkdir(debpath)
else:
    print("folder already exsists")
data = []
print(data) 
path = '/home/himanshu/Downloads'
for filename in os.listdir(path):
    filepath = path + "/" + filename
    print(filepath)

    if filename.endswith('.mp4') | filename.endswith('.mkv'):
        print(filename + " is a video")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Videos')
        data.append(1)
    elif filename.endswith('.mp3') | filename.endswith('.wav'):
        print(filename + " is a audio")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Audio')
        data.append(1)
    elif filename.endswith('.jpg') | filename.endswith('.png') | filename.endswith('.jpeg') | filename.endswith('.ico'):
        print(filename + " is a image")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Images')
        data.append(1)
    elif filename.endswith('.deb'):
        print(filename + " is a deb package")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Deb')
        data.append(1)
    elif filename.endswith('.gz') | filename.endswith('.zip') | filename.endswith('.xz') | filename.endswith('.tgz') | filename.endswith('.bz2') | filename.endswith('.tar'):
        print(filename + " is a zip file")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Zip')
        data.append(1)
    elif filename.endswith('.pdf') | filename.endswith('.pptx')| filename.endswith('.ods')| filename.endswith('.doc') | filename.endswith('.xls') | filename.endswith('.xlsx') | filename.endswith('.odt'):
        print(filename + " is a document")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Docs')
        data.append(1)
    elif filename.endswith('.c') | filename.endswith('.html') | filename.endswith('.desktop') | filename.endswith('.py') | filename.endswith('.atom') | filename.endswith('.json')| filename.endswith('.js') | filename.endswith('.php') | filename.endswith('.ts') | filename.endswith('.css')| filename.endswith('.sql'):
        if filename != "automanage.py" and filename != "automanage.desktop":
        	print(filename + " is a coding file")
        	shutil.move(filepath, '/home/himanshu/Downloads/Manager/Codes')
        	data.append(1)
    elif filename != "Manager":
        print(filename + " is an unknown type of file or we just dont know what to do with it")
        shutil.move(filepath, '/home/himanshu/Downloads/Manager/Common')
        data.append(0)
print(data)
pt.plot(data)
pt.show()
