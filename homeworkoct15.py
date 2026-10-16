def validata_username(username):
    return len(username)>3
def validata_passward(passward) :
    return len(passward)>= 8 and any(ch.isdigit()for ch in passward)
def validata_email(email):
    return "@" in email
def signup(username,passward,email):
    if validata_username(username)and validata_passward(passward)and validata_email(email):
        return "your entered data is correct."
    else:
        return "please try with different username,password and enmail."

print(signup("shubham","abc12345","test@gmail.com"))
