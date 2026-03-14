import React, { useEffect, useState } from 'react';
import AttendanceCard from './components/AttendanceCard';

const Dashboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/attendance_data/attendance.json')
      .then(res => res.json())
      .then(setData)
      .catch(err => console.error('Failed to fetch attendance:', err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Attendance Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {data.slice().reverse().map((entry, index) => (
          <AttendanceCard key={index} {...entry} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
