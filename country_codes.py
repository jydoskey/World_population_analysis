from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    
        
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        else:
            if country_name == 'Bolivia':
                return 'bo'
            elif country_name == 'Congo, Dem. Rep.':
                return 'cd'
            elif country_name == 'Congo, Rep.':
                return 'cg'
            elif country_name == 'Egypt, Arab Rep.':
                return 'eg'
            elif country_name == 'Gambia, The':
                return 'gm'
            elif country_name == 'Hong Kong SAR, China':
                return 'hk'
            elif country_name == 'Iran, Islamic Rep.':
                return 'ir'
            elif country_name == 'Korea, Dem. Rep.':
                return 'kp'
            elif country_name == 'Korea, Rep.':
                return 'kr'
            elif country_name == 'Venezuela, RB':
                return 've'
            elif country_name == 'Vietnam':
                return 'vn'
            elif country_name == 'Yemen, Rep.':
                return 'ye'
            
    #If the contry wasn't found, return None.
    return None
            
print(get_country_code('Yemen, Rep.'))
        
#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))
#print(get_country_code('Afghanistan'))