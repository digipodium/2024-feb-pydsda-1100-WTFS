contacts = {
    'police': 112,
    'emergency':101,
}

while True:
    name = input('🔍Search any contact:')
    # closing the program
    if len(name) == 0:
        print("👋 Bye")
        break
    # searching the contact
    if name in contacts:
        print(f"📞 {name} : {contacts[name]}")
    elif name == 'all':
        for name, number in contacts.items():
            print(f"📞 {name} : {number}")
        print('-'*20)
    else:
        print(f"🚫 {name} not found")
        ch = input(f'🤔 Add {name} to contacts? (y/n): ')
        if ch == 'y':
            number = input(f'📞 Enter {name} number: ')
            contacts[name] = number
            print(f"✅ {name} added to contacts")
            print('-'*20)