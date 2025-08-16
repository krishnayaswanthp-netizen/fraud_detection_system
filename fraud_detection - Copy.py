from twilio.rest import Client
import time
import pandas as pd



pd.read_csv(r"C:\Users\OneDrive\Desktop\FraudDetection\creditcard.csv")



TWILIO_ACCOUNT_SID = '920c22f84a913186808ce79c4bca1884CA'
TWILIO_AUTH_TOKEN = '850fa148d2adc7170f1a06752b2682a4'
TWILIO_PHONE = '+1xxxxxxxxxx'
USER_PHONE = '+91xxxxxxxxxx'



client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)




def send_alert_sms(transaction_data):
    message = client.messages.create(
        body=f"Suspicious transaction detected: {transaction_data}\nReply YES to approve, NO to block.",
        from_=TWILIO_PHONE,
        to=USER_PHONE
    )
    print(f"Alert sent: SID {message.sid}")



def simulate_user_response():
    print("Waiting for user response...")
    time.sleep(10)
    return "NO"  # or "YES"



def handle_transaction_with_user_check(transaction_data):
    # Simulating fraud prediction (1 = fraud, 0 = safe)
    prediction = 1
    if prediction == 1:
        send_alert_sms(transaction_data)
        response = simulate_user_response()
        if response.strip().upper() == "YES":
            print("User approved the transaction.")
        else:
            print("Transaction blocked. Freezing account...")
    else:
        print("Transaction approved.")



# Simulate a transaction
sample_transaction = {"amount": 5000, "location": "New York", "time": "02:00 AM"}



handle_transaction_with_user_check(sample_transaction)