import json
import os
import sys
import torch
import torch.nn as nn
import torch.optim as optim
import yaml
from src.dataset import get_dataloaders
from src.model import get_model

def train():
    #with open("configs/training_config.yaml") as f:
    #    config = yaml.safe_load(f)

    config_path = os.getenv("TRAINING_CONFIG_PATH", "configs/training_config.yaml")
    
    with open(config_path) as f:
        config = yaml.safe_load(f)


    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_loader, val_loader = get_dataloaders(config)
    model = get_model(num_classes=10).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['learning_rate'])

    best_val_loss = float('inf')
    patience_counter = 0

    os.makedirs(os.path.dirname(config['model_save_path']), exist_ok=True)

    for epoch in range(config['epochs']):
        model.train()
        running_loss, correct, total = 0.0, 0, 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

        train_loss = running_loss / total
        train_acc = correct / total

        model.eval()
        val_running_loss, val_correct, val_total = 0.0, 0, 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_running_loss += loss.item() * images.size(0)
                _, predicted = outputs.max(1)
                val_total += labels.size(0)
                val_correct += predicted.eq(labels).sum().item()

        val_loss = val_running_loss / val_total
        val_acc = val_correct / val_total

        print(json.dumps({
            "epoch": epoch + 1,
            "train_loss": train_loss,
            "train_acc": train_acc,
            "val_loss": val_loss,
            "val_acc": val_acc
        }), flush=True)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            torch.save(model.state_dict(), config['model_save_path'])
        else:
            patience_counter += 1
            if patience_counter >= config['patience']:
                print(json.dumps({"early_stopping": epoch + 1}), flush=True)
                break

if __name__ == '__main__':
    train()
