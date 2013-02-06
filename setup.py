from distutils.core import setup

setup(
    name='wtframework',
    version='0.0.1',
    author='David Lai',
    author_email='david@wiredrive.com',
    packages=['wtframework.wtf.wdtestobjects',
              'wtframework.wtf.config',
              'wtframework.wtf.email',
              'wtframework.wtf.utils',
              'wtframework.wtf.web',
              'wtframework.wtf',
              'wtframework',
              'wtframework.wtf._example_files_',
              ],
    scripts=['bin/wtf_init.py'],
    url='https://github.com/dlai0001/WD-WTF',
    license='LICENSE.txt',
    description='Wiredrive Web Test Framework',
    long_description=open('README.md').read(),
    install_requires=[
        "Mox>=0.5.3",
        "nose>=1.2.1",
        "NoseXUnit>=0.3.3",
        "ddt>=0.2.0",
        "pyyaml>=3.10",
        "selenium>=2.29.0",
        "python-rest-client>=0.3",
    ],
)
