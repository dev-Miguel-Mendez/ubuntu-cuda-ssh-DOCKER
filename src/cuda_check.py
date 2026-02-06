import torch

print(torch.cuda.is_available())        #* Checks whether CUDA is actually usable by PyTorch at runtime
print(torch.cuda.device_count())        #* Checks how many CUDA-capable GPUs PyTorch can see


#* Prints the name of the first detected GPU, if any
print(
    torch.cuda.get_device_name(0)
    if torch.cuda.device_count() else None
) 



print(torch.version.cuda)                #* Reports the CUDA version PyTorch was built against (INFORMATIONAL ONLY)