import React, { useEffect, useState } from "react";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import SnackbarContent from "@mui/material/SnackbarContent";
import { ButtonGroup } from "@mui/material";
export default function DenseTable(e) {
  const [data, setData] = useState([]);
  const fetchData = () => {
    const url = `https://cors-anywhere.herokuapp.com/http://3.36.51.8:8000/dashboard/`;;
    fetch(url)
      .then((response) => response.json())
      .then((responseData) => {
        setData(responseData.RecentReport.Reports);
      });
    };
  useEffect(()=>{
    fetchData();
  },[]);

  console.log(data);
  return <Stack spacing={2.3}>   
  {Array.from(data).map((item)=>(
<SnackbarContent
  message={item.Date}
  action={<Stack spacing={2} direction="row">
  <ButtonGroup>
    <Button variant="contained" color="success">
      C
    </Button>
    <Button variant="text" color="success" style={{color:"white"}}>
      {item.Checked}
    </Button>
  </ButtonGroup>
  
  <ButtonGroup>
    <Button variant="contained">D</Button>
    <Button variant="text"  style={{color:"white"}}>{item.Detected}</Button>
  </ButtonGroup>
</Stack>}
/>
  ))}
</Stack>;
}
