import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Portfolio() {

  const [portfolio, setPortfolio] = useState<any>(null);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/portfolio")
      .then((response) => {

        setPortfolio(response.data);

      })
      .catch((error) => {

        console.error(error);

      });

  }, []);

  if (!portfolio) {

    return (
      <Layout>
        <h2>Loading Portfolio...</h2>
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
          Portfolio Advisor
        </h1>

        <hr />

        <p>
          Risk Score:
          {" "}
          {portfolio.risk_score}
        </p>

        <p>
          Diversification Score:
          {" "}
          {portfolio.diversification_score}
        </p>

        <p>
          Recommendation:
          {" "}
          {portfolio.recommendation}
        </p>

      </div>

    </Layout>

  );

}