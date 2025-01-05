import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const fetchNotifications = () => {
      axios.get('http://localhost:3003/notifications')
        .then((response) => {
          setNotifications(response.data);
        })
        .catch((error) => console.error('Error fetching notifications:', error));
    };

    // Fetch notifications initially and periodically (e.g., every 10 seconds)
    fetchNotifications();
    const interval = setInterval(fetchNotifications, 10000);

    return () => clearInterval(interval); // Cleanup interval on component unmount
  }, []);

  return (
    <div>
      <h2>Notifications</h2>
      <ul>
        {notifications.map((notification, index) => (
          <li key={index}>{notification.Message}</li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
