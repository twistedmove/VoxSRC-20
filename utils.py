import torch


def save_checkpoint(model, criterion, optimizer, epoch):
    torch.save(
        model.state_dict(),
        f'checkpoints/model_{epoch+1:02d}.pt'
    )
    torch.save(
        criterion.state_dict(),
        f'checkpoints/criterion_{epoch+1:02d}.pt'
    )
    torch.save(
        optimizer.state_dict(),
        f'checkpoints/optimizer_{epoch+1:02d}.pt'
    )


def load_checkpoint(model, model_path, device):
    if model_path:
        model.load_state_dict(torch.load(model_path, map_location=device))