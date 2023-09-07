import pyrebase


config={
  'apiKey': "AIzaSyDPJsywvUXWTosCTFRkftTXTr36SJS5wtY",
  'authDomain': "python-8ecab.firebaseapp.com",
  'databaseURL': "https://python-8ecab-default-rtdb.firebaseio.com",
  'projectId': "python-8ecab",
  'storageBucket': "python-8ecab.appspot.com",
  'messagingSenderId': "562078592422",
  'appId': "1:562078592422:web:1e52ce41c9f1ce71eef367"
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()
newUser = None
def login():
    print('login:')
    email = input('Email: ')
    password = input('Password: ')
    try:
        user = auth.sign_in_with_email_and_password(email,password)
        if user:
            print('success')
            newUser = user
            return user
        else:
            print('login fail')
    except Exception as e:
        error_message = str(e)
        if 'EMAIL_NOT_FOUND' in error_message:
            print('Email not found')
        elif 'INVALID_EMAIL' in error_message:
            print('Email in invalid format')
        elif 'INVALID_PASSWORD' in error_message:
            print('Email or password invalid')
        else:
            print('Signup failed:', error_message)
        return None
    

def signup():
    print('singUp')
    email = input('Email: ')
    password = input('Password: ')
    try:
        user = auth.create_user_with_email_and_password(email,password)    
        print('Successfully')
        return user
    except Exception as e:
        error_message = str(e)
        if 'EMAIL_EXISTS' in error_message:
            print('Email already exists. Please choose a different email.')
        elif 'INVALID_EMAIL' in error_message:
            print('Invalid email format. Please enter a valid email address.')
        else:
            print('Signup failed:', error_message)
        return None
    
#signup()
#redefine password
def redefinePass():
    email = input('Email to redefine: ')
    try:
        redefine = auth.send_password_reset_email(email)
        return redefine
    except Exception as e:
        print('Failed. Something happened.')