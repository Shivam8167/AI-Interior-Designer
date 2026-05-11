import { useState } from "react";
import "./App.css";

import ModeSelector from "./components/ModeSelector";
import TextToImage from "./components/TextToImage";
import ImageToImage from "./components/ImageToImage";
import ImageGallery from "./components/ImageGallery";
import Loader from "./components/Loader";

function App() {
  const [mode, setMode] = useState("");

  
  const [room, setRoom] = useState("1");
  const [style, setStyle] = useState("1");
  const [color, setColor] = useState("1");

  const [numImages, setNumImages] = useState(1);
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  
  // TEXT → IMAGE
  
  const generateImage = async () => {
    setLoading(true);

    const formData = new FormData();
    formData.append("room_choice", room);
    formData.append("style_choice", style);
    formData.append("color_choice", color);
    formData.append("num_images", String(numImages));

    const res = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    const urls = data.images.map(
      (p) => "http://127.0.0.1:8000/" + p
    );

    setImages(urls);
    setLoading(false);
  };

  // IMAGE → IMAGE
  
  const generateImg2Img = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("room_choice", room);
    formData.append("style_choice", style);
    formData.append("color_choice", color);
    formData.append("num_images", String(numImages));

    setLoading(true);

    const res = await fetch("http://127.0.0.1:8000/img2img", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();

    const urls = data.images.map(
      (p) => "http://127.0.0.1:8000/" + p
    );

    setImages(urls);
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="hero-section">

        <h1>AI Interior Designer</h1>

        <p className="hero-description">
          AI Interior Designer is an intelligent room transformation platform
          that helps users generate beautiful and realistic interior designs
          using Artificial Intelligence. Users can select different room
          types, design styles, color themes, and generate multiple unique
          interior concepts instantly. The platform simplifies interior
          planning by allowing users to visualize modern, luxury, cozy, and
          minimal room ideas without needing professional design experience.
          It saves time, improves creativity, and helps users experiment with
          different aesthetics before making real-world design decisions for
          their homes or projects.
        </p>

        <div className="mode-info-container">

          <div className="mode-info-card">

            <h3>Text to Image</h3>

            <p>
              Generate completely new AI-designed interiors by selecting
              room type, style, colors, and design preferences.
            </p>

            <button
              className={`mode-btn ${mode === "text" ? "active-mode" : ""}`}
              onClick={() => setMode("text")}
            >
              Text to Image
            </button>

          </div>

          <div className="mode-info-card">

            <h3>Image to Image</h3>

            <p>
              Upload your existing room image and transform it into
              stunning AI-generated interior redesigns instantly.
            </p>

            <button
              className={`mode-btn ${mode === "image" ? "active-mode" : ""}`}
              onClick={() => setMode("image")}
            >
              Image to Image
            </button>

          </div>

</div>

      </div>

      {mode === "text" && (
        <TextToImage
          room={room}
          setRoom={setRoom}
          style={style}
          setStyle={setStyle}
          color={color}
          setColor={setColor}
          numImages={numImages}
          setNumImages={setNumImages}
          generateImage={generateImage}
        />
      )}

      {mode === "image" && (
        <ImageToImage
          setFile={setFile}
          room={room}
          setRoom={setRoom}
          style={style}
          setStyle={setStyle}
          color={color}
          setColor={setColor}
          numImages={numImages}
          setNumImages={setNumImages}
          generateImg2Img={generateImg2Img}
        />
      )}

      {loading && <Loader />}

      <ImageGallery images={images} />
    </div>
  );
}

export default App;