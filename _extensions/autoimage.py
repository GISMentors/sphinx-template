# source: https://gist.github.com/kroger/3856821
# customization by Martin Landa

import os
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Figure


def find_image(path, filename):
    dirs = [os.path.join(path,o) for o in os.listdir(path) if os.path.isdir(os.path.join(path,o))]
    dirs.insert(0, '.')
    for path in dirs:
        fname = os.path.join(path, filename)
        if os.path.exists(fname + '.pdf'):
            return fname + '.pdf'
        elif os.path.exists(fname + '.png'):
            return fname + '.png'
        elif os.path.exists(fname):
            return filename
    
    return False

def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))
       
class Autoimage(Figure):
    option_spec = {'scale-html': directives.percentage,
                   'scale-latex': directives.percentage,
                   'scale-epub2': directives.percentage,
                   'scale-mobi': directives.percentage,
                   'scale': directives.percentage,
                   'class': directives.class_option,
                   'align': align,
                   }

    def run(self):
        old_filename = self.arguments[0]
        env = self.state.document.settings.env
        builder_name = env.app.builder.name
            
        if builder_name == 'latex':
            self.arguments[0] = find_image(env.config.image_dir, old_filename)
            if env.config.black_and_white:
                bw_image = find_image(env.config.image_dir_black_white, old_filename)
                if bw_image:
                    self.arguments[0] = bw_image
        else:
            self.arguments[0] = find_image(env.config.image_dir, old_filename)

        # this doesn't quite work because sphinx stores the previous
        # values and share among builds. If I do a make clean between
        # each run it works. Yuck.
        # I need to run sphinx-build with -E
        if builder_name == 'latex':
            classname = self.options.get('class', [''])[0]
            if classname == 'small':
                self.options['scale'] = 40
            elif classname == 'middle':
                self.options['scale'] = 80
            elif classname == 'large':
                self.options['scale'] = 100
            else:
                self.options['scale'] = self.options.get('scale-' + builder_name, 60)
                
            self.options['align'] = self.options.get('align', 'center')
        return super(Autoimage, self).run()


def setup(app):
    app.add_directive('figure', Autoimage)
    app.add_config_value('image_dir', '.', False)
    app.add_config_value('black_and_white', False, True)
    app.add_config_value('image_dir_black_white', 'figs-bw', False)
