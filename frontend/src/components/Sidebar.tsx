import { Link } from "react-router-dom";

export default function Sidebar() {

  const linkStyle = {
    color: "#E5E7EB",
    textDecoration: "none",
    padding: "12px 16px",
    borderRadius: "10px",
    display: "block",
    fontSize: "15px",
    fontWeight: 500,
  };

  return (

    <div
      style={{
        width: "280px",
        height: "100vh",
        backgroundColor: "#0F172A",
        position: "fixed",
        left: 0,
        top: 0,
        padding: "24px",
        borderRight: "1px solid #1F2937",

        overflowY: "auto",
        overflowX: "hidden",
      }}
    >

      {/* Header */}

      <div
        style={{
          marginBottom: "35px",
        }}
      >

        <h1
          style={{
            color: "white",
            marginBottom: "5px",
            fontSize: "56px",
          }}
        >
          EFIP
        </h1>

        <p
          style={{
            color: "#9CA3AF",
            fontSize: "12px",
          }}
        >
          Enterprise Financial Intelligence Platform
        </p>

      </div>

      {/* Overview */}

      <div
        style={{
          color: "#6B7280",
          fontSize: "12px",
          marginBottom: "10px",
          textTransform: "uppercase",
          fontWeight: "bold",
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

      {/* Intelligence */}

      <div
        style={{
          marginTop: "25px",
          marginBottom: "10px",
          color: "#6B7280",
          fontSize: "12px",
          textTransform: "uppercase",
          fontWeight: "bold",
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

      {/* AI Governance */}

      <div
        style={{
          marginTop: "25px",
          marginBottom: "10px",
          color: "#6B7280",
          fontSize: "12px",
          textTransform: "uppercase",
          fontWeight: "bold",
        }}
      >
        AI Governance
      </div>

      <Link to="/monitoring" style={linkStyle}>
        📡 Monitoring
      </Link>

      <Link to="/explainability" style={linkStyle}>
        🧠 Explainable AI
      </Link>

      <Link to="/system" style={linkStyle}>
        🛡 System Status
      </Link>

      {/* Footer Card */}

      <div
        style={{
          marginTop: "40px",
          marginBottom: "30px",

          background: "#111827",
          border: "1px solid #374151",
          borderRadius: "12px",
          padding: "15px",
        }}
      >

        <h4
          style={{
            color: "white",
            marginBottom: "10px",
          }}
        >
          Enterprise Edition
        </h4>

        <p
          style={{
            color: "#9CA3AF",
            fontSize: "12px",
            marginBottom: "10px",
          }}
        >
          Multi-Agent Financial Intelligence Platform
        </p>

        <div
          style={{
            color: "#10B981",
            fontWeight: "bold",
            fontSize: "12px",
          }}
        >
          ● System Online
        </div>

        <div
          style={{
            color: "#9CA3AF",
            marginTop: "10px",
            fontSize: "11px",
          }}
        >
          Version 18.19
        </div>

      </div>

    </div>

  );

}