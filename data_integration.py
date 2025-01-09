import pandas as pd

# data integration 

# integrate csv data
transaction_data =  [
    {"transaction_id": 1, "user_id": 101, "transaction_amount": 150.00, "transaction_type": "deposit", "timestamp": "2025-01-01 09:15:00", "merchant_name": "ABC Store"},
    {"transaction_id": 2, "user_id": 102, "transaction_amount": 200.00, "transaction_type": "withdrawal", "timestamp": "2025-01-01 10:45:00", "merchant_name": "XYZ Shop"},
    {"transaction_id": 3, "user_id": 103, "transaction_amount": 350.00, "transaction_type": "deposit", "timestamp": "2025-01-01 12:00:00", "merchant_name": "ElectroMart"},
    {"transaction_id": 4, "user_id": 104, "transaction_amount": 500.00, "transaction_type": "withdrawal", "timestamp": "2025-01-01 13:30:00", "merchant_name": "SuperBank"},
    {"transaction_id": 5, "user_id": 101, "transaction_amount": 100.00, "transaction_type": "deposit", "timestamp": "2025-01-02 08:00:00", "merchant_name": "TechStore"},
    {"transaction_id": 6, "user_id": 102, "transaction_amount": 50.00, "transaction_type": "withdrawal", "timestamp": "2025-01-02 09:00:00", "merchant_name": "ABC Store"},
    {"transaction_id": 7, "user_id": 103, "transaction_amount": 450.00, "transaction_type": "deposit", "timestamp": "2025-01-02 10:20:00", "merchant_name": "Gadget World"},
    {"transaction_id": 8, "user_id": 104, "transaction_amount": 250.00, "transaction_type": "withdrawal", "timestamp": "2025-01-02 14:45:00", "merchant_name": "MarketHub"},
    {"transaction_id": 9, "user_id": 101, "transaction_amount": 300.00, "transaction_type": "deposit", "timestamp": "2025-01-03 16:00:00", "merchant_name": "HomeGoods"},
    {"transaction_id": 10, "user_id": 102, "transaction_amount": 200.00, "transaction_type": "withdrawal", "timestamp": "2025-01-03 17:25:00", "merchant_name": "SuperBank"},
    {"transaction_id": 11, "user_id": 103, "transaction_amount": 100.00, "transaction_type": "deposit", "timestamp": "2025-01-04 08:30:00", "merchant_name": "TechStore"},
    {"transaction_id": 12, "user_id": 104, "transaction_amount": 150.00, "transaction_type": "withdrawal", "timestamp": "2025-01-04 11:00:00", "merchant_name": "MarketHub"},
    {"transaction_id": 13, "user_id": 101, "transaction_amount": 50.00, "transaction_type": "deposit", "timestamp": "2025-01-05 09:00:00", "merchant_name": "ElectroMart"},
    {"transaction_id": 14, "user_id": 102, "transaction_amount": 300.00, "transaction_type": "withdrawal", "timestamp": "2025-01-05 10:30:00", "merchant_name": "Gadget World"},
    {"transaction_id": 15, "user_id": 103, "transaction_amount": 200.00, "transaction_type": "deposit", "timestamp": "2025-01-06 12:15:00", "merchant_name": "SuperBank"},
    {"transaction_id": 16, "user_id": 104, "transaction_amount": 400.00, "transaction_type": "withdrawal", "timestamp": "2025-01-06 13:45:00", "merchant_name": "TechStore"},
    {"transaction_id": 17, "user_id": 101, "transaction_amount": 75.00, "transaction_type": "deposit", "timestamp": "2025-01-07 08:00:00", "merchant_name": "MarketHub"},
    {"transaction_id": 18, "user_id": 102, "transaction_amount": 500.00, "transaction_type": "withdrawal", "timestamp": "2025-01-07 09:45:00", "merchant_name": "HomeGoods"},
    {"transaction_id": 19, "user_id": 103, "transaction_amount": 250.00, "transaction_type": "deposit", "timestamp": "2025-01-08 10:00:00", "merchant_name": "SuperBank"},
    {"transaction_id": 20, "user_id": 104, "transaction_amount": 300.00, "transaction_type": "withdrawal", "timestamp": "2025-01-08 11:30:00", "merchant_name": "ElectroMart"}
]

# tra_df = pd.DataFrame(transaction_data)
# tra_df.to_csv("transaction_data", index=False)

user_data = [
    {"user_id" : 101, "name": "John Doe", "age": 28, "gender": "Male", "location": "New York"},
    {"user_id" : 102, "name": "Jane Smith", "age": 34, "gender": "Female", "location": "Los Angeles"},
    {"user_id" : 103,"name": "David Brown", "age": 40, "gender": "Male", "location": "San Francisco"},
    {"user_id" : 104,"name": "Emily White", "age": 26, "gender": "Female", "location": "Chicago"},
    {"user_id" : 105,"name": "Mike Johnson", "age": 32, "gender": "Male", "location": "Miami"},
    {"user_id" : 106,"name": "Olivia Clark", "age": 29, "gender": "Female", "location": "Boston"},
    {"user_id" : 107,"name": "Liam Walker", "age": 33, "gender": "Male", "location": "Seattle"},
    {"user_id" : 108,"name": "Sophia Lee", "age": 31, "gender": "Female", "location": "Atlanta"},
    {"user_id" : 109,"name": "James Harris", "age": 25, "gender": "Male", "location": "Dallas"},
    {"user_id" : 110,"name": "Charlotte Lewis", "age": 35, "gender": "Female", "location": "Denver"},
    {"user_id" : 111,"name": "Daniel King", "age": 38, "gender": "Male", "location": "Washington D.C."},
    {"user_id" : 112,"name": "Mia Scott", "age": 28, "gender": "Female", "location": "Portland"},
    {"user_id" : 113,"name": "Matthew Martinez", "age": 27, "gender": "Male", "location": "Houston"},
    {"user_id" : 114,"name": "Ava Robinson", "age": 30, "gender": "Female", "location": "Austin"},
    {"user_id" : 115,"name": "Lucas Lopez", "age": 36, "gender": "Male", "location": "San Diego"},
    {"user_id" : 116,"name": "Grace Miller", "age": 27, "gender": "Female", "location": "Las Vegas"},
    {"user_id" : 117,"name": "Benjamin Carter", "age": 29, "gender": "Male", "location": "New York"},
    {"user_id" : 118,"name": "Amelia Thomas", "age": 32, "gender": "Female", "location": "Los Angeles"},
    {"user_id" : 119,"name": "Henry Garcia", "age": 34, "gender": "Male", "location": "San Francisco"},
    {"user_id" : 120,"name": "Chloe Wilson", "age": 26, "gender": "Female", "location": "Chicago"}
]

# user_df = pd.DataFrame(user_data)
# user_df.to_csv("user_data", index=False)

log_data = [
    {"log_id":1, "user_id": 101, "ip_address": "192.168.1.1", "failed_login_attempt": 1, "timestamp": "2025-01-01 08:00:00"},
    {"log_id":2, "user_id": 102, "ip_address": "192.168.1.2", "failed_login_attempt": 2, "timestamp": "2025-01-01 09:10:00"},
    {"log_id":3, "user_id": 103, "ip_address": "192.168.1.3", "failed_login_attempt": 1, "timestamp": "2025-01-01 10:15:00"},
    {"log_id":4, "user_id": 104, "ip_address": "192.168.1.4", "failed_login_attempt": 3, "timestamp": "2025-01-01 11:25:00"},
    {"log_id":5, "user_id": 101, "ip_address": "192.168.1.5", "failed_login_attempt": 1, "timestamp": "2025-01-02 08:20:00"},
    {"log_id":6, "user_id": 102, "ip_address": "192.168.1.6", "failed_login_attempt": 0, "timestamp": "2025-01-02 09:40:00"},
    {"log_id":7, "user_id": 103, "ip_address": "192.168.1.7", "failed_login_attempt": 2, "timestamp": "2025-01-02 10:55:00"},
    {"log_id":8, "user_id": 104, "ip_address": "192.168.1.8", "failed_login_attempt": 1, "timestamp": "2025-01-02 12:00:00"},
    {"log_id":9, "user_id": 101, "ip_address": "192.168.1.9", "failed_login_attempt": 0, "timestamp": "2025-01-03 07:30:00"},
    {"log_id":10, "user_id": 102, "ip_address": "192.168.1.10", "failed_login_attempt": 1, "timestamp": "2025-01-03 08:50:00"},
    {"log_id":11, "user_id": 103, "ip_address": "192.168.1.11", "failed_login_attempt": 1, "timestamp": "2025-01-03 10:00:00"},
    {"log_id":12, "user_id": 104, "ip_address": "192.168.1.12", "failed_login_attempt": 0, "timestamp": "2025-01-03 11:15:00"},
    {"log_id":13, "user_id": 101, "ip_address": "192.168.1.13", "failed_login_attempt": 2, "timestamp": "2025-01-04 09:00:00"},
    {"log_id":14, "user_id": 102, "ip_address": "192.168.1.14", "failed_login_attempt": 1, "timestamp": "2025-01-04 10:20:00"},
    {"log_id":15, "user_id": 103, "ip_address": "192.168.1.15", "failed_login_attempt": 0, "timestamp": "2025-01-04 11:40:00"},
    {"log_id":16, "user_id": 104, "ip_address": "192.168.1.16", "failed_login_attempt": 3, "timestamp": "2025-01-04 12:50:00"},
    {"log_id":17, "user_id": 101, "ip_address": "192.168.1.17", "failed_login_attempt": 0, "timestamp": "2025-01-05 08:30:00"},
    {"log_id":18, "user_id": 102, "ip_address": "192.168.1.18", "failed_login_attempt": 1, "timestamp": "2025-01-05 09:45:00"},
    {"log_id":19, "user_id": 103, "ip_address": "192.168.1.19", "failed_login_attempt": 2, "timestamp": "2025-01-05 10:55:00"},
    {"log_id":20, "user_id": 104, "ip_address": "192.168.1.20", "failed_login_attempt": 1, "timestamp": "2025-01-05 11:10:00"}
]

log_df=pd.DataFrame(log_data)
log_df.to_csv("log_data", index=False)


# df_transaction_data = pd.read_csv("transaction_data")
# df_log_data = pd.read_csv("log_data")
# df_user_data = pd.read_csv("user_data")
# #print(df_transaction_data.head())
# #print(df_log_data.head())
# print(df_transaction_data.info)