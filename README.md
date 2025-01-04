# **Distributed Event Management System**

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Architecture](#architecture)
5. [Getting Started](#getting-started)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [Contact](#contact)

---

## **Overview**

The Distributed Event Management System is a platform designed to streamline the organization and participation in events. Users can register for events, purchase tickets, and receive real-time updates. The system leverages a microservices architecture with Docker and AWS DynamoDB for scalable and distributed operations.

---

## **Features**

- Event Registration and Management
- Ticket Sales and Validation
- User Notifications and Real-Time Updates
- RESTful APIs and WebSocket Communication
- Scalable, Containerized Deployment with Kubernetes

---

## **Technologies Used**

- **Backend**: Python, Flask
- **Database**: AWS DynamoDB (NoSQL)
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud Provider**: AWS (EC2, DynamoDB)
- **Testing Tools**: Postman, cURL

---

## **Architecture**

The architecture consists of three main services:
1. **Event Registration Service**
2. **Ticketing Service**
3. **User Engagement Service**

Each service is containerized using Docker, communicates via REST APIs, and uses WebSockets for real-time notifications. AWS DynamoDB serves as the NoSQL database.

---

## **Getting Started**

### **Prerequisites**

- Docker
- AWS CLI configured with appropriate credentials
- Kubernetes (for orchestration)

### **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/distributed-event-management-system.git
   cd distributed-event-management-system

2. Build Docker images:
   ```bash
   docker-compose build

3. Start the services:
   ```bash
   docker-compose up

---

## **Troubleshooting**

### **Common Errors**

### **1. 500 Internal Server Error:**

- Verify AWS credentials are configured.
- Check if DynamoDB tables exist with the correct schema.

### **2. No Credentials Error:**

- Set environment variables for AWS credentials:
   ```bash
   export AWS_ACCESS_KEY_ID="<your-access-key>"
   export AWS_SECRET_ACCESS_KEY="<your-secret-access>"

### **3. Docker Issues:**

- Check logs: docker-compose logs.

---

## **Contributing**

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature-name.
3. Commit changes: git commit -m "Add feature".
4. Push branch: git push origin feature-name.
5. Submit a pull request.

---

## **Contact**

Author: Shubham Limkar | Email: shubham.limkar@ucdconnect.ie

Author: Maithilee Nargide | Email: maithilee.nargide@ucdconnect.ie

Thank You!
