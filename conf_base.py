# -*- coding: utf-8 -*-
#
# GISMentors documentation build configuration file, created by
# sphinx-quickstart on Sat Feb 22 16:10:58 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from sphinx import version_info
from utils import get_month_year

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath(os.path.join('..', 'sphinx-template', '_extensions')))
extensions = [ 'sphinx.ext.extlinks', 'sphinx.ext.todo', 'sphinx.ext.imgmath', 
               'video', 'notes', 'autoimage', 'writter']
# problem with loading, disabled
# 'sphinx.ext.mathjax',
if version_info[0] <= 1 and version_info[1] < 6:
    extensions.append('numfig')
else:
    numfig = True

extlinks = {'grasscmd': ('http://grass.osgeo.org/grass74/manuals/%s.html', ''),
            'grasscmd2': ('http://grass.osgeo.org/grass74/manuals/%s', ''),
            'grasscmdaddons': ('http://grass.osgeo.org/grass74/manuals/addons/%s.html', ''),
            'wikipedia': ('http://cs.wikipedia.org/wiki/%s', ''),
            'wikipedia-en': ('http://en.wikipedia.org/wiki/%s', ''),
            'epsg' : ('http://epsg.io/%s', 'EPSG:'),
            'pgiscmd': ('http://postgis.net/docs/%s.html', ''),
            'pgiscmd2': ('http://postgis.net/docs/%s', ''),
            'pgsqlcmd': ('http://www.postgresql.org/docs/current/static/%s.html', ''),
            'skoleni' : ('http://training.gismentors.eu/%s', ''),
            'grass-script' : ('http://grass.osgeo.org/grass74/manuals/libpython/script.html#script.%s', ''),
            'pygrass-gis' : ('http://grass.osgeo.org/grass74/manuals/libpython/pygrass.gis.html#pygrass.gis.%s', ''),
            'pygrass-modules' : ('http://grass.osgeo.org/grass74/manuals/libpython/pygrass.modules.interface.html#pygrass.modules.interface.module.%s', ''),
            'pygrass-vector' : ('http://grass.osgeo.org/grass74/manuals/libpython/pygrass.vector.html#pygrass.vector.%s', ''),
            'pygrass-raster' : ('http://grass.osgeo.org/grass74/manuals/libpython/pygrass.raster.html#pygrass.raster.%s', ''),
            'python3': ('https://docs.python.org/3/library/%s.html', ''),
            }

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['../sphinx-template/_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'cs'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'agogo'
###html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []
### html_theme_path = ['../sphinx-template/_themes']

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = 'x'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../sphinx-template/_static', '_static']
html_style = 'gismentors.css'

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#    'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

# Additional stuff for the LaTeX preamble.
    'preamble': "".join([]),
    'releasename': u'verze',
    'date': '%s %s' % get_month_year(),
}

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "images/opengeolabs-logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# -- Bootstrap Theme options -------------------------------------------


# html_theme_options = {
#     'navbar_site_name': "Obsah",
#     'navbar_pagenav': False,
#     'globaltoc_depth': 2,
# }

todo_include_todos = True

# -- GISMentors roles -------------------------------------------

rst_prolog = """
.. role:: map
   :class: map

.. role:: mapset
   :class: mapset

.. role:: notecmd
   :class: admonition.cmd

.. role:: fignote

.. role:: secnotoc
    :class: secnotoc

.. role:: item
    :class: item

.. role:: param
    :class: param

.. role:: dbtable
   :class: dbtable

.. role:: dbcolumn
   :class: dbcolumn

.. role:: sqlcmd
   :class: sqlcmd

.. role:: red
   :class: red

.. role:: lcode
   :class: lcode

.. |mIconPostgis| image:: {sep}{path}{sep}_static{sep}icons{sep}qgis{sep}mIconPostgis.png
   :width: 24px
.. |mActionAddPostgisLayer| image:: {sep}{path}{sep}_static{sep}icons{sep}qgis{sep}mActionAddPostgisLayer.png
   :width: 24px
.. |mIconEditable| image:: {sep}{path}{sep}_static{sep}icons{sep}qgis{sep}mIconEditable.png
   :width: 24px
.. |mActionCapturePolygon| image:: {sep}{path}{sep}_static{sep}icons{sep}qgis{sep}mActionCapturePolygon.png
   :width: 24px
""".format(path=os.path.dirname(os.path.abspath(__file__)), sep=os.path.sep)

### GRASS icons
rst_prolog += """
.. |grass-boundary-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}boundary-create.png
   :width: {width}
.. |grass-execute| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}execute.png
   :width: {width}
.. |grass-map-export| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}map-export.png
   :width: {width}
.. |grass-undo| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}undo.png
   :width: {width}
.. |grass-polygon-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}polygon-create.png
   :width: {width}
.. |grass-line-edit| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}line-edit.png
   :width: {width}
.. |grass-layer-raster-profile| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-raster-profile.png
   :width: {width}
.. |grass-point-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}point-add.png
   :width: {width}
.. |grass-script-save| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}script-save.png
   :width: {width}
.. |grass-module-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}module-add.png
   :width: {width}
.. |grass-raster3d| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}raster3d.png
   :width: {width}
.. |grass-python| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}python.png
   :width: {width}
.. |grass-layer-opacity| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-opacity.png
   :width: {width}
.. |grass-area-measure| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}area-measure.png
   :width: {width}
.. |grass-table-manager| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}table-manager.png
   :width: {width}
.. |grass-attributes-display| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}attributes-display.png
   :width: {width}
.. |grass-cats-display| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}cats-display.png
   :width: {width}
.. |grass-layer-rgb-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-rgb-add.png
   :width: {width}
.. |grass-layer-vector-more| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-vector-more.png
   :width: {width}
.. |grass-table| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}table.png
   :width: {width}
.. |grass-raster-calculator| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}raster-calculator.png
   :width: {width}
.. |grass-gcp-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}gcp-add.png
   :width: {width}
.. |grass-zoom-out| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-out.png
   :width: {width}
.. |grass-relation-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}relation-create.png
   :width: {width}
.. |grass-layer-group-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-group-add.png
   :width: {width}
.. |grass-gcp-rms| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}gcp-rms.png
   :width: {width}
.. |grass-overlay-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}overlay-add.png
   :width: {width}
.. |grass-3d-help| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}3d-help.png
   :width: {width}
.. |grass-flythrough| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}flythrough.png
   :width: {width}
.. |grass-polygon-delete| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}polygon-delete.png
   :width: {width}
.. |grass-layer-shaded-relief-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-shaded-relief-add.png
   :width: {width}
.. |grass-vertex-delete| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vertex-delete.png
   :width: {width}
.. |grass-layer-label-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-label-add.png
   :width: {width}
.. |grass-gcp-remove| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}gcp-remove.png
   :width: {width}
.. |grass-layer-import| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-import.png
   :width: {width}
.. |grass-measure-length| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}measure-length.png
   :width: {width}
.. |grass-move| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}move.png
   :width: {width}
.. |grass-layer-info| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-info.png
   :width: {width}
.. |grass-redraw| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}redraw.png
   :width: {width}
.. |grass-scalebar-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}scalebar-add.png
   :width: {width}
.. |grass-layer-open| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-open.png
   :width: {width}
.. |grass-raster| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}raster.png
   :width: {width}
.. |grass-polygon| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}polygon.png
   :width: {width}
.. |grass-layer-bottom| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-bottom.png
   :width: {width}
.. |grass-gcp-save| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}gcp-save.png
   :width: {width}
.. |grass-zoom-region| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-region.png
   :width: {width}
.. |grass-vertex-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vertex-create.png
   :width: {width}
.. |grass-page-settings| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}page-settings.png
   :width: {width}
.. |grass-edit| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}edit.png
   :width: {width}
.. |grass-layer-cell-cats-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-cell-cats-add.png
   :width: {width}
.. |grass-zoom-last| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-last.png
   :width: {width}
.. |grass-legend-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}legend-add.png
   :width: {width}
.. |grass-check| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}check.png
   :width: {width}
.. |grass-rgb| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}rgb.png
   :width: {width}
.. |grass-print| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}print.png
   :width: {width}
.. |grass-raster-stats| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}raster-stats.png
   :width: {width}
.. |grass-layer-aspect-arrow-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-aspect-arrow-add.png
   :width: {width}
.. |grass-layer-wms-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-wms-add.png
   :width: {width}
.. |grass-tools| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}tools.png
   :width: {width}
.. |grass-select| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}select.png
   :width: {width}
.. |grass-font| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}font.png
   :width: {width}
.. |grass-options| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}options.png
   :width: {width}
.. |grass-player-stop| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}player-stop.png
   :width: {width}
.. |grass-monitor-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}monitor-create.png
   :width: {width}
.. |grass-layer-vector-chart-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-vector-chart-add.png
   :width: {width}
.. |grass-layer-more| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-more.png
   :width: {width}
.. |grass-reload| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}reload.png
   :width: {width}
.. |grass-layer-raster3d-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-raster3d-add.png
   :width: {width}
.. |grass-cell-cats| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}cell-cats.png
   :width: {width}
.. |grass-point-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}point-create.png
   :width: {width}
.. |grass-layer-redraw| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-redraw.png
   :width: {width}
.. |grass-layer-raster-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-raster-add.png
   :width: {width}
.. |grass-map-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}map-add.png
   :width: {width}
.. |grass-loop-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}loop-add.png
   :width: {width}
.. |grass-settings| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}settings.png
   :width: {width}
.. |grass-erase| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}erase.png
   :width: {width}
.. |grass-aspect-arrow| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}aspect-arrow.png
   :width: {width}
.. |grass-georectify| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}georectify.png
   :width: {width}
.. |grass-layer-his-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-his-add.png
   :width: {width}
.. |grass-pdf-export| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}pdf-export.png
   :width: {width}
.. |grass-unlocked| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}unlocked.png
   :width: {width}
.. |grass-shaded-relief| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}shaded-relief.png
   :width: {width}
.. |grass-pointer| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}pointer.png
   :width: {width}
.. |grass-data-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}data-add.png
   :width: {width}
.. |grass-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}create.png
   :width: {width}
.. |grass-layer-vector-thematic-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-vector-thematic-add.png
   :width: {width}
.. |grass-redo| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}redo.png
   :width: {width}
.. |grass-vector-thematic| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vector-thematic.png
   :width: {width}
.. |grass-image-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}image-add.png
   :width: {width}
.. |grass-centroid-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}centroid-create.png
   :width: {width}
.. |grass-quit| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}quit.png
   :width: {width}
.. |grass-layer-raster-histogram| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-raster-histogram.png
   :width: {width}
.. |grass-text-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}text-add.png
   :width: {width}
.. |grass-vector-chart| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vector-chart.png
   :width: {width}
.. |grass-info| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}info.png
   :width: {width}
.. |grass-region| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}region.png
   :width: {width}
.. |grass-line-delete| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}line-delete.png
   :width: {width}
.. |grass-map-settings| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}map-settings.png
   :width: {width}
.. |grass-layer-command-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-command-add.png
   :width: {width}
.. |grass-layer-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-add.png
   :width: {width}
.. |grass-gcp-delete| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}gcp-delete.png
   :width: {width}
.. |grass-label-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}label-add.png
   :width: {width}
.. |grass-print-compose| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}print-compose.png
   :width: {width}
.. |grass-cats-copy| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}cats-copy.png
   :width: {width}
.. |grass-python-export| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}python-export.png
   :width: {width}
.. |grass-stats| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}stats.png
   :width: {width}
.. |grass-line-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}line-create.png
   :width: {width}
.. |grass-show| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}show.png
   :width: {width}
.. |grass-gcp-create| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}gcp-create.png
   :width: {width}
.. |grass-map-info| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}map-info.png
   :width: {width}
.. |grass-modeler-main| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}modeler-main.png
   :width: {width}
.. |grass-locked| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}locked.png
   :width: {width}
.. |grass-layer-up| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-up.png
   :width: {width}
.. |grass-save| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}save.png
   :width: {width}
.. |grass-image-export| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}image-export.png
   :width: {width}
.. |grass-modeler-variables| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}modeler-variables.png
   :width: {width}
.. |grass-vector| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vector.png
   :width: {width}
.. |grass-line-split| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}line-split.png
   :width: {width}
.. |grass-3d-rotate| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}3d-rotate.png
   :width: {width}
.. |grass-label| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}label.png
   :width: {width}
.. |grass-layer-raster-more| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-raster-more.png
   :width: {width}
.. |grass-script-load| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}script-load.png
   :width: {width}
.. |grass-wms| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}wms.png
   :width: {width}
.. |grass-layer-grid-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-grid-add.png
   :width: {width}
.. |grass-zoom-extent| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-extent.png
   :width: {width}
.. |grass-his| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}his.png
   :width: {width}
.. |grass-player-back| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}player-back.png
   :width: {width}
.. |grass-player-repeat-back-forward| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}player-repeat-back-forward.png
   :width: {width}
.. |grass-vector-tools| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vector-tools.png
   :width: {width}
.. |grass-north-arrow-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}north-arrow-add.png
   :width: {width}
.. |grass-layer-vector-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-vector-add.png
   :width: {width}
.. |grass-zoom-in| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-in.png
   :width: {width}
.. |grass-help| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}help.png
   :width: {width}
.. |grass-shortest-distance| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}shortest-distance.png
   :width: {width}
.. |grass-layer-remove| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-remove.png
   :width: {width}
.. |grass-rectangle-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}rectangle-add.png
   :width: {width}
.. |grass-open| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}open.png
   :width: {width}
.. |grass-zoom-layer| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-layer.png
   :width: {width}
.. |grass-zoom-more| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}zoom-more.png
   :width: {width}
.. |grass-mapset-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}mapset-add.png
   :width: {width}
.. |grass-line-add| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}line-add.png
   :width: {width}
.. |grass-vertex-move| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}vertex-move.png
   :width: {width}
.. |grass-layer-down| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-down.png
   :width: {width}
.. |grass-3d-settings| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}3d-settings.png
   :width: {width}
.. |grass-line-move| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}line-move.png
   :width: {width}
.. |grass-player-pause| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}player-pause.png
   :width: {width}
.. |grass-pan| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}pan.png
   :width: {width}
.. |grass-layer-export| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-export.png
   :width: {width}
.. |grass-layer-raster-analyze| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-raster-analyze.png
   :width: {width}
.. |grass-ps-export| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}ps-export.png
   :width: {width}
.. |grass-layer-edit| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}layer-edit.png
   :width: {width}
""".format(path=os.path.dirname(os.path.abspath(__file__)), sep=os.path.sep, width='1.5em')
