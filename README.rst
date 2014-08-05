sentry-fogbugz
==============

An extension for Sentry which integrates with `Fogbugz`_ Bug Tracking. Specifically, it allows you to easily create cases from events within Sentry.


Install
-------

Install the package and its requirements via ``pip``. Ideally I should put all the dependences into the ``setup.py`` and let the ``setup.py`` or ``pip`` install them automatically. But unfortunately, the official fogbuz python API client have a strict and unreasonable requirement on the BeautifulSoup lib which is conflict with Sentry's requirement. Thus you have to install its dependences manually or via the ``requirements.txt``::

    pip install sentry-fogbugz
    pip install fogbugz-orm
    pip install "BeautifulSoup>=3.2.1,<3.3.0 "

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