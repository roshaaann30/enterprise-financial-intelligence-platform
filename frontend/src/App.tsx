import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Company from "./pages/Company";
import Forecasts from "./pages/Forecasts";
import Portfolio from "./pages/Portfolio";
import KnowledgeGraph from "./pages/KnowledgeGraph";
import Timeline from "./pages/Timeline";
import AIChat from "./pages/AIChat";
import Scenario from "./pages/Scenario";
import Monitoring from "./pages/Monitoring";
import Explainability from "./pages/Explainability";
import SystemStatus from "./pages/SystemStatus";
import MLflow from "./pages/MLflow";
import DVC from "./pages/DVC";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Dashboard */}
        <Route path="/" element={<Dashboard />} />

        {/* Analytics */}
        <Route path="/company" element={<Company />} />
        <Route path="/forecasts" element={<Forecasts />} />
        <Route path="/portfolio" element={<Portfolio />} />

        {/* Intelligence */}
        <Route path="/knowledge" element={<KnowledgeGraph />} />
        <Route path="/timeline" element={<Timeline />} />
        <Route path="/chat" element={<AIChat />} />
        <Route path="/scenario" element={<Scenario />} />

        {/* Governance */}
        <Route path="/monitoring" element={<Monitoring />} />
        <Route path="/explainability" element={<Explainability />} />
        <Route path="/system" element={<SystemStatus />} />

        {/* MLOps */}
        <Route path="/mlflow" element={<MLflow />} />
        <Route path="/dvc" element={<DVC />} />

        {/* Fallback */}
        <Route
          path="*"
          element={<Navigate to="/" replace />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;