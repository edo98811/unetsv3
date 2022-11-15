

import nibabel.freesurfer as fs
import nibabel as nib
import os
import json
from monai.bundle import run

def read_annot(path, annotname):
    return fs.read_annot(str(path + annotname))

def read_img(path, imgname):
    return nib.load(str(path + imgname))

def list_files(dir):
        r_img = []
        r_annot = []
        #r_all = []

        for root, dirs, files in os.walk(dir):
            #r_all.append(os.path.join(root))
            for name in files:
                l_name = name.split(".")
                if len(l_name) < 2:
                    continue
                if l_name[-1] == "annot":
                    r_annot.append(os.path.join(root, name))
                elif l_name[-2] == "T1":
                    r_img.append(os.path.join(root, name))

        return {
            #"r_all":r_all,
            "r_img":r_img,
            "r_annot":r_annot
        }

def write_dict(all_files, filename):
    json_object = json.dumps(all_files, indent=4)

    with open(filename +".json", "w") as outfile:
        outfile.write(json_object)

def load_dict(filename):
    with open(filename +".json", "r") as infile:
        img_dict = json.load(infile)

    return img_dict

def convert_img(img_list):
    if not os.path.isdir("dataset"):
        os.makedirs("dataset")

    for img in img_list:
        type(img)
        len(img)
        img = nib.load(img)

        subj = img.split("/")[-2]
        nib.save(img, f"dataset/{subj}_T1.nii.gz")


