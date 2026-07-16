import { useEffect, useState } from "react";
import axios from "axios";

import KPICard from "../components/KPICard";
import Layout from "../components/Layout";

export default function Dashboard() {
  const [data, setData] = useState<any>(null);

  const [riskData, setRiskData] = useState({
    average_return: 0,
    volatility: 0,
    sharpe_ratio: 0,
    max_drawdown: 0,
    risk_score: 0,
  });

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/dashboard")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.error(error);
      });

    axios
      .get("http://127.0.0.1:8000/portfolio-risk")
      .then((response) => {
        setRiskData(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  if (!data) {
    return (
      <Layout>
        <h2>Loading...</h2>
      </Layout>
    );
  }

  return (
    <Layout>
      <div>
        <h1
          style={{
            fontSize: "3rem",
            fontWeight: "700",
            textAlign: "center",
            marginBottom: "10px",
          }}
        >
          Enterprise Financial Intelligence
        </h1>

        <h3
          style={{
            textAlign: "center",
            color: "#9CA3AF",
            fontWeight: "400",
            marginTop: "0",
            marginBottom: "30px",
          }}
        >
          AI-Powered Financial Analytics Platform
        </h3>

        <hr />

        <h2
          style={{
            textAlign: "center",
            marginTop: "30px",
            marginBottom: "30px",
          }}
        >
          Executive Overview
        </h2>

        <div
          style={{
            display: "flex",
            gap: "20px",
            justifyContent: "center",
            flexWrap: "wrap",
          }}
        >
          <KPICard
            title="Risk Score"
            value={data.risk_score}
          />

          <KPICard
            title="Forecast Score"
            value={data.forecast_score}
          />

          <KPICard
            title="Portfolio Score"
            value={data.portfolio_score}
          />

          <KPICard
            title="Model Health"
            value={data.model_health}
          />
        </div>

        {/* Portfolio Risk Analytics */}

        <h2
          style={{
            textAlign: "center",
            marginTop: "50px",
            marginBottom: "30px",
          }}
        >
          Portfolio Risk Analytics
        </h2>

        <div
          style={{
            display: "flex",
            gap: "20px",
            justifyContent: "center",
            flexWrap: "wrap",
          }}
        >
          <KPICard
            title="Average Return"
            value={riskData.average_return}
          />

          <KPICard
            title="Volatility"
            value={riskData.volatility}
          />

          <KPICard
            title="Sharpe Ratio"
            value={riskData.sharpe_ratio}
          />

          <KPICard
            title="Max Drawdown"
            value={riskData.max_drawdown}
          />

          <KPICard
            title="Risk Score"
            value={riskData.risk_score}
          />
        </div>
      </div>
    </Layout>
  );
}