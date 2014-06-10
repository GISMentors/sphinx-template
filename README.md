GISMentor's Sphinx template
===========================

Example for Bash and GRASS-GIS repository

    export repo=GRASS-GIS

1. Download GIT repositories:

        git clone git@github.com:GISMentors/sphinx-template.git
        git clone git@github.com:GISMentors/${repo}.git

2. Copy selected files from `_static` directory

        cp sphinx-template/_static/bgtop.png \
         sphinx-template/_static/bgfooter.png \
         sphinx-template/_static/gismentors.css \
         ${repo}/_static

3. Copy `conf.py`

        cp sphinx-template/conf.py ${repo}

4. Modify background images (`bgtop.png` and `bgfooter.png`) in `<repo>`

5. Modify `gismentors.css` in `<repo>`

6. Modify `conf.py` in `<repo>`

7. Goto to `<repo>` and build

        cd ${repo} && make html