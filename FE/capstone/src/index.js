import React from "react";
import "./index.css";
import App from "./App";
import { BrowserRouter } from "react-router-dom";
import {createRoot} from 'react-dom/client';
import { ProSidebarProvider } from "react-pro-sidebar";
const root = createRoot(document.getElementById("root"));
root.render( <BrowserRouter>
  <ProSidebarProvider>
    <App />
  </ProSidebarProvider>
</BrowserRouter>);