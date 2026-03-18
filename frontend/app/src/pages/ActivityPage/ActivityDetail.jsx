import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function ActivityDetail() {
  const { id } = useParams();
  const [activity, setActivity] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/activities/${id}`)
      .then(res => res.json())
      .then(data => setActivity(data));
  }, [id]);

  if (!activity) return <p>Loading...</p>;

  return (
    <div style={{
      padding: "40px",
      background: "#f9fafb",
      minHeight: "100vh"
    }}>

      {/* Back Button */}
      <button
        onClick={() => window.history.back()}
        style={{
          marginBottom: "20px",
          padding: "8px 16px",
          borderRadius: "8px",
          border: "none",
          background: "#e5e7eb",
          cursor: "pointer"
        }}
      >
        ← Back
      </button>

      <div style={{
        maxWidth: "1000px",
        margin: "0 auto",
        display: "grid",
        gridTemplateColumns: "1fr 1fr",
        gap: "40px",
        alignItems: "center"
      }}>

        {/* Image */}
        <img
          src={activity.image}
          alt={activity.name}
          style={{
            width: "100%",
            height: "350px",
            objectFit: "cover",
            borderRadius: "16px",
            boxShadow: "0 8px 20px rgba(0,0,0,0.1)"
          }}
        />

        {/* Details */}
        <div>

          {/* Category Badge */}
          <span style={{
            display: "inline-block",
            background: "#e5e7eb",
            padding: "5px 10px",
            borderRadius: "8px",
            marginBottom: "10px"
          }}>
            {activity.category}
          </span>

          {/* Title */}
          <h1 style={{
            fontSize: "2rem",
            marginBottom: "10px",
            color: "#111827"
          }}>
            {activity.name}
          </h1>

          {/* Description */}
          <p style={{
            color: "#6b7280",
            marginBottom: "20px",
            lineHeight: "1.6"
          }}>
            {activity.description}
          </p>

          {/* Duration */}
          <p style={{ marginBottom: "10px" }}>
            <strong>Duration:</strong> {activity.duration}
          </p>

          {/* Price */}
          <h2 style={{
            margin: "20px 0",
            color: "#111827"
          }}>
            ${activity.price}
          </h2>

          {/* CTA */}
          <button style={{
            padding: "12px 24px",
            background: "#111827",
            color: "#fff",
            border: "none",
            borderRadius: "8px",
            fontSize: "1rem",
            cursor: "pointer"
          }}
          onMouseOver={(e) => e.currentTarget.style.opacity = "0.8"}
          onMouseOut={(e) => e.currentTarget.style.opacity = "1"}
          >
            Book Now
          </button>

        </div>
      </div>
    </div>
  );
}