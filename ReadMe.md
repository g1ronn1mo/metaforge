# Document Property Extractor

This project is a Flask-based microservice that extracts specific properties from a given document using the Doctran library and OpenAI's GPT model. The extracted properties include the document category, mentions of people, and a simplified explanation of the document's content.

## Features

- **Classification**: Classifies documents into different categories.
- **Data Mining**: Extracts structured data that can be used for data analysis.
- **Style Transfer**: Provides simplified explanations of documents.

## Requirements

- Docker
- Docker Compose


## Usage

1. Build and start the Docker container:

    ```sh
    docker-compose up --build
    ```

2. The Flask app will be running on `http://localhost:5000`.

3. To extract properties from a document, make a POST request to the `/extract` endpoint with the document text in JSON format. For example:

    ```sh
    curl -X POST http://localhost:5000/extract \
    -H "Content-Type: application/json" \
    -d '{
        "text": "[Generated with ChatGPT]\n\nConfidential Document - For Internal Use Only\n\nDate: July 1, 2023\n\nSubject: Updates and Discussions on Various Topics\n\nDear Team,\n\nI hope this email finds you well. In this document, I would like to provide you with some important updates and discuss various topics that require our attention. Please treat the information contained herein as highly confidential.\n\nSecurity and Privacy Measures\nAs part of our ongoing commitment to ensure the security and privacy of our customers' data, we have implemented robust measures across all our systems. We would like to commend John Doe (email: john.doe@example.com) from the IT department for his diligent work in enhancing our network security. Moving forward, we kindly remind everyone to strictly adhere to our data protection policies and guidelines. Additionally, if you come across any potential security risks or incidents, please report them immediately to our dedicated team at security@example.com.\n\nHR Updates and Employee Benefits\nRecently, we welcomed several new team members who have made significant contributions to their respective departments. I would like to recognize Jane Smith (SSN: 049-45-5928) for her outstanding performance in customer service. Jane has consistently received positive feedback from our clients. Furthermore, please remember that the open enrollment period for our employee benefits program is fast approaching. Should you have any questions or require assistance, please contact our HR representative, Michael Johnson (phone: 418-492-3850, email: michael.johnson@example.com).\n\nMarketing Initiatives and Campaigns\nOur marketing team has been actively working on developing new strategies to increase brand awareness and drive customer engagement. We would like to thank Sarah Thompson (phone: 415-555-1234) for her exceptional efforts in managing our social media platforms. Sarah has successfully increased our follower base by 20% in the past month alone. Moreover, please mark your calendars for the upcoming product launch event on July 15th. We encourage all team members to attend and support this exciting milestone for our company.\n\nResearch and Development Projects\nIn our pursuit of innovation, our research and development department has been working tirelessly on various projects. I would like to acknowledge the exceptional work of David Rodriguez (email: david.rodriguez@example.com) in his role as project lead. David's contributions to the development of our cutting-edge technology have been instrumental. Furthermore, we would like to remind everyone to share their ideas and suggestions for potential new projects during our monthly R&D brainstorming session, scheduled for July 10th.\n\nPlease treat the information in this document with utmost confidentiality and ensure that it is not shared with unauthorized individuals. If you have any questions or concerns regarding the topics discussed, please do not hesitate to reach out to me directly.\n\nThank you for your attention, and let's continue to work together to achieve our goals.\n\nBest regards,\n\nJason Fan\nCofounder & CEO\nPsychic\njason@psychic.dev\n"
    }'
    ```

## Running Tests

1. Ensure the Docker container is running:

    ```sh
    docker compose up
    ```

2. Run the test script:

    ```sh
    python test_app.py
    ```

   The test script will print the response data from the `/extract` endpoint and verify the extracted properties.
