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

from torch.utils import data

if __name__ == '__main__':
    basepath = '/media/neuropsycad/disk12t/EdoardoFilippiMasterThesis/implementations/unetsv3/dataset2'


    # data.dataloader()
    files = dm.list_files(basepath, "*")
    img_list = []
    label_list = []
    #
    #
    #
    # data = data.DataLoader(
    #     basepath,
    #     batch_size=1,
    #     shuffle=False,
    #     num_workers=1,
    #     collate_fn=None,
    #     pin_memory=True,
    #)

    for filename in files["r_img"]:
        img_list.append(dm.read_img(filename))
    for filename in files["r_label"]:
        label_list.append(dm.read_img(filename))


    print(len(label_list))
    print(label_list[0].shape)
    print(type(label_list[0]))
    dv.see_random_slice(label_list[0].dataobj)
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
