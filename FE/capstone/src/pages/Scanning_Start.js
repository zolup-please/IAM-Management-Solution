import React, { useState } from "react";
import ButtonAppBar from "../ButtonAppBar";
import "../index.css";
import Sidenav from "../Sidenav";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { useTheme } from '@mui/material/styles';
import data from "../scanning_data.json"
import CheckList from "../CheckList";

import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import SnackbarContent from '@mui/material/SnackbarContent';
import { Typography } from "@mui/material";
import Card from '@mui/material/Card';

import IconButton from '@mui/material/IconButton';

import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

function Scanning_Start() {
  const theme = useTheme();
  let request_body = { "checkedCount": 0,
  "checkedList": [  {
    "1.1.1": false,
    "1.1.2": false,
    "1.1.3": false,
    "1.1.4": false,
    "1.1.5": false,
    "1.1.6": false,
    "1.1.7": false
},
{
    "1.2.1": false,
    "1.2.2": false
},
{
    "1.3.1": false,
    "1.3.2": false,
    "1.3.3": false,
    "1.3.4": false,
    "1.3.5": false,
    "1.3.6": false
},
{
    "1.4.1": false,
    "1.4.2": false
},
{
    "2.1.1": false,
    "2.1.2": false,
    "2.1.3": false
},
{
    "2.2.1": false,
    "2.2.2": false,
    "2.2.3": false,
    "2.2.4": false
},
{
    "2.3.1": false,
    "2.3.2": false,
    "2.3.3": false,
    "2.3.4": false
},
{
    "2.4.1": false,
    "2.4.2": false
}]
}
  const [count, setCount] = useState([[],[],[],[],[],[],[],[],[]]);
  const [open, setOpen] = React.useState(false);



  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
  };
  const CreateRequestBody = ()=>{
    request_body.checkedCount = resultCount();
    for(var i  = 0; i< 9; i++){
      let tmp = Object.values(count[i])
      console.log(tmp)
      for(var j = 0; j<tmp.length; j++){
        console.log(tmp[j])
        request_body.checkedList[i][tmp[j]] = true;
      }

    }
    console.log("완성된 body"+JSON.stringify(request_body))
  }
  const resultCount=()=> {
    let sum = 0;
    for(var i = 0; i<9; i++){
      sum +=count[i].length;
    }
    return sum;
  };
  const startScan=()=>{
    setOpen(true);
    CreateRequestBody();
    fetch("https://cors-anywhere.herokuapp.com/http://52.78.94.58:8000/scanning/", {

  method: "POST",
   headers: {
      'Content-Type': 'application/json',
    },
  body: JSON.stringify(request_body),
})
.then((response) => response.json())
.then((result) => console.log(result));

   // alert("스캔을 시작합니다. ")
  }
  const resultPrint = (
    <Typography component="div" variant="h5">
    {resultCount()+" 개 선택됨"}
  </Typography>

  );
  const action = (
    <Button color="secondary" size="small">
      lorem ipsum dolorem
    </Button>
  );
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
      <Paper elevation={3}
      sx={{height: '100%', display:"flex"}}>
        <div style={{height: 900, overflow: "auto", width: '70%'}}>
          <Menu>{
          Array.from(Object.keys(data.ScanningList)).map((e,i)=>(
            <Typography component="div" variant="h5"><SubMenu label={e+" ("+count[i].length+"/"+data.ScanningList[e].length+")"} style={{marginRight:15}}>
            <MenuItem style={{height: "100%", }} id="list-item">
              <CheckList tagName={data.ScanningList[e]} setCount={setCount} index={i}></CheckList>
            </MenuItem>
          </SubMenu>
          </Typography>
          ))
          }
          </Menu>

        </div>
        <div style={{width: "30%", display:"flex"}}>
          <Paper elevation={3}
          sx={{width: "100%"}}>
            
                <Stack spacing={2} sx={{ maxWidth: 600, padding: 5}}>
      <SnackbarContent message={resultPrint} />
      <Card sx={{ display: 'flex' }}>
        
      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', pl: 1, pb: 1 }}>
          
          <IconButton aria-label="play/pause" onClick={startScan}>
            <PlayArrowIcon sx={{ height: 50, width: 50 }} />
          </IconButton>
          <Typography component="div" variant="h5">
            Start Scanning
          </Typography>

        </Box>

      </Box>

      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose} sx={{display:"absolute"}}>
        <MuiAlert onClose={handleClose} sx={{ width: 600, height: 100}}>
        <Typography component="div" variant="h6">Now Start Scanning..</Typography>
        <Typography component="div" variant="h5">수 분 이내로 결과 리포트를 받아 볼 수 있습니다.</Typography>
        </MuiAlert>
      </Snackbar>

    </Card>
    
    </Stack>
    </Paper>
  </div>
</Paper>

</Box>
      </div>
    </div>
  );
}

export default Scanning_Start;
