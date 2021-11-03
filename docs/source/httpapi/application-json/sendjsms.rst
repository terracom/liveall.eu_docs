Send SMS
========

The end-point to use for send-out is:
   ``https://sms.liveall.eu/apiext/Sendout/SendJSMS``

Main object variables
---------------------

apitoken
   ``string`` a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

senderid
   ``string`` 	the sender name of the SMS. The maximum number of characters is 11

messages
   | ``object`` is an array ob objects that holds the data of the message.
   | Object consists of 3 properties:
   | **destination** (the cell’s number (without leading zeros or leading + sign), for example for Greece: 306912345678),
   | **message** (the message’s text)
   | and an optional property **value_tokens** as described here: :ref:`value_tokens variables`

sendon
   ``unsigned integer - (optional)`` an optional scheduling parameter. You can define the future datetime of the send-out of the message.
   This variable is a type of unsigned integer - unix timestamp. You can find more reference on
   https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html#function_unix-timestamp
   That is, in case you want to send the message on 2016-07-06 12:17:45 you must provide the value 1467796665

pricecat
   ``unsigned integer - (optional)`` by setting that parameter you can choose between normal and low cost price category.
   Set 1 in case you want to send the message with low cost, or ignore it or set the value to 0, in case you want to send with normal cost

forms
   ``object - (optional)`` an object that has form data. Please read below

value_tokens variables
----------------------

| This optional object contains key/values with URL parameter name and its value to set for each SMS sent to the recipient.
| That means


Complete JSON object example
----------------------------

The following JSON shows a possible payload for SMS send-out, that send a different text to each destination with a single request:

.. code-block:: json

   {
    "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d86357c5d52",
    "senderid": "mySender",
    "messages": [
        {
            "destination": "306912345678",
            "message": "Test message A"
        },
        {
            "destination": "306912345677",
            "message": "Test message B. In order to consent, tap on the following link {%form_link_token}",
            "value_tokens": {
              "MIKES_REPLACE_VALUE_TOKEN": "306912345677-j22Jd4p4c6"
            }
        },
        {
            "destination": "306912345676",
            "message": "Test message C. In order to consent, tap on the following link {%form_link_token}",
            "value_tokens": {
              "MIKES_REPLACE_VALUE_TOKEN": "ZTq9Jzj8LH"
            }
        }
    ],
    "forms": {
      "actual_url": "https://forms.onlineformsservice.example?mysoid={MIKES_REPLACE_VALUE_TOKEN}"
    }
   }

.. _`your account’s page`: https://www.liveall.eu/user
