#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


setup(
    name='idealgeo',
    version='0.0.3',
    license='Apache-2.0',
    description="Client library for IdealSpot's Geodata API.",
    long_description='{}\n{}'.format(
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst')),
    ),
    author='Josh Winters',
    author_email='josh@idealspot.com',
    url='https://gitlab.com/idealspot/geodata/python-idealgeo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://python-idealgeo.readthedocs.io/',
        'Changelog': 'https://python-idealgeo.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://gitlab.com/jbwinters/python-idealgeo/issues',
    },
    keywords=[
        'demographics', 'geodata', 'geospatial', 'gis', 'idealgeo', 'idealspot', 'python-idealgeo',
        'geometry', 'geography', 'labor', 'population', 'statistics', 'demographic', 'geographic',
        'geographic data', 'geographic information', 'geographic information system', 'geographic information systems',
        'geospatial analysis', 'geospatial data', 'geospatial information', 'geospatial information system',
        'united states', 'us', 'usa', 'us census', 'us census bureau', 'us census data', 'us census geography',
        'nation', 'country', 'state', 'county', 'city', 'town', 'village', 'census tract', 'block group',
        'block', 'place', 'zip code', 'zip code tabulation area', 'zcta',
        'census block', 'census block group', 'census tract', 'census tract block group',
        'national', 'state', 'county', 'county subdivision', 'place',
        'population', 'population density', 'population estimate', 'population estimate base',
        'population estimate base year', 'population estimate year', 'population estimate year',
        'points of interest', 'poi', 'point of interest', 'points of interest',
        'vehicle', 'vehicles', 'vehicle count', 'vehicles count', 'vehicle counts', 'vehicles counts',
        'vehicle traffic', 'vehicles traffic', 'vehicle traffic count', 'vehicles traffic count',
        'aadt', 'average annual daily traffic', 'traffic', 'traffic count', 'traffic counts',
    ],
    python_requires='>=3.7',
    install_requires=[
        'click',
        'requests',
        'pydantic',
        'geojson-pydantic',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'idealgeo = idealgeo.cli:main',
        ]
    },
)
