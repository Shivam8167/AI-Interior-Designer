import os
import random
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch





DATASET_PATH = r"D:\AI Interior Designer\Dataset for AI Interior Design\House_Room_Dataset"





all_images = []

for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            all_images.append(os.path.join(root, file))


print("Total images found:", len(all_images))





img_path = random.choice(all_images)

print("Selected image:", img_path)


init_image = Image.open(img_path).convert("RGB")

init_image = init_image.resize((512, 512))





model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")




prompt = "modern interior design, dark theme, luxury living room, realistic, high quality"




image = pipe(
    prompt=prompt,
    image=init_image,
    strength=0.75,
    guidance_scale=8
).images[0]




output_path = "outputs/Living room/random_output.png"

image.save(output_path)

print("Saved to:", output_path)
print("Done")