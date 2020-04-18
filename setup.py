import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'pywebio', '__version__.py')) as f:
    exec(f.read(), about)

with open('README.md') as f:
    readme = f.read()

setup(
    name=about['__package__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires=">=3.5.2",
    packages=find_packages(),
    package_data={
        # data files need to be listed both here (which determines what gets
        # installed) and in MANIFEST.in (which determines what gets included
        # in the sdist tarball)
        "pywebio": [
            "html/codemirror/darcula.css",
            "html/codemirror/active-line.js",
            "html/codemirror/matchbrackets.js",
            "html/codemirror/loadmode.js",
            "html/codemirror/python.js",
            "html/css/bootstrap.min.css",
            "html/css/mditor.min.css",
            "html/css/jquery.toast.min.css",
            "html/css/mditor.min.css.map",
            "html/css/app.css",
            "html/css/codemirror.min.css",
            "html/js/FileSaver.min.js",
            "html/js/mditor.min.js",
            "html/js/.DS_Store",
            "html/js/codemirror.js",
            "html/js/pywebio.js",
            "html/js/mustache.min.js",
            "html/js/jquery.min.js",
            "html/js/bootstrap.min.js",
            "html/js/bs-custom-file-input.min.js",
            "html/js/popper.min.js",
            "html/js/jquery.toast.min.js",
            "html/js/require.min.js",
            "html/js/codemirror.min.js",
            "html/image/favicon_open_16.png",
            "html/image/favicon_closed_32.png",
            "html/index_cdn.html",
            "html/index.html",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        'tornado>=4.3.0',  # After this version, the new async/await keywords in Python 3.5 are supported
    ],
    extras_require={
        'flask': ['flask'],
        'dev': [
            'selenium==3.*',
            'percy-python-selenium',
        ]
    },
    project_urls={
        'Documentation': 'https://pywebio.readthedocs.io',
        'Source': 'https://github.com/wang0618/PyWebIO',
    },
)
