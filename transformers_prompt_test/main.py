import torch

from transformers import pipeline 


#$ A pipeline is  for INFERENCE ONLY
    #$ A pipeline is a high-level abstraction that bundles inference steps.



generator = pipeline(
    # "document-question-answering",
    "text-generation",
    # model="facebook/opt-125m" #! This will auto download the model. However, you can also download it manually (with git lfs) and you just need to point to the folder containing the model.
    model="./unquantized_llm_from_facebook",
    tokenizer="./unquantized_llm_from_facebook",
    torch_dtype=torch.float16 #$ or torch.float32  | controls  precision, not quantization.
)

answer = generator("What is the capital of France?",  max_new_tokens=20)
print(answer)