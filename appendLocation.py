
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
    ref2 = db.reference()
    ref = db.reference('UserLocation/0Zby2XwOGUX6fJiYFDzE2iDQxWo2')
    #ref.delete()
    from time import gmtime, strftime
    ref.delete()
    #var myRef = database.getReference()
    #val userLocation =UserLocation(key!!, latitude, longitude)
    #myRef.child("UserLocation").child(key!!).push().setValue(userLocation)
    ref2.child("UserLocation").child("0Zby2XwOGUX6fJiYFDzE2iDQxWo2").push().update({
        "createdTime" : str(strftime("%Y-%m-%d %H:%M:%S", gmtime())),
        "key" : "0Zby2XwOGUX6fJiYFDzE2iDQxWo2",
        "latitude" : 35.235648659,
        "logitude" : 129.085798161
    })
    #ref.push().set({
    #    "createdTime" : str(strftime("%Y-%m-%d %H:%M:%S", gmtime())),
    #    "key" : "0Zby2XwOGUX6fJiYFDzE2iDQxWo2",
    #    "latitude" : 35.14213567,
    #    "logitude" : 129.0513298
    #})
    

def main():
    firebase_database()

main()
