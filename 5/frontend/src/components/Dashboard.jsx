import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const Dashboard = () => {
  const chartData = [
    { name: 'Jan', value: 400 },
    { name: 'Feb', value: 300 },
    { name: 'Mar', value: 500 },
    { name: 'Apr', value: 600 },
    { name: 'May', value: 700 },
  ];

  const notifications = [
    "Server maintenance scheduled at 3 PM.",
    "New user registrations increased by 20%.",
    "Weekly report available for download."
  ];

  const tableData = [
    { id: 1, name: 'Product A', sales: 100 },
    { id: 2, name: 'Product B', sales: 200 },
    { id: 3, name: 'Product C', sales: 300 },
  ];

  return (
    <div className="container mt-4">
      <div className="row g-4">
        {/* Notifications Card */}
        <div className="col-12 col-lg-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Notifications</h5>
              <ul className="list-group list-group-flush">
                {notifications.map((note, index) => (
                  <li key={index} className="list-group-item">{note}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Line Chart Card */}
        <div className="col-12 col-lg-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Sales Overview</h5>
              <div style={{ width: '100%', height: 300 }}>
                <ResponsiveContainer>
                  <LineChart data={chartData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Line type="monotone" dataKey="value" stroke="#8884d8" />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>
        </div>

        {/* Table Card */}
        <div className="col-12">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Top Products</h5>
              <table className="table table-striped">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Product Name</th>
                    <th>Sales</th>
                  </tr>
                </thead>
                <tbody>
                  {tableData.map(row => (
                    <tr key={row.id}>
                      <td>{row.id}</td>
                      <td>{row.name}</td>
                      <td>{row.sales}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
