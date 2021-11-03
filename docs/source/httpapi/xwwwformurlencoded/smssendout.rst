SMS sendout
===========

.. contents:: Contents
  :local:
  :backlinks: none


Endpoint URL
------------
The end-point for sending SMS via HTTP (**POST**) calls is the following:
  ``https://sms.liveall.eu/apiext/Sendout/SendSMS``

Variables
---------

apitoken
  a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

destination
  the cell’s number (without leading zeros or leading + sign), for example for Greece: 306912345678. In case you need to send the same message to more than one recipients, then you may supply that variable with these numbers delimited by one of the following characters ``;.^`` It is recommended to send batches with a single request instead of making multiple requests, in case you want to send the same text to multiple destinations

senderid
  the sender name of the SMS. The maximum number of characters is 11

message
  the SMS text

*sendon (optional)*
  an optional scheduling parameter. You can define the future datetime of the send-out of the message. This variable is a type of unsigned integer - unix timestamp. You can find more reference on https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html#function_unix-timestamp That is, in case you want to send the message on 2016-07-06 12:17:45 you must provide the value 1467796665

*pricecat (optional)*
  by setting that parameter you can choose between normal and low cost price category. Set 1 in case you want to send the message with low cost, or ignore it or set the value to 0, in case you want to send with normal cost


If you want to test the API we recommend to use the Postman_.

Error Response
--------------

In case of error, the result could be like the following:
  ``Error: <Error code> - <Error message>``

where:

=============== ==============
<Error code>    is the request’s error code as shown below
<Error message> is the error message, describing the problem with the request
=============== ==============

Successful Response
-------------------

In case of success, for a single destination number, we get:
  ``OK ID:123456789``

(ID: is the submitted SMS id number) and in case of multiple destinations we get something like the below:
  ``OK ID:123456787|OK ID:123456788|OK ID:123456789``


.. _`your account’s page`: https://www.liveall.eu/user
.. _Postman: https://www.postman.com/downloads/

