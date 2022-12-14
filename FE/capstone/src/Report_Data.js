import * as React from 'react';
import { Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import BasicTable from './BasicTable';
import "./index.css";

export default function Report_Data(data) {
//console.log(data.report);
  return (
    <div>
{
    Array.from(Object.keys(data.report)).map((e,i)=>(
        <Menu>
            <SubMenu label={e} >
            <MenuItem style={{height: "100%"}} id="item">
                <BasicTable data={data.report[e]} idx={e}></BasicTable>
            </MenuItem>
        </SubMenu>

            
        </Menu>
    ))
    }
    </div>

  );
}