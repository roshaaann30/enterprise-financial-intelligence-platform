import { useState } from "react";
import axios from "axios";

import Layout from "../components/Layout";

export default function Chat() {

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          question,
        }
      );

      setAnswer(
        response.data.answer
      );

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <Layout>

      <div
        style={{
          maxWidth: "900px",
          margin: "0 auto",
        }}
      >

        <h1>AI Financial Assistant</h1>

        <hr />

        <textarea

          value={question}

          onChange={(e) =>
            setQuestion(
              e.target.value
            )
          }

          rows={5}

          style={{
            width: "100%",
            padding: "10px",
          }}

          placeholder="Ask a financial question..."

        />

        <br />
        <br />

        <button
          onClick={askQuestion}
        >
          Ask AI
        </button>

        <br />
        <br />

        <div>

          <h3>Response</h3>

          <p>{answer}</p>

        </div>

      </div>

    </Layout>

  );

}