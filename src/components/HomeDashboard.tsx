import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { ArrowUpRight, ArrowDownRight, MoreVertical, Plus } from 'lucide-react';

const data = [
  { name: 'Jan', value: 400 },
  { name: 'Feb', value: 300 },
  { name: 'Mar', value: 200 },
  { name: 'Apr', value: 278 },
  { name: 'May', value: 189 },
];

const HomeDashboard: React.FC = () => {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="flex items-center justify-between mb-2">
            <h2 className="text-lg font-semibold">Total Ads</h2>
            <span className="text-green-500 flex items-center">
              <ArrowUpRight className="w-4 h-4 mr-1" />
              12%
            </span>
          </div>
          <p className="text-3xl font-bold">1,234</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="flex items-center justify-between mb-2">
            <h2 className="text-lg font-semibold">Active Channels</h2>
            <span className="text-red-500 flex items-center">
              <ArrowDownRight className="w-4 h-4 mr-1" />
              5%
            </span>
          </div>
          <p className="text-3xl font-bold">56</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <div className="flex items-center justify-between mb-2">
            <h2 className="text-lg font-semibold">Total Detections</h2>
            <span className="text-green-500 flex items-center">
              <ArrowUpRight className="w-4 h-4 mr-1" />
              18%
            </span>
          </div>
          <p className="text-3xl font-bold">89,012</p>
        </div>
      </div>
      <div className="bg-white p-4 rounded-lg shadow mb-8">
        <h2 className="text-lg font-semibold mb-4">Detection Trends</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="value" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="bg-white rounded-lg shadow">
        <div className="flex items-center justify-between p-4 border-b">
          <h2 className="text-lg font-semibold">Recent Detections</h2>
          <button className="text-blue-500 hover:text-blue-700">View All</button>
        </div>
        <table className="w-full">
          <thead>
            <tr className="bg-gray-50">
              <th className="p-2 text-left">Ad Name</th>
              <th className="p-2 text-left">Channel</th>
              <th className="p-2 text-left">Timestamp</th>
              <th className="p-2 text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            {[1, 2, 3].map((_, index) => (
              <tr key={index} className="border-t">
                <td className="p-2">Ad {index + 1}</td>
                <td className="p-2">Channel {index + 1}</td>
                <td className="p-2">{new Date().toLocaleString()}</td>
                <td className="p-2">
                  <button className="text-gray-500 hover:text-gray-700">
                    <MoreVertical className="w-4 h-4" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="fixed bottom-8 right-8">
        <button className="bg-blue-500 text-white p-4 rounded-full shadow-lg hover:bg-blue-600 transition-colors">
          <Plus className="w-6 h-6" />
        </button>
      </div>
    </div>
  );
};

export default HomeDashboard;