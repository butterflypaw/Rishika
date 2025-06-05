
import React from 'react';

const Dashboard = () => {
  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col-md-6 col-lg-4 mb-4">
          <div className="card shadow">
            <div className="card-body">
              <h5 className="card-title">Chart</h5>
              <p className="card-text">Placeholder for a chart.</p>
            </div>
          </div>
        </div>
        <div className="col-md-6 col-lg-4 mb-4">
          <div className="card shadow">
            <div className="card-body">
              <h5 className="card-title">Table</h5>
              <p className="card-text">Placeholder for a table.</p>
            </div>
          </div>
        </div>
        <div className="col-md-6 col-lg-4 mb-4">
          <div className="card shadow">
            <div className="card-body">
              <h5 className="card-title">Notifications</h5>
              <p className="card-text">Placeholder for notifications.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
