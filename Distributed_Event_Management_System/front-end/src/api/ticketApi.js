import axios from 'axios';

const API_BASE_URL = 'http://localhost:3002'; // Ticketing Service Base URL

// Purchase a ticket (Add a new ticket)
export const purchaseTicket = async (ticketData) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/add_ticket`, ticketData);
    return response.data;
  } catch (error) {
    console.error('Error purchasing ticket:', error);
    throw error;
  }
};

// Fetch tickets by UserID (using front-end filtering)
export const fetchTicketsByUser = async (userId) => {
  try {
    const allTickets = await getAllTickets();
    return allTickets.filter(ticket => ticket.UserID === userId);
  } catch (error) {
    console.error('Error fetching tickets by user ID:', error);
    throw error;
  }
};

// Fetch all tickets
export const getAllTickets = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/tickets`);
    return response.data;
  } catch (error) {
    console.error('Error fetching all tickets:', error);
    throw error;
  }
};

// Fetch a specific ticket by TicketID
export const fetchTicketById = async (ticketId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/get_ticket/${ticketId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching ticket by ID:', error);
    throw error;
  }
};
