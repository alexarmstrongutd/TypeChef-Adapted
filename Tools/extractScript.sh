#!/bin/bash

#MUST PASS RESULT DIRECTORY NAME IN SCRIPT

unzip (){
	for D in $1/*; do
		
		if [ -d "${D}" ]; then
			unzip ${D} $2
		else
			if [[ ${D} = *vaa_detailreport.gz ]]; then
				echo FILE
				echo $D
				gunzip -c ${D} >$2/$(basename $D .gz)
			fi
		fi
	done
}

if [[ $# -eq 1 ]]; then
	mkdir $1
	unzip $(pwd) $1
else
	echo "YOU MUST USE 1 PARAMETER FOR THE RESULTING FILENAME"
fi
