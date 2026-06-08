AI Interior Designer
Overview

AI Interior Designer is an intelligent room transformation platform that generates realistic interior design concepts using Artificial Intelligence. Users can create new room designs from text inputs or redesign existing room images by selecting room types, design styles, color themes, and furniture preferences.

The project combines Stable Diffusion, FastAPI, React.js, and Retrieval-Augmented Generation (RAG) to produce personalized and visually appealing interior design concepts.

Features
Text-to-Image Generation

Generate completely new interior designs by selecting:

Room Type
Bedroom
Living Room
Kitchen
Bathroom
Design Style
Modern
Minimal
Luxury
Cozy
Color Theme
White
Beige
Grey
Brown
Forest Green
Midnight Blue
Wine Red
Number of Images
Image-to-Image Redesign

Upload an existing room image and redesign it while preserving the original room structure and layout.

RAG-Based Design Knowledge

Uses a custom knowledge base containing:

Room-specific design guidelines
Style recommendations
Color psychology
Furniture suggestions

The system dynamically retrieves relevant information and injects it into prompts before image generation.

Intelligent Prompt Engineering

Automatically generates detailed prompts using:

Room type
Interior style
Color theme
Furniture recommendations
Design guidelines
Negative Prompting

Improves image quality by avoiding:

Low quality outputs
Blurry textures
Distorted furniture
Bad anatomy
Watermarks
Text artifacts
Multiple Image Generation

Generate multiple design variations in a single request.

Modern User Interface

Built using React.js with:

Interactive landing page
Glassmorphism UI
Background image support
Smooth scrolling navigation
Responsive design
System Architecture
Frontend (React.js)
        │
        ▼
FastAPI Backend
        │
        ├── Text-to-Image Pipeline
        │
        ├── Image-to-Image Pipeline
        │
        └── RAG Retrieval System
                │
                ▼
          ChromaDB Vector Store
                │
                ▼
          Knowledge Base
                │
                ▼
      Stable Diffusion Model
Tech Stack
Frontend
React.js
CSS3
JavaScript
Backend
FastAPI
Python
AI Models
Stable Diffusion
Stable Diffusion Img2Img Pipeline
RAG Components
LangChain
ChromaDB
HuggingFace Embeddings
all-MiniLM-L6-v2
Image Processing
Pillow
Vector Database
ChromaDB
Project Structure
AI Interior Designer
│
├── Frontend
│   ├── src
│   │   ├── components
│   │   │   ├── TextToImage.jsx
│   │   │   ├── ImageToImage.jsx
│   │   │   ├── ImageGallery.jsx
│   │   │   └── Loader.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│
├── Backend
│   ├── api.py
│   ├── direct_retrieve.py
│   ├── vector_store.py
│   ├── retrieve.py
│   ├── load_doc.py
│   │
│   ├── chroma_db
│   │
│   └── knowledge_base
│       ├── bedroom_design.txt
│       ├── bathroom_design.txt
│       ├── kitchen_design.txt
│       ├── livingroom_design.txt
│       ├── modern_design.txt
│       ├── minimalistic_design.txt
│       ├── luxury_design.txt
│       ├── cozy_design.txt
│       ├── beige_color.txt
│       ├── white_color.txt
│       ├── grey_color.txt
│       ├── brown_color.txt
│       ├── forest_green_color.txt
│       ├── midnight_blue_color.txt
│       ├── wine_red_color.txt
│       └── furniture_recommendation.txt
│
└── outputs
RAG Workflow
Step 1

User selects:

Bedroom
Luxury
Wine Red
Step 2

System retrieves:

bedroom_design.txt
luxury_design.txt
wine_red_color.txt
furniture_recommendation.txt
Step 3

Retrieved context is combined into a final prompt.

Step 4

Prompt is sent to Stable Diffusion.

Step 5

AI generates realistic interior design images.

Prompt Generation Example
Generated Prompt
Create a luxury bedroom interior.

Color theme: wine red.

Use the following design guidelines:

Luxury interiors use premium materials,
elegant furniture,
warm lighting,
velvet fabrics,
gold accents,
rich textures.

Ultra realistic,
professional interior design,
high detail,
4k render.
Negative Prompt
blurry,
low quality,
worst quality,
distorted furniture,
watermark,
text,
duplicate objects,
cropped,
extra furniture,
bad lighting
Installation
Clone Repository
git clone <repository-url>
cd AI-Interior-Designer
Create Virtual Environment
python -m venv venv
Activate Environment

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Build Vector Database
python vector_store.py

Expected Output

Loaded 16 documents
Vector database created successfully
Run Backend
uvicorn api:app --reload

Server

http://127.0.0.1:8000
Run Frontend
npm install
npm run dev

Frontend

http://localhost:5173
Future Improvements
Higher-resolution image generation
SDXL support
ControlNet integration
Interior object detection
Room segmentation
AI furniture placement
Material recommendation engine
Design cost estimation
Save generated projects
User authentication
Cloud deployment
Learning Outcomes

This project demonstrates:

Generative AI
Stable Diffusion
Prompt Engineering
Retrieval-Augmented Generation (RAG)
Vector Databases
ChromaDB
FastAPI Development
React Frontend Development
Full Stack AI Application Development
Author

Shivam Paul

AI Interior Designer – A Full Stack Generative AI Application that combines Stable Diffusion and RAG to create personalized, realistic interior design concepts from both text descriptions and existing room images.
