import { useEffect, useState } from "react";
import axios from "axios";
import Layout from "../components/Layout";

export default function DVC() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/dvc-status")
      .then((response) => {
        setData(response.data);
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
      <h1>DVC Dataset Versioning</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",
          gap: "20px",
          marginTop: "20px",
        }}
      >
        <div>
          <h3>DVC Enabled</h3>
          <h2>{String(data.dvc_enabled)}</h2>
        </div>

        <div>
          <h3>Datasets</h3>
          <h2>{data.datasets}</h2>
        </div>

        <div>
          <h3>Tracked File</h3>
          <h2>{data.tracked_file}</h2>
        </div>

        <div>
          <h3>Status</h3>
          <h2>{data.status}</h2>
        </div>
      </div>
    </Layout>
  );
}