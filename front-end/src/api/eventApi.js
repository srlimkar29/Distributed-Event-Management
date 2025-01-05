import axios from 'axios';

const API_BASE_URL = 'http://localhost:3001'; // Event Registration Service Base URL

// Fetch all events
export const fetchEvents = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/events`);
    return response.data;
  } catch (error) {
    console.error('Error fetching events:', error);
    throw error;
  }
};

// Fetch an event by EventID and OrganizerID
export const fetchEventById = async (eventId, organizerId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/get_event/${eventId}/${organizerId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching event by ID:', error);
    throw error;
  }
};

// Add a new event (if needed in the front end)
export const addEvent = async (eventData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/add_event`, eventData);
    return response.data;
  } catch (error) {
    console.error('Error adding event:', error);
    throw error;
  }
};
