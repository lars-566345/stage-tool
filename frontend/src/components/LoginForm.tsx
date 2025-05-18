import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

interface TokenAuthResponse {
  data?: {
    login?: {
      success: boolean;
      errors?: Record<string, string[]>;
      profile?: {
        firstName: string;
        lastName: string;
      } | null;
    };
  };
  errors?: any;
}

function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? decodeURIComponent(match[2]) : null;
}

const LoginForm: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [profileName, setProfileName] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setErrorMessage(null);
    setProfileName(null);

    try {
      const csrfToken = getCookie('csrftoken');

      const headers: Record<string, string> = {
        "Content-Type": "application/json",
      };
      
      if (csrfToken) {
        headers["X-CSRFToken"] = csrfToken;
      }

      const response = await fetch("http://localhost:8000/graphql/", {
        method: "POST",
        credentials: "include",
        headers,
        body: JSON.stringify({
          query: `
            mutation Login($username: String!, $password: String!) {
              login(username: $username, password: $password) {
                success
                errors
                token
              }
            }
          `,
          variables: { username, password },
        }),
      });

      const result: TokenAuthResponse = await response.json();

      if (result.data?.login?.success) {
        const profile = result.data.login.profile;
        if (profile) {
          setProfileName(`${profile.firstName} ${profile.lastName}`);
        }
        navigate("/dashboard")
      } else if (result.data?.tokenAuth?.errors) {
        const errors = result.data.tokenAuth.errors;
        const messages = Object.values(errors)
          .flat()
          .join(" ");
        setErrorMessage(messages);
      } else if (result.errors) {
        setErrorMessage(result.errors.map((e: any) => e.message).join(", "));
      } else {
        setErrorMessage("Unknown error during login");
      }
    } catch (err) {
      setErrorMessage("Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleLogin} style={{ maxWidth: 320, margin: "auto" }}>
      <h2>Login</h2>

      <input
        type="text"
        value={username}
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
        required
        style={{ display: "block", width: "100%", marginBottom: 10, padding: 8 }}
      />

      <input
        type="password"
        value={password}
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        required
        style={{ display: "block", width: "100%", marginBottom: 10, padding: 8 }}
      />

      <button type="submit" disabled={loading} style={{ width: "100%", padding: 10 }}>
        {loading ? "Logging in..." : "Login"}
      </button>

      {errorMessage && <p style={{ color: "red", marginTop: 10 }}>{errorMessage}</p>}

      {profileName && (
        <p style={{ marginTop: 10, color: "green" }}>
          Logged in as: <strong>{profileName}</strong>
        </p>
      )}
    </form>
  );
};

export default LoginForm;
