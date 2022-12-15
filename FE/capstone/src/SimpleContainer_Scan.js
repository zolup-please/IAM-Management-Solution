
import "./index.css";
import { Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import SnackbarContent from "@mui/material/SnackbarContent";
import { Button, ButtonGroup, Stack } from "@mui/material";
import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";
import Report_Data from "./Report_Data"
import fuckingJson from "./sample.json"

export default function SimpleContainer_Scan() {
    const [data, setData] = useState(fuckingJson);
    const fetchData = () => {
      const url = `https://cors-anywhere.herokuapp.com/http://43.200.7.198:8000/scanning/recent`;
      fetch(url)
        .then((response) => response.json())
        .then((responseData) => {
          setData(responseData.Reports);
        });
      };
    useEffect(()=>{
      fetchData();
    },[]);
  console.log("RECENT SCANNING DATA ",data);
  return (
    <Menu>
    { Array.from(data).map((e)=>(
        <SubMenu id="scan" label={
        <SnackbarContent
        message={<Typography component="div" variant="h6">{e.Date}</Typography>}
        action={<Stack spacing={4} direction="row">
        <ButtonGroup>
          <Button variant="contained" color="success">
            C
          </Button>
          <Button variant="text" color="success"  style={{color:"white"}}>
            {e.Checked}
          </Button>
        </ButtonGroup>
        
        <ButtonGroup>
          <Button variant="contained">D</Button>
          <Button variant="text"  style={{color:"white"}}>{e.Detected}</Button>
        </ButtonGroup>
      </Stack>}
      />
      }>
            <MenuItem style={{height: "100%"}} id="list-item">
              <Report_Data report={e.report}></Report_Data>
            </MenuItem>
          </SubMenu>
        
      ))}
    </Menu>
  );
}