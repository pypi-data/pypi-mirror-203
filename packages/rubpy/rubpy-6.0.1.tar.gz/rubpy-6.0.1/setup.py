from setuptools import find_packages, setup

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name='rubpy',
    version='6.0.1',
    author='Shayan Heidari',
    url='https://github.com/shayanheidari01/rubika',
    author_email = 'contact@shayanheidari.info',
    description='This is an unofficial library and fastest library for deploying robots on Rubika accounts.',
    python_requires='>=3.7',
    long_description=readme,
    long_description_content_type = 'text/markdown',
    packages=find_packages(exclude=['rubpy*']),
    install_requires=['aiohttp', 'pycryptodome'],
    extras_require={
        'opencv-python': ['opencv-python']
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
)