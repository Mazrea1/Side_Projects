import pandas


data = [
    ["Bart", "Lisa", "Homer", "Marge"],
    ["10", "8", "39", "36"],
    ["939-555-0113", "939-555-0114", "939-555-0115", "939-555-0116"],
    ["Taurus", "Virgo", "Taurus", "Pisces"]
]

pd = pandas.DataFrame(data, columns= ["name", "age", "phone_number", "astrological_sign"])

print(pd)