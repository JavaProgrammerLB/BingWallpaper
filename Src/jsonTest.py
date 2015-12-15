import json

obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print(repr(obj))
print(encodedjson)


decodejson = json.loads(encodedjson)
print(type(decodejson))
print(decodejson[4]['key1'])
print(decodejson)
