import torch
from diffusers import StableDiffusionPipeline


model_id = "OFA-Sys/small-stable-diffusion-v0"


pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    safety_checker=None,
    low_cpu_mem_usage=True
)

pipe = pipe.to("cpu")


prompt = input("Enter prompt: ")

num_images = 5


for i in range(num_images):

    print("Generating", i+1)

    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7
    ).images[0]

    image.save(f"outputs/text_{i}.png")

    torch.cuda.empty_cache()  # safe even on CPU


print("Done")