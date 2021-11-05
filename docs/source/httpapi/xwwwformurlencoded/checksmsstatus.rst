Check the status of a submitted message
=======================================

.. contents:: Contents
  :local:
  :backlinks: none

Endpoint URL
------------

The end-point for sending SMS via HTTP (**POST**) calls is the following:

.. code:: flatline

  https://sms.liveall.eu/apiext/Sendout/GetSMSStatus


curl example
------------

.. code:: flatline

  curl --location --request POST 'https://sms.liveall.eu/apiext/Sendout/GetSMSStatus' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'apitoken=7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8' \
    --data-urlencode 'smsids=20817547,20818326'


Variables
---------

apitoken
   a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

smsids
   supply the SMS id(s) of the already submitted message(s). You may use one of the following delimiters, between SMS ids, in case you want to provide more than one message: ``,.^``


Error Response
--------------

In case of error, the result could be like the following:
   ``Error: <Error code> - <Error message>``

where:

===============   ==============
<Error code>      is the request’s error code as shown below
<Error message>   is the error message, describing the problem with the request
===============   ==============

Successful Response
-------------------

and in case of success, for one message, the result would be in the form of:
   ``<SMSId>:<Submtited On>:<Last status datetime>:<Destination number>:<Status number>:<Status text>:<Quantity of SMS>:<Charge amount>``

For example:
   ``20817547:1465021934:1465021977:306912456789:200000:Delivered:1:0.0379``

For the case you want the status for more than one messages, you will be returned with the results delimiter with character ``|``, for example:
   ``20817547:1465021934:1465021977:306912456789:200000:Delivered:1:0.0379|20818326:1467226402:0:306912345789:100007:Queued:1:0``

Description of result fields
----------------------------

==============================   ===========
Field	                           Description
==============================   ===========
SMSId Integer                    the sms id
Submited On (Integer)	         the date and time of the message’s submission
Last status datetime (Integer)   the datetime of the last status of message
Destination number (String)	   the cell’s number
Status number (Integer)          the numeric status code (*)
Quantity of SMS (Integer)	      how many SMS are consumed for the message
Charge amount (Float)	         the total charge of the message
==============================   ===========

.. _`your account’s page`: https://www.liveall.eu/user
