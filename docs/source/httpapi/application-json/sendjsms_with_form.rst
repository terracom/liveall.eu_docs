Send SMS with a form
====================

.. figure:: ../../static/Sms-icon-small.png
   :alt: sms-icon-small

Description
-----------

That document describes the same API as the :doc:`sendjsms` but it covers the case when we send form links to the message recipients.
The usage is simple enough and goes like this:

1. provide an additional property [forms] as described here: :ref:`[forms] object`
2. SMS body must have a token: ``{%form_link_token}``. That token will be replaced with the final URL that message recipient will tap on his phone
3. object for each destination must also have a property ``value_tokens`` that is a key/value holder with the values of each parameter on the URL
4. the above key/value holder replaces the values of the corresponding param for each destination

Find out more on :ref:`[forms] object` and :ref:`[value_tokens] object`


Endpoint URL
------------

The end-point to use for send-out is:

.. code:: flatline

   https://sms.liveall.eu/apiext/Sendout/SendJSMS


curl example
------------

.. code:: flatline

  curl --location --request POST 'https://sms.liveall.eu/apiext/Sendout/SendJSMS' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8",
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
                "SOMEID_VAL_TOKEN": "306912345677-j22Jd4p4c6"
              }
          },
          {
              "destination": "306912345676",
              "message": "Test message C. In order to consent, tap on the following link {%form_link_token}",
              "value_tokens": {
                "SOMEID_VAL_TOKEN": "ZTq9Jzj8LH"
              }
          }
      ],
      "forms": {
        "actual_url": "https://forms.onlineformsservice.example/myforms/get/?mysoid={SOMEID_VAL_TOKEN}"
      }
     }'

JSON object example
-------------------

The following JSON shows a possible payload for SMS send-out, that send a different text to each destination with a single request:

.. code:: json

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
            "message": "Test message B. In order to consent, tap on the following link {%form_link_token}",
            "value_tokens": {
              "SOMEID_VAL_TOKEN": "306912345677-j22Jd4p4c6"
            }
        },
        {
            "destination": "306912345676",
            "message": "Test message C. In order to consent, tap on the following link {%form_link_token}",
            "value_tokens": {
              "SOMEID_VAL_TOKEN": "ZTq9Jzj8LH"
            }
        }
    ],
    "forms": {
      "actual_url": "https://forms.onlineformsservice.example/myforms/get/?mysoid={SOMEID_VAL_TOKEN}"
    }
   }


JSON Object variables
---------------------

:guilabel:`apitoken`
   ``string`` a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

:guilabel:`senderid`
   ``string`` 	the sender name of the SMS. There is a limit to 11 characters (latin characters). Allowed characters are: ``[A-Za-z0-9\-\.\!\#\%\&\(\)\<\>]``

:guilabel:`messages`
   ``object`` is an array ob objects that holds the data of the message. Object consists of 3 properties:
   **[destination]** (the cell’s number (without leading zeros or + sign), for example for Greece: 306912345678),
   **[message]** (the message’s text)
   and the :ref:`[value_tokens] object`

:guilabel:`sendon`
   ``(optional) - unsigned integer`` an optional scheduling parameter. You can define a future datetime a message to be sent.
   This variable is a type of unsigned integer - unix timestamp. You can find more reference on
   https://dev.mysql.com/doc/refman/5.5/en/date-and-time-functions.html#function_unix-timestamp
   That is, in case you want to send the message on 2016-07-06 12:17:45 you must provide the value 1467796665

:guilabel:`pricecat`
   ``(optional) - unsigned integer`` by setting that parameter you can choose between normal and low cost price category (where applicable).
   Set 1 in case you want to send the message with low cost, or ignore it or set the value to 0, in case you want to send with normal cost

:guilabel:`forms`
   ``object`` an object that has form data. Please read `[forms] object`_


[value_tokens] object
---------------------

[value_tokens] object contains **key/values** with URL parameter name and its value to set for each SMS sent to the recipient.
For example, for the below URL:

``?name=<USERNAME_VALUE_TOKEN>&enabled=<ISENABLED_VALUE_TOKEN>&campaign_source=email``

for a **specific** destination, we would have the following JSON object:

.. code:: json

   {
      "destination": "3069XXXXXXXX",
      "message": "Test message A. In order to consent, tap on the following link {%form_link_token}",
      "value_tokens": {
         "USERNAME_VALUE_TOKEN": "Mike",
         "ISENABLED_VALUE_TOKEN": "true"
      }
   }

meaning that, [**value_tokens**] object will have as many entries as the parameters that must have different value for each destination.
In the above example the URI query has 3 parameters, but we need to have different values only on 2 of them, since the 1 is static


[forms] object
--------------

[forms] object currently contains a property called [actual_url]. Its data type is a ``string`` and it holds the actual URL of the form.
This URL will be shortened by our **internal shortener system** - will shorten the URL part that **does not** contain the URL parameters.

.. code-block:: flatline
   :caption: How is the long URL with its parameters being shortened
   :emphasize-lines: 2,5,8

   1. Long URL:
   https://forms.onlineformsservice.example/myforms/get/?mysoid={SOMEID_VAL_TOKEN}#23

   2. Part of the URL to be shortened
   https://forms.onlineformsservice.example/myforms/get/

   3. Short URL with all the parameters
   https://lval.eu/XXX?mysoid={SOMEID_VAL_TOKEN}#23

.. code-block:: flatline
   :caption: How the tokens are replaced 
   :emphasize-lines: 2

   For a destination for example with SOMEID_VAL_TOKEN=ZTq9Jzj8LH, the final URL would be:
   https://lval.eu/1?mysoid=ZTq9Jzj8LH#23

As you can see in the :ref:`JSON object example`, there is a token: ``{SOMEID_VAL_TOKEN}`` which that will be replaced by the
``SOMEID_VAL_TOKEN`` value of the ``value_tokens`` key/value object and have a different value for each destination.

Responses and response properties
---------------------------------
The same applies as on the :doc:`sendjsms` reference


.. _`your account’s page`: https://www.liveall.eu/user
