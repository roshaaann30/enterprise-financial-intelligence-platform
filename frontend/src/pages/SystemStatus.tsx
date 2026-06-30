import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function SystemStatus() {

  const [data, setData] =
    useState<any>(null);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:8000/system"
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
          Loading System Status...
        </h2>

      </Layout>

    );

  }

  return (

    <Layout>

      <div>

        <h1>
          Production Readiness Dashboard
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
            title="API Health"
            value={data.api_health}
          />

          <Card
            title="Database"
            value={data.database}
          />

          <Card
            title="Models"
            value={data.models}
          />

          <Card
            title="Environment"
            value={data.environment}
          />

          <Card
            title="Version"
            value={data.version}
          />

          <Card
            title="Latency"
            value={data.latency}
          />

          <Card
            title="Uptime"
            value={data.uptime}
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
        border: "1px solid #374151",
        borderRadius: "12px",
        padding: "20px",
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