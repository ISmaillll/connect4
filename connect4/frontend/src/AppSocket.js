import React, { useState, useEffect } from 'react';
import SocketService from './server.js';
const App = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    // Subscribe to the 'message' event
    SocketService.onMessage((msg) => {
      setMessages((prevMessages) => [...prevMessages, msg]);
    });

    // Clean up the subscription on component unmount
    return () => {
      SocketService.offMessage();
    };
  }, []); // Run once on component mount

  const handleSendMessage = () => {
    SocketService.sendMessage(message);
    setMessage('');
  };

  return (
    <div>
      <ul>
        {messages.map((msg, index) => (
          <li key={index}>{msg}</li>
        ))}
      </ul>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>Send Message</button>
    </div>
  );
};

export default App;

