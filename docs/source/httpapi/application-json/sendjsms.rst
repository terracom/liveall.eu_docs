Send SMS
========

.. figure:: ../../static/Sms-icon-small.png
   :alt: sms-icon-small

.. contents:: Contents
  :local:
  :backlinks: none

------------------------------------------------

Description
-----------

Using that type of API gives you the flexibility to send to a single or multiple destinations SMS by calling the web-service once.
Also you are dealing with a JSON object (as a payload), which is much more straight-forward to a programer.

.. note:: you can send a different text to each destination as you may have noticed below

------------------------------------------------

Endpoint URL
------------

.. code:: flatline

   https://sms.liveall.eu/apiext/Sendout/SendJSMS

------------------------------------------------

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

------------------------------------------------

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

------------------------------------------------

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

For more details see the `APPENDIX`_

------------------------------------------------

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

------------------------------------------------

APPENDIX
--------

Response properties
^^^^^^^^^^^^^^^^^^^

=================== ===========
Name                Description
=================== ===========
**success**         when false, then no message sent and the whole request is considered failed
**OperationErrors** | when success is false, we get an array of objects with errors.
                    | Each object has 4 properties:
                    | **errorCode**: the error code (integer) of the error,
                    | **errorMessage**: the descriptive text of the error and
                    | **SMSErrorType**: this indicates the source of the problem (please see below)
                    | **valueOfError**: the value that caused the error (for debugging or troubleshooting purposes)
**data**            | in case of success, web-service is returning an array ob objects - 
                    | one for each destination, having 2 properties:
                    | **destination**: the cell’s number and
                    | **smsid**: the unique id of the SMS
=================== ===========


OperationErrors
^^^^^^^^^^^^^^^

This is an array with objects having the properties ``errorCode``, ``errorMessage``, ``SMSErrorType``, ``valueOfError``.
In case of success this object is null

.. tabs::

    .. tab:: errorCode
        :tabid: errCD

        .. code-block:: csharp

            public enum SMS_SERVICE_ERROR_CODES
            {
                NO_ERROR                            = 0,
                EMPTY_SENDERID                      = 1,
                INVALID_SENDERID                    = 2,
                UNAUTHORIZED_NUM_SENDER_ID          = 3,
                ALPHA_SENDERID_TOO_LONG             = 4,
                NUM_SENDERID_TOO_LONG               = 5,
                INTERR_NO_SMS_TYPE_PROV             = 6,
                INTERR_NO_SMS_TEXT                  = 7,
                INTERNAL_ERROR                      = 8,
                ILLEGAL_SENDERID                    = 9,
                SMS_TEXT_EMPTY                      = 10,
                SMS_TEXT_LEN_TOO_LONG               = 11,
                NO_DESTINATION_NUMBERS_PROVIDED     = 12,
                INVALID_DESTINATION_NUMBER          = 13,
                INVALID_GREEK_DEST_NUM              = 14,
                INVALID_CYPR_DEST_NUM               = 15,
                INVALID_ITALIAN_DEST_NUM            = 16,
                NOTFOUND_BUFFERED_BATCH_HEAD        = 17,
                INSUFFICIENT_USER_BALANCE           = 18,
                INTERR_COULDNT_FOUND_BUFFBATCH      = 19,
                INVALID_BATCHID_GIVEN               = 20,
                ERROR_CREATING_SMSLOGFILE           = 21,
                ERROR_WHEN_TRYING_TO_BLACKLIST      = 22,
                ERROR_ON_GETTING_CONTACTS           = 23,
                ERROR_NO_CONTACT_TO_DELETE          = 24,
                RECORD_ALREADY_EXISTS               = 25,
                RECORD_DOES_NOT_EXISTS              = 26,
                RECORD_CHANGE_FROM_DIFF_SESSION     = 27,
                PBOOK_CONTACT_CELL_EMPTY            = 28,
                PBOOK_CONTACT_NAME_EMPTY            = 29,
                PBOOK_INVLD_CELL                    = 30,
                PBOOKGRP_NO_GROUP_PRVD_TO_DEL       = 31,
                ACCSETT_EMPTY_SETTINGS              = 32,
                INVALID_IMPORT_FILE                 = 33,
                INSUFFICIENT_INVLD_PARAMETER_DATA   = 34,
                ERROR_IMPORTING_CONTACTS            = 35,
                INS_UPD_DUPLICATE_CELL_FOUND        = 36,
                NOT_ENOUGH_CREDITS_FOR_HLR_QUERY    = 37,
                ERROR_WHEN_TRYING_SUBMIT_USERHLR    = 38,
                API_TOKEN_NOT_PROVIDED              = 39,
                API_TOKEN_MISMATCH                  = 40,
                INVALID_SCHEDULED_SENDOUT_DATE      = 41,
                SMSIDS_PARAMETER_INVALID            = 42,
                NO_SUBMITTED_SMS_FOUND              = 43,
                INVALID_API_TOKEN                   = 44,
                VOUCHER_FROM_DIFFERENT_DOMAIN       = 45,
                VOUCHER_NOT_FOUND_OR_NON_FREE       = 46,
                VOUCHER_AMOUNT_CREDIT_FAILED        = 47,
                ERROR_UPDATING_CHARGED_VOUCHER      = 48,
                ERROR_DATA_NOT_FOUND                = 49,
                APITOKEN_USR_BELONGS_OTHER_MASTER   = 50,
                SUBACCOUNT_ALREADY_ASSIGNED         = 51,
                SENDERID_TOO_SHORT                  = 52,
                ERROR_CREATING_FILE                 = 53,
                IM_TEXT_EMPTY                       = 54,
                IM_TEXT_LONGER_THAN_EXPECTED        = 55,
                IM_SENDERID_NOT_APPROVED            = 56,
                IM_IMAGE_INVALID                    = 57,
                IM_ACTION_INVALID                   = 58,
                EMPTY_OR_INVALID_PARAMETERS         = 59,
                DATA_VERIFICATION_ERROR             = 60,
                SENDERID_INJ_NUMERIC_DETECTED       = 61,
                SMSFORM_NO_VALUETOKEN_FOUND         = 62,
                SMSFORM_NO_FORM_DATA_FOUND          = 63,
            }

    .. tab:: SMSErrorType
        :tabid: SMSErrType
        
        .. code-block:: csharp

            public enum SMS_INGRENTIENT_TYPES
            {
                SENDERID        = 1,
                TEXT            = 2,
                DESTINATION_NUM = 3,
                OTHER           = 4,
            }



.. _`your account’s page`: https://www.liveall.eu/user


