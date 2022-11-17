import matplotlib as plt
import torch

def see_random_slice(img):
    torch.manual_seed(42)
    fig = plt.figure(figsize=(9, 9))
    rows, cols = 4, 4
    for i in range(1, rows * cols + 1):
        random_idx = torch.randint(0, len(img.shape[1]), size=[1]).item() #transforms in normal python int
        img, label = img[random_idx,:,:]
        fig.add_subplot(rows, cols, i)
        plt.imshow(img.squeeze(), cmap="gray")
        plt.title(f"slice: {random_idx}")
        plt.axis(False);