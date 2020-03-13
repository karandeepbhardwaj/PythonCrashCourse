def get_formatted_name(city, country, population=''):
    if population:
        return city.title()+", "+ country.title()+ " - population "+ str(population)
    else:
        return city.title()+", "+ country.title()