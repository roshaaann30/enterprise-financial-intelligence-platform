import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Monitoring() {

  const [data, setData] =
    useState<any>(null);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:8000/monitoring"
      )
      .then((response) => {

        setData(
          response.data
        );

      });

  }, []);

  if (!data) {

    return (

      <Layout>

        <h2>
          Loading Monitoring...
        </h2>

      </Layout>

    );

  }

  return (

    <Layout>

      <div>

        <h1>
          Enterprise Monitoring
        </h1>

        <hr />

        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(3, 1fr)",
            gap: "20px",
            marginTop: "20px",
          }}
        >

          <Card
            title="Model Accuracy"
            value={`${data.model_accuracy}%`}
          />

          <Card
            title="Confidence"
            value={`${data.prediction_confidence}%`}
          />

          <Card
            title="Drift Score"
            value={`${data.drift_score}%`}
          />

          <Card
            title="Data Quality"
            value={`${data.data_quality}%`}
          />

          <Card
            title="API Health"
            value={data.api_health}
          />

          <Card
            title="System Status"
            value={data.system_status}
          />

        </div>

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
        padding: "25px",
        borderRadius: "12px",
        border: "1px solid #374151",
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