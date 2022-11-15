# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import nibabel.freesurfer as fs
import nibabel as nb
import os
import json
from monai.bundle import run

def read_annot(path, annotname):
    return fs.read_annot(str(path + annotname))

def read_img(path, imgname):
    return nb.load(str(path + imgname))

def load_data(all_files_list):
    pass

def list_files(dir):
        r_img = []
        r_annot = []
        r_all = []

        for root, dirs, files in os.walk(dir):
            r_all.append(os.path.join(root))
            for name in files:
                if name.split(".").len() > 2:
                    continue
                if name.split(".")[-1] == "annot":
                    r_img.append(os.path.join(root, name))
                elif name.split(".")[-2] == "T1":
                    r_annot.append(os.path.join(root, name))

        return {
            "r_all":r_all,
            "r_img":r_img,
            "r_annot":r_annot
        }
def write_file(all_files, filename):
    json_object = json.dumps(all_files, indent=4)

    with open(filename +".json", "w") as outfile:
        outfile.write(json_object)

if __name__=="__main__":
    basepath = "/media/neuropsycad/disk12t/VascoDiogo/OASIS/FS7/"

    all_files = list_files(basepath)

    write_file(all_files,"directory")
    #run(runner_id=None, meta_file=None, config_file=None, logging_file=None, args_file=None)
    #run(None, meta_file="configs/metadata.json", config_file="configs/train.json", logging_file="configs/logging.conf", args_file=None)


"""
funzioni 

read img
read annot

load all data (magari non serve nemmeno)

load 


prende solo i file che hanno le estensioni giuste (.annot)


"""
