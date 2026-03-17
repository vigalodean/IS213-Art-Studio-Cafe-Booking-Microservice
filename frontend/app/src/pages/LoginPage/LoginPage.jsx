import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export default function LoginPage() {
  const navigate = useNavigate();
  const { login, loading, error } = useAuth();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await login(username, password);
    if (res.success) navigate("/");
    else alert(res.message || "Login failed");
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>Login</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 12, maxWidth: 300 }}>
        <input placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <button type="submit" disabled={loading}>{loading ? "Logging in..." : "Login"}</button>
        {error && <p style={{ color: "red" }}>Error: {error.message}</p>}
      </form>
      <button onClick={() => navigate("/register")} style={{ marginTop: 10 }}>Go to Register</button>
    </div>
  );
}