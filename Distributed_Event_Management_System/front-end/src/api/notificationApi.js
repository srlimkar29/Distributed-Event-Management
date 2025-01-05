import axios from 'axios';

const API_BASE_URL = 'http://localhost:3003'; 

export const fetchNotifications = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/notifications`);
    return response.data;
  } catch (error) {
    console.error('Error fetching notifications:', error);
    throw error;
  }
};

export const sendNotification = async (notificationData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/notify`, notificationData);
    return response.data;
  } catch (error) {
    console.error('Error sending notification:', error);
    throw error;
  }
};
