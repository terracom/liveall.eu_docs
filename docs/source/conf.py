# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Liveall.eu Docs'
copyright = '2021, Liveall.eu'
author = 'Mike Nakos'

release = '12'
version = 'v12'

# -- General configuration

# autodoc_mock_imports = ['_tkinter']

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'hoverxref.extension',
]

sphinx_tabs_valid_builders = ['linkcheck']

# The master toctree document.
master_doc = 'index'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Liveall.eu Docs'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
