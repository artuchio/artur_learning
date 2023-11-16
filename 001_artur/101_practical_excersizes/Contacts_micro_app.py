def add_contact(name, phone, email):
    if name not in marvel_hero_contacts:
        marvel_hero_contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Social Media": {}
        }
        print(f'Contact with {name} added successfully!')
    else:
        print(f'{name} contact already exists!')
##
##
def view_contact(name):
    if name in marvel_hero_contacts:
        contact_info = marvel_hero_contacts[name]
        print(f'Contact information for {name}:')
        print('Phone: ', contact_info['Phone'])
        print('Email: ', contact_info['Email'])
        print('Social Media:')
        for platform, handle in contact_info["Social Media"].items():
            print(f'{platform}: {handle}')
    else:
        print(f'{name} contact does not exist!')
##
##
def update_contact(name, phone, email):
    if name in marvel_hero_contacts:
        marvel_hero_contacts['Phone'] = phone
        marvel_hero_contacts['Email'] = email
        print(f'Contact information for {name} updated successfully!')
    else:
        print(f'{name} is not in contacts!')
##
##
def delete_contact(name):
    if name in marvel_hero_contacts:
        del marvel_hero_contacts[name]
        print(f'Contact for {name} deleted successfully ')
    else:
        print(f'{name} is not in contacts')

marvel_hero_contacts = {
    "Iron Man (Tony Stark)": {
        "Phone": "555-123-4567",
        "Email": "geniusbillionaire@starkindustries.com",
        "Social Media": {
            "Twitter": "@IronManOfficial",

        }
    },
    "Captain America (Steve Rogers)": {
        "Phone": "555-987-6543",
        "Email": "star-spangled.avenger@email.com",
        "Social Media": {
            "Twitter": "@CapAmerica",

        }
    },
    "Black Widow (Natasha Romanoff)": {
        "Phone": "555-555-5555",
        "Email": "natasha.spy@shield.gov",
        "Social Media": {
            "Twitter": "@BlackWidow",

        }
    },
    "Thor": {
        "Phone": "555-777-8888",
        "Email": "godofthunder@asgard.com",
        "Social Media": {
            "Twitter": "@MightyThor",

        }
    },
    "Hulk (Bruce Banner)": {
        "Phone": "555-456-7890",
        "Email": "smashinggreen@scientist.com",
        "Social Media": {
            "Twitter": "@TheIncredibleHulk",

        }
    },
    "Spider-Man (Peter Parker)": {
        "Phone": "555-234-5678",
        "Email": "webhead@spidey.net",
        "Social Media": {
            "Twitter": "@SpiderMan",

        }
    },
    "Doctor Strange (Stephen Strange)": {
        "Phone": "555-321-6549",
        "Email": "mysticdoctor@email.com",
        "Social Media": {
            "Twitter": "@DoctorStrange",

        }
    },
    "Black Panther (T'Challa)": {
        "Phone": "555-876-5432",
        "Email": "kingofwakanda@wakanda.org",
        "Social Media": {
            "Twitter": "@RealBlackPanther",

        }
    }
}
# add_contact('Roman', '555-555-5555', 'roman@example.com')
# update_contact('Mary', '555-555-5555', 'mary@example.com')
# view_contact('Captain America (Steve Rogers)')
# delete_contact('Black Widow (Natasha Romanoff)')
# # Accessing the information for a specific hero
# iron_man_info = marvel_hero_contacts["Iron Man (Tony Stark)"]
# print("Iron Man's Phone:", iron_man_info["Phone"])
# print("Iron Man's Email:", iron_man_info["Email"])
# print("Iron Man's Twitter:", iron_man_info["Social Media"]["Twitter"])