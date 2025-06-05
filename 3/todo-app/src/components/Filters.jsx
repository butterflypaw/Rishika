import React from 'react';

function Filters({ filter, setFilter }) {
  return (
    <div className="filters">
      <button onClick={() => setFilter('all')} className={filter === 'all' ? 'active' : ''}>All</button>
      <button onClick={() => setFilter('active')} className={filter === 'active' ? 'active' : ''}>Active</button>
      <button onClick={() => setFilter('completed')} className={filter === 'completed' ? 'active' : ''}>Completed</button>
    </div>
  );
}

export default Filters;