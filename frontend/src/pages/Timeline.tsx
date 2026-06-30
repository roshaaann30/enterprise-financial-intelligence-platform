import { useEffect, useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Timeline() {

  const [events, setEvents] =
    useState<any[]>([]);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:8000/timeline"
      )
      .then((response) => {

        setEvents(
          response.data
        );

      });

  }, []);

  return (

    <Layout>

      <div>

        <h1>
          Event Intelligence Timeline
        </h1>

        <hr />

        <div
          style={{
            marginTop: "30px",
          }}
        >

          {events.map(
            (
              event,
              index
            ) => (

              <div
                key={index}
                style={{
                  display: "flex",
                  gap: "20px",
                  marginBottom: "25px",
                  alignItems: "center",
                }}
              >

                <div
                  style={{
                    minWidth: "100px",
                    fontWeight: "bold",
                  }}
                >
                  {event.date}
                </div>

                <div
                  style={{
                    width: "20px",
                    height: "20px",
                    borderRadius: "50%",
                    background: "#3B82F6",
                  }}
                />

                <div
                  style={{
                    background: "#111827",
                    padding: "15px",
                    borderRadius: "10px",
                    border:
                      "1px solid #374151",
                    flex: 1,
                  }}
                >

                  <h3>
                    {event.event}
                  </h3>

                  <p>
                    Market Impact:
                    {" "}
                    {event.impact}
                  </p>

                </div>

              </div>

            )
          )}

        </div>

      </div>

    </Layout>

  );

}