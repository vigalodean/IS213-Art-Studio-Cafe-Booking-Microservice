import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ActivityList() {
  const [activities, setActivities] = useState([]);
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:8000/getAllActivities")
      .then(res => res.json())
      .then(data => setActivities(data.activities || []))
      .catch(err => console.error("Error fetching activities:", err));
  }, []);

  const filteredActivities = activities.filter(activity =>
    activity.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
   <div style={{ padding: "40px", background: "#f9fafb", minHeight: "100vh" }}>
      <h1 style={{
        fontSize: "2.5rem",
        fontWeight: "700",
        marginBottom: "30px",
        color: "#1f2937"
      }}>
        Art Activities 🎨
      </h1>

      {/* Search Bar */}
      <input
        type="text"
        placeholder="Search activities..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          width: "100%",
          padding: "12px 16px",
          marginBottom: "25px",
          borderRadius: "10px",
          border: "1px solid #ddd",
          fontSize: "1rem"
        }}
      />

      {/* Grid */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: "20px"
      }}>
        {filteredActivities.length === 0 ? (
          <p>No activities found 😢</p>
        ) : (
          filteredActivities.map(activity => (
            <div
              key={activity.id}
              style={{
                background: "#fff",
                borderRadius: "12px",
                overflow: "hidden",
                boxShadow: "0 6px 12px rgba(0,0,0,0.08)",
                cursor: "pointer",
                transition: "0.2s"
              }}
              onClick={() => navigate(`/activity/${activity.id}`)}
              onMouseOver={(e) => e.currentTarget.style.transform = "scale(1.03)"}
              onMouseOut={(e) => e.currentTarget.style.transform = "scale(1)"}
            >
              <img
                src={activity.image}
                alt={activity.name}
                style={{
                  width: "100%",
                  height: "180px",
                  objectFit: "cover"
                }}
              />

              <div style={{ padding: "12px" }}>
                <h3 style={{ margin: "0 0 5px" }}>{activity.name}</h3>
                <p style={{ margin: 0, color: "#666" }}>${activity.price}</p>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}