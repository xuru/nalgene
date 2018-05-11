from setuptools import setup, find_packages


def long_description():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name="nalgene",
    version='0.1.0',
    description='A natural language generation language',
    long_description=long_description(),
    author="Sean Robertson",
    author_email='sprobertson@gmail.com',
    url='https://github.com/spro/nalgene',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing :: Linguistic'
    ],
    packages=find_packages(exclude=['docs', 'examples', 'tests/*']),
    keywords=['natural language generation', 'NLG', 'text generation', 'nlglib', 'library'],
    install_requires=['click'],
    include_package_data=True,
    package_dir={'nalgene': 'nalgene'},
    zip_safe=True,
    entry_points='''
    [console_scripts]
    nalgene=nalgene.commands:cli
    ''',
)
