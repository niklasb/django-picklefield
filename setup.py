from setuptools import find_packages, setup

with open('README.rst') as file_:
    long_description = file_.read()

setup(
    name='django-picklefield',
    version='3.0.1',
    description='Pickled object field for Django',
    long_description=long_description,
    author='Simon Charette',
    author_email='charette.s+django-picklefiel@gmail.com',
    url='http://github.com/gintas/django-picklefield',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['django pickle model field'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    python_requires='>=3',
    install_requires=['Django>=2.2'],
    extras_require={
        'tests': ['tox'],
    },
)
