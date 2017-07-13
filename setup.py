from distutils.core import setup

setup(
    name='reescraper',
    version='1.0.0',
    packages=['reescraper'],
    install_requires=[
        'arrow',
        'requests'
      ],
    url='https://github.com/blackleg/reescraper',
    license='MIT',
    author='blackleg',
    author_email='hectorespertpardo@gmail.com',
    description='Red Eléctrica de España data scraper'
)
