
import React, { useState, useEffect } from 'react';

const TodoApp = () => {
  const [tasks, setTasks] = useState(() => JSON.parse(localStorage.getItem('tasks')) || []);
  const [filter, setFilter] = useState('all');
  const [newTask, setNewTask] = useState('');

  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  const addTask = () => {
    if (newTask.trim()) {
      setTasks([...tasks, { id: Date.now(), text: newTask.trim(), completed: false }]);
      setNewTask('');
    }
  };

  const toggleTask = (id) => {
    setTasks(tasks.map(task => (task.id === id ? { ...task, completed: !task.completed } : task)));
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  const editTask = (id, newText) => {
    setTasks(tasks.map(task => (task.id === id ? { ...task, text: newText } : task)));
  };

  const filteredTasks = tasks.filter(task => {
    if (filter === 'active') return !task.completed;
    if (filter === 'completed') return task.completed;
    return true;
  });

  return (
    <div className="container my-4">
      <h1 className="text-center">To-Do List</h1>
      <div className="mb-3 d-flex">
        <input
          type="text"
          className="form-control me-2"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Add a new task"
        />
        <button className="btn btn-primary" onClick={addTask}>Add</button>
      </div>
      <div className="btn-group mb-3">
        <button className="btn btn-outline-secondary" onClick={() => setFilter('all')}>All</button>
        <button className="btn btn-outline-secondary" onClick={() => setFilter('active')}>Active</button>
        <button className="btn btn-outline-secondary" onClick={() => setFilter('completed')}>Completed</button>
      </div>
      <ul className="list-group">
        {filteredTasks.map(task => (
          <li key={task.id} className="list-group-item d-flex justify-content-between align-items-center">
            <div>
              <input
                type="checkbox"
                className="form-check-input me-2"
                checked={task.completed}
                onChange={() => toggleTask(task.id)}
              />
              <span
                contentEditable={!task.completed}
                suppressContentEditableWarning={true}
                onBlur={(e) => editTask(task.id, e.target.textContent)}
                style={{ textDecoration: task.completed ? 'line-through' : 'none' }}
              >
                {task.text}
              </span>
            </div>
            <button className="btn btn-danger btn-sm" onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;
