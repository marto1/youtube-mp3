#
#   @author         Martin N. Gergov    <martingergov1@gmail.com>
#   @license        MIT/X11
#   @date           21/04/2016 (dd-mm-yyyy)
#
from setuptools import setup, find_packages

VERSION = {
        'major' : 0,
        'minor' : 1,
        'patch' : 0,
        }

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name            = 'youtube-mp3',
    version         = '%(major)i.%(minor)i.%(patch)s' % VERSION,
    description     = 'Python cli and library for youtube-mp3.org.',
    author          = 'Martin N. Gergov',
    author_email    = 'martingergov1@gmail.com',
    packages        = ['youtubemp3',],
    package_data={
    },
    license         = 'MIT/X11',
    url='https://github.com/marto1/youtube-mp3',
    download_url    = 'https://github.com/marto1/youtube-mp3',
    keywords        = ['youtube-mp3', 'mp3', 'youtube', 'download'],
    long_description=read('README'),
    classifiers     = [
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2',
    ],
        install_requires=["docopt", "requests",],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
