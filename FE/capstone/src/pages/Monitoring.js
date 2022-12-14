import React from "react";
import ButtonAppBar from "../ButtonAppBar";
import "../index.css";
import Sidenav from "../Sidenav";

function Monitoring() {
  return (
    <div>
      <ButtonAppBar></ButtonAppBar>
      <div className="Sidebar">
        <Sidenav></Sidenav>
        <h1>모니터링 페이지 입니다?</h1>
      </div>
    </div>
  );
}

export default Monitoring;
