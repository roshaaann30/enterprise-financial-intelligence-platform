import Layout from "../components/Layout";

import ReactFlow, {
  Background,
  Controls,
  MiniMap,
} from "reactflow";

import "reactflow/dist/style.css";

export default function KnowledgeGraph() {

  const nodes = [

    {
      id: "1",

      position: {
        x: 400,
        y: 50,
      },

      data: {
        label: "Apple",
      },

      style: {
        background: "#2563EB",
        color: "white",
        width: 180,
        textAlign: "center",
      },

    },

    {
      id: "2",

      position: {
        x: 150,
        y: 250,
      },

      data: {
        label: "CEO: Tim Cook",
      },

      style: {
        background: "#10B981",
        color: "white",
      },

    },

    {
      id: "3",

      position: {
        x: 400,
        y: 250,
      },

      data: {
        label: "Product: iPhone",
      },

      style: {
        background: "#F59E0B",
        color: "white",
      },

    },

    {
      id: "4",

      position: {
        x: 650,
        y: 250,
      },

      data: {
        label: "Competitor: Microsoft",
      },

      style: {
        background: "#EF4444",
        color: "white",
      },

    },

    {
      id: "5",

      position: {
        x: 400,
        y: 400,
      },

      data: {
        label: "Industry: Technology",
      },

      style: {
        background: "#8B5CF6",
        color: "white",
      },

    },

  ];

  const edges = [

    {
      id: "e1-2",

      source: "1",

      target: "2",

      label: "CEO",

      animated: true,

    },

    {
      id: "e1-3",

      source: "1",

      target: "3",

      label: "PRODUCT",

      animated: true,

    },

    {
      id: "e1-4",

      source: "1",

      target: "4",

      label: "COMPETITOR",

      animated: true,

    },

    {
      id: "e1-5",

      source: "1",

      target: "5",

      label: "INDUSTRY",

      animated: true,

    },

  ];

  return (

    <Layout>

      <h1
        style={{
          textAlign: "center",
          marginBottom: "20px",
        }}
      >
        Enterprise Knowledge Graph
      </h1>

      <div
        style={{
          height: "850px",
          border: "1px solid #374151",
          borderRadius: "12px",
        }}
      >

        <ReactFlow
          nodes={nodes}
          edges={edges}
          fitView
        >

          <MiniMap />

          <Controls />

          <Background />

        </ReactFlow>

      </div>

    </Layout>

  );

}