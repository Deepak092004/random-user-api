import requests

def fetch_random_user():
    
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        username =user_data["login"]["username"]
        location = user_data["location"]["city"]
        age = user_data["dob"]["age"]
        return username, location, age
    else:
        raise Exception("Failed to fetch user data") 
def main():
    try:
        username, location ,age= fetch_random_user()
        print(f"Username: {username}, Location: {location}, AGE: {age}")
    except Exception as e:
        print(str(e))   
    finally:
        print("Execution completed.")
if __name__ == "__main__":
    main()
 
    
    
