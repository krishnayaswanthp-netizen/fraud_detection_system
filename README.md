# fraud_detection_system
fraud detection system  :  This project simulates a fraud detection system that integrates machine learning logic (fraud prediction) with Twilio SMS alerts for real-time user verification. When a suspicious transaction is detected, the system automatically:
Sends an SMS alert to the registered user.

Requests approval by replying YES (approve) or NO (block).

Simulates freezing/blocking of accounts if the user denies the transaction.

🔹 Features

Reads and processes credit card transaction data (creditcard.csv).

Detects potential fraudulent activity (currently simulated).

Uses Twilio API to send SMS alerts.

Simulates real-time user responses and acts accordingly.

Can be extended with an actual fraud detection ML model for real-world use.

🔹 Tech Stack

Python (pandas, time)

Twilio API (SMS service)

CSV dataset (credit card transactions)
