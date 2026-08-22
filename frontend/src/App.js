import React, { useState, useEffect } from 'react';

function App() {
    const [message, setMessage] = useState('');
    const [tasks, setTasks] = useState([]);

    const submitTask = async () => {
        await fetch('/api/tasks', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message }),
        });
        setMessage('');
        fetchTasks();
    };

    const fetchTasks = async () => {
        const res = await fetch('/api/tasks');
        const data = await res.json();
        setTasks(data);
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div>
            <h1>Task Manager</h1>
            <input value={message} onChange={(e) => setMessage(e.target.value)} />
            <button onClick={submitTask}>Submit Task</button>
            <ul>
                {tasks.map(task => <li key={task.id}>{task.message}</li>)}
            </ul>
        </div>
    );
}

export default App;