import React from "react";

function ImageToImage({
  setFile,
  room,
  setRoom,
  style,
  setStyle,
  color,
  setColor,
  numImages,
  setNumImages,
  generateImg2Img
}) {
  return (
    <div className="form-box">
      <label>Upload Image:</label>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <label>Room:</label>
      <select value={room} onChange={(e) => setRoom(e.target.value)}>
        <option value="1">Bedroom</option>
        <option value="2">Kitchen</option>
        <option value="3">Bathroom</option>
        <option value="4">Living Room</option>
      </select>

      <label>Style:</label>
      <select value={style} onChange={(e) => setStyle(e.target.value)}>
        <option value="1">Modern</option>
        <option value="2">Luxury</option>
        <option value="3">Minimal</option>
        <option value="4">Cozy</option>
      </select>

      <label>Color:</label>
      <select value={color} onChange={(e) => setColor(e.target.value)}>
        <option value="1">White</option>
        <option value="2">Beige</option>
        <option value="3">Grey</option>
        <option value="4">Brown</option>
        <option value="5">Blue</option>
        <option value="6">Green</option>
      </select>

      <label>No. of Images:</label>
      <input
        type="number"
        value={numImages}
        onChange={(e) => setNumImages(e.target.value)}
      />

      <button onClick={generateImg2Img}>Redesign</button>
    </div>
  );
}

export default ImageToImage;