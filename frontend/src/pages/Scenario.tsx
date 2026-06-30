import { useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Scenario() {

  const [revenueChange, setRevenueChange] =
    useState("");

  const [interestChange, setInterestChange] =
    useState("");

  const [inflationChange, setInflationChange] =
    useState("");

  const [result, setResult] =
    useState<any>(null);

  const runSimulation = async () => {

    try {

      const response =
        await axios.post(
          "http://127.0.0.1:8000/scenario",
          {
            revenue_change:
              revenueChange,
            interest_change:
              interestChange,
            inflation_change:
              inflationChange,
          }
        );

      setResult(
        response.data
      );

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <Layout>

      <div>

        <h1>
          Scenario Simulator
        </h1>

        <hr />

        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(3, 1fr)",
            gap: "20px",
            marginTop: "30px",
          }}
        >

          <div>

            <label>
              Revenue Change (%)
            </label>

            <input
              type="number"
              value={revenueChange}
              onChange={(e) =>
                setRevenueChange(
                  e.target.value
                )
              }
              style={inputStyle}
            />

          </div>

          <div>

            <label>
              Interest Rate Change (%)
            </label>

            <input
              type="number"
              value={interestChange}
              onChange={(e) =>
                setInterestChange(
                  e.target.value
                )
              }
              style={inputStyle}
            />

          </div>

          <div>

            <label>
              Inflation Change (%)
            </label>

            <input
              type="number"
              value={inflationChange}
              onChange={(e) =>
                setInflationChange(
                  e.target.value
                )
              }
              style={inputStyle}
            />

          </div>

        </div>

        <button
          onClick={runSimulation}
          style={buttonStyle}
        >
          Run Simulation
        </button>

        {result && (

          <div
            style={{
              marginTop: "40px",
            }}
          >

            <h2>
              Simulation Results
            </h2>

            <div
              style={{
                display: "grid",
                gridTemplateColumns:
                  "repeat(4, 1fr)",
                gap: "20px",
                marginTop: "20px",
              }}
            >

              <Card
                title="Forecast Impact"
                value={`${result.forecast_impact}%`}
              />

              <Card
                title="Risk Score"
                value={`${result.risk_score}`}
              />

              <Card
                title="Confidence"
                value={`${result.confidence}%`}
              />

              <Card
                title="Assessment"
                value={result.assessment}
              />

            </div>

          </div>

        )}

      </div>

    </Layout>

  );

}

function Card(
  {
    title,
    value,
  }: {
    title: string;
    value: string;
  }
) {

  return (

    <div
      style={{
        background: "#111827",
        border: "1px solid #374151",
        borderRadius: "12px",
        padding: "20px",
        textAlign: "center",
      }}
    >

      <h3>
        {title}
      </h3>

      <h1>
        {value}
      </h1>

    </div>

  );

}

const inputStyle = {

  width: "100%",

  padding: "12px",

  marginTop: "10px",

  background: "#111827",

  color: "white",

  border: "1px solid #374151",

  borderRadius: "8px",

} as const;

const buttonStyle = {

  marginTop: "30px",

  padding: "12px 24px",

  background: "#2563EB",

  color: "white",

  border: "none",

  borderRadius: "8px",

  cursor: "pointer",

  fontSize: "16px",

} as const;