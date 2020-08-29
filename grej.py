US_VOLUME_UNITS = { # minim approx 61.6115 ml
    'min': (61.6115,'ml','SI_VOL'),
    'fl dr': (60,'min','US_VOL'),
    'tsp': (80,'min','US_VOL'),
    'Tbsp': (3,'tsp','US_VOL'),
    'fl oz': (2,'Tbsp','US_VOL'),
    'jig': (3,'Tbsp','US_VOL'), # us shot
    'gi': (4,'fl oz','US_VOL'), # us gill
    'cup': (2,'gi','US_VOL'), # us cup
    'pt': (2,'cup','US_VOL'), # us pint
    'qt': (2,'pt','US_VOL'), # us quart
    'pot': (2,'qt','US_VOL'), # us pottle
    'gal': (4,'qt','US_VOL'), # us gallon
    'bbl': (31.5, 'gal','US_VOL'), # us barrel
    'hogshead': (63,'gal','US_VOL')
}
#    'imp gal': 4546, # imperial

SI_VOLUME_UNITS = { # in multiples of ml
    'ml': None , # som bas
    'krm': (1,'ml','SI_VOL'),
    'tsk': (5,'ml','SI_VOL'),
    'cl':  (10,'ml','SI_VOL'),
    'msk': (15,'ml','SI_VOL'),
    'dl':  (100,'ml','SI_VOL'),
    'l':   (1000,'ml','SI_VOL'),
    'L':   (1,'l','SI_VOL'),
    'ltr': (1,'l','SI_VOL'),
    'hl':  (100,'l','SI_VOL')
     }
SI_WEIGHT_UNITS = { # in multiples of ml
    'mg': None,
    'g': (1e3, 'mg', 'SI_WT'),
    'hg': (1e5, 'mg', 'SI_WT'),
    'kg': (1e6, 'mg', 'SI_WT'),
    'ton': (1e3, 'kg', 'SI_WT')
}
UNIT_SYSTEMS = {
    'SI_VOL': SI_VOLUME_UNITS,
    'SI_WGT': SI_WEIGHT_UNITS,
    'US_VOL': US_VOLUME_UNITS
}
def normalize(quantity):
    try:
        print(quantity)
        system = quantity[2]
        unit = quantity[1]
        measure = quantity[0]
        conv = UNIT_SYSTEMS[system][unit]
        print('converting: 1 {} = {}'.format(unit, conv))
        if conv:
            newquant =(measure*conv[0],conv[1],conv[2])
            return normalize(newquant)
        else:
            return quantity 
    except:
        print('Exception')
        return quantity



def main():
    myquant = (5,'gal','US_VOL')
    print(normalize(myquant))


class Recept:
    def __init__(self):
        pass



if __name__ == "__main__":
    # execute only if run as a script
    main()