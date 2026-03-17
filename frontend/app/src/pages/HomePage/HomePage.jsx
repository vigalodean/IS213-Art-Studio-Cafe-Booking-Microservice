import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import apiClient from "../../services/apiClient";

export default function HomePage() {
  const navigate = useNavigate();
  const { user, logout } = useAuth();
  const [calendarUrl, setCalendarUrl] = useState("");
  const [calendarError, setCalendarError] = useState("");
  const [loadingCalendarUrl, setLoadingCalendarUrl] = useState(false);

  useEffect(() => {
    if (!user) {
      setCalendarUrl("");
      setCalendarError("");
      setLoadingCalendarUrl(false);
      return;
    }

    const fetchCalendarUrl = async () => {
      setLoadingCalendarUrl(true);
      setCalendarError("");

      try {
        const res = await apiClient.get("/calendar-url");
        console.log("Calendar URL response:", res.data);

        if (res.data?.booking_url) {
          setCalendarUrl(res.data.booking_url);
        } else {
          throw new Error("No booking_url in response");
        }
      } catch (err) {
        console.error("Error fetching calendar URL:", err);
        setCalendarError("Unable to load booking link. Please try again later.");
        setCalendarUrl("https://google.com/");
      } finally {
        setLoadingCalendarUrl(false);
      }
    };

    fetchCalendarUrl();
  }, [user]);

  const openBookingLink = () => {
    const url = calendarUrl || "https://google.com/";
    window.open(url, "_blank");
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>Home Page</h1>
      {user ? <p>Welcome, {user.username}!</p> : <p>Please log in.</p>}
      {!user && <>
        <button
            onClick={() => (navigate("/login"))}
            style={{ marginLeft: 10 }}
        >
            Login
        </button>
        <button
            onClick={() => (navigate("/register"))}
            style={{ marginLeft: 10 }}
        >
            Register
        </button>
      </>
        }
      {user && <button onClick={() => logout()} style={{ marginLeft: 10 }}>Logout</button>}
      {user && (
        <>
          <button onClick={openBookingLink} style={{ marginLeft: 10 }}>
            {loadingCalendarUrl ? "Loading…" : "Booking a time slot"}
          </button>
          {calendarError && <p style={{ color: "red" }}>{calendarError}</p>}
        </>
      )}
    </div>
  );
}