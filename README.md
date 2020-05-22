# TypeChef-Installation-Documentation


**This documentation is written for Ubuntu/Debian based environments**

**Important Note: Please make sure all the installed folders share the same parent directory**

## TypeChef-VAA Installation

<!-- Note sudo apt install openjdk-7-jdk needs to be done for Busybox -->

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










