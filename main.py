import email_preferences


# Paths We Use
path_email = 'email_template/content.txt'


# Open Email Payload
email_payload = open(path_email, 'r').read()

print(email_payload)