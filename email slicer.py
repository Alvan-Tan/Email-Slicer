def email_slice(email):
    # Getting username of email, the portion before @
    index = email.index("@")
    username = email[:index]

    # Getting domain, the portion after @
    domain = email[index + 1:]
    return username, domain
def email_check(email):
    if email.count("@") > 1 or email.count("@") == 0:
        return False
    return True
def domain_check(domain):
    if domain.count(".") < 1:
        return False
    return True
# Get the email that needs to be sliced from the user, taking into account accidental white spaces before or after

email = input("Please input your email: ").strip()

# Simple validity check, an email could only have 1 @
while not email_check(email):
    print("Invalid email")
    email = input("Please input your email: ").strip()

username, domain = email_slice(email)

# Simple validity check, a domain should have at least 1 .
while not domain_check(domain):
    print("Invalid email")
    email = input("Please input your email: ").strip()
    # Need to recheck new email
    while not email_check(email):
        print("Invalid email")
        email = input("Please input your email: ").strip()
    username, domain = email_slice(email)

# Output

print(f"Your username is {username}, your domain is {domain}")