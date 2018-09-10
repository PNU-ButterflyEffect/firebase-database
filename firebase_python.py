column_name = []
building_info = []

def firebase_database():
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    import requests
    cred = credentials.Certificate("anjeonmingug-f7d32-firebase-adminsdk-wciai-f17b75f446.json")
    #firebase_admin.initialize_app(cred)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://anjeonmingug-f7d32.firebaseio.com/'
    })

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    #ref = db.reference('restricted_access/secret_document')
    #print(ref.get())
    ref = db.reference('building_reviews')
    #ref.delete()
    for row in building_info:
        s = row[1]
        addresses = [x.strip() for x in s.split('/')]
        
        if(len(addresses) > 1):
            new_post_ref= ref.push()
            print(new_post_ref)
            review_contents = {"count":0,}
            print(addresses[1])
            ref.child(addresses[1]).set(review_contents)


def parsingCSV():
    import csv
    with open('data.csv', newline='') as csvfile:
        info = list(csv.reader(csvfile))
        for d in info[0]:
            column_name.append(d)
        #print(column_name)
        for row in info[1:]:
            building_info.append(row)

def querySample():
    # Retrieve the five tallest dinosaurs in the database sorted by height.
    # 'result' will be a sorted data structure (list or OrderedDict).
    result = dinos.order_by_child('height').limit_to_last(5).get()

    # Retrieve the 5 shortest dinosaurs that are taller than 2m.
    result = dinos.order_by_child('height').start_at(2).limit_to_first(5).get()

    # Retrieve the score entries whose values are between 50 and 60.
    result = db.reference('scores').order_by_value() \
    .start_at(50).end_at(60).get()

def main():
    parsingCSV()
    firebase_database()

main()
