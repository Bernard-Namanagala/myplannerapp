import re
def validate_email(email):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex, email):
            return True
        else:
            return False
    
def validate_username(username):
        if len(username) < 3:
            return (False,'Username is too short')
        else:
            if len(username) > 20:
                return [False, 'Username is too long']
            else:
                regex ='^\w*$'
                if not re.search(regex, username):
                    return [False, 'Username contains invalid characters']
                else:
                    return [True,""]

def validate_password(password):
    if len(password) < 3:
        return (False,'Passoword is too short')
    else:
        if len(password) > 120:
            return [False, 'password is too long']
        else:
            regex ='^[\w@#]*$'
            if not re.search(regex, password):
                return [False, 'password contains invalid characters']
            else:
                return [True,""]

