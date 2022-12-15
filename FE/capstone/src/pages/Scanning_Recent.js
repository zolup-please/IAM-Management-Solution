import React from "react";
import ButtonAppBar from "../ButtonAppBar";
import "../index.css";
import Sidenav from "../Sidenav";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Container from '@mui/material/Container';
import { Typography } from "@mui/material";
import SimpleContainer_Scan from "../SimpleContainer_Scan";


function Scanning_Recent() {

  return (
    <div>
      <ButtonAppBar></ButtonAppBar>
      <div className="Sidebar">
        <Sidenav></Sidenav>

      
      <Box
      sx={{
          m: 1,
          padding: '10px',
          width: '100%',
          height: '100%',
        
      }}
    >
      <Paper elevation={3} sx={{height: '100%', display:"flex", backgroundColor: "#EEEEF2"}}>
        <div style={{height: 900, width:"100%", overflow: "auto"}}>

        <Container fixed>
          <Box sx={{padding:5}}>
          <Typography component="div" variant="h5">최근 리포트</Typography>

          </Box>
          <div style={{width:"100%"}}>
          <SimpleContainer_Scan></SimpleContainer_Scan>
      </div>

      </Container>
          </div>
      </Paper>
    </Box>
    </div>
    </div>
  );
}

export default Scanning_Recent;
