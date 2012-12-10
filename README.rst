Sayhi
=====

Just an example how to make python packages for CentOS right.

Building RPM
------------

::

    rpmbuild --define "version 0.1" --define "release 1" -bb contrib/sayhi.spec
