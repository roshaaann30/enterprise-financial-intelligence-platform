import { useState } from "react";
import axios from "axios";

export default function AIChat() {

  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {

    const res = await axios.post(
      "http://127.0.0.1:8000/chat",
      {
        message: message,
      }
    );

    setResponse(res.data.response);
  };

  return (
    <div
      style={{
        padding: "30px",
        color: "white",
      }}
    >
      <h1>Enterprise AI Analyst</h1>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask about a company..."
        style={{
          width: "70%",
          padding: "12px",
          fontSize: "16px",
        }}
      />

      <button
        onClick={sendMessage}
        style={{
          marginLeft: "10px",
          padding: "12px 20px",
          cursor: "pointer",
        }}
      >
        Ask AI
      </button>

      <div
        style={{
          marginTop: "30px",
          background: "#111827",
          padding: "20px",
          borderRadius: "10px",
          whiteSpace: "pre-wrap",
        }}
      >
        {response}
      </div>
    </div>
  );
}