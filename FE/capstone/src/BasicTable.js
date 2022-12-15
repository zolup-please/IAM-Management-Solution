import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Typography } from "@mui/material";


const IdInfo = {
  "checkedList": {
    "1.1.1": "AWS 계정 Root 사용자의 액세스 키가 30일 이내에 재발급되지 않았습니다.",
    "1.1.2": "IAM 사용자의 액세스 키가 90일 이내에 교체되지 않았습니다.",
    "1.1.3": "IAM 사용자의 액세스 키가 2개 이상 활성화되어 있습니다.",
    "1.1.4": "2개 이상의 SSH Public Key가 활성화된 IAM 사용자가 존재합니다.",
    "1.1.5": "IAM 사용자의 액세스 키가 2개 이상 활성화되어 있습니다.",
    "1.1.6": "2개 이상의 SSH Public Key가 활성화된 IAM 사용자가 존재합니다.",
    "1.1.7": "SSH Public Key가 90일 이내에 재발급 되지 않았습니다.",

    "1.2.1": "AWS 계정 Root 사용자의 MFA가 비활성화되어 있습니다.",
    "1.2.2": "IAM 사용자의 MFA가 비활성화 되어 있습니다.",

    "1.3.1": "IAM 암호 정책이 사용되지 않았습니다.",
    "1.3.2": "강력한 IAM 암호 정책을 설정하지 않았습니다.",
    "1.3.3": "IAM 암호 정책이 14자 이상의 암호를 요구하도록 설정하지 않았습니다.",
    "1.3.4": "IAM 암호 정책이 암호 재사용을 방지하도록 설정하지 않았습니다.",
    "1.3.5": "IAM 암호 정책이 암호를 90일 이내에 만료하도록 설정하지 않았습니다.",
    "1.3.6": "암호가 만료되거나 만료일이 7일 이내인 IAM 사용자가 존재합니다.",

    "1.4.1": "만료되거나 만료일이 7일 이내인 SSL/TLS 인증서가 존재합니다.",
    "1.4.2": "2014년 4월 1일 이전에 업로드 된 SSL/TLS 인증서가 존재합니다.",

    "2.1.1": "IAM USER에게 연결된 서비스",
    "2.1.2": "IAM GROUP에게 연결된 서비스",
    "2.1.3": "IAM ROLE에게 연결된 서비스",

    "2.2.1": "90일 이내 액세스 키나 패스워드를 통해 IAM 사용자가 접속한 기록이 없습니다.",
    "2.2.2":  "90일 이내 IAM GROUP을 이용하여 AWS 서비스에서 접근한 기록이 없습니다.",
    "2.2.3": "90일 이내 IAM ROLE을 사용한 기록이 없습니다.",
    "2.2.4": "90일 이내 해당 IAM POLICY를 이용하여 AWS 서비스에서 접근한 기록이 없습니다.",

    "2.3.1": "IAM USER에 연결된 관리형/인라인 정책이 없습니다.",
    "2.3.2": "IAM GROUP에 연결된 IAM USER가 없습니다.",
    "2.3.3": "IAM ROLE에 연결된 관리형/인라인 정책이 없습니다.",
    "2.3.4": "고객 관리형 IAM POLICY에 연결된 AIM 엔티티가 없습니다.",

    "2.4.1": "자신이 해당하는 조직의 조직원들과는 다른 권한이 존재합니다.",
    "2.4.2": "기존에 만들어진 정책과 동일한 정책이 생성되었습니다."
}}

export default function BasicTable(e) {
    function createData(name, calories) {
        return { name, calories };
      }
      
      let rows = [
      ];
      console.log("<BasicTable>로 넘어온 데이터 :",e.data);
    Array.from(Object.keys(e.data.Report)).map((v)=>{
                console.log(e.data.Report[v]);
                  if(Array.isArray(e.data.Report[v])){
                    let str = e.data.Report[v];
                    if(str.length==0){
                      rows.push(createData(v,"None")) 
                    }else{
                      console.log("str: ",str)
                      rows.push(createData(v,str[0])) 
                      for(var i = 1; i<str.length; i++){
                          rows.push(createData("",str[i]))
                      }
                    }

                }else{
                  rows.push(createData(v,e.data.Report[v]));
                }
    })

  return (
    <div style={{padding:10}}>
      <Typography component="div" variant="h5">{IdInfo.checkedList[e.idx]}</Typography>
      <br></br>
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead style={{backgroundColor: "rgb(50, 50, 50)"}}>
          <TableRow>
            <TableCell><Typography component="div" variant="h6" style={{color: "white"}}>점검 명</Typography></TableCell>
            <TableCell align="left"><Typography component="div" variant="h6" style={{color: "white"}}>점검 결과</Typography></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row" style={{width:300, fontWeight: "bold"}}>
                {row.name}
              </TableCell>
              <TableCell align="left" style={{}}>{row.calories}</TableCell>
              
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    </div>
  );
}