import torch
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms

def get_dataloaders(config):
    transform_train = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])
    transform_val = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ])

    full_dataset = datasets.CIFAR10(root=config['data_dir'], train=True, download=True, transform=transform_train)
    val_dataset_raw = datasets.CIFAR10(root=config['data_dir'], train=False, download=True, transform=transform_val)

    train_size = int(0.8 * len(full_dataset))
    val_size = len(full_dataset) - train_size
    train_dataset, sub_val_dataset = random_split(full_dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=config['batch_size'], shuffle=True, num_workers=2)
    val_loader = DataLoader(sub_val_dataset, batch_size=config['batch_size'], shuffle=False, num_workers=2)

    return train_loader, val_loader
