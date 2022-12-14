import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';



export default function BasicTable(e) {
    function createData(name, calories) {
        return { name, calories };
      }
      
      let rows = [
      ];
    Array.from(Object.keys(e.data.Report)).map((v)=>{
        console.log(e.data.Report[v])
            
                if(Array.isArray(e.data.Report[v]) && e.data.Report[v].length > 0){
                    let str = e.data.Report[v];
                    rows.push(createData(v,str[0])) 
                    for(var i = 1; i<str.length; i++){
                        rows.push(createData("",str[i]))
                    }
                    
                }
            


           
    })
    console.log(rows);
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>점검 명</TableCell>
            <TableCell align="left">점검 결과</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="left">{row.calories}</TableCell>
              
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}