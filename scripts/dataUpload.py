import sys
import os
import subprocess

def addfile(cdir,dirName,prefix=""):
    if(prefix ==""):
        print("write 'here' to add the file here")
        print("write 'abort' to cancel")
        print("or write the name of the dir to enter that dir\n\n")
    print(f"{prefix}The current dir is {dirName}")
    possible = ["here","abort"]
    for fil in os.listdir(cdir):
        p = os.path.join(cdir,fil)
        if(os.path.isdir(p)):
            possible.append(fil)
            print(f"{prefix}{fil}")
    ans = ""
    while(ans not in possible):
        ans = input(f"{prefix}Your action:   ")
    if(ans not in ["here","abort"]):
        p = os.path.join(cdir,ans)
        return addfile(p,ans,prefix+"\t")
    elif(ans == "here"):
        return cdir
    elif(ans == "abort"):
        print(">>> ABORTING UPLOAD <<<")
        sys.exit()
    else:
        print("HOW IN THE FUCK")
    


def search(dir_path,filename):
    results = []
    for fil in os.listdir(dir_path):
        p = os.path.join(dir_path,fil)
        if(os.path.isdir(p)):
            results.extend(search(p,filename))
        elif(fil == filename):
            results.append(p)
    return results


try:
    filename =  sys.argv[1]
    filePath = sys.argv[2]
except IndexError:
    raise Exception("You need to pass an arguement to the script")
    sys.exit()

data_dir = "/home/tim/repositories/personal/data"
results = search(data_dir,filename)

if(len(results) > 1):
    raise Exception("Multiple files are found with the same name")
elif(len(results) == 0):
    print("No match for specific filename")
    
    ans = ""
    while(ans != "y" and ans != "n"):
        ans = input("Do you whish to add as a new file? [y/n]   ").lower()

    if(ans == "y"):
        isFile = False
        scp_path = addfile(data_dir,"data/")
    elif(ans == "n"):
        sys.exit()
    else:
        print("WTF")
        sys.exit()
else: # 1 match
    isFile = True
    scp_path = results[0]

print(f"Copying\t{filePath} to\n\t{scp_path}")
ans = ""
while(ans != "y" and ans != "n"):
    ans = input("Do you whish to copy? [y/n]   ").lower()
if(ans == "n"):
    sys.exit()
    
copy_command = f"scp {filePath} {scp_path}"
copying = subprocess.Popen(copy_command.split(),stdout=subprocess.PIPE)
output, _ =copying.communicate()
if(output): print(output)

#changes dir
os.chdir(data_dir)

copying = subprocess.Popen(["git","add",scp_path],stdout=subprocess.PIPE)
output, _ =copying.communicate()
if(output): print(output)

copying = subprocess.Popen(["git","commit","-m",f"'Updated {filename}'"],stdout=subprocess.PIPE)
output, _ =copying.communicate()
if(output): 
    for line in output.splitlines():
        print(line)

copying = subprocess.Popen(["git","push"],stdout=subprocess.PIPE)
output, _ =copying.communicate()
if(output): print(output)
