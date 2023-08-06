A Python interface to FirmaSAT
==============================

This is a Python interface to the core FirmaSAT library, which must be
installed on your system. FirmaSAT is available from
https://www.cryptosys.net/firmasat/.

Classes
-------

**Sello**
   Operates on the Sello (signature) node in a SAT XML document.

**Tfd**
   Operates on the Timbre Fiscal Digital (TFD) element, if present.

**Pkix**
   PKI X.509 security utilities. Operates on private keys and
   X.509 certificates.

**Xmlu**
   XML utilities. Operates on SAT-specific XML documents.

**Gen**
   General info about the core library DLL, e.g. version
   number, compile date.

**Err**
   Details of errors returned by the core library DLL.

All code in is one module ``firmasat.py`` for simplicity of
distribution. All methods are static methods.

Errors
------

Most errors (missing files, invalid format) will result in a
``firmasat.Error`` exception, although some methods are more forgiving
and will return a negative error code instead. Passing a bad argument type
will result in an ``ArgumentError`` exception


Examples
--------

To use in Python's REPL:

::

    >>> from firmasat import *
    >>> Gen.version()
    105028

If you don't like ``import *`` and find ``firmasat`` a bit long to type
each time, try

::

    >>> import firmasat as fs
    >>> fs.Gen.version()
    105028

To sign a CFDI document, create the base XML file with all the required
data except the following nodes

::

    Sello=""
    Certificado=""
    NoCertificado="30001000000300023708"

You must add the 20-digit serial number of your signing certificate to the 
``NoCertificado`` node. See below.

Then run the ``Sello.sign_xml()`` method with full paths to your ``key``
and ``cer`` files.

::

    n = Sello.sign_xml('new.xml', 'base.xml', "emisor.key", password, "emisor.cer")

This creates a new file ``new.xml`` with the Sello and Certificado nodes
completed.


Finding a certificate's serial number
-------------------------------------

::

    >>> firmasat.Pkix.query_cert('emisor.cer', 'serialNumber')
    '30001000000300023708'

or using FirmaSAT from the command line

::

    > firmasat NUMBERCERT emisor.cer
    30001000000300023708


Tests
-----

There is a series of tests in ``test_firmasat.py``. This requires a
subdirectory ``work`` in the same folder as the ``test_firmasat.py``
module containing all the required test files. 
The test function then creates a temporary
subdirectory which is deleted automatically (add the argument
``nodelete`` on the command line to keep this temp directory).

::

    test/
        test_firmasat.py  # this module
        work/        # this _must_ exist
            <all required test files>
            tmp.XXXXXXXX/    # created by `setup_temp_dir()`
                <copy of all required test files>
                <files created by tests>

This structure is already set up in the distribution file, so unzip the
file ``firmasat-x.x.x.zip`` and open a command-line prompt in the
``test`` subdirectory. You can do any of the following.

1. ``python test_firmasat.py``

2. ``py.test -v``

3. Open the file ``test_firmasat.py`` using IDLE and select
   ``Run > Run Module (F5)``.

We've tested this using the Python 3.10.8 interpreter and IDLE, the
PyDev environment in Eclipse, and using ``py.test``.

System requirements
-------------------

Windows platforms only. Python 3 must be installed on your system (at
least 3.6). FirmaSAT v10.50 or above must also be installed.

Contact
-------

For more information or to make suggestions, please contact us at
http://www.cryptosys.net/contact/.

| David Ireland
| DI Management Services Pty Ltd
| Australia
| http://www.cryptosys.net/contact/
| 18 April 2023
