# kuukaudet.py

# Open the file kuukaudet.txt and read the months into a list
with open("kuukaudet.txt", "r", encoding="utf-8") as file:
    months = file.read().splitlines()

# Define messages for the months
messages = {
    "Tammikuu": "Aloitetaan uusi vuosi!",
    "Helmikuu": "Vielä vähän talvea jäljellä.",
    "Maaliskuu": "Kevät tekee tuloaan!",
    "Huhtikuu": "Kevät on täällä!",
    "Toukokuu": "Nautitaan lämpimistä päivistä.",
    "Kesäkuu": "Kesä on vihdoin täällä!",
    "Heinäkuu": "Kesä on parhaimmillaan!",
    "Elokuu": "Kesä alkaa kääntyä syksyyn.",
    "Syyskuu": "Syksy saapuu.",
    "Lokakuu": "Syksyn väriloisto on kauneimmillaan.",
    "Marraskuu": "Valmistaudutaan talveen.",
    "Joulukuu": "Joulun aika on täällä!"
}

# Print messages for each month
for month in months:
    if month in messages:
        print(f"{month}: {messages[month]}")
    else:
        # This should not happen if all months are covered
        print(f"{month}: Viestiä ei löydy.")