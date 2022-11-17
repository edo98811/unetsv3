

import nibabel.freesurfer as fs
import nibabel as nib
import os
import json
from monai.bundle import run

def read_annot(annotname, path=""):
    return fs.read_annot(str(path + annotname))

def read_img(imgname, path = ""):
    return nib.load(str(path + imgname))

def list_files(dir,imgname,labelname="",filetype="nii.gz"):
    """
    input
        imgname = str
        labelname = str
        filetype = str, default = nii.gz
    """

    r_img = []
    r_label = []
    #r_all = []
    fl_len = len(filetype.split("."))
    for root, dirs, files in os.walk(dir):
        #r_all.append(os.path.join(root))
        for name in files:
            l_name = name.split(".")
            if len(l_name) < fl_len+1:
                continue
            if l_name[-fl_len-1] == imgname:# and l_name[-fl_len:-1] == filetype:
                r_label.append(os.path.join(root, name))
            elif l_name[-fl_len-1] == labelname:
                r_img.append(os.path.join(root, name))

        return {
            #"r_all":r_all,
            "r_img":r_img,
            "r_annot":r_label
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
    if not os.path.isdir("../dataset"):
        os.makedirs("../dataset")

    for img_name in img_list:

        img = nib.load(img_name)

        subj = img_name.split("/")[-3]
        nib.save(img, f"../dataset/{subj}_T1.nii.gz")




