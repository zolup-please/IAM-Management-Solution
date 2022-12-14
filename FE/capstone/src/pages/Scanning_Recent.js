import React from "react";
import ButtonAppBar from "../ButtonAppBar";
import "../index.css";
import Sidenav from "../Sidenav";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Container from '@mui/material/Container';
import { Typography } from "@mui/material";
import { Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import SnackbarContent from "@mui/material/SnackbarContent";
import { ButtonGroup } from "@mui/material";
import data from "../sample.json"
import Report_Data from "../Report_Data";

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
          <Menu>
        { Array.from(data).map((e)=>(
          <Typography component="div" variant="h6">
            <SubMenu id="scan" label={
            <SnackbarContent
            message={e.Date}
            action={<Stack spacing={4} direction="row">
            <ButtonGroup>
              <Button variant="contained" color="success">
                C
              </Button>
              <Button variant="text" color="success">
                {e.Checked}
              </Button>
            </ButtonGroup>
            
            <ButtonGroup>
              <Button variant="contained">D</Button>
              <Button variant="text">{e.Detected}</Button>
            </ButtonGroup>
          </Stack>}
          />
          } style={{backgroundColor: "white"}}>
                <MenuItem style={{height: 600}} id="list-item">
                  <Report_Data report={e.report}></Report_Data>
                </MenuItem>
              </SubMenu>
          </Typography>
          ))}
        </Menu>
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
