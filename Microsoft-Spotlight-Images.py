import os, sys, getpass, tempfile, shutil

def findSpotLight(user):
    spot_dir = "C:/Users/" + user + "/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
    if not os.path.isdir(spot_dir):
        input("Function cancelled. Microsoft Spotlight directory was not found.")
        return None
    return spot_dir
    
def makeTempDir(user):
    return tempfile.mkdtemp(None, None, "C:/Users/" + user + "/Desktop")

def copyFiles(source_dir, target_dir, min_size):
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        file = os.path.join(source_dir, file_name)
        if os.path.getsize(file) >= min_size:
            shutil.copy(file, target_dir)

def concatPNG(dir_path):
    if not os.path.isdir(dir_path):
        input("Invalid directory. Press 'ENTER' to close.")
        return 2
    file_names = os.listdir(dir_path)
    if len(file_names) == 0:
        input("No files available in directory.")
        return 3
    for file_name in file_names:
        file = os.path.join(dir_path, file_name)
        if os.path.isfile(file) and os.path.splitext(file_name)[1] == '':
            os.rename(file, file + '.png')
    

def run():
    user = getpass.getuser()
    if spot_dir := findSpotLight(user):
        temp_dir = makeTempDir(user)
        copyFiles(spot_dir, temp_dir, 120000)
        concatPNG(temp_dir)
        return 0
    return 1    
    
if __name__ == "__main__":
    run()
    
