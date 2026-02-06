import subprocess



DEFAULT_IMAGE_NAME = "ubuntu-ssh-pytorch"
DEFAULT_CONTAINER_NAME = "container-ubuntu-ssh-pytorch"


image_name = input(f"Enter the image name (default: {DEFAULT_IMAGE_NAME}): ") or DEFAULT_IMAGE_NAME
container_name  = input(f"Enter the container name (default: {DEFAULT_CONTAINER_NAME}): ") or DEFAULT_CONTAINER_NAME

DEFAULT_ALLOWED_PUBLIC_KEY = "abc123"
allowed_public_key = input(f"Enter the allowed public key (default: {DEFAULT_ALLOWED_PUBLIC_KEY}): ") or DEFAULT_ALLOWED_PUBLIC_KEY

subprocess.run(f"docker rm -f {container_name}",  shell=True) #* Removing previous container with the same name.

#$ Notice  how  "gpus all" is used to give the container access the GPU(s) in the host.
CMD = f"""
    docker run \
    --name {container_name} \
    --gpus all \
    -e ALLOWED_PUBLIC_KEY={allowed_public_key} \
    -d \
    {image_name} \
"""

print(f"\n Running: \n  {CMD}")

subprocess.run(CMD, shell=True)

print('\n')