from setuptools import setup, find_packages

name = 'gpt4all'

setup(
    name=name,
    version='0.0.0',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='{}'.format(name),
)
