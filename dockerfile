
#$ This is my own base image, it just starts an ssh server and it's the base ubuntu:24.04 image
#$ This doesn't necessarily have to be auto-pulled from the registry here. You can pull the image beforehand. However, the first time you build this image with auto-pulling, it will save it to your local Docker images.

FROM ubuntu-24-simple-ssh



RUN apt update 
RUN apt install -y python3-pip
#$ This should also install all required CUDA dependencies (you can also choose to have them already installed on the base image as CUDA system packages).
    #! Keep in mind: CUDA dependencies are very large. 
RUN pip install torch --break-system-packages
RUN pip install numpy --break-system-packages #$ Torch needs this.
#? TODO: Remove pip cache or things not needed after installation.



#$ This is a small script to check to test for CUDA usability.
COPY src/cuda_check.py /cuda_check.py
RUN chmod 777 /cuda_check.py

CMD ["sleep", "infinity"]