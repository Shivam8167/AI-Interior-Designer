from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

prompt = "dark modern bedroom interior, window, stone wall"

image = pipe(prompt).images[0]

image.save("outputs/test.png")

print("Done")