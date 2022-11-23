from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from data_manipulation import load_dict, read_img
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

# TODO: controllare il tipo di dati

class MriDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, data_file_path, dim,  transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.data_file_path = data_file_path
        self.data_plane = dim

        files = load_dict(data_file_path)

        self.label_list = files["r_annot"]
        self.dataset_list = files["r_img"]
        self.img_dim = read_img(self.dataset_list[0]).shape[dim] # poi questo adrà modificato
        self.transform = transform

    def __len__(self):
        return len(self.files["r_img"]*self.img_dim)

    def __getitem__(self, idx):

        img_n = idx % self.img_dim
        img_idx =  idx - img_n * self.img_dim


        # FIXME: aggiungere un controllo che i tipi di dati siano corretti, e aggiungere modo piu veloce di fare questo controllo
        vol_img = read_img(self.dataset_list[img_n])
        vol_label = read_img(self.dataset_list[img_n])

        if self.img_dim == 0:
            img = vol_img[img_idx,:,:]
            label = vol_label[img_idx,:,:]
        elif self.img_dim == 1:
            img = vol_img[ :, img_idx, :]
            label = vol_label[ :, img_idx, :]
        elif self.img_dim == 2:
            img = vol_img[:,: ,img_idx]
            label = vol_label[:,: ,img_idx]

        sample = {'image': img, 'label': label}

        if self.transform:
            sample = self.transform(sample)

        return sample


        # if torch.is_tensor(idx):
        #     idx = idx.tolist()

        # img_name = os.path.join(self.root_dir,
        #                         self.landmarks_frame.iloc[idx, 0])
        # image = io.imread(img_name)
        # landmarks = self.landmarks_frame.iloc[idx, 1:]
        # landmarks = np.array([landmarks])
        # landmarks = landmarks.astype('float').reshape(-1, 2)
        # sample = {'image': image, 'landmarks': landmarks}

        # return sample