import React, { useState } from 'react';

function TaskItem({ task, onToggle, onDelete, onEdit }) {
  const [isEditing, setIsEditing] = useState(false);
  const [text, setText] = useState(task.text);

  const handleEdit = () => {
    if (isEditing) {
      onEdit(task.id, text);
    }
    setIsEditing(!isEditing);
  };

  return (
    <li className={task.completed ? 'completed' : ''}>
      <input type="checkbox" checked={task.completed} onChange={() => onToggle(task.id)} />
      {isEditing ? (
        <input value={text} onChange={(e) => setText(e.target.value)} />
      ) : (
        <span>{task.text}</span>
      )}
      <button onClick={handleEdit}>{isEditing ? 'Save' : 'Edit'}</button>
      <button onClick={() => onDelete(task.id)}>Delete</button>
    </li>
  );
}

export default TaskItem;