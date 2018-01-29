#!/usr/bin/env python

import os
import sys

if len(sys.argv) < 3:
    sys.exit("icons output")

path=sys.argv[1]
output=sys.argv[2]

str=""".. |grass-%s| image:: {sep}{path}{sep}_static{sep}icons{sep}grass{sep}%s.png
   :width: {width}
"""

fd = open(output, 'w')
for f in os.listdir(path):
    if os.path.splitext(f)[1] != '.png':
        continue

    basename = os.path.splitext(f)[0]

    fd.write(str % (basename, basename))
fd.close()
