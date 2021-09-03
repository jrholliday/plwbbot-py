# About
This is a python port of the PLWBBOT nodejs project located at
https://github.com/SKEPDIMI/plwbbot

From that project's readme:
> This is a script that will create bogus tips to prolifewhistleblower.com, 
> a Texan anonymous tip line for reporting abortions. Hopefully these fake 
> tips help make the system useless.


# Installation
None.  This script (currently) uses only Python standard library imports.


# Running the script
Right now, the website appears to either be firewalled or down for many. The 
following command will give you a bogus store in text format, which you can 
copy/paste onto the website yourself.
```sh
python3 plwbbot.py
```


# Inspiration
From the official prolifewhistleblower.com web page:
> The Texas Heartbeat Act is unique because it calls upon private citizens 
> to hold abortion providers and their enablers accountable. Any person can 
> sue any abortion provider who kills an unborn child after six weeks of 
> gestation—and any person can sue anyone who aids or abets these illegal 
> abortions. All of these individuals must pay damages to the person who 
> sued them of at least $10,000 for each illegal abortion that they perform 
> or assist.
> 
> Texas Right to Life will ensure that these lawbreakers are held 
> accountable for their actions. Use the links below to report anyone who is 
> violating the Texas Heartbeat Act by aiding or abetting a post-heartbeat 
> abortion. And report any person or entity that aids or abets (or that 
> intends to aid or abet) an illegal abortion in Texas.

Fuck these assholes.


# Modifying the dataset
Modifying the dataset is crucial. It is technically very easy for the 
website maintainers to find the template answers published here and clean it 
from their database.  Therefore it's recommended that upon cloning this repo 
for usage, you replace the existing template answers with your own answers. 
All data is generated and pulled from json files and is easily modifiable.
Data in ./data/*.json is probably okay as-is (for now).  Data in
./answer_generator/*.json should be modified and added to as much as possible.
Just follow the style you see.


# Contributing
Feel free to contribute by adding more fake answers and improving the 
execution of the script.
