Extract message log for a date
==============================

.. figure:: ../../static/messages-log.png
   :alt: messages-log-icon

Description
-----------

This endpoint extract the messages log for a specific date in a string format (csv)


Endpoint URL
------------

.. code:: flatline

   https://sms.liveall.eu/apiext/Sendout/GetSMSHistory


curl example
------------

.. code:: flatline

  curl --location --request POST 'https://sms.liveall.eu/apiext/Sendout/GetSMSHistory' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'apitoken=7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8' \
      --data-urlencode 'submit_date=20210524'

Form parameters
---------------

:guilabel:`apitoken`
   ``string`` a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

:guilabel:`submit_date`
   | ``string`` we define the date we want to extract the messages log. The date format must be in a form of: **yyyyMMdd**
   | where **yyyy** is the 4 digit year numeber
   | **MM** the 2 digit month number
   | **dd** the date of the month
   | For instance, if we need to get the log for 24 of May 2021, then string value would be: ``20210524``

:guilabel:`timezone_offset`
   | ``(optional) - integer`` this is your timezone value **based on UTC**. you have to specify it if you'are not in the same timezone as Athens/Greece.
   | Bear in mind that, ``GMT is not UTC`` - (GMT: Greenwich Mean Time, UTC: Coordinated Universal Time), because on winter time, GMT is +0 and on summer time is +1.
   | So for example if you're in Rome and your computer has winter time you must define 1 and on summer 2.
   | Accordingly, if you're in New York, on winter you enter -5 and on summer -4

:guilabel:`senderid`
   ``(optional filter) - string`` Filter results based on the sender_id

:guilabel:`destination`
   ``(optional filter) - string`` Filter results based on the destination(s) number

:guilabel:`sms_id`
   ``(optional filter) - integer`` Filter results based on the SMS id

:guilabel:`batch_id`
   ``(optional filter) - integer`` Filter results based on the batch id

:guilabel:`gt_sms_id`
   ``(optional filter) - integer`` Filter, gets rows with SMS id greater than the value specified. Suppose there are results with SMS id (1, 2, 3, 4, 5) and we define 2, then we will get the rows (3, 4, 5)


Error Response
--------------

There are 2 cases of error:

Validation issue, which service will reply with
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Error: <Error code> - <Error message>``

where:

=============== ==============
<Error code>    is the request’s error code as shown below
<Error message> is the error message, describing the problem with the request
=============== ==============


Internal error
^^^^^^^^^^^^^^

In that case, service will return http status: 500 as descibed here: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_errors


Successful Response
-------------------

In case of success, we will have a string response with so many lines as the rows found. If no row found, then we will get an empty string.
Lines are delimited with character ``\n``. Below is an example of a successful response with 2 rows found:

.. code:: flatline

   47680777|8350040|terracom|306912345678|1585742558|Delivered|1|0.0379|UNDEFINED
   47680768|8350041|Liveall.eu|306912345679|1585742462|Delivered|1|0.0379|UNDEFINED

Below are the descriptions of each field of the above example response:

1. sms id
2. batch id
3. sender id
4. recipient's phone number
5. Last status datetime, in Unixtime - You can check the value here: `Online epoch converter`_
6. SMS Status string value - Possible values are here: 




.. _`your account’s page`: https://www.liveall.eu/user
.. _`Online epoch converter`: https://www.epochconverter.com/