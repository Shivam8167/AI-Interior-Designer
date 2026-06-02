function TextToImage({
  room,
  setRoom,
  style,
  setStyle,
  color,
  setColor,
  numImages,
  setNumImages,
  generateImage,
  setShowScrollIndicator,
}) {

  // ROOM DATA

  const rooms = [
    {
      name: "bedroom",
      label: "Bedroom",
      image:
        "https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmVkcm9vbSUyMGludGVyaW9yfGVufDB8fDB8fHww",
    },

    {
      name: "kitchen",
      label: "Kitchen",
      image:
        "https://plus.unsplash.com/premium_photo-1680382578857-c331ead9ed51?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8S2l0Y2hlbiUyMGludGVyaW9yfGVufDB8fDB8fHww",
    },

    {
      name: "bathroom",
      label: "Bathroom",
      image:
        "https://plus.unsplash.com/premium_photo-1681487208776-e308bfaa0539?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8QmF0aHJvb20lMjBpbnRlcmlvcnxlbnwwfHwwfHx8MA%3D%3D",
    },

    {
      name: "livingroom",
      label: "LivingRoom",
      image:
        "https://images.unsplash.com/photo-1612152598218-9acf01c968e3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fExpdmluZ3Jvb20lMjBpbnRlcmlvcnxlbnwwfHwwfHx8MA%3D%3D",
    },
  ];

  // STYLE DATA

  const styles = [
    {
      name: "modern",
      label: "Modern",
      image:
        "https://images.unsplash.com/photo-1724582586529-62622e50c0b3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bW9kZXJuJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D",
    },

    {
      name: "luxury",
      label: "Luxury",
      image:
        "https://plus.unsplash.com/premium_photo-1748021847732-b1b7f7a5797c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTA3fHxsdXh1cnklMjBraXRjaGVuJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D",
    },

    {
      name: "minimal",
      label: "Minimal",
      image:
        "https://media.istockphoto.com/id/1973276016/photo/modern-minimalist-bathroom-interior-bathtub-and-bathroom-cabinet-white-sink-interior-plants.webp?a=1&b=1&s=612x612&w=0&k=20&c=GNHYDMcotvGw-Xfoxbc6gv7suCKoU9SNKPHt3hwSnfs=",
    },

    {
      name: "cozy",
      label: "Cozy",
      image:
        "https://plus.unsplash.com/premium_photo-1733760125513-f7a3171dc79a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fGNvenklMjBsaXZpbmclMjByb29tJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D",
    },
  ];

  return (
    <div className="form-box">

      {/*STEP 1 - ROOM TYPE*/}

      {!room && (
        <>

          <h2>Select Room Type</h2>

          <div className="room-grid">

            {rooms.map((item) => (
              <div
                key={item.name}
                className="room-card"
                onClick={() => {
                  setRoom(item.name);
                }}
              >
                <img src={item.image} alt={item.label} />

                <h3>{item.label}</h3>
              </div>
            ))}

          </div>

        </>
      )}

      {/*STEP 2 - STYLE*/}

      {room && !style && (
        <>

          <div className="top-bar">

            <button
              className="back-btn"
              onClick={() => {
                setRoom("");
                setStyle("");
              }}
            >
              ← Back
            </button>

            <h2>Select Room Style</h2>

          </div>

          <div className="room-grid">

            {styles.map((item) => (
              <div
                key={item.name}
                className="room-card"
                onClick={() => setStyle(item.name)}
              >
                <img src={item.image} alt={item.label} />

                <h3>{item.label}</h3>
              </div>
            ))}

          </div>

        </>
      )}

      {/*STEP 3 - COLOR*/}

      {style && (
        <>

          <div className="top-bar">

            <button
              className="back-btn"
              onClick={() => {
                setStyle("");
                setColor("");
              }}
            >
              ← Back
            </button>

            <h2>Select Color Theme</h2>

          </div>

          <div className="color-grid">

            <div
              className={`color-card ${
                color === "white" ? "active-color" : ""
              }`}
              onClick={() => {
                setColor("white");
                setShowScrollIndicator(true);
              }}
            >
              <div className="color-circle white"></div>
              <p>White</p>
            </div>

            <div
              className={`color-card ${
                color === "beige" ? "active-color" : ""
              }`}
              onClick={() => {
                setColor("beige");
                setShowScrollIndicator(true);
              }}
            >
              <div className="color-circle beige"></div>
              <p>Beige</p>
            </div>

            <div
              className={`color-card ${
                color === "grey" ? "active-color" : ""
              }`}
              onClick={() => {
                setColor("grey");
                setShowScrollIndicator(true);
              }}
            >
              <div className="color-circle grey"></div>
              <p>Grey</p>
            </div>

            <div
              className={`color-card ${
                color === "brown" ? "active-color" : ""
              }`}
              onClick={() => {
                setColor("brown");
                setShowScrollIndicator(true);
              }}
            >
              <div className="color-circle brown"></div>
              <p>Brown</p>
            </div>

            <div
              className={`color-card ${
                color === "blue" ? "active-color" : ""
              }`}
              onClick={() => {
                setColor("blue");
                setShowScrollIndicator(true);
              }}
            >
              <div className="color-circle blue"></div>
              <p>Blue</p>
            </div>

            <div
              className={`color-card ${
                color === "green" ? "active-color" : ""
              }`}
              onClick={() => {
                setColor("green");
                setShowScrollIndicator(true);
              }}
            >
              <div className="color-circle green"></div>
              <p>Green</p>
            </div>

          </div>

          {/*NUMBER OF IMAGES*/}

          {color && (

            <div className="image-count-box">

              <h3>Number of Images</h3>

              <input
                className="image-count-input"
                type="number"
                min="1"
                max="6"
                value={numImages}
                onChange={(e) => setNumImages(e.target.value)}
                style={{
                  width: "80px",
                  height: "35px",
                  textAlign: "center"
                }}
              />

              <button
                className="generate-btn"
                onClick={generateImage}
              >
                Generate Designs
              </button>

            </div>

          )}

        </>
      )}

    </div>
  );
}

export default TextToImage;

// https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmVkcm9vbSUyMGludGVyaW9yfGVufDB8fDB8fHww
// https://plus.unsplash.com/premium_photo-1680382578857-c331ead9ed51?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8S2l0Y2hlbiUyMGludGVyaW9yfGVufDB8fDB8fHww
// https://plus.unsplash.com/premium_photo-1681487208776-e308bfaa0539?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8QmF0aHJvb20lMjBpbnRlcmlvcnxlbnwwfHwwfHx8MA%3D%3D
// https://images.unsplash.com/photo-1612152598218-9acf01c968e3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fExpdmluZ3Jvb20lMjBpbnRlcmlvcnxlbnwwfHwwfHx8MA%3D%3D

// https://images.unsplash.com/photo-1724582586529-62622e50c0b3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bW9kZXJuJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D
// https://plus.unsplash.com/premium_photo-1748021847732-b1b7f7a5797c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTA3fHxsdXh1cnklMjBraXRjaGVuJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D
// https://media.istockphoto.com/id/1973276016/photo/modern-minimalist-bathroom-interior-bathtub-and-bathroom-cabinet-white-sink-interior-plants.webp?a=1&b=1&s=612x612&w=0&k=20&c=GNHYDMcotvGw-Xfoxbc6gv7suCKoU9SNKPHt3hwSnfs=
// https://plus.unsplash.com/premium_photo-1733760125513-f7a3171dc79a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fGNvenklMjBsaXZpbmclMjByb29tJTIwaW50ZXJpb3J8ZW58MHx8MHx8fDA%3D