GISMentor's Sphinx template
===========================

Example for Bash and GRASS-GIS repository

    export repo=grass-gis

1. Download GIT repositories:

        git clone git@github.com:GISMentors/sphinx-template.git
        git clone git@github.com:GISMentors/${repo}.git

2. Copy selected files from `_static` directory

   	mkdir ${repo}/_static
        cp sphinx-template/_static/bgtop.png \
         sphinx-template/_static/bgfooter.png \
         sphinx-template/_static/gismentors.css \
         ${repo}/_static

3. Copy `conf.py` and `Makefile`

        cp sphinx-template/conf.py sphinx-template/Makefile ${repo}
	
4. Optionaly modify background images (`bgtop.png` and `bgfooter.png`) in `<repo>`

5. Optionaly modify `gismentors.css` in `<repo>`

6. Modify `conf.py` in `<repo>`

8. Goto to `<repo>`, add index.rst and build

        cd ${repo}
	echo "Test" > index.rst
	make html

Directives
----------
* youtube
* vimeo
* notegrass6
* notecmd
* noteadvanced

Notes
-----

QGIS Icons:

     cd ~/src/QGIS/images/themes/default
     for f in *.svg; do
          inkscape --export-png=$HOME/git/gismentors/sphinx-template/_static/icons/qgis/${f%%.svg}.png $f ;
     done
