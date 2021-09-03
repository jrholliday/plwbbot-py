# -*- coding: utf-8 -*-

###############################################################################

"""Create mock tips/stories for the Prolife Whistle Blower anonymous tip line.

https://prolifewhistleblower.com/anonymous-form/

Inspired by (ported from) SKEPDIMI/plwbbot
https://github.com/SKEPDIMI/plwbbot
"""

# Standard library imports
import json
import random
import string


###############################################################################

def typo(phrase, rate = 0.02):
    new_phrase = []
    words = phrase.split(' ')
    for word in words:
        outcome = random.random()
        if outcome <= rate and len(word) > 3:
            ix = random.choice(range(len(word)))
            new_word = ''.join([
                word[w] if w != ix else random.choice(string.ascii_lowercase)
                for w in range(len(word))
            ])
            new_phrase.append(new_word)
        else:
            new_phrase.append(word)

    new_phrase = ' '.join([w for w in new_phrase])
    if random.random() < 0.5:
        new_phrase += "."

    return new_phrase



def get_time():
    '''Return a random "3 weeks" like time frame.'''
    number = random.randint(2, 5)
    units = random.choice(["weeks", "months", "days"])
    return f"{number} {units}"


# ------------------------------------------------------------------------------------ #

# Load data arrays (for random picking)
first_names = json.load(open('data/firstNames.json'))
social_media = json.load(open('data/socialMedia.json'))
clinics = json.load(open('data/clinics.json'))
zip_codes = json.load(open('data/zip_codes.json'))

told_variants = json.load(open('data/toldVariants.json'))
photo_variants = json.load(open('data/photoVariants.json'))
state_variants = json.load(open('data/stateVariants.json'))

stories = json.load(open('answer_generator/stories.json'))
evidence = json.load(open('answer_generator/evidence.json'))


data = {
    "name"     : random.choice(first_names),
    "social"   : random.choice(social_media),
    "told"     : random.choice(told_variants),
    "photos"   : random.choice(photo_variants),
    "clinic"   : random.choice(clinics[0]) + random.choice(clinics[1]),
    "state"    : random.choice(state_variants),
    "location" : random.choice(zip_codes),
    "time"     : get_time(),
}


# ------------------------------------------------------------------------------------ #

print("Story:")
print(typo(random.choice(stories).format(**data)))
print("")

print("Evidence:")
print(typo(random.choice(evidence).format(**data)))
print("")

print("Clinic:")
print(data["clinic"])
print("")

print("City:")
print(data["location"]['city'])
print("")

print("State:")
print(data["state"])
print("")

print("Zip:")
print(data["location"]['zip'])
print("")

print("County:")
print(data["location"]['county'])
print("")

###############################################################################
