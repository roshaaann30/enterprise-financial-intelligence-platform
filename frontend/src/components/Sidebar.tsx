import { Link } from "react-router-dom";

const SIDEBAR_WIDTH = 280;

export default function Sidebar() {
  const linkStyle = {
    color: "#E5E7EB",
    textDecoration: "none",
    padding: "12px 16px",
    borderRadius: "10px",
    display: "block",
    fontSize: "15px",
    fontWeight: 500,
    marginBottom: "4px",
  };

  return (
    <aside
      style={{
        width: `${SIDEBAR_WIDTH}px`,
        height: "100vh",
        backgroundColor: "#071633",
        position: "fixed",
        left: 0,
        top: 0,
        borderRight: "1px solid #1F2937",
        overflowY: "auto",
        overflowX: "hidden",
        padding: "24px",
        boxSizing: "border-box",
        zIndex: 1000,
      }}
    >
      <div style={{ marginBottom: "40px" }}>
        <h1
          style={{
            color: "white",
            fontSize: "58px",
            margin: 0,
            lineHeight: 1,
          }}
        >
          EFIP
        </h1>

        <p
          style={{
            color: "#9CA3AF",
            fontSize: "12px",
            marginTop: "10px",
          }}
        >
          Enterprise Financial Intelligence Platform
        </p>
      </div>

      <div
        style={{
          color: "#64748B",
          fontSize: "12px",
          fontWeight: "bold",
          marginBottom: "12px",
          textTransform: "uppercase",
        }}
      >
        Overview
      </div>

      <Link to="/" style={linkStyle}>
        📊 Dashboard
      </Link>

      <Link to="/company" style={linkStyle}>
        🏢 Company Analysis
      </Link>

      <Link to="/forecasts" style={linkStyle}>
        📈 Forecasting
      </Link>

      <Link to="/portfolio" style={linkStyle}>
        💼 Portfolio Advisor
      </Link>

      <div
        style={{
          color: "#64748B",
          fontSize: "12px",
          fontWeight: "bold",
          marginTop: "30px",
          marginBottom: "12px",
          textTransform: "uppercase",
        }}
      >
        Intelligence
      </div>

      <Link to="/knowledge" style={linkStyle}>
        🕸 Knowledge Graph
      </Link>

      <Link to="/timeline" style={linkStyle}>
        🕒 Event Timeline
      </Link>

      <Link to="/chat" style={linkStyle}>
        🤖 AI Analyst
      </Link>

      <Link to="/scenario" style={linkStyle}>
        🧪 Scenario Simulator
      </Link>

      <div
        style={{
          color: "#64748B",
          fontSize: "12px",
          fontWeight: "bold",
          marginTop: "30px",
          marginBottom: "12px",
          textTransform: "uppercase",
        }}
      >
        AI Governance
      </div>

      <Link to="/monitoring" style={linkStyle}>
        📡 Monitoring
      </Link>

      <Link to="/explainability" style={linkStyle}>
        🧠 Explainability
      </Link>

      <Link to="/system" style={linkStyle}>
        🛡 System Status
      </Link>

      <div
        style={{
          color: "#64748B",
          fontSize: "12px",
          fontWeight: "bold",
          marginTop: "30px",
          marginBottom: "12px",
          textTransform: "uppercase",
        }}
      >
        MLOps
      </div>

      <Link to="/mlflow" style={linkStyle}>
        ⚙️ MLflow Tracking
      </Link>

      <div
        style={{
          marginTop: "40px",
          padding: "16px",
          background: "#0B1D44",
          border: "1px solid #1E3A8A",
          borderRadius: "12px",
        }}
      >
        <h4
          style={{
            color: "white",
            marginTop: 0,
            marginBottom: "10px",
          }}
        >
          Enterprise Edition
        </h4>

        <p
          style={{
            color: "#9CA3AF",
            fontSize: "12px",
            marginBottom: "12px",
          }}
        >
          Multi-Agent Financial Intelligence Platform
        </p>

        <div
          style={{
            color: "#22C55E",
            fontSize: "12px",
            fontWeight: "bold",
          }}
        >
          ● System Online
        </div>

        <div
          style={{
            color: "#9CA3AF",
            fontSize: "11px",
            marginTop: "10px",
          }}
        >
          Version 19.5
        </div>
      </div>
    </aside>
  );
}