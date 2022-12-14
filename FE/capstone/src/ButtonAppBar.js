import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";


export default function ButtonAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar style={{backgroundColor:"rgb(50, 50, 50)"}}>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1}} id="title">
            Capstone Project
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
