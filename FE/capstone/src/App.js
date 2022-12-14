import { Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Monitoring from "./pages/Monitoring";
import Scanning_Start from "./pages/Scanning_Start";
import Scanning_Recent from "./pages/Scanning_Recent";

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/scan1" element={<Scanning_Start />} />
        <Route path="/scan2" element={<Scanning_Recent />} />
        <Route path="/monitor" element={<Monitoring />} />
      </Routes>
    </div>
  );
};

export default App;
