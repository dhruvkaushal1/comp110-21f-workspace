schools: dict[str, int]


schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

#print dictionary
print(schools)
#print part of dictionary
print(schools["Duke"])
#using f string for printing
print(f"UNC has {schools['UNC']} students")
#remove key value
schools.pop("Duke")

#test for existence

is_duke_present: bool = "Duke" in schools

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

