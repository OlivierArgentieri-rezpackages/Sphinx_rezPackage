# Sphinx rez Package


## Presentation

(just a reminder)

Just an [rez](https://github.com/nerdvegas/rez) Package example with script to easily generate documentation in html and md.

with [Sphinx](https://github.com/sphinx-doc/sphinx), [Sphinx-markdown-builder](https://github.com/clayrisser/sphinx-markdown-builder) and [recommonmark](https://github.com/readthedocs/recommonmark)
- rst and conf : doc\sphinx\source 
- out of html and md : doc\sphinx\build


## Getting Started

Put this package into you rez packages folder

```
rez-pip -i PyYAML
rez-pip -i Sphinx
rez-pip -i sphinx_rtd_theme
rez-pip -i sphinx_markdown_builder
```

Edit requires in packages.py if you want to edit dependencies.

## Usage

Execute doc_html.sh or _md and it should work.

.bat is used on windows for rez command :

``` rez-env Sphinx_rezPackage -- doc_html ```

