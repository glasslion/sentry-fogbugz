sentry-fogbugz
==============

An extension for Sentry which integrates with `Fogbugz`_ Bug Tracking. Specifically, it allows you to easily create cases from events within Sentry.


Install
-------

::

    pip install sentry-fogbugz

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
