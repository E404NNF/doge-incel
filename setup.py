from setuptools import setup

setup(
    name='doge-incel',
    version='3.6.0',
<<<<<<< HEAD
    url='https://github.com/E404NNF/incel-homophobic-doge',
    author='E404NNF',
    author_email='',
    description=('wow very terminal incel/homophbic doge'),
=======
    url='https://github.com/E404NNF/incel-homophobic-doge',
    author='E404NNF',
    author_email='',
    description=('wow very terminal incel/homophbic doge'),
>>>>>>> parent of 821e6b4... Update setup.py
    license='MIT',
    packages=['doge-incel'],
    package_data={'doge-incel': ['static/*.txt']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    entry_points={'console_scripts': ['doge-incel = doge.core:main']},
)
