import os

def insecure_function(user_input):
    # Command Injection Vulnerability
    os.system("echo " + user_input)

def sql_injection(user_input):
    # SQL Injection Vulnerability
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    print(query)

def hardcoded_password():
    # Hardcoded Password Vulnerability
    password = "supersecretpassword"
    print("Password is: " + password)

def main():
    user_input = input("Enter something: ")
    insecure_function(user_input)
    sql_injection(user_input)
    hardcoded_password()

if __name__ == "__main__":
    main()
