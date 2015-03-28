import sphinx.writers.latex
BaseTranslator = sphinx.writers.latex.LaTeXTranslator

class DocTranslator(BaseTranslator):

    def visit_Text(self, node):
        if hasattr(self, 'verbatim') and self.verbatim is not None:
            self.verbatim += node.astext()
        else:
            text = self.encode(node.astext())
            if '\\textasciitilde{}' in text:
                text = text.replace('\\textasciitilde{}', '~')
#            if not self.no_contractions:
#                text = educate_quotes_latex(text)
            self.body.append(text)

sphinx.writers.latex.LaTeXTranslator = DocTranslator

import sphinx.writers.html
BaseTranslator = sphinx.writers.html.SmartyPantsHTMLTranslator

class CustomHTMLTranslator(BaseTranslator):

    def bulk_text_processor(self, text):
        if '~' in text:
            text = text.replace('~', '&nbsp;')
        return text

sphinx.writers.html.SmartyPantsHTMLTranslator = CustomHTMLTranslator

def setup(app):
    return {'version': '0.1'}
