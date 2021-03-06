Check the account balance
=========================

.. contents:: Contents
  :local:
  :backlinks: none

------------------------------------------------

Endpoint URL
------------

The end-point for sending SMS via HTTP (**POST**) calls is the following:

.. code:: flatline

  https://sms.liveall.eu/apiext/Sendout/GetAccountBalance


------------------------------------------------

curl example
------------

.. code:: flatline

  curl --location --request POST 'https://sms.liveall.eu/apiext/Sendout/GetAccountBalance' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'apitoken=7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8' \
    --data-urlencode 'countryprefix=30'


Variables
---------

apitoken
   the api token (as mentioned in previous end-points)

*countryprefix (optional)*
   an optional country code. If you provide that, you will get the available SMS count, based on the price of the provided country (normal & low cost)

------------------------------------------------

Successful Responses
--------------------

- Case we don’t provide country code

``OK Balance:169.64|SmsRemainCount:-1|LCSmsRemainCount:-1``

- Case that we provide the country code

``OK Balance:169.64|SmsRemainCount:4475|LCSmsRemainCount:5317``

================  =====================
Resp. Variable    Description
================  =====================
Balance           the account’s balance in euros
SmsRemainCount    the remaining SMS (for the case we want to send with normal cost)
LCSmsRemainCount  the remaining SMS (for the case we want to send with low cost)
================  =====================

------------------------------------------------

Error Response
--------------
``Error: <Error code> - <Error message>``

where:

=============== ==============
<Error code>    is the request’s error code as shown below
<Error message> is the error message, describing the problem with the request
=============== ==============

