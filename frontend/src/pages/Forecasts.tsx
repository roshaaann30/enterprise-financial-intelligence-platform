import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Forecasts() {

  const [forecast, setForecast] = useState<any>(null);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/forecast")
      .then((response) => {

        setForecast(response.data);

      })
      .catch((error) => {

        console.error(error);

      });

  }, []);

  if (!forecast) {

    return (
      <Layout>
        <h2>Loading Forecast...</h2>
      </Layout>
    );

  }

  return (

    <Layout>

      <div
        style={{
          textAlign: "center",
        }}
      >

        <h1>
          Forecast Dashboard
        </h1>

        <hr />

        <h2>
          Revenue Growth Forecast
        </h2>

        <p>
          Expected Growth:
          {" "}
          {forecast.revenue_growth}%
        </p>

        <p>
          Confidence:
          {" "}
          {forecast.forecast_confidence}%
        </p>

      </div>

    </Layout>

  );

}