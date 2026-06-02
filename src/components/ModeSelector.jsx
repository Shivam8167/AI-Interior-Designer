function ModeSelector({ mode, setMode }) {
  return (
    <div style={{ marginBottom: "20px" }}>
      <button onClick={() => setMode("text")}>
        Text to Image
      </button>

      <button onClick={() => setMode("image")} style={{ marginLeft: "10px" }}>
        Image to Image
      </button>
    </div>
  );
}
export default ModeSelector;