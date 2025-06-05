
import React from 'react';
import Chart from './components/Chart';
import Table from './components/Table';
import Notification from './components/Notification';
import './App.css';

function App() {
  return (
    <div className="dashboard">
      <div className="widget"><Chart /></div>
      <div className="widget"><Table /></div>
      <div className="widget"><Notification /></div>
    </div>
  );
}

export default App;
