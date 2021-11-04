Send SMS
========

Description
-----------

Using that type of API gives you the flexibility to send to a single or multiple destinations SMS by calling the web-service once.
Also you are dealing with a JSON object (as a payload), which is much more straight-forward to a programer.

.. note:: you can send a different text to each destination as you may have noticed below

Endpoint URL
------------

.. code:: flatline

   https://sms.liveall.eu/apiext/Sendout/SendJSMS


curl example
------------

.. code:: flatline

  curl --location --request POST 'https://sms.liveall.eu/apiext/Sendout/SendJSMS' \
  --header 'Content-Type: application/json' \
  --data-raw '  {
        "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8",
        "senderid": "mySender",
        "messages": [
            {
                "destination": "306912345678",
                "message": "Test message A"
            },
            {
                "destination": "306912345677",
                "message": "Test message B"
            }
        ]
    }
  '

JSON object example
-------------------

.. code-block:: json

  {
      "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8",
      "senderid": "mySender",
      "messages": [
          {
              "destination": "306912345678",
              "message": "Test message A"
          },
          {
              "destination": "306912345677",
              "message": "Test message B"
          }
      ]
  }


JSON Object variables
---------------------

:guilabel:`apitoken`
   ``string`` a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

:guilabel:`senderid`
   ``string`` 	the sender name of the SMS. There is a limit to 11 characters (latin characters). Allowed characters are: ``[A-Za-z0-9\-\.\!\#\%\&\(\)\<\>]``

:guilabel:`messages`
   ``object`` is an array of objects that holds the data of the message, as shown in the above example. Object consists of 2 properties:
   **destination** (the cell’s number (without leading zeros or + sign), for example for Greece: 306912345678),
   and **message** (the message’s text)

:guilabel:`sendon`
   ``(optional) - unsigned integer`` an optional scheduling parameter. You can define a future datetime a message to be sent.
   This variable is a type of unsigned integer - unix timestamp. You can find more reference on
   https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html#function_unix-timestamp
   That is, in case you want to send the message on 2016-07-06 12:17:45 you must provide the value 1467796665

:guilabel:`pricecat`
   ``(optional) - unsigned integer`` by setting that parameter you can choose between normal and low cost price category (where applicable).
   Set 1 in case you want to send the message with low cost, or ignore it or set the value to 0, in case you want to send with normal cost



.. _`your account’s page`: https://www.liveall.eu/user
