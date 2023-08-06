# libonvif

Python enabled library for communicating with onvif devices.


This python library has a dependency on libxml2. This library is
released as a source distribution, and as such will require that
the dependency is installed on the host machine prior to compilation.

If compiling on Debian or Ubuntu linux, use the following command 
to install the dependency

```
sudo apt install libxml2-dev
```

If compiling on Windows, the use of Anaconda is recommended.  To install
the dependency in this scenario, use the follwing command under a conda
prompt

```
conda install libxml2
```

To install libonvif python module
```
pip install libonvif
```
To uninstall
```
pip uninstall libonvif
```

Copyright (c) 2020, 2023 Stephen Rhodes 

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

