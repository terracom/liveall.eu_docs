Old API (obsolete)
==================

.. figure:: ../../static/httpapi-image.png
   :alt: old-api-logo

.. contents:: Contents
  :local:
  :backlinks: none
  :depth: 1


1. Send SMS
-----------

1.1 Description
^^^^^^^^^^^^^^^

We maintain the old http api for backwards compatibility (there are no improvements on this api),
because `Liveall.eu`_ has an ecosystem of 3rd party applications-sites that may not switched to our new API yet.

.. note:: All newcomers to the service cannot use that API. They **must** use newer versions of API


1.2 Endpoint URL
^^^^^^^^^^^^^^^^

.. code:: flatline

   https://www.liveall.eu/webservice/sms/sendSMSHTTP.php

   OR

   https://www.liveall.eu/webservice/sms/sendSMSHTTPUTF8.php


1.3 curl example
^^^^^^^^^^^^^^^^

.. code:: flatline

  curl --location --request GET 'https://www.liveall.eu/webservice/sms/sendSMSHTTP.php' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username=myusername' \
    --data-urlencode 'password=mypass' \
    --data-urlencode 'destination=306912345678' \
    --data-urlencode 'sender=mySender' \
    --data-urlencode 'message=This is a test message from me!'


1.4 Variables
^^^^^^^^^^^^^

:guilabel:`username`
   ``string`` the username

:guilabel:`password`
   ``string`` the password

:guilabel:`destination`
   ``string`` the destination cell number (must **not contain** leading characters ``+`` or ``00``). If you want to send to multiple destinations, then separate numbers with the character  ``.``

:guilabel:`sender`
   ``string`` the sender name of the SMS. There is a limit to 11 characters (latin characters).

:guilabel:`message`
   ``string`` the SMS text

:guilabel:`pricecat`
   ``(optional) - unsigned integer`` by defining this parameter you can send with low-cost (if you set 1 to it) instead of sending with the default normal cost (where applicable)


1.5 Error Response
^^^^^^^^^^^^^^^^^^

In case of error, we get one of the following responses:

.. code:: flatline

   Error: 1001 - No username given.
   Error: 1002 - No password given.
   Error: 1003 - No destination number given.
   Error: 1004 - Unknown destination error.
   Error: 1005 - Invalid destination number.
   Error: 1006 - Alphanumeric sender address is longer than accepted.
   Error: 1007 - Numeric sender address is longer than accepted.
   Error: 1008 - No sender name or number given.
   Error: 1009 - Message contains invalid character.
   Error: 1010 - Error sending SMS - Gateway call error.
   Error: 1011 - Greek numbers must have 12 digits (including country code).
   Error: 1011 - There is no SMS text given.
   Error: 1012 - User authendication failure. Username and/or password mismatch.
   Error: 1013 - Not available credits for user.
   Error: 1014 - Given user id mismatch.
   Error: 1015 - Unknown error with sender.
   Error: 1016 - Not enough alphanumeric characters on sender address. Required
   Error: 1017 - Destination number(s) not supported.
   Error: 1018 - Not enough credits when sending sms to that destination.
   Error: 1019 - Error inserting row on transactions table. Aborting
   Error: 1020 - Error With sms charge on this destination.
   Error: 1021 - Invalid characters on sender address.
   Status: 1022 - Awaiting cost confirmation. SMS did't sent yet.
   Status: 1023 - Not enough credits left for SMS postage.
   Status: 1024 - Error validating Sms.
   Status: 1025 - Error while checking balance of user.
   Status: 1026 - Batch of SMS queued and is about to be transmited.
   Error: 1027 - No SMS ID given.
   Error: 1028 - No valid parameters given.
   Error: 1029 - The allowed length of sms is no more than 612 characters (4 SMS).
   Error: 1031 - The SMS Service is temporary unavailable. Try again in a few minutes.
   Error: 1032 - Error submiting SMS. Please try again a bit more later.
   Error: 1033 - Not enough balance on your account to make HLR lookup. Please buy credits.
   Error: 1036 - The sender name you have provided is not allowed.
   Error: 1038 - User is disabled
   Error: 1039 - HLR, Invalid number(s) provided
   Error: 1040 - No HLR ID given.
   Error: 1041 - DBID for HLR query not found
   Error: 1042 - Api token not provided
   Error: 1043 - Internal error


1.6 Successful Response
^^^^^^^^^^^^^^^^^^^^^^^

On a successful SMS submit, you get the following result:

.. code:: flatline

   OK ID:<SMS_HTTP_request_ID>

where ``SMS_HTTP_request_ID`` is the SMS id of your SMS web-request

.. admonition:: Example results

   ``OK ID:1234`` when sending to a single cell number, or ``OK ID:1234|OK ID:1235|OK ID:1236`` when sending to more than one destination.


2. Check the status of SMS
--------------------------

2.1 Description
^^^^^^^^^^^^^^^

By calling the above end-point you can check the status of SMS previously sent by our platform


2.2 Endpoint URL
^^^^^^^^^^^^^^^^

.. code:: flatline

   https://www.liveall.eu/webservice/sms/getSMSStatus.php


2.3 curl example
^^^^^^^^^^^^^^^^

.. code:: flatline

  curl --location --request GET 'https://www.liveall.eu/webservice/sms/getSMSStatus.php' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username=myusername' \
    --data-urlencode 'password=mypass' \
    --data-urlencode 'SMSId=1111'


2.4 Variables
^^^^^^^^^^^^^

:guilabel:`username`
   ``string`` the username

:guilabel:`password`
   ``string`` the password

:guilabel:`SMSId`
   ``unsigned integer`` the SMS id we have been returned by web-service, on message’s submission


2.5 Error Response
^^^^^^^^^^^^^^^^^^

Possible results for above end-point are, in case of error:

.. code:: flatline

   Error: 1012 - User authendication failure. Username and/or password mismatch.
   Error: 1027 - No SMS ID given.
   Error: 1028 - No valid parameters given.


2.6 Successful Response
^^^^^^^^^^^^^^^^^^^^^^^

On a successful response we get the following result:

.. code:: flatline

   <SMSId>:<Submtited On>:<Destination number>:<Delivered On>:<Status number>:<Quantity of SMS>:<Charge amount>

.. admonition:: Example result

   ``2345:20101212152514:306912345678:20101212152519:2048:1:0.057``

2.7 Response properties
^^^^^^^^^^^^^^^^^^^^^^^

===========================   ===========
Name                          Description
===========================   ===========
SMSId [Integer]               the SMS ID
Submited On [String]          | datetime of SMS submit. Date format is:
                              | YYYYMMDDHHmmSS [YYYY:year, MM:month 00~12, DD:day of month 00~31,
                              | HH:hour 00~24, mm:minutes 00~59, SS:seconds 00~59]
Destination number [String]   the phone number
Delivered On [String]         | datetime of last SMS status. Date format is:
                              | YYYYMMDDHHmmSS [YYYY:year, MM:month 00~12, DD:day of month 00~31,
                              | HH:hour 00~24, mm:minutes 00~59, SS:seconds 00~59]
Status number [Integer]       the status code. `2.8 Possible SMS statuses`_
Quantity of SMS [Integer]     the quantity of SMS needed to send the message
Charge amount [float]         the charged amount
===========================   ===========


2.8 Possible SMS statuses
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: flatline

   1: Queued
   2: Queued on SMSC
   4: Waiting Validation
   8: Unknown subscriber
   16: Temporary unavailable
   32: Pending
   64: Undelivered
   128: Expired
   256: Non-Delivered to SMSC
   512: Error
   1024: Unknown error
   2048: Delivered
   16384: HLR Sent
   32768: HLR Completed


3. Check the current balance of messaging account
-------------------------------------------------


3.1 Description
^^^^^^^^^^^^^^^

This endpoint fetches the current balance of the account

3.2 Endpoint URL
^^^^^^^^^^^^^^^^

.. code:: flatline

   https://www.liveall.eu/webservice/sms/getAccountBalance.php


3.3 curl example
^^^^^^^^^^^^^^^^

.. code:: flatline

  curl --location --request GET 'https://www.liveall.eu/webservice/sms/getAccountBalance.php' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username=myusername' \
    --data-urlencode 'password=mypass' \
    --data-urlencode 'countryprefix=30'


3.4 Variables
^^^^^^^^^^^^^

:guilabel:`username`
   ``string`` the username

:guilabel:`password`
   ``string`` the password

:guilabel:`countryprefix`
   ``(optional) string`` an optional country code. If you provide that, you will get the available SMS count, based on the price of the provided country (normal & low cost)


3.5 Error Response
^^^^^^^^^^^^^^^^^^

Possible results for above end-point are, in case of error:

.. code:: flatline

   Error: 1001 - No username given.
   Error: 1002 - No password given.


3.6 Successful Response
^^^^^^^^^^^^^^^^^^^^^^^

On a successful response we get the following result:

.. code:: flatline

   Status: 1000 - Balance:BalanceInEuro|SmsRemainCount:RemainingSMSCount

where:

=================    ==============
BalanceInEuro        is the request’s error code as shown below
RemainingSMSCount    is the error message, describing the problem with the request
=================    ==============

.. _`Liveall.eu`: https://www.liveall.eu
