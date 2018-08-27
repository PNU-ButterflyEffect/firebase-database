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

    
    ref = db.reference('building_info')
    for row in building_info:
        #s = row[1]
        #addresses = [x.strip() for x in s.split('/')]
        #address = addresses[1]
        #r = requests.get('http://apis.vworld.kr/new2coord.do?q=' + address + '&apiKey=F5474C61-0BE5-3D90-B68C-6CE08F99A4B1&domain=http://map.vworld.kr/&output=json')
        #print(r.json)
        # EPSG_4326_X, EPSG_4326_Y
        ref.push().set({
            column_name[0] : row[0],
            column_name[1] : row[1],
            column_name[2] : row[2],
            column_name[3] : row[3],
            column_name[4] : row[4],
            column_name[5] : row[5],
            column_name[6] : row[6],
            column_name[7] : row[7],
            column_name[8] : row[8],
            column_name[9] : row[9],
            column_name[10] : row[10]

        })
    

def parsingCSV():
    import csv
    with open('data.csv', newline='') as csvfile:
        info = list(csv.reader(csvfile))
        for d in info[0]:
            column_name.append(d)
        #print(column_name)
        for row in info[1:]:
            building_info.append(row)

def main():
    parsingCSV()
    firebase_database()

main()
