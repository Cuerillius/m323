from dataclasses import dataclass

# Aufgabe 1
@dataclass
class Mitarbeiter:
    name: str
    abteilung: str
    gehalt: int

mitarbeiter: list[Mitarbeiter] = [
    Mitarbeiter("Max Mustermann", "IT", 50000),
    Mitarbeiter("Erika Musterfrau", "Marketing", 45000),
    Mitarbeiter("Klaus Klein", "IT", 55000),
    Mitarbeiter("Julia Gross", "HR", 40000),
]

def list_it_people(lst: list[Mitarbeiter]):
    filteredPeople = list(filter(lambda x: x.gehalt >= 50000 and x.abteilung == "IT", lst))
    return list(map(lambda x: x.name.split(" ")[0].upper(),filteredPeople))

print(list_it_people(mitarbeiter))


# Aufgabe 2

kurse: list = [
  "Programmierung in Scala",
  "Datenbanken",
  "Webentwicklung mit JavaScript",
  "Algorithmen und Datenstrukturen"
]


def filter_and_format(lst: list, reversed: bool = False):
    return sorted((x.replace(" ", "") for x in lst if "Daten" in x), reverse=reversed)
    
print(filter_and_format(kurse))