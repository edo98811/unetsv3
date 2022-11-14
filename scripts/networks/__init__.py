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


def readannot(path, annotname):
    return fs.read_annot("")

def readimg(path, imgname):
    return nb.load("")

def list_files(dir):
        r = []
        for root, dirs, files in os.walk(dir):
            for name in files:
                r.append(os.path.join(root, name))
        return r

if __name__=="__main__":
    basepath = "ciao"

    all_files = list_files(basepath)


# prova



