import ButtonAppBar from "../ButtonAppBar";
import "../index.css";
import Sidenav from "../Sidenav";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import DenseTable from "../DenseTable";
import { Button, ButtonGroup, Stack } from "@mui/material";
import Barchart from "../Barchart";
import json_data from "../Dashboard_Report.json";
import { Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import SimpleContainer from "../SimpleContainer";
const Dashboard = () => {
    return (
      <div>
        <ButtonAppBar></ButtonAppBar>
        <div className="Sidebar">
          <Sidenav></Sidenav>
          <div style={{ display: "flex", width: "100%" }}>
            <div className="Recent-Scanning">
              <Box
                sx={{
                  backgroundColor: "#EEEEF2",
  
                  height: "95%",
                  padding: "15px",
                  borderRadius: "10px",
                }}
              >
                <center>
                  <h2> 최근 스캐닝 결과</h2>
                </center>
  
                <DenseTable report={json_data.RecentReport.Reports}></DenseTable>
              </Box>
            </div>
            <div className="IAM">
              <div className="IAM_Info">
                <Box
                  sx={{
                    backgroundColor: "#EEEEF2",
                    padding: "15px",
                    borderRadius: "10px",
                    marginBottom: "10px",
                    height: "100%",
                  }}
                >
                  <h2>IAM 활동</h2>
                  <Barchart data={json_data.IAMActivities}></Barchart>
                </Box>
              </div>
              <div className="IAM_Change">
                <Box
                  sx={{
                    backgroundColor: "#EEEEF2",
                    padding: "20px",
                    marginTop: "10px",
                    height: "75%",
                    borderRadius: "10px",
                  }}
                >
                  <h2>변동사항</h2>
                 <SimpleContainer></SimpleContainer>
                </Box>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  
};

export default Dashboard;
