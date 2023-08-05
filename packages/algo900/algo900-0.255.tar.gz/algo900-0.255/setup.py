from setuptools import setup, find_packages

setup(
    name='algo900',
    version='0.255',
    packages=find_packages(where="src"),
	include_package_data=True,
	description= "Python version of Synthetic difference in differences",
    install_requires=[
        # any dependencies required by your package
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
