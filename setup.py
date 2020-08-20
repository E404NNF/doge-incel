from setuptools import setup

setup(
    name='doge-incel',
    version='3.6.0',
    url='https://github.com/E404NNF/incel-homophobic-doge',
    author='E404NNF',
    author_email='lowe.thiderman@gmail.com',
    description=('wow very terminal incel/homophbic doge'),
    license='MIT',
    packages=['doge'],
    package_data={'doge': ['static/*.txt']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    entry_points={'console_scripts': ['doge-incel = doge.core:main']},
)

