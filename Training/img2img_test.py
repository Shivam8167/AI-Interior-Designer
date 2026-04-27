import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image


model_id = "OFA-Sys/small-stable-diffusion-v0"


pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    safety_checker=None,
    low_cpu_mem_usage=True
)

pipe = pipe.to("cpu")


path = input("Enter image path: ")
prompt = input("Enter prompt: ")

init_image = Image.open(path).convert("RGB")
init_image = init_image.resize((512, 512))


num_images = 5


for i in range(num_images):

    print("Generating", i+1)

    image = pipe(
        prompt=prompt,
        image=init_image,
        strength=1.0,
        guidance_scale=7
    ).images[0]

    image.save(f"outputs/redesign_{i}.png")

    torch.cuda.empty_cache()


print("Done")