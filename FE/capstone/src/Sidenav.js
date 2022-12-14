import React from "react";
import { Sidebar, Menu, MenuItem } from "react-pro-sidebar";
import "./index.css";
import { Link } from "react-router-dom";
import { Typography } from "@mui/material";

const Sidenav = () => {
  return (
    <>
      <Sidebar id="Menu">
        <Menu>
          <MenuItem routerLink={<Link to="/"></Link>} id="item"> <Typography component="div" variant="h6">  Dashboard </Typography> </MenuItem>
            <MenuItem routerLink={<Link to="/scan1"></Link>} id="item">
            <Typography component="div" variant="h6">Scanning</Typography>
            </MenuItem>
            <MenuItem routerLink={<Link to="/scan2"></Link>} id="item">  <Typography component="div" variant="h6">Report </Typography> </MenuItem>
        </Menu>
      </Sidebar>
    </>
  );
};
export default Sidenav;
