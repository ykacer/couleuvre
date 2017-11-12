from setuptools import setup

from couleuvre import text # pour pouvoir faire from couleuvre import message

setup(
    name = 'couleuvre',
    packages = ['couleuvre'], # this must be the same as the name above
    include_package_data=True,
    version = '0.1',
    description = 'just to test packaging',
    author = 'Youcef Kacer',
    author_email = 'youcef.kacer@gmail.com',
    url = 'https://github.com/ykacer/github', # use the URL to the github repo
    download_url = 'https://github.com/ykacer/couleuvre/archive/0.1.tar.gz', # I'll explain this in a second
    keywords = ['testing', 'logging', 'example'], # arbitrary keywords
    classifiers = [],
    entry_points = {
       'console_scripts': ["couleuvre-sm = couleuvre.__main__:main",]
                   }
    )

