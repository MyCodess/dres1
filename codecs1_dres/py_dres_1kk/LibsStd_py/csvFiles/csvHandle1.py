import csv

# =========== nts:
# ALWAYS use  newline='' by openning the csv file! see footnote PyRefDocs/library/csv.html :
# It should always be safe to specify newline='', since the csv module does its own (universal) newline handling.
# The newline parameter is set to the empty string so that the open function doesn’t perform any conversion of the character \n
# see also https://wellsr.com/python/introduction-to-csv-dialects-with-the-python-csv-module/

# ###########################################################################
def readCsvFile(filepath1: str):
    print(f"\n==================== reading csv-file {filepath1} : ===============================")
    with open(filepath1, 'rt', newline='', encoding='utf-8') as f1:
        reader1 =  csv.reader(f1, delimiter=';',  lineterminator='\n', strict=True)
        try:
            for entry1 in reader1:  print(reader1.line_num, " : ", entry1)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# ###########################################################################
def readCsvStr(csvlist1: list[str]):
    print("\n==================== reading directly csv-strings in an array: ====================")
    for row in csv.reader(csvlist1):
        print(row)


# ###########################################################################
# -- since no DictReader.fieldnames passed/defined, then the first line of csv-file is header/fieldnames!
# -- DictReader.fieldnames If not passed as a parameter when creating the object, this attribute is initialized upon first access or when the first record is read from the file
def readCsvToDict(filepath1: str):
    print(f"\n==================== reading csv-file {filepath1} into an OrderedDict: ============")
    with open(filepath1, 'rt', newline='', encoding='utf-8') as f1:
        try:
            # - no-explicit-filed-names here! so csv-file-first-line is the header/fieldnames:
            for entry1 in csv.DictReader(f1, delimiter=';',  lineterminator='\n', strict=True): print(entry1)
            # - explicit-filed-names here:
            # - for entry1 in csv.DictReader(f1, delimiter=';',  lineterminator='\n', strict=True, fieldnames=["col1", "col2", "col3"]): print(entry1)
                # - only certain fileds handling:  print(entry1["name"], " : ", entry1["ipv4address"])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# ###########################################################################
def main(*args, **kwargs):
    readCsvFile('./f1.csv')
    readCsvStr(['one,two,three', 'a,b,c', '11,12,13'])
    readCsvToDict('./f1.csv')


if __name__ == '__main__':
    main()

