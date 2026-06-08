print("retrieve.py loaded successfully")
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from rag.direct_retrieve import get_design_context

from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
from PIL import Image
import torch
import io
import os
import time

app = FastAPI()

# ===============================
# CORS
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# OUTPUT FOLDER
# ===============================
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

app.mount("/outputs", StaticFiles(directory=OUTPUT_DIR), name="outputs")

# ===============================
# MODEL
# ===============================
model_id = "OFA-Sys/small-stable-diffusion-v0"

print("🔄 Loading models...")

text_pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    safety_checker=None
).to("cpu")

img_pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    safety_checker=None
).to("cpu")

print("✅ Models loaded!")

# ===============================
# MAPS (UNCHANGED FROM YOUR CODE)
# ===============================
room_map = {
    "bedroom": "bedroom interior",
    "kitchen": "kitchen interior",
    "bathroom": "bathroom interior",
    "livingroom": "living room interior",
}

style_map = {
    "modern": "modern",
    "minimal": "minimal",
    "luxury": "luxury",
    "cozy": "cozy",
}

color_map = {
    "white": "white color theme",
    "beige": "beige color theme",
    "grey": "grey color theme",
    "brown": "brown color theme",
    "midnight blue": "midnight blue color theme",
    "forest green": "forest green color theme",
    "wine red": "wine red color theme",
}

# ===============================
# ROOT
# ===============================
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

# ===============================
# TEXT → IMAGE (UNCHANGED LOGIC)
# ===============================
@app.post("/generate")
async def generate(
    room_choice: str = Form(...),
    style_choice: str = Form(...),
    color_choice: str = Form(...),
    num_images: int = Form(...)
):
    try:

        room = room_map.get(room_choice, "bedroom interior")
        style = style_map.get(style_choice, "modern")
        color = color_map.get(color_choice, "neutral color theme")

        rag_context = get_design_context(
            room_choice,
            style_choice,
            color_choice
        )

        print("\nRAG CONTEXT:")
        print(rag_context)

        prompt = f"""{rag_context} ultra realistic interior design, 4k"""
        # {style} {room}, {color}, 

        print("PROMPT:", prompt)

        image_paths = []

        for i in range(num_images):
            negative_prompt = """
            blurry,
            low quality,
            empty room,
            unfinished interior,
            poor lighting,
            low detail,
            distorted furniture,
            bad composition,
            cropped,
            extra objects,
            ugly,
            deformed,
            duplicate furniture
            """

            image = text_pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=50,
                guidance_scale=8
            ).images[0]

            path = f"{OUTPUT_DIR}/text_{int(time.time())}_{i}.png"
            image.save(path)

            image_paths.append(path)

        return {"images": image_paths}

    except Exception as e:
        print("ERROR:", e)
        return JSONResponse(content={"error": str(e)})

# ===============================
# IMAGE → IMAGE (UNCHANGED LOGIC)
# ===============================
@app.post("/img2img")
async def img2img(
    file: UploadFile = File(...),
    room_choice: str = Form(...),
    style_choice: str = Form(...),
    color_choice: str = Form(...),
    num_images: int = Form(...)
):
    try:
        contents = await file.read()

        init_image = Image.open(io.BytesIO(contents)).convert("RGB")
        init_image = init_image.resize((512, 512))

        room = room_map.get(room_choice, "bedroom")
        style = style_map.get(style_choice, "modern")
        color = color_map.get(color_choice, "neutral color theme")

        rag_context = get_design_context(
            room_choice,
            style_choice,
            color_choice
        )

        print("\nRAG CONTEXT:")
        print(rag_context)

        prompt = f"""Redesign same room. {rag_context} keep layout unchanged, 4k interior design"""
        # {room}, {style}, {color} 

        print("PROMPT:", prompt)

        image_paths = []

        for i in range(num_images):
            negative_prompt = """
            blurry,
            low quality,
            empty room,
            unfinished interior,
            poor lighting,
            low detail,
            distorted furniture,
            bad composition,
            cropped,
            extra objects,
            ugly,
            deformed,
            duplicate furniture
            """

            image = img_pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                image=init_image,
                strength=0.8,
                guidance_scale=8,
                num_inference_steps=50
            ).images[0]

            path = f"{OUTPUT_DIR}/redesign_{int(time.time())}_{i}.png"
            image.save(path)

            image_paths.append(path)

        return {"images": image_paths}

    except Exception as e:
        print("ERROR:", e)
        return JSONResponse(content={"error": str(e)})