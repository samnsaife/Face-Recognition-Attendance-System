import React from 'react';
import Dashboard from './Dashboard';
import Navbar from './components/Navbar';
import './App.css';

function App() {
  return (
    <div className="App bg-gray-100 min-h-screen">
      <Navbar />
      <Dashboard />
    </div>
  );
}

export default App;
