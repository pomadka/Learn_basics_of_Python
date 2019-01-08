def list_benefint():
    listOfStrgs = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return listOfStrgs

var = list_benefint()
print var

def sentence(info):
    return "%s is a benefit of functions!" %info
print sentence("Bla")

def name_the_benefits_of_functions():
    list_of_benefits = list_benefint()

    for gaf in list_of_benefits:    # gaf it's - listOfStrgs
        print(sentence(gaf ))

name_the_benefits_of_functions()