# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='Flask-GoogleAuth',
    version='0.3',
    url='https://github.com/sashka/flask-googleauth',
    license='BSD',
    author='Alexander Saltanov',
    author_email='asd@mokote.com',
    description='Super simple OpenID and Google Federated Auth for Flask apps.',
    long_description=open('README.rst', 'r').read(),
    py_modules=['flask_googleauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask', 'requests', 'blinker'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
