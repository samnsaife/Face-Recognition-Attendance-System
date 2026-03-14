import React from 'react';

const AttendanceCard = ({ name, time, location }) => {
  return (
    <div className="bg-white shadow-md rounded-xl p-4 hover:shadow-xl transition">
      <h2 className="text-xl font-semibold text-indigo-600">{name}</h2>
      <p className="text-gray-600 mt-2">🕒 {time}</p>
      <p className="text-gray-600">📍 {location?.join(', ')}</p>
    </div>
  );
};

export default AttendanceCard;
