 Car Dealership Chatbot (Rasa)

A simple yet functional AI assistant built using the Rasa Framework.
This chatbot helps users explore available cars, check price ranges, schedule test drives, and ask general dealership queries.
Created as part of my journey into AI Engineering and conversational AI development.

📌 Features

🔍 Browse Cars by brand, model, or type (SUV, sedan, hatchback, etc.)

💰 Get Price Estimates for selected cars

🧾 View Car Specifications

📅 Book Test Drive Appointments

❓ Ask General Questions about dealership timings or services

🤖 Built using NLU (Natural Language Understanding) + Dialogue Management with Rasa

🛠️ Tech Stack

Rasa Open Source (NLU + Core)

Python 3.8+

YAML-based configuration (domain, nlu, stories, rules)

Custom actions using Python

SQLite / In-memory tracker store

📂 Project Structure
car-dealership-chatbot/
│
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   └── rules.yml
│
├── domain.yml
├── config.yml
├── actions/
│   └── actions.py
│
├── endpoints.yml
├── README.md
└── tests/

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/car-dealership-chatbot.git
cd car-dealership-chatbot

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Train the Model
rasa train

5️⃣ Run the Chatbot

Start action server (if using custom actions):

rasa run actions


Start chatbot shell:

rasa shell
