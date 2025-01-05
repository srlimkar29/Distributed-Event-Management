import React, { useState } from "react";
import { purchaseTicket } from "../api/ticketApi"; // Ensure ticketApi.js is properly imported

const TicketPurchase = () => {
  const [ticket, setTicket] = useState({ EventID: "", UserID: "" });

  const handleSubmit = (e) => {
    e.preventDefault();
    purchaseTicket(ticket)
      .then(() => alert("Ticket purchased successfully"))
      .catch((error) => console.error("Error purchasing ticket:", error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Event ID"
        value={ticket.EventID}
        onChange={(e) => setTicket({ ...ticket, EventID: e.target.value })}
      />
      <input
        type="text"
        placeholder="User ID"
        value={ticket.UserID}
        onChange={(e) => setTicket({ ...ticket, UserID: e.target.value })}
      />
      <button type="submit">Purchase Ticket</button>
    </form>
  );
};

export default TicketPurchase;
