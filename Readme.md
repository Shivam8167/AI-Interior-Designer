AI Interior Designer

AI Interior Designer is an AI-powered web application that generates realistic and modern interior room designs using Generative AI and Deep Learning techniques. Users can create new room designs using text-based selections or redesign existing room images using image-to-image generation.

The project combines a React frontend with a FastAPI backend and uses Stable Diffusion models for AI image generation.

--------------------------------------------------

FEATURES

- Text-to-Image Interior Generation
- Image-to-Image Room Redesign
- Room Type Selection
  - Bedroom
  - Kitchen
  - Bathroom
  - Living Room
- Interior Style Selection
  - Modern
  - Luxury
  - Minimal
  - Cozy
- Color Theme Selection
- Multiple Image Generation
- AI-powered realistic interior visualization
- Interactive and modern frontend UI
- FastAPI backend integration
- Stable Diffusion image generation pipeline

--------------------------------------------------

TECH STACK

Frontend
- React.js
- Vite
- CSS3

Backend
- Python
- FastAPI
- Uvicorn

AI / ML
- PyTorch
- Hugging Face Diffusers
- Stable Diffusion
- PIL
- Transformers

--------------------------------------------------

PROJECT STRUCTURE

AI-Interior-Designer/
│
├── Backend/
│   ├── __pycache__/
│   ├── outputs/
│   └── api.py
│
├── Code/
│
├── Dataset for AI Interior Design/
│
├── Frontend/
│   └── aiInteriorFrontend/
│       ├── public/
│       ├── src/
│       │   ├── assets/
│       │   ├── components/
│       │   │   ├── ImageGallery.jsx
│       │   │   ├── ImageToImage.jsx
│       │   │   ├── Loader.jsx
│       │   │   ├── ModeSelector.jsx
│       │   │   └── TextToImage.jsx
│       │   │
│       │   ├── App.css
│       │   ├── App.jsx
│       │   ├── index.css
│       │   └── main.jsx
│       │
│       ├── package.json
│       ├── vite.config.js
│       └── node_modules/
│
├── models/
│   └── room_classifier.pth
│
├── outputs/
│   ├── Bathroom/
│   ├── Bedroom/
│   ├── img2img/
│   ├── Kitchen/
│   └── Living room/
│
├── Training/
│   ├── diffusion_test.py
│   ├── img2img_test.py
│   ├── main.py
│   ├── random_img2img.py
│   ├── room_classifier.py
│   └── text2img.py
│
└── README.md

--------------------------------------------------

WORKING FLOW

Text to Image
1. User selects room type
2. User selects room style
3. User selects color theme
4. User selects number of images
5. AI generates realistic room interiors

Image to Image
1. User uploads room image
2. User selects redesign preferences
3. AI transforms uploaded room into redesigned interior

--------------------------------------------------

INSTALLATION

Clone Repository

git clone https://github.com/your-username/AI-Interior-Designer.git
cd AI-Interior-Designer

--------------------------------------------------

BACKEND SETUP

Install Dependencies

pip install -r requirements.txt

Run Backend Server

cd Backend
uvicorn api:app --reload

Backend runs on:

http://127.0.0.1:8000

--------------------------------------------------

FRONTEND SETUP

Install Dependencies

cd Frontend/aiInteriorFrontend
npm install

Run Frontend

npm run dev

Frontend runs on:

http://localhost:5173

--------------------------------------------------

AI MODELS USED

- Stable Diffusion Pipeline
- Stable Diffusion Img2Img Pipeline
- Room Classification Model
- Hugging Face Diffusers

--------------------------------------------------

CHALLENGES FACED

- Connecting FastAPI backend with React frontend
- Handling large AI model loading time
- Managing image generation performance
- Fixing API form-data validation errors
- Creating responsive multi-step UI
- Optimizing generated image quality

--------------------------------------------------

FUTURE IMPROVEMENTS

- User authentication
- Save generated designs
- More room categories
- More interior styles
- Cloud deployment
- Better image enhancement
- AI furniture recommendation system

--------------------------------------------------

AUTHOR

Shivam Paul

--------------------------------------------------

LICENSE

This project is for educational and learning purposes.