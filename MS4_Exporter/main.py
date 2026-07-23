import json
import os
import time
import subprocess
import hashlib
import pathlib

def find_files(d):
    os.chdir(d)
    mscz=[x for x in subprocess.run("find ./*.mscz | cut -c 1-2 --complement", shell=True, capture_output=True, text=True).stdout.split('\n') if x!=""]
    pdf=[x for x in subprocess.run("find ./*.mscz | cut -c 1-2 --complement | sed s/.mscz/.pdf/g", shell=True, capture_output=True, text=True).stdout.split('\n') if x!=""]
    mp3=[x for x in subprocess.run("find ./*.mscz | cut -c 1-2 --complement | sed s/.mscz/.mp3/g", shell=True, capture_output=True, text=True).stdout.split('\n') if x!=""]
    mxl=[x for x in subprocess.run("find ./*.mscz | cut -c 1-2 --complement | sed s/.mscz/.mxl/g", shell=True, capture_output=True, text=True).stdout.split('\n') if x!=""]
    return list(zip(mscz,pdf,mp3,mxl))

def compute_file_hash(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()
def existence_checker(os_var):
    if os_var in os.environ:
        return True
    else:
        return False
def export_files(z):
    os.chdir(EXPORT_DIR)
    commands=[]
    print(str(len(z))+" Files found to Export")
    counter=1
    time.sleep(2)
    subprocess.run ("clear", shell=True)
  
    local_bin=str("/"+os.environ['MS4_VERSION']+" --appimage-extract-and-run")

    for _ in z:
        print(str(counter)+"/"+str(len(z)))
        if existence_checker("MS4_PDF"):
            if os.environ['MS4_PDF']:
                subprocess.run(local_bin+" -o "+EXPORT_DIR+"/"+PDF_DIR+"/"+_["pdf"]+" "+IMPORT_DIR+"/"+_["mscz"], shell=True, capture_output=True, text=True)
        if existence_checker("MS4_MP3"):
            if os.environ['MS4_MP3']:
                subprocess.run(local_bin+ " -o "+EXPORT_DIR+"/"+MP3_DIR+"/"+_["mp3"]+" "+IMPORT_DIR+"/"+_["mscz"], shell=True, capture_output=True, text=True)
        if existence_checker("MS4_MXL"):
            if os.environ['MS4_MXL']:
                subprocess.run(local_bin+" -o "+EXPORT_DIR+"/"+MXL_DIR+"/"+_["mxl"]+" "+IMPORT_DIR+"/"+_["mscz"], shell=True, capture_output=True, text=True)
        counter=counter+1
        subprocess.run("clear",shell=True)
def save_json():
    with open(data_FILE,"w") as f:
        json.dump(musescore_data,f,indent=2,ensure_ascii=False)

def init():
    # DATAFILE
    if not os.path.isfile(data_FILE):
        subprocess.run("touch "+data_FILE, shell=True, capture_output=True, text=True)
    # EXPORT_DIRS
    if existence_checker("MS4_PDF"):
        if not os.path.isdir(EXPORT_DIR+"/"+PDF_DIR) and os.environ['MS4_PDF']:
            os.makedirs(EXPORT_DIR+"/"+PDF_DIR)
    if existence_checker("MS4_MP3"):
        if not os.path.isdir(EXPORT_DIR+"/"+MP3_DIR) and os.environ['MS4_MP3']:
            os.makedirs(EXPORT_DIR+"/"+MP3_DIR)
    if existence_checker("MS4_MXL"):
        if not os.path.isdir(EXPORT_DIR+"/"+MXL_DIR) and os.environ['MS4_MXL']:
            os.makedirs(EXPORT_DIR+"/"+MXL_DIR)


data_FILE='/app/export/MS4_Export.json'
IMPORT_DIR='/app/import'
EXPORT_DIR='/app/export'
PDF_DIR='PDF'
MP3_DIR='MP3'
MXL_DIR='MXL'

if __name__== "__main__":
    init()
    musescore_data=[]
    for _ in list(find_files(IMPORT_DIR)):
        musescore_data.append({"SHA256":compute_file_hash(_[0]),"mscz":_[0],"pdf":_[1],"mp3":_[2],"mxl":_[3]})

    with open(data_FILE,"r") as f:
        try: 
            db=json.load(f)
        except:
            db=[]

        sha_new=[]
        sha_old=[]
        for _ in db:
            sha_old.append(_["SHA256"])

        for _ in musescore_data:
            sha_new.append(_["SHA256"])
    
        diff=list(set(sha_new)-set(sha_old))
        if [_ for _ in musescore_data if _["SHA256"] in diff] !=[]:
            export_files([_ for _ in musescore_data if _["SHA256"] in diff])
            print("Export Complete")
            save_json()
        else:
            print ("Nothing to do")


