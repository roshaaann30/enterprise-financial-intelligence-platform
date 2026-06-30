import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Company from "./pages/Company";
import Forecasts from "./pages/Forecasts";
import Portfolio from "./pages/Portfolio";
import KnowledgeGraph from "./pages/KnowledgeGraph";
import Timeline from "./pages/Timeline";
import AIChat from "./pages/AIChat";
import Monitoring from "./pages/Monitoring";
import Explainability from "./pages/Explainability";
import Scenario from "./pages/Scenario";
import SystemStatus from "./pages/SystemStatus";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Dashboard />} />

        <Route path="/company" element={<Company />} />

        <Route path="/forecasts" element={<Forecasts />} />

        <Route path="/portfolio" element={<Portfolio />} />

        <Route path="/knowledge" element={<KnowledgeGraph />} />

        <Route path="/timeline" element={<Timeline />} />

        <Route path="/chat" element={<AIChat />} />

        <Route path="/monitoring" element={<Monitoring />} />

        <Route
          path="/explainability"
          element={<Explainability />}
        />

        <Route
          path="/scenario"
          element={<Scenario />}
        />

        <Route
          path="/system"
          element={<SystemStatus />}
        />

      </Routes>

    </BrowserRouter>

  );

}

export default App;