# script from http://christop.club/2014/02/21/blogging-with-ipython-and-jekyll/

# How to use:
# - adapt BLOG_DIR if necessary

# - then cd into this directory ("notebooks")  and run
#  
#  ipython nbconvert --config ../__ipynb/jekyll.py <FILENAME.ipynb>
#   (or jupyter for newer versions)
# -  move /notebooks/<file.md> to _posts 
# - you will probably need to rename it, e.g. giving it a date, edit it a.s.o.

try:
    from urllib.parse import quote  # Py 3
except ImportError:
    from urllib2 import quote  # Py 2
import os
import sys

HOME_DIR = "/home/shoefer/"
#HOME_DIR = "/Users/Hoefer/"

try:
    BLOG_DIR = os.environ['BLOG_DIR']
except:
    BLOG_DIR = os.path.join(HOME_DIR, 'workspace/shoefer.github.io')
    #BLOG_DIR = os.path.join(HOME_DIR, 'Workspace/shoefer.github.io')

f = None
for arg in sys.argv:
    if arg.endswith('.ipynb'):
        f = arg.split('.ipynb')[0]
        break


c = get_config()
c.NbConvertApp.export_format = 'markdown'
c.MarkdownExporter.template_path = [os.path.join(BLOG_DIR, '__ipynb')]
print c.MarkdownExporter.template_path 
print c.MarkdownExporter.template_path
c.MarkdownExporter.template_file = 'jekyll.tpl'
#c.Exporter.file_extension = 'md'

def path2support(path):
    """Turn a file path into a URL"""
    parts = path.split(os.path.sep)
    return '{{site.url}}/notebooks/' + '/'.join(quote(part) for part in parts)

c.MarkdownExporter.filters = {'path2support': path2support}

if f:
    c.NbConvertApp.output_base = f.lower().replace(' ', '-')
    c.FilesWriter.build_directory = BLOG_DIR + '/notebooks'
