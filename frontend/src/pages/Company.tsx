import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Company() {

  const [company, setCompany] = useState<any>(null);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/company")
      .then((response) => {

        setCompany(response.data);

      })
      .catch((error) => {

        console.error(error);

      });

  }, []);

  if (!company) {

    return (
      <Layout>
        <h2>Loading Company...</h2>
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
          Company Intelligence
        </h1>

        <hr />

        <h2>
          {company.company}
        </h2>

        <p>
          Risk Score: {company.risk_score}
        </p>

        <p>
          Investment Rating:
          {" "}
          {company.investment_rating}
        </p>

      </div>

    </Layout>

  );

}