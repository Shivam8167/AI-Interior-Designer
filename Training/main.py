import torch
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from PIL import Image
import os


model_id = "OFA-Sys/small-stable-diffusion-v0"

os.makedirs("outputs", exist_ok=True)


print("\n===== AI Interior Designer =====")
print("1 - Text to Image")
print("2 - Image Redesign")

choice = input("Select option: ")


# =========================
# TEXT TO IMAGE
# =========================

# =========================
# TEXT TO IMAGE
# =========================

if choice == "1":

    print("Loading Text2Img model...")

    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        safety_checker=None,
        low_cpu_mem_usage=True
    ).to("cpu")

    print("Model ready")


   
    print("\nSelect Room Type:")
    print("1 - Bedroom")
    print("2 - Kitchen")
    print("3 - Bathroom")
    print("4 - Living Room")

    room_choice = input("Enter choice: ")

    room_map = {
        "1": "bedroom interior",
        "2": "kitchen interior",
        "3": "bathroom interior",
        "4": "living room interior"
    }

    room = room_map.get(room_choice, "bedroom interior")


    
    print("\nSelect Style:")
    print("1 - Modern")
    print("2 - Luxury")
    print("3 - Minimal")
    print("4 - Cozy")

    style_choice = input("Enter choice: ")

    style_map = {
        "1": "modern",
        "2": "luxury",
        "3": "minimalist",
        "4": "cozy"
    }

    style = style_map.get(style_choice, "modern")

   
    print("\nSelect Color Theme:")
    print("1 - White")
    print("2 - Beige")
    print("3 - Grey")
    print("4 - Brown")
    print("5 - Blue")
    print("6 - Green")

    color_choice = input("Enter choice: ")

    color_map = {
        "1": "white color theme",
        "2": "beige color theme",
        "3": "grey color theme",
        "4": "brown wooden theme",
        "5": "blue color theme",
        "6": "green natural theme"
    }

    color = color_map.get(color_choice, "neutral color theme")


    
    prompt = f"{style} {room} interior, with {color}, add some furnitures and lightings, ultra realistic, high detail, 4k, interior design"

    print("\nGenerated Prompt:")
    print(prompt)


    num_images = int(input("\nHow many images you want: "))


    for i in range(num_images):

        print(f"Generating {i+1}...")

        image = pipe(
            prompt=prompt,
            num_inference_steps=30,
            guidance_scale=7
        ).images[0]

        image.save(f"outputs/text_{i}.png")

    print("Done!")


# =========================
# IMAGE TO IMAGE
# =========================

# =========================
# IMAGE TO IMAGE
# =========================

elif choice == "2":

    print("Loading Img2Img model...")

    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        safety_checker=None,
        low_cpu_mem_usage=True
    ).to("cpu")

    print("Model ready")


    path = input("Enter image path: ")

    
    print("\nSelect Room Type:")
    print("1 - Bedroom")
    print("2 - Kitchen")
    print("3 - Bathroom")
    print("4 - Living Room")

    room_choice = input("Enter choice: ")

    room_map = {
        "1": "bedroom",
        "2": "kitchen",
        "3": "bathroom",
        "4": "living room"
    }

    room = room_map.get(room_choice, "bedroom")


    
    print("\nSelect Style:")
    print("1 - Modern")
    print("2 - Luxury")
    print("3 - Minimal")
    print("4 - Cozy")

    style_choice = input("Enter choice: ")

    style_map = {
        "1": "modern",
        "2": "luxury",
        "3": "minimalist",
        "4": "cozy"
    }

    style = style_map.get(style_choice, "modern")

    
    print("\nSelect Color Theme:")
    print("1 - White")
    print("2 - Beige")
    print("3 - Grey")
    print("4 - Brown")
    print("5 - Blue")
    print("6 - Green")

    color_choice = input("Enter choice: ")

    color_map = {
        "1": "white color theme",
        "2": "beige color theme",
        "3": "grey color theme",
        "4": "brown wooden theme",
        "5": "blue color theme",
        "6": "green natural theme"
    }

    color = color_map.get(color_choice, "neutral color theme")


    
    prompt = f"{style} redesign of the same room, and make it a {room} with {color},  keep layout unchanged, improve lighting, add furnitures, add other necessary things if needed, realistic, high detail, interior design"

    print("\nGenerated Prompt:")
    print(prompt)


    num_images = int(input("\nHow many images you want: "))


    init_image = Image.open(path).convert("RGB")
    init_image = init_image.resize((512, 512))

    import gc
    torch.set_grad_enabled(False)

    for i in range(num_images):

        print(f"Generating {i+1}...")

        image = pipe(
            prompt=prompt,
            image=init_image,
            strength=0.7,          
            guidance_scale=11,
            num_inference_steps=60
        ).images[0]

        image.save(f"outputs/redesign_{i}.png")
        del image
        gc.collect()

    print("Done!")


else:
    print("Invalid option")