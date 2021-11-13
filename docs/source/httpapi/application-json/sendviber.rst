Send Viber messages
===================

.. figure:: ../../static/logo-viber_small1.png
   :alt: viber-icon-small

.. contents:: Contents
  :local:
  :backlinks: none

------------------------------------------------

Description
-----------

Viber endpoint makes the IM sendout convenient offering bulk messages transmission with a SMS fallback capability

------------------------------------------------

Endpoint URL
------------

.. code:: flatline

   https://sms.liveall.eu/apiext/Sendout/SendIM

------------------------------------------------

curl example
------------

.. code:: flatline

  curl --location --request POST 'https://sms.liveall.eu/apiext/Sendout/SendIM' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8",
    "senderid": "Liveall.eu",
    "sms_text": "my SMS text 2",
    "pricecat": 1,
    "im_type": "IM_SMSFB",
    "im_sender_name": "my viber sender name",
    "im_text": "1546 - This is a test Viber msg",
    "im_image_urls": [ "https://www.liveall.eu/sites/liveall.eu/files/lall-logo-by3.png" ],
    "im_actions": [{ "caption": "Visit Us", "url": "https://www.liveall.eu" }],
    "destinations": [
      "306912345678",
      "306923456789"
    ]
  }
  '

JSON Object variables
---------------------

:guilabel:`apitoken`
   ``string`` a unique hash code for each account that authorizes each web request. That code you can find it on `your account’s page`_

:guilabel:`im_type`
   ``string`` there are 2 options. **IM** for excplicit Viber sendout and **IM_SMSFB** in case you want to send a Viber message and if that number is invalid, then an SMS will be sent with an alternative body text (fallback option)

:guilabel:`im_sender_name`
   ``string`` the sender name of the Viber message (this will be defined and be enabled by us)

:guilabel:`im_text`
   ``string`` The Viber message (max 1000 characters)

:guilabel:`destinations`
   ``array of string`` an array of string that holds the cell numbers

:guilabel:`im_image_urls`
   ``(optional) - array of string`` an array of strings that holds the images to be included with Viber message
   
   .. rubric:: (WARNING!) - only one image is permited

:guilabel:`im_actions`
   | ``(optional) - array of object`` an array of objects with actions to be included on message. Every object has 2 properties.
   | i) caption: which is the text that will be displayed in action’s button and
   | ii) url: that holds the url of the action (when the recipient taps the action’s button he will be redirected to this ur - opened in phone’s browser).

   .. rubric:: (WARNING!) - Only one action is also permited for Viber

:guilabel:`senderid`
   ``(optional) - string`` if you defined **IM_SMSFB** as im_type, then you must set this option for SMS sender name

:guilabel:`pricecat`
   ``(optional) - integer`` (same as above) it is the price category for SMS. 0 or nothing for normal and 1 for low cost

:guilabel:`sms_text`
   ``(optional) - string`` (same as above) the text of the fallback SMS


------------------------------------------------

JSON object example (No SMS fallback)
-------------------------------------

.. code:: json

  {
    "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8",
    "im_type": "IM",
    "im_sender_name": "my viber sender name",
    "im_text": "1546 - This is a test Viber msg",
    "im_image_urls": [ "https://www.liveall.eu/sites/liveall.eu/files/lall-logo-by3.png" ],
    "im_actions": [{ "caption": "Visit Us", "url": "https://www.liveall.eu" }],
    "destinations": [
      "306912345678",
      "306923456789"
    ]
  }

------------------------------------------------

JSON object example (With SMS fallback)
---------------------------------------

.. code:: json

  {
    "apitoken": "7ace3e49cae13ae4f5ccb8a6a8a0d6a8fe120aa82ae46ad6ee4c9d8",
    "senderid": "Liveall.eu",
    "sms_text": "my SMS text 2",
    "pricecat": 1,
    "im_type": "IM_SMSFB",
    "im_sender_name": "my viber sender name",
    "im_text": "1546 - This is a test Viber msg",
    "im_image_urls": [ "https://www.liveall.eu/sites/liveall.eu/files/lall-logo-by3.png" ],
    "im_actions": [{ "caption": "Visit Us", "url": "https://www.liveall.eu" }],
    "destinations": [
      "306912345678",
      "306923456789"
    ]
  }

------------------------------------------------

Error Response
--------------

In case of error, we got something like the following:

.. code:: json

  {
      "success": false,
      "OperationErrors": [
          {
              "errorCode": 56,
              "errorMessage": "Sender id for IM is not approved",
              "SMSErrorType": 4,
              "valueOfError": ""
          }
      ],
      "SubmissionID": 0,
      "data": null
  }

------------------------------------------------

Successful Response
-------------------

.. code:: json

  {
      "success": true,
      "OperationErrors": null,
      "SubmissionID": 0,
      "data": [
          11271180,
          11271181
      ]
  }

------------------------------------------------

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
