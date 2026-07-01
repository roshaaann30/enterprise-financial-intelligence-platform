import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function MLflow() {

  const [data, setData] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/mlflow-status")
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        console.error(err);
        setError("Unable to connect to MLflow API");
      });

  }, []);

  if (error) {
    return (
      <Layout>
        <h1>MLflow Experiment Tracking</h1>
        <p>{error}</p>
      </Layout>
    );
  }

  if (!data) {
    return (
      <Layout>
        <h2>Loading...</h2>
      </Layout>
    );
  }

  return (
    <Layout>

      <h1>MLflow Experiment Tracking</h1>

      <hr />

      <h2>Tracking: {data.tracking}</h2>

      <h2>Experiments: {data.experiments}</h2>

      <h2>Latest Model: {data.latest_model}</h2>

      <h2>Status: {data.status}</h2>

    </Layout>
  );
}