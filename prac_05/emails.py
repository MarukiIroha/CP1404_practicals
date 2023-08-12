"""
Emails
Estimate: 50 minutes
Actual:   41 minutes
"""
name = {}
email = input("Email: ")
while email != '':
    user_name = email.split('@')[0].split('.')
    choice = input(f"Is your name {' '.join(user_name).title()}? (Y/n)").upper()
    if choice != 'Y' and choice != '':
        user_name = input("Name: ")
        name[user_name] = email
    else:
        name[' '.join(user_name).title()] = email
    email = input("Email: ")
for email, name in name.items():
        print(f"{email} ({name})")