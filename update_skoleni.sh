#!/bin/bash

set -e

SCRIPT=`realpath $0`
SCRIPT_PATH=`dirname $SCRIPT`

echo "buildim" `date` >> /tmp/build.log
workshops=("grass-gis-zacatecnik" "postgis-zacatecnik" "postgis-pokrocily"
           "otevrena-geodata" "open-source-gis" "grass-gis-pokrocily" "qgis-zacatecnik" "qgis-pokrocily"
           "geopython-zacatecnik" "geopython-pokrocily" "isprs-summer-school-2016")

function update_git {
	cd ${SCRIPT_PATH}/..
        echo '-----------------------------------------------------------'
	echo updating $1
        echo '-----------------------------------------------------------'
	cd $1
	git pull # --rebase
};

function update_html {
	cd ${SCRIPT_PATH}/..
        echo '-----------------------------------------------------------'
	echo generating HTML for $1
        echo '-----------------------------------------------------------'
	cd $1
	make clean
        make html
}

function update_pdf {
    cd ${SCRIPT_PATH}/..
    echo '-----------------------------------------------------------'
    echo generating PDF for $1
    echo '-----------------------------------------------------------'
    cd $1
    make latexpdf
    cp _build/latex/*.pdf html
    cd html
    pdf=`basename *.pdf | sed 's/-[0-9].*/.pdf/g'`
    ln -sf `basename *.pdf` $pdf
}

# update sphinx template
cd ${SCRIPT_PATH}
git pull # --rebase

# update all workshops
for dir in ${!workshops[*]}
do
    workshop=${workshops[$dir]}
    update_git $workshop
    if [ $workshop == "isprs-summer-school-2016" ] ; then
	(cd ${SCRIPT_PATH}; git checkout en)
    fi
    update_html $workshop
    if [ $workshop == "grass-gis-zacatecnik" -o \
	$workshop == "otevrena-geodata" -o \
	$workshop == "postgis-zacatecnik" -o \
        $workshop == "qgis-zacatecnik" ] ; then
	update_pdf $workshop
    fi
    if [ $workshop == "isprs-summer-school-2016" ] ; then
	(cd ${SCRIPT_PATH}; git checkout master)
    fi
done
