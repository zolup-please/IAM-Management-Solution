import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import BasicTable from './BasicTable';


export default function Report_Data(data) {
//console.log(data.report);
  return (
    <div>
{
    Array.from(Object.keys(data.report)).map((e,i)=>(
        <Menu>
            <SubMenu label={e} >
            <MenuItem style={{height: "100%"}}>
                <BasicTable data={data.report[e]}></BasicTable>
            </MenuItem>
        </SubMenu>

            
        </Menu>
    ))
    }
    </div>

  );
}