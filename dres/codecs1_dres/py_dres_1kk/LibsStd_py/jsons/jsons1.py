"""
    PyRefDocs/html/library/json.html
"""

import json
import pprint

def jsons_encodings1():
    print("\n========== encoding:  py-obj --> json-str with dumpS() : ==================")
    print("-- Serialize obj to a JSON formatted str using the conversion table. see pydoc jsons.dump[s] -------")
    print("-- dumpS(obj) --> string   <--->    dump(obj) --> stream/file  ---------")
    print("\n---------- Basic Encoding ----------------------------------------")
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
    print(json.dumps("\"foo\bar"))
    print(json.dumps('\u1234'))
    print(json.dumps('\\'))
    print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

    print("\n---------- Compact encoding : ------------------------------------")
    print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True, separators=(',', ':')))
    print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

    print("\n---------- Pretty Encoding ---------------------------------------")
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], indent=4))
    print(json.dumps("\"foo\bar", indent=4))
    print(json.dumps('\u1234', indent=4))
    print(json.dumps('\\', indent=4))
    print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True, indent=4))
    print("\n-- return-type-of-dumps:  ", type(json.dumps({"c": 0, "b": 0, "a": 0})))


def jsons_decodings1():
    print("\n============== read json-str ---> py-data /decode with loads : =============")
    print("-- loads(json-str/bytes) --> py-obj/dict   <--->    load(json-stream) --> py-obj/dict  ---------")
    print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
    for ii in json.loads('["foo", {"bar":["baz", null, 1.0, 2]}, {"aa": 21}, {"bb": 22}]'):
        print(ii)
    print("\n-- return-type-of-loads:  ", type(json.loads('{"c": 0, "b": 0, "a": 0}')))

def jsons_decode_file1():
    print("============== read json-file ---> py-data /decode with loads : =============")
    with open('./f1.json') as fd1:
        json_data1 = json.load(fd1)
    print(f"\n-- json_data1 :  {json_data1}")
    print("\n-- json_data1 formatted: -----")
    pprint.pp(json_data1, indent=4)

if __name__ == "__main__":
    jsons_encodings1()
    jsons_decodings1()
    #_  jsons_decode_file1()
