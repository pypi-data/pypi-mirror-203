from setuptools import setup


with open('README.md') as file:
    readme = file.read()


setup(
    name='lcu-connector',
    version='1.0.0',
    author='Gabriel Viana',
    author_email='ssiriusbeck@gmail.com',
    description='Easy-to-use wrapper for the League Client API.',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=['lcu_connector'],
    install_requires=['requests', 'psutil'],
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
    ],
    license='MIT',
    project_urls={
        'Source': 'https://github.com/pySiriusDev/LCU-Connector',
        'Download': 'https://github.com/pySiriusDev/LCU-Connector/releases',
        'Instagram': 'https://instagram.com/biellviana',
        'Twitter': 'https://twitter.com/_siriusbeck'
    }
)
