import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./components/Home";
import Realm from "./components/Realm";

function App() {
  return (
    <>
      <Router>
        {/* <Navbar /> */}
        {/* <div style={{ marginTop: "90px" }}></div> */}
        <Routes>
          <Route path="/" element={<Home />}>
            {/* <Home /> */}
          </Route>
          <Route path="/realm/:id" element={<Realm />}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
