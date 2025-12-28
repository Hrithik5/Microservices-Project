
# Microservices-Based Video-to-MP3 Converter

This project is a microservices-based application that converts video files into MP3 format. It leverages Python, RabbitMQ, MongoDB, MySQL, Docker, and Kubernetes to ensure efficient processing, storage, and delivery of MP3 files.

## Architectural Diagram
![image](https://github.com/user-attachments/assets/3590b08b-d7c5-4611-b7e2-4671ce1d3bf0)



## Tech Stack

**Programming Language:** Python

**Message Broker:** RabbitMQ

**Database:** MongoDB, MySQL

**Containerization:** Docker

**Orchestration:** Kubernetes

**Authentication:** JWT


## WorkFlow

* A user initiates a video conversion to MP3, which triggers a request to the Gateway 
* The Gateway stores the video in MongoDB and sends a message to the RabbitMQ queue, notifying downstream services that a video is ready for processing 
* The video-to-MP3 converter service consumes messages from the RabbitMQ queue, retrieves the video from MongoDB, converts it to MP3, stores the MP3 in MongoDB, and sends a new message to the queue 
* The notification service consumes messages from the queue and sends an email notification to the client, informing them that the MP3 is ready for download 
* The client uses a unique ID and JWT to make a request to the API Gateway to download the MP3, which is then pulled from MongoDB and served to the client 

