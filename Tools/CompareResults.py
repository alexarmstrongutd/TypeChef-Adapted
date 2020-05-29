
import sys
import json

def createSet(jsonDictList):

    result = set()
    mapping = dict()
    for x in jsonDictList:
        result.add((x['filename'].split('/')[-1],int(x['line'] if x['line'] != "" else 0)))

        mapping[(x['filename'].split('/')[-1],int(x['line'] if x['line'] != "" else 0))] = x
    return result,mapping

def main():
    featuresSet1 = None
    featuresSet2 = None
    mapping1 = None
    mapping2 = None
    with open(sys.argv[1],'r') as fileDict:
        featuresArray = json.load(fileDict)
        if len(featuresArray) > 1 and featuresArray[0]["tool"] != "Typechef-VAA":
            print("PLEASE USE TYPECHEF AS THE FIRST ARGUEMENT")
        featuresSet1,mapping1 = createSet(featuresArray)
    with open(sys.argv[2], 'r') as fileDict:
        featuresArray = json.load(fileDict)
        featuresSet2,mapping2 = createSet(featuresArray)
    diff1 = featuresSet1 - featuresSet2
    diff2 = featuresSet2 - featuresSet1
    same = list(featuresSet1.intersection(featuresSet2))
    diff1 = list(diff1)
    diff2 = list(diff2)
    print("The first tool {} had {} warnings not in {}".format(sys.argv[1],len(diff1),sys.argv[2]))
    print("The second tool {} had {} warnings not in {}".format(sys.argv[2],len(diff2),sys.argv[1]))
    print("The first tool {} and second tool {} had {} common warnings".format(sys.argv[1],sys.argv[2],len(same)))
    print()
    with open(sys.argv[3],"w+") as csvfile:
        csvfile.write("Filename, Line #, TypeChef-Type, {}-Type\n".format(sys.argv[2]))
        for x in same:
            csvfile.write("{}, {}, {}, {}\n".format(x[0],x[1],mapping1[x]["type"],mapping2[x]["type"]))



main()