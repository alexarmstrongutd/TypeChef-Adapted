import json
import subprocess
import sys
def test_output():    
    with open('test.txt') as json_file:
        try:
            json_object = json.loads(json_file)
        except ValueError as e:
            assert 0
        pass

def test_main():
    #result = subprocess.check_call(["find","-name" , "*vaa_detailreport", "|", "parallel", "--xargs", "python", "../src/parser.py", "test"])
		resultList = subprocess.check_output("find -name '*vaa_detailreport'",shell=True).decode().strip().split('\n')
		fileNames = ""
		for x in resultList:
			fileNames += x + " "
		fileNames = fileNames.strip()
		subprocess.check_call("python parser.py test " +fileNames,shell=True,stdout=sys.stdout)

test_main()				
