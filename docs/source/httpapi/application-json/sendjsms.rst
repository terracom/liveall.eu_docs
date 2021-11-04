Send SMS
========

.. figure:: ../../static/Sms-icon-small.png
   :alt: sms-icon-small

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


Error Response
--------------

In case of error, we get something like the below:

.. code-block:: json

    {
        "success": false,
        "OperationErrors": [
            {
                "errorCode": 13,
                "errorMessage": "Invalid destination number",
                "SMSErrorType": 3,
                "valueOfError": "3069"
            }
        ],
        "SubmissionID": 0,
        "data": null
    }

**[success]** will be false and you'll find the object **[OperationErrors]** with error details

Successful Response
-------------------

.. code-block:: json

    {
        "success": true,
        "OperationErrors": null,
        "SubmissionID": 0,
        "data": [
            {
                "destination": "306912345678",
                "smsid": 20818588
            },
            {
                "destination": "306912345677",
                "smsid": 20818589
            },
            {
                "destination": "306912345676",
                "smsid": 20818590
            }
        ]
    }

**[success]** is true and the **[data]** property contains the **[smsid]** for each SMS

Response properties
-------------------

===============     ===========
Name                Description
===============     ===========
success             when false, then no message sent and the whole request is considered failed
OperationErrors     | when success is false, we get an array of objects with errors.
                    | Each object has 3 properties:
                    | **errorCode**: the error code (integer) of the error,
                    | **errorMessage**: the descriptive text of the error and
                    | **valueOfError**: the value that caused the error (for debugging purposes)
data                | in case of success, web-service is returning an array ob objects - 
                    | one for each destination, having 2 properties:
                    | **destination**: the cell’s number and
                    | **smsid**: the unique id of the SMS
===============     ===========




.. _`your account’s page`: https://www.liveall.eu/user
