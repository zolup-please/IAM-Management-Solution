
import "./index.css";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { Button, ButtonGroup, Stack } from "@mui/material";
import React, { useEffect, useState } from "react";
import { Typography } from "@mui/material";

export default function SimpleContainer() {
    const [data, setData] = useState([]);
    const fetchData = () => {
      const url = `https://cors-anywhere.herokuapp.com/http://43.200.7.198:8000/dashboard/`;;
      fetch(url)
        .then((response) => response.json())
        .then((responseData) => {
          setData(responseData.Changes);
        });
      };
    useEffect(()=>{
      fetchData();
    },[]);
  return (
    <Container maxWidth="lx" fixed>
                    <Box
                      sx={{
                        bgcolor: "white",
                        width: "100%",
                        padding: "10px",
                        borderRadius: "10px",
                      }}
                    >
                      <Stack spacing={2} direction="row">
                        <ButtonGroup size="large" sx={{ paddingLeft: "30px" }}>
                          <Button variant="text" color="primary">
                          <Typography component="div" variant="h6" style={{color:"black"}}>총 계정</Typography>
                          </Button>
                          <Button variant="contained" color="warning">
                            {data.Total}
                          </Button>
                        </ButtonGroup>
                        <ButtonGroup size="large" sx={{ paddingLeft: "30px" }}>
                          <Button variant="text" color="primary">
                          <Typography component="div" variant="h6" style={{color:"black"}}>계정 생성</Typography>
                          </Button>
                          <Button variant="contained" color="success">
                          {data.Created}
                          </Button>
                        </ButtonGroup>
                        <ButtonGroup size="large" sx={{ paddingLeft: "30px" }}>
                          <Button variant="text" color="primary">
                          <Typography component="div" variant="h6" style={{color:"black"}}>계정 삭제</Typography>
                          </Button>
                          <Button variant="contained" color="primary">
                          {data.Deleted}
                          </Button>
                        </ButtonGroup>
                      </Stack>
                    </Box>
                  </Container>
  );
}