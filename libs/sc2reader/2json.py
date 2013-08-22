import sc2reader
from sc2reader.scripts.sc2json import toJSON
configuredToJSON = toJSON(indent=2)
replay = sc2reader.load_replay('1.sc2replay')
print configuredToJSON(replay)