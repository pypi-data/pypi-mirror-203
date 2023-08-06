import setuptools

NAME = "dcg_analytics_log"
VERSION = "0.0.1"
DESCRIPTION = "A databricks library to build customners prediction reporting and monitor machine learning processes."
URL = ""
AUTHOR = "Bao Minh Doan Dang"
AUTHOR_EMAIL = "b.doandang@dymatrix.de"


setuptools.setup(name=NAME,
                 version=VERSION,
                 description=DESCRIPTION,
                 url=URL,
                 author=AUTHOR,
                 author_email=AUTHOR_EMAIL,
                 packages=setuptools.find_packages(),
                 python_requires=">=3.8",
                 keywords=["machine learning", "monitoring"]
                 )
