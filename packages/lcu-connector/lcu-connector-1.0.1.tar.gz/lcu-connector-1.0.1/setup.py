from setuptools import setup


with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name="lcu-connector",
    version="1.0.1",
    author="Gabriel Viana",
    author_email='ssiriusbeck@gmail.com',
    description="Easy-to-use wrapper for the League Client API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["lcu_connector"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    install_requires=[
        'requests',
        'psutil'
    ],
    dependency_links=['https://github.com/pySiriusDev/lcu-connector'],
    project_urls={
        'Source': 'https://github.com/pySiriusDev/lcu-connector',
        'Download': 'https://github.com/pySiriusDev/lcu-connector/releases',
        'Instagram': 'https://instagram.com/biellviana',
        'Twitter': 'https://twitter.com/_siriusbeck'
    },
    keywords=[
        'league client',
        'league client api',
        'league client api wrapper',
        'api wrapper'
        'league of legends',
        'league of legends api',
        'lcu-driver',
        'lcu driver',
        'lcu-connector',
        'lcu connector'
    ]
)