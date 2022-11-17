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

import data_manipulation as dm
import data_visualization as dv

if __name__ == '__main__':
    basepath =  '/media/neuropsycad/disk12t/EdoardoFilippiMasterThesis/implementations/unetsv3/dataset2'

    files = dm.list_files(basepath,"*")
    imglist = []

    for filename,i in enumerate(files["r_imm"]):
        imglist.append(dm.read_img(filename))

    dv.see_random_slice(imglist[1])




"""
import data_manipulation as dm

if __name__ == "__main__":

    data_list = dm.load_dict("img_and_annot")

    dm.convert_img(data_list["r_label"])
    dm.convert_img(data_list["r_label"])

    basepath = "/media/neuropsycad/disk12t/VascoDiogo/OASIS/FS7/"

    all_files = dm.list_files(basepath)
    dm.write_dict(all_files, "img_and_annot")
    
    basepath = "/media/neuropsycad/disk12t/VascoDiogo/OASIS/FS7/"

    all_files = list_files(basepath)

    write_file(all_files,"directory")
    #run(runner_id=None, meta_file=None, config_file=None, logging_file=None, args_file=None)
    #run(None, meta_file="configs/metadata.json", config_file="configs/train.json", logging_file="configs/logging.conf", args_file=None)



"""
