import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Explainability() {

  const [data, setData] =
    useState<any>(null);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:8000/explainability"
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
          Loading Explainability...
        </h2>

      </Layout>

    );

  }

  return (

    <Layout>

      <div>

        <h1>
          Explainable AI Dashboard
        </h1>

        <hr />

        <div
          style={{
            display: "flex",
            gap: "20px",
            marginTop: "20px",
          }}
        >

          <Card
            title="Prediction"
            value={data.prediction}
          />

          <Card
            title="Confidence"
            value={`${data.confidence}%`}
          />

        </div>

        <h2
          style={{
            marginTop: "40px",
          }}
        >
          Feature Importance
        </h2>

        {data.top_features.map(
          (
            feature: any,
            index: number
          ) => (

            <div
              key={index}
              style={{
                marginBottom: "15px",
              }}
            >

              <div>

                {feature.feature}

              </div>

              <div
                style={{
                  width: "100%",
                  background: "#374151",
                  height: "20px",
                  borderRadius: "10px",
                }}
              >

                <div
                  style={{
                    width:
                      `${feature.importance}%`,
                    background:
                      "#3B82F6",
                    height: "20px",
                    borderRadius:
                      "10px",
                  }}
                />

              </div>

            </div>

          )
        )}

        <h2
          style={{
            marginTop: "40px",
          }}
        >
          Model Comparison
        </h2>

        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "repeat(3, 1fr)",
            gap: "20px",
          }}
        >

          {data.models.map(
            (
              model: any,
              index: number
            ) => (

              <Card
                key={index}
                title={model.name}
                value={`${model.score}%`}
              />

            )
          )}

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
        padding: "20px",
        borderRadius: "12px",
        border:
          "1px solid #374151",
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