phonebook = {
    "Roma" : 89042222222,
    "Mum" : 89053333333,
    "Ann" : 89035555555
}
del phonebook["Ann"]
phonebook ["Mum"] = 89041073895

if "Mum" in phonebook:
    print "Good"
if "Ann" not in phonebook:
    print "Where is she??"
