# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst import directives

class NoteCmd(directives.admonitions.BaseAdmonition):
    required_arguments = 1
    node_class = nodes.admonition

    def run(self):
        self.options['classes'] = ['notecmd']
        self.arguments[0] = u'Příklad ' + self.arguments[0] + u' z příkazové řádky'
        return super(NoteCmd, self).run()

def setup(builder):
    directives.register_directive('notecmd', NoteCmd)
