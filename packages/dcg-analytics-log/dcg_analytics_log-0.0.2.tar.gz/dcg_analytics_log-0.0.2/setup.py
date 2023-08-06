import setuptools

NAME = "dcg_analytics_log"
VERSION = "0.0.2"
DESCRIPTION = "A databricks library to build customners prediction reporting and monitor machine learning processes."
URL = ""
AUTHOR = "Bao Minh Doan Dang"
AUTHOR_EMAIL = "s.derwisch@dymatrix.de"


setuptools.setup(name=NAME,
                 version=VERSION,
                 description=DESCRIPTION,
                 url=URL,
                 author=AUTHOR,
                 author_email=AUTHOR_EMAIL,
                 python_requires=">=3.8",
                 keywords=["machine learning", "monitoring"],
                 packages=["dcg_analytics_log", "dcg_analytics_log.data", "dcg_analytics_log.report", "dcg_analytics_log.monitoring"]
                 )
