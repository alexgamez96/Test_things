import json
with open('destinations.json', 'r') as file:
    data= dict(json.load(file))
#Esto es para que lo imprima bonito
#print(type(data['transcoderConfigurations']['fileTranscoder']))
#data=dict(data)
#    print(type(i['sourceParameters']))
#    for x in {i['sourceParameters']}:
#        print(f"{x['fileExtension']}")
#print(json.dumps(data['transcoderConfigurations']['fileTranscoder'],indent=4, sort_keys=True))
print(" ")
#print(json.dumps(data['transcoderConfigurations'],indent=4, sort_keys=True)) 

# test para ver si se puede añadir y comitear junto
print(data[0])
#print(data[0]["outputs"][0]["id"])