sentry-fogbugz
==============

An extension for Sentry which integrates with `Fogbugz`_ Bug Tracking. Specifically, it allows you to easily create cases from events within Sentry.


Install
-------

Install the sentry-fogbugz package and its requirements with the following commands.

::

    pip install sentry-fogbugz
    pip install fogbugz-orm
    pip install "BeautifulSoup>=3.2.1,<3.3.0 "


Ideally I should put all the dependences inside the ``setup.py`` so people can install the dependences automatically with a single command like ``python setup.py install`` or ``pip sentry-fogbugz``.

But unfortunately, FogBugzPy(the official fogbuz python API client) strictly requires ``BeautifulSoup==3.2`` and that is conflict with Sentry's requirement (for now Sentry requires ``BeautifulSoup==3.2.1``). Although FogBugzPy is compatible with ``BeautifulSoup==3.2.1``, but based on my communication with its auther, I believe it's unlikely that FogBugzPy would fix that problem.

Thus you have to install ``sentry-fogbugz`` and its dependences separately to avoid the conflicts.


Get a FogBugz XML API Token
----------------------------

Open a browser and load the following URL into it, replacing the text in [square brackets] with values appropriate to your install:
::

    https://[yourfogbugz]/api.asp?cmd=logon&email=[youremail]&password=[yourpassword]

The API should give you an XML response with a token that looks something like this:
::

    <response>
        <token>
            <![CDATA[ TOKEN_STRING ]]>
       </token>
    </response>

Reference: `How To Get a FogBugz XML API Token ( From Fog Creek )`_



.. _Fogbugz: http://www.fogcreek.com/fogbugz/
.. _How To Get a FogBugz XML API Token ( From Fog Creek ): http://help.fogcreek.com/8447/how-to-get-a-fogbugz-xml-api-token
