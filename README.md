# TypeChef-Installation-Documentation


**This documentation is written for Ubuntu/Debian based environments**

**Important Note: Please make sure all the installed folders share the same parent directory**

## TypeChef-VAA Installation


1. Run ```sudo apt-get update``` to update your system
2. Run ```sudo apt-get upgrade``` to download and install the updates
3. Run ```sudo apt-get install git``` to install git if not installed already
4. Run ```git clone https://github.com/aJanker/TypeChef-VAA``` to download the TypeChef-VAA program
5. Run ```sudo apt-get install openjdk-8-jdk``` to install Java 8
6. Create a new directory in the current working directory called sbt-launch-files
7. Copy the file sbt-launch.jar from TypeChef-VAA to this new directory
8. Switch to the sbt-launch-files directory and run jar xvf sbt-launch.jar to extract the jar
9. Now that the jar is extracted we can remove the jar in the sbt-launch-files directory
10. Modify sbt/sbt.boot.properties, sbt.boot.properties0.7, sbt.boot.properties0.10.0, sbt.boot.properties0.10.1, sbt.boot.properties0.11.0, sbt.boot.properties0.11.1, sbt.boot.properties0.11.2, sbt.boot.properties0.11.3 (files from the sbt-launch.jar archive) to change the line maven-central to maven-central: https://repo1.maven.org/maven2/ i.e. modify the line that says ```maven-central``` to ```maven-central: https://repo1.maven.org/maven2/``` in each of these files
11. Create a new sbt-launch.jar file using ```jar cvmf META-INF/MANIFEST.MF sbt-launch.jar *```
12. Run ```mv sbt-launch.jar ../TypeChef-VAA/sbt-launch.jar``` to modify the original jar file
13. Run ```sudo update-alternatives --config java``` and switch to Java 8 on your machine
14. Modify line 302 of Frontend/src/main/scala/de/fosd/typechef/Frontend.scala within TypeChef-VAA to correct the syntax error warnDegree - fDefDegree to (warnDegree - fDefDegree)
15. Run ```./publish.sh``` to install TypeChef-VAA


**For all the programs with Typechef be sure to clone the GNUCHeader repo**

```git clone https://github.com/aJanker/TypeChef-GNUCHeader.git```

## Busybox-VAA Installation
1. Run ```git clone https://github.com/aJanker/TypeChef-Sampling-Busybox.git``` for the TypeChef Busybox
2. Be sure to clone the GNUCHeader repo
3. Run ```git clone https://github.com/ckaestne/TypeChef-BusyboxAnalysis/tree/dd858c16eb59091d89f9f48c5c54073708553aac``` for the repo to create the files needed for the analysis
4. Run ```git reset --hard dd858c16eb59091d89f9f48c5c54073708553aac``` to change to the working commit
5. Go to the casestudy/systems/redhat/usr/include directory in the TypeChef-SamplingBusybox repo and run ```cp -r * ~/TypeChef-Work/TypeChef-GNUCHeader/usr_include/ ``` replace TypeChef-Work with your directory name
6. Now from the redhat directory go to lib/gcc/x86_64-redhat-linux/4.4.4/include and run ```cp -r * ~/TypeChef-Work/TypeChef-GNUCHeader/x86_64-linux-gnu/4.8/``` replace TypeChef-Work with your directory name (at this point you can delete the sampling repo directory)
7. Go to the Busybox analysis directory (not the sampling one)
8. Run ```wget https://github.com/paulgazz/kconfig_case_studies/raw/v1.0/cases/busybox_1_28_0/busybox-1.28.0.tar.bz2```
9. Run ```tar -xvf busybox-1.28.0.tar.bz2``` and remove the tar.bz2 file afterwards
10. Rename busybox-1.28.0 to gitbusybox
11. Go back to the parent folder holding all the program folders and run ```wget https://piccolo.link/sbt-1.3.4.zip```
12. Run ```unzip sbt-1.3.4.zip``` and remove the zip afterwards
13. Run ``` wget https://archive.apache.org/dist/maven/maven-3/3.1.1/binaries/apache-maven-3.1.1-bin.tar.gz``` to download maven
14. Run ```tar -xvf apache-maven-3.1.1-bin.tar.gz``` and remove the tarball afterwards
15. Go to the lib folder within apache-maven and run ```jar xf maven-model-builder-3.1.1.jar org/apache/maven/model/pom-4.0.0.xml```
16. Go to org/apache/maven/model/pom-4.0.0.xml within the lib folder and replace all instances of http with https
17. Within the lib folder run ```jar uf maven-model-builder-3.1.1.jar org/apache/maven/model/pom-4.0.0.xml```
18. Add both apache-maven-3.1.1/bin and sbt/bin to your PATH (be sure to restart shell or source .profile)
19. Go to the Busybox analysis (not sampling one) remove the KBuildMiner directory and run ```git clone https://github.com/ckaestne/KBuildMiner```
20. Go the KBuildMiner directory now and run ```mvn compile``` you will probably get a build error so we need to fix this
21. Download JDK 7 and extract it whereever in my case I used the same directory as all the other files
22. Add the JDK 7 bin folder to your PATH
23. Rerun mvn compile in KBuildMiner and you will get a download error remove Java 7 from the path and use Jva 8 again to work
24. Run ```mvn dependency:build-classpath -Dmdep.outputFile=.classpath-scala```
25. Replace the content of prepareGit.sh with the content in this pastebin https://pastebin.com/yGu4euA2
26. Run ```sbt mkrun``` and ```./prepareGit.sh``` in the Busybox analysis folder
27. Create a new folder called Busybox-VAA in the main working directory
28. Go to that directory and run ```wget https://github.com/paulgazz/kconfig_case_studies/raw/v1.0/cases/busybox_1_28_0/busybox-1.28.0.tar.bz2``` and extract the tar file
29. Move the filelist, header.h,and featureModel.dimacs file from the gitbusybox folder and mheader.h in the analysis over to our new VAA directory
30. Take the contents of features file in the gitbusybox folder and append it to the openfeatures.txt file in the GNUCHeader file
31. Now create a file called runVAA.sh and copy the contents from this pastebin into the script https://pastebin.com/tDbvu2xW
32. Delete the last line and uncomment out the second to last line regarding to invoking typechef.sh
33. Run ```chmod +x runVAA.sh``` and run the script
34. The script should now work instructions on how to extract results are later

## Axtls-VAA header setup
**Note you can skip this step if you opted for the repo header build**
**When you need to modify
1. Run ```sudo apt-get install libfcgi-dev```
2. Run ```sudo apt-get install libzzip-dev```
3. Run ```sudo apt-get install libsqlite-dev```
4. Run ```sudo apt-get install libmysqlclient-dev```
5. Run ```sudo apt-get install libpq-dev```
6. Run ```sudo apt-get install alien```
7. Download .rpm packages http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html
   1. oracle-instantclinet*-basic-*.rpm
   2. oracle-instantclinet*-devel-*.rpm
   3. oracle-instantclinet*-sqlplus-*.rpm
8. Run ```sudo alien -i oracle-instantclinet*-basic-*.rpm```
9. Run ```sudo alien -i oracle-instantclinet*-devel-*.rpm```
10. Run ```sudo alien -i oracle-instantclinet*-sqlplus-*.rpm```
11. Download apr-util, apr, and httpd using a web browser or wget and move them to a location that you will include in the runVAA script and run configure on each of them in that order (this may take some time)
12. Download perl using a web browser or wget and run configure

**Follow the below steps when you have the runVAA.sh file available in the steps**
1. Modify the runVAA.sh script with the -I flags to point to the header files of apr-util, apr, httpd, and perl
2. Modify runVAA.sh to point to your version of oracle/<version number>/client in the usr/include directory
3. Point the -I flags towards your /usr/include folder so TypeChef can recognize the header files



## Axtls-VAA installation
**You may get your own headers although I highly would not recommend it or you may clone the required headers to run the analysis from the github repo**

1. Run ```wget https://github.com/paulgazz/kconfig_case_studies/raw/v1.0/cases/axtls_2_1_4/axTLS-2.1.4.tar.gz``` in your main parent directory to download axTLS
2. Run ```tar -xvf axTLS-2.1.4.tar.gz``` to extract the file and remove the tarball when finished
3. Either do the above steps or run ```git clone https://github.com/alexarmstrongutd/Axtls-Headers.git```
4. If you cloned the repo move the contents over into the GNUCHeader folder
5. Go to the directory axtls-code and run ```make allyesconfig```
6. Run ```sudo apt install liblua5.3-dev``` to install lua headers needed for make
7. Run ```make``` there will be some problems due to missing C# files but ignore them
8. Clone this repo in the main parent directory
9. Copy HeaderCreator.py from the tools directory over into axtls-code directory
10. Run ```python3 HeaderCreator.py``` to create openfeatures.txt and header.h
11. Append the contents of openfeatures.txt into the openfeatures file in the GNUCHeaders Directory
12. Run ```wget https://github.com/paulgazz/kconfig_case_studies/raw/master/cases/axtls_2_1_4/kconfig.dimacs``` for the dimacs file
13. Run ```git clone https://github.com/alexarmstrongutd/Axtls-Scripts.git``` on the main parent directory
14. Move all the files in the scripts directory into axtls-code
15. For the all files use runVAA.sh for the minimal setup use runVAA2.sh
16. Run ```mv kconfig.dimacs featureModel.dimacs``` and ```mv header.h config.h```
17. If you did not opt to use the Header repo please refer to steps above referring to how to modify runVAA.sh accordingly
18. Run ```./runVAA.sh``` or ```./runVAA2.sh``` depending on your choice


## Notes Regarding Toybox
While the header.h file can be created by modifying the source code in the Busybox analysis folder the program does not use C preprocessor ifs and instead uses the base if statements using macros defined using config options which cannot be understood by TypeChef. Future work requires there be explicit #if options in the source files.

To generate the header.h file specifically modify the src/main/scala/de/fosd/typechef/busybox/KconfigReader.scala file in the busybox analysis directory and change the value of outheader at around line 73 to this
``` 
           outHeader += "#ifdef CONFIG_" + flag + "\n" +
                "   #define CFG_" + flag + " 1\n" +
                "   #define " + "USE" + "_" + flag + "(...) __VA_ARGS__\n" +
                "#else\n" +
                "   #define CFG_" + flag + " 0\n" +
                "   #define " + "USE" + "_" + flag + "(...)\n" +
                "#endif\n\n"
```

Make sure toybox is in the gitbusybox directory
Then rerun sbt mkrun and run ./prepreGit.sh it should not work since KBuildMiner should fail but the parser runs and still generates the header.h file we are looking for. Then simply copy over the resulting header.h file and move it into the generated folder and rename it to config.h to extract the filelist use the findCFiles.py tool and redirect the output to generate the filelist. This also generated a file called headerLocations.txt run extractLocations.py program to generate the list of header locations to use with runVAA.sh. To have runVAA.sh just use the busybox one and modify the locations of the -I flags accordingly to the results of the headerSet.txt file also be sure to include the diamacs file for toybox. After doing all that you should be able to run the partial analysis successfully.


## How to extract the results
1. Copy the cleanVAA.sh, extractScript.sh, ResultStats.py and both parser.py files from the Tools directory in this repo into the directory with runVAA.sh
2. Run ```./cleanVAA.sh``` to clear any results first before testing
3. Run the appropriate runVAA.sh file on your program
4. Run ```extractScript.sh <Directory Name>``` Directory name should be a non existant directory
5. Run ```python3 test_parser.py ><Output File>``` to get the Json results
6. Run ```python3 ResultStats.py <OutputFile from test_parser.py>``` to get the Stat results










