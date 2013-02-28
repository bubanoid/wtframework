##########################################################################
#This file is part of WTFramework. 
#
#    WTFramework is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WTFramework is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with WTFramework.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

from distutils.core import setup

setup(
    name='wtframework',
    version='0.1.0',
    author='David Lai',
    author_email='david@wiredrive.com',
    packages=['wtframework',
              'wtframework.wtf',
              'wtframework.wtf.assettools',
              'wtframework.wtf.config',
              'wtframework.wtf.data',
              'wtframework.wtf.email',
              'wtframework.wtf.utils',
              'wtframework.wtf.testobjects',
              'wtframework.wtf.web',
              'wtframework.wtf._devtools_',
              'wtframework.wtf._devtools_.filetemplates',
              ],
    scripts=['bin/wtf_init.py', 'bin/wtf_tools.py'],
    url='https://github.com/wiredrive/wtframework',
    license='LICENSE.txt',
    description='WTF - Web Test Framework',
    long_description=open('README.md').read(),
    install_requires=[
        "nose>=1.2.1",
        "NoseXUnit>=0.3.3",
        "ddt>=0.2.0",
        "pyyaml>=3.10",
        "selenium>=2.30.0",
    ],
)
