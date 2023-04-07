import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"add your firebase url here"
})

ref = db.reference('Students')
data = {
    "152183":
        {
            "name": "Wassim",
            "field": "Cyber Security",
            "group": "SSIR-C",
            "year": 2,
            "total_attandance": 7,
            "last_attendance": "2022-12-11 14:51:00"
        },
"349701":
        {
            "name": "Othmen",
            "field": "software enginer",
            "group": "GLS-B",
            "year": 2,
            "total_attandance": 1,
            "last_attendance": "2023-01-27 11:25:00"
        }
}


for key, value in data.items():
    ref.child(key).set(value)
