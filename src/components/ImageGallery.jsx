function ImageGallery({ images }) {
  return (
    <div className="image-grid">
      {images.map((img, index) => (
        <div key={index} className="image-card">
          <img src={img} alt="result" />
          <br />
          <a href={img} download>Download</a>
        </div>
      ))}
    </div>
  );
}
export default ImageGallery;