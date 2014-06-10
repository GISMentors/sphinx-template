# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.join('..', 'sphinx_template'))
from conf_base import *

# -- General configuration ------------------------------------------------

# General information about the project.
project = u'Školení GRASS GIS'
copyright = u'2014, Martin Landa (GISMentors.eu)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '%s alpha' % version

# -- Options for HTML output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Skoleni-GRASS-GIS'
