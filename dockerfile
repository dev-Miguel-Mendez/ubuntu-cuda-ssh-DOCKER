
#$ This is my own base image, it just starts an ssh server and it's the base ubuntu:24.04 image
#$ This doesn't necessarily have to be auto-pulled from the registry here. You can pull the image beforehand. However, the first time you build this image with auto-pulling, it will save it to your local Docker images.

FROM priapisman677/ubuntu-24-simple-ssh:latest 
#$ Same as:



#! We need to run everything in a single RUN so that the downloads from `apt update` are not cached in a layer and can be deleted in the same layer where they are downloaded.
RUN apt update  \ 
    && apt install -y python3-pip git nano\
    && rm -fr /var/lib/apt/lists/* #$ This removes the package index files from `apt update`

#$ This should also install all required CUDA dependencies (you can also choose to have them already installed on the base image as CUDA system packages).
    #! Keep in mind: CUDA dependencies are very large. 
RUN pip install torch numpy --no-cache-dir --break-system-packages \
    && rm -fr /root/.cache/pip #$ Explicitly remove ALL pip cache.

    #- Seems like  `--no-cache-dir` reduced   the disk usage (and content size) by half! But I'm not exactly sure of what part of the reduction came from other optimizations I was doing (e.g. removing apt cache).


#$ This is a small script to check to test for CUDA usability.
COPY src/cuda_check.py /cuda_check.py
RUN chmod 777 /cuda_check.py




CMD ["sleep", "infinity"]