import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ActivityList() {
  const [activities, setActivities] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:8000/getAllActivities")
      .then(res => res.json())
      .then(data => setActivities(data.activities || []))
      .catch(err => console.error("Error fetching activities:", err));
  }, []);

  if (activities.length === 0) return <p>Loading activities...</p>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Art Activities 🎨</h1>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(3, 1fr)",
        gap: "20px"
      }}>
        {activities.map(activity => (
          <div key={activity.id}
            style={{
              border: "1px solid #ddd",
              padding: "10px",
              borderRadius: "10px",
              cursor: "pointer",
              transition: "transform 0.2s ease"
            }}
            onClick={() => navigate(`/activity/${activity.id}`)}
            onMouseOver={(e) => e.currentTarget.style.transform = "scale(1.05)"}
            onMouseOut={(e) => e.currentTarget.style.transform = "scale(1)"}
          >
            <img src={activity.image} alt={activity.name} width="100%" />
            <h3>{activity.name}</h3>
            <p>${activity.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}