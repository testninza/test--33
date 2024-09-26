import requests

# Hardcoded secrets
API_KEY = "1234567890abcdef"
DB_PASSWORD = "password123"
JWT_SECRET = "mySuperSecretJWTKey"
password= "XyZ9876Pafffff"


def get_data_from_api(endpoint):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def connect_to_db():
    # Simulating a database connection with a hardcoded password
    connection = f"Connecting to DB with password: {DB_PASSWORD}"
    return connection

def create_jwt_token(user_id):
    # Simulating JWT token creation with a hardcoded secret
    token = f"JWT token for {user_id} using secret {JWT_SECRET}"
    return token

# Vulnerable function calls
data = get_data_from_api("https://api.example.com/data")
db_connection = connect_to_db()
jwt_token = create_jwt_token("user123")

print(data)
print(db_connection)
print(jwt_token)
