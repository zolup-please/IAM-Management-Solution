import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';


const columns = [
  { field: 'id', headerName: 'ID', width: 130 },
  { field: 'Description', headerName: '점검 옵션', width: 230 },
  { field: 'Detail', headerName: '설명', width: 630 },
];

export default function CheckList(e) {
    const rows = e.tagName;
    let size = 0;
    if(rows.length < 2){
        size = rows.length*200
    }else if(rows.length < 3){
        size = rows.length*130
    }else{
        size = rows.length*(95)
    }
  return (
    <div style={{height: size,width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={[rows.length]}
        rowsPerPageOptions={[rows.length]}
        checkboxSelection
        onSelectionModelChange={(ids)=>{
            e.setCount((prev)=>{
                prev[e.index] = ids;
                console.log(prev)
                return {...prev}
            });
        }}
      />
    </div>
  );
}