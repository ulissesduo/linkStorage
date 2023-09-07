import webbrowser

while True:
    user_input = input("Type 'open browser' to open a web browser (or 'exit' to quit): ")
    
    if user_input.lower() == 'open browser':
        # Open the default web browser
        webbrowser.open('https://console.firebase.google.com/')  # You can change the URL to the desired webpage
    elif user_input.lower() == 'exit':
        break
    else:
        print("Invalid command. Please type 'open browser' to open a web browser or 'exit' to quit.")
