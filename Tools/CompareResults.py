
import sys
import json

def createSet(jsonDictList):

    result = set()
    for x in jsonDictList:
        result.add((x['filename'].split('/')[-1],x['line']))
    return result

def main():
    featuresSet1 = None
    featuresSet2 = None
    with open(sys.argv[1],'r') as fileDict:
        featuresArray = json.load(fileDict)
        featuresSet1 = createSet(featuresArray)
    with open(sys.argv[2], 'r') as fileDict:
        featuresArray = json.load(fileDict)
        featuresSet2 = createSet(featuresArray)
    diff1 = featuresSet1 - featuresSet2
    diff2 = featuresSet2 - featuresSet1
    diff1 = list(diff1)
    diff2 = list(diff2)
    print("The first tool {} had {} warnings not in {}".format(sys.argv[1],len(diff1),sys.argv[2]))
    print("The second tool {} had {} warnings not in {}".format(sys.argv[2],len(diff2),sys.argv[1]))
    print()

main()