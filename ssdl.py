import os
import linecache
import webbrowser
from pathlib import Path

path = str(Path.home())
ssdlp = path + "\\pyscoresaberapplication.json"


hash = input("Paste the map hash from scoresaber: ")
#get map id after reading hash, save map info to a temp file
result = os.popen("curl https://api.beatsaver.com/maps/hash/" + hash).read()
string = result
with open (ssdlp, "w") as request:
    request.write(result)
x = linecache.getline(ssdlp, 2)
part = (x.replace('"id": "', ''))
id = (part.replace('",', ''))
idstrp = id.strip()
print ("Found map id:",idstrp, "- Attempting oneclick install from beatsavior")
#Once we got the id we attempt beatsavior oneclick install
name = linecache.getline(ssdlp, 3)
partname = (name.replace('"name": "', ''))
partid = (partname.replace('",', ''))
namestrip = partid.strip()
print("Started downloading map", namestrip, ", check progress from ModAssistant window")
webbrowser.open("beatsaver://" + idstrp, new=0, autoraise=False)
#Delete local file, ready for next use
os.remove(ssdlp)