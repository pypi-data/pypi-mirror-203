from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '''0.11'''
DESCRIPTION = '''Search and replace values with df.loc without Exceptions due to dtype incompatibility'''

# Setting up
setup(
    name="a_pandas_ex_easy_loc",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_easy_loc',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_pandas_ex_less_memory_more_speed', 'a_pandas_ex_plode_tool', 'cprinter', 'flatten_everything', 'numpy', 'pandas'],
    keywords=['loc', 'iloc', 'df.at', 'df.iat', 'pandas', 'DataFrame', 'Series'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['a_pandas_ex_less_memory_more_speed', 'a_pandas_ex_plode_tool', 'cprinter', 'flatten_everything', 'numpy', 'pandas'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*