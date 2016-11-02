"""
Flask-Theme
------------
Flask-Theme provides infrastructure for theming support in Flask
applications. It takes care of:

- Loading themes
- Rendering templates from themes
- Serving static files like CSS and images from themes


Links
`````
* `documentation <http://flask-theme.readthedocs.io/>`_
* `development version
<https://github.com/yetship/flask-theme>`_


"""
from setuptools import setup
import sys
requires = ['Flask>=0.6']
if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name='Flask-Theme',
    version='0.1.0',
    url='https://github.com/yetship/flask-theme',
    license='MIT',
    author='Yetship',
    author_email='liqianglau@outlook.com',
    description='Provides infrastructure for theming Flask applications',
    long_description=__doc__,
    packages=['flask_theme'],
    zip_safe=False,
    platforms='any',
    install_requires=requires,
    tests_require='nose',
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
