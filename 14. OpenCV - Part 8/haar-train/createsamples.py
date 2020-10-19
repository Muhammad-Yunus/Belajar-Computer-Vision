import subprocess
import re

print ("[INFO] initializing samples data...")
positive  = "positives.txt"
negative  = "negatives.txt"
outputdir = "samples"
totalnum     = 1000 
cmd          = "tools\\opencv_createsamples.exe -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 32 -h 32" 
positive_data = []
negative_data = []

with open (positive, "r") as positive_file:
    positive_data=positive_file.readlines()
    positive_file.close() 
      
with open (negative, "r") as negative_file:
    negative_data=negative_file.readlines()
    negative_file.close()

print ("[INFO] get directory location... ")

directory_pos = "\\".join(positive_data[0].split("\\")[0:-1])
directory_neg = "\\".join(negative_data[0].split("\\")[0:-1])

print ("[INFO] positive directory : %s " % directory_pos )
for i, positive_file_path in enumerate(positive_data) :
    
    filename = negative_data[i].split("\\")[-1]
    vec = outputdir + "\\" + filename.strip() + ".vec"
    
    positive_file_path = "positive_images\\" + positive_file_path.replace(directory_pos + "\\", "").strip()
    negative_file_path =  "negative_images\\" + negative_data[i].replace(directory_neg + "\\", "")
    
    print("-------------------------------------------------------------")
    subprocess.call(["tools\\opencv_createsamples.exe",
                "-bgcolor", "0",
                "-bgthresh", "0",
                "-maxxangle", "1.1", 
                "-maxyangle", "1.1",
                "maxzangle", "0.5",
                "-maxidev", "40", 
                "-w", "32",
                "-h", "32",
                "-img", positive_file_path, 
                "-bg", negative_file_path,
                "-vec", vec,
                "-num", "2"])
                
print ("[INFO] FINISH create samples...")