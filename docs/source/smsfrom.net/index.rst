SMS from .net library
=====================

.. figure:: ../static/MS-.NET-framework2.png
   :alt: ms-net-framework-logo

.. contents:: Contents
  :local:
  :backlinks: none


The target framework of the library is the .Net Framework 4.8.

.. note:: Download the library from the following link: `Terracom.Liveall.ConnectorLib`_

**[Terracom.Liveall.ConnectorLib.Connector]** class is used to send your messages by calling the endpoint of the HTTP API, as described here: :doc:`../httpapi/application-json/sendjsms`

In order to use it, after downloading it, extract the file contents in your project and then add the 2 DLLs (Terracom.Liveall.ConnectorLib.dll & Newtonsoft.Json.dll) as references

.. seealso::
   |Add_reference|

To start with the class first you have to create an object with the new operator and invoke the Init() method by supplying it with the API access token and the sender name:

.. code:: csharp
   
   Connector sms_connector = new Connector();
   sms_connector.Init("YOUR_ACCOUNT_API_TOKEN", "SenderName");

Then we use either **SendSms()** or **SendSmsAsync()** to send in a synchronous or asynchronous way accordingly. There are also other helper methods we introduce below

---------------------------------------------------------

Connector.SendSmsAsync()
------------------------

.. code:: csharp

   //-------------------------------------------------------------------------------------
   /// FUNCTION PROTOTYPE
   public async Task<Models.OP_RESULT> SendSmsAsync(Models.HttpApiJSMSParts[] messages, int price_category = 0, DateTime? send_on = null);
   //-------------------------------------------------------------------------------------
   /// USAGE EXAMPLE
   #region ~~~~~~~~~~~~~~~~~~~~~~~~ TEST SMS SENDOUT ASYNC
   Models.OP_RESULT res = null;
   Task.Run(async () =>
   {
   res = await sms_connector.SendSmsAsync(
      new Models.HttpApiJSMSParts[] {
         new Models.HttpApiJSMSParts {
         destination = "306901234567",
         message = "Test message (async) - English. Δοκιμαστικό μήνυμα (Ελληνικά)"
      }
   });
   }).Wait();

   if (res.ErrorCode != SMS_SERVICE_ERROR_CODES.NO_ERROR)
      Console.WriteLine("Problem sending SMS. Error message: {0}", res.ErrorMessage);
   else
      Console.WriteLine("SMS sent sucessfully! SMSId for 1st sent message: {0}", res.SubmitInfo.FirstOrDefault().smsid);

   #endregion
   //-------------------------------------------------------------------------------------

This is the async version of the SMS sendout method. Below are the parameters and the result type

**Parameters**

:guilabel:`messages`
   ``Array`` of :hoverxref:`Models.HttpApiJSMSParts` that contains every destination/message pair to be sent

:guilabel:`price_category`
   ``(optional) - int`` it is the price category to use. Default value: 0. 1 for low-cost where applicable

:guilabel:`send_on`
   ``(optional) - DateTime?`` It is the DateTime for the SMS batch to be sent

**Return value**

Data type: :hoverxref:`Models.OP_RESULT`

---------------------------------------------------------

Connector.SendSms()
-------------------

.. code:: csharp

   //-------------------------------------------------------------------------------------
   /// FUNCTION PROTOTYPE
   public Models.OP_RESULT SendSms(Models.HttpApiJSMSParts[] messages, int price_category = 0, DateTime? send_on = null);
   //-------------------------------------------------------------------------------------
   /// USAGE EXAMPLE
   #region ~~~~~~~~~~~~~~~~~~~~~~~~ SYNC SMS SENDOUT
   Models.OP_RESULT res1 = sms_connector.SendSms(
      new Models.HttpApiJSMSParts[] {
         new Models.HttpApiJSMSParts {
         destination = "306901234567",
         message = "Test message (sync) - English. Δοκιμαστικό μήνυμα (Ελληνικά)"
      }
   });

   if (res1.ErrorCode != SMS_SERVICE_ERROR_CODES.NO_ERROR)
      Console.WriteLine("Problem sending SMS. Error message: {0}", res1.ErrorMessage);
   else
      Console.WriteLine("SMS sent sucessfully! SMSId for 1st sent message: {0}", res1.SubmitInfo.FirstOrDefault().smsid);
   
   #endregion
   //-------------------------------------------------------------------------------------

This is the sync version of the SMS sendout method. Below are the parameters and the result type

**Parameters**

:guilabel:`messages`
   ``Array`` of :hoverxref:`Models.HttpApiJSMSParts` that contains every destination/message pair to be sent

:guilabel:`price_category`
   ``(optional) - int`` it is the price category to use. Default value: 0. 1 for low-cost where applicable

:guilabel:`send_on`
   ``(optional) - DateTime?`` It is the DateTime for the SMS batch to be sent

**Return value**

Data type: :hoverxref:`Models.OP_RESULT`

---------------------------------------------------------

Connector.GetSMSHistoryAsync()
------------------------------

.. code:: csharp

   //-------------------------------------------------------------------------------------
   /// FUNCTION PROTOTYPE
   public async Task<Models.OP_RESULT_SMSLOG> GetSMSHistoryAsync(Models.SMSLogParameters parameters);
   //-------------------------------------------------------------------------------------
   /// USAGE EXAMPLE
   #region ~~~~~~~~~~~~~~~~~~~~~~~~ GET SMS HISTORY OF A SPECIFIC DATE
   Models.OP_RESULT_SMSLOG res = null;
   Task.Run(async () => {
      res = await sms_connector.GetSMSHistoryAsync(new Models.SMSLogParameters()
      {
         submit_date = "20200402",
         //timezone_offset = 2,
         //sms_id = 47680777,
      });
   }).Wait();

   if (res.ErrorCode == SMS_SERVICE_ERROR_CODES.NO_ERROR)
   {
      Console.WriteLine("Results\r\n\r\n" +
         "Sms id\t\tBatch id\tSender id\tDestination\tStatus DT\tStatus\t\tQty\t\tMsg charge\tIM Status\r\n" +
         "=========================================================================================================================================");

      foreach (var line in res.SMSLogRows)
      {
         Console.WriteLine($"{line.SMS_ID}\t{line.BatchID}\t\t{line.Sender_ID}\t{line.Destination}\t{line.LastStatusUnixDatetime}\t" +
            $"{line.StatusStr}\t{line.SMS_Qty}\t\t{line.MessageCharge}\t\t{line.InstantMessageStatusStr}");
      }
   }
   else
   {
      Console.WriteLine($"Problem while trying to fetch SMS log data: {res.ErrorCode} - {res.ErrorMessage}");
   }

   #endregion
   //-------------------------------------------------------------------------------------

Fetches the SMS history of a specific date. For more info see at :doc:`../httpapi/xwwwformurlencoded/getmessagelogforadate`

**Parameters**

:guilabel:`parameters`
   :hoverxref:`Models.SMSLogParameters` it contains all the available properties as parameters

**Return value**

Data type: :hoverxref:`Models.OP_RESULT_SMSLOG`

---------------------------------------------------------

Connector.GetSMSStatusAsync()
------------------------------

.. code:: csharp

   //-------------------------------------------------------------------------------------
   /// FUNCTION PROTOTYPE
   public async Task<Models.OP_RESULT_SMSSTAT> GetSMSStatusAsync(uint[] sms_ids);
   //-------------------------------------------------------------------------------------
   /// USAGE EXAMPLE
   #region ~~~~~~~~~~~~~~~~~~~~~~~~ GET SENT SMS STATUS BY ID
   Models.OP_RESULT_SMSSTAT res = null;
   Task.Run(async () => {
      res = await sms_connector.GetSMSStatusAsync(new uint[] { 99999998, 99999999 });
   }).Wait();

   if (res.ErrorCode == SMS_SERVICE_ERROR_CODES.NO_ERROR)
   {
      foreach (var sms_stat in res.StatusInfo)
      {
         Console.WriteLine($"sms_id: {sms_stat.sms_id}, recipient: {sms_stat.recipient}, " +
            $"last_status_time: {sms_stat.last_status_time}, status_code: {sms_stat.status_code}, " +
            $"ststus_txt: {sms_stat.status_txt}");
      }
   }
   else
   {
      Console.WriteLine($"Failed to get SMS status: {res.ErrorCode} - {res.ErrorMessage}");
   }

   #endregion
   //-------------------------------------------------------------------------------------

Gets the status of sent message(s) providing their sms_id(s) in array

**Parameters**

:guilabel:`sms_ids`
   ``Array on uint`` an array of the SMS IDs to be looked-up

**Return value**

Data type: :hoverxref:`Models.OP_RESULT_SMSSTAT`

---------------------------------------------------------


Connector.GetAccountBalanceAsync()
----------------------------------

.. code:: csharp

   //-------------------------------------------------------------------------------------
   /// FUNCTION PROTOTYPE
   public async Task<Models.OP_RESULT_ACCOUNT_INFO> GetAccountBalanceAsync(string countryprefix = null);
   //-------------------------------------------------------------------------------------
   /// USAGE EXAMPLE
   #region ~~~~~~~~~~~~~~~~~~~~~~~~ GET ACCOUNT BALANCE
   Models.OP_RESULT_ACCOUNT_INFO res = null;
   Task.Run(async () => {
      res = await sms_connector.GetAccountBalanceAsync("30");
   }).Wait();

   if (res.ErrorCode == SMS_SERVICE_ERROR_CODES.NO_ERROR)
      Console.WriteLine($"Balance: {res.AccountBalance.Balance}, SMS balance: {res.AccountBalance.SmsRemainCount}");
   else
      Console.WriteLine($"Problem when trying to get account info: {res.ErrorCode} - {res.ErrorMessage}");
   #endregion
   //-------------------------------------------------------------------------------------

| Gets various info about the account - currently this returns the current balance and the remaining SMS count
| GetAccountBalanceAsync() has an optional parameter (countryprefix). When this is provided, it can calculate the remaining SMS count - for the provided country, otherwise only the balance is returned.
| For example if you provide 30, it will return the remaining SMS for Greece

**Parameters**

:guilabel:`countryprefix`
   ``string`` this is the country prefix to calculate the remaining SMS for the specified country

**Return value**

Data type: :hoverxref:`Models.OP_RESULT_ACCOUNT_INFO`

---------------------------------------------------------

Send SMS with VB.NET
--------------------

Library can also be used by VB.NET. There is an example below that demonstrates the usage

.. code:: csharp

   Imports Terracom.Liveall.ConnectorLib

   Module Module1
      Sub Main()
            Dim sms_connector As New Connector()
            Dim res As Models.OP_RESULT
            Dim submit_info(1) As Models.HttpApiJSMSParts
            Dim si As New Models.HttpApiJSMSParts

            si.destination = "306912345678"
            si.message = "Test message - English. Δοκιμαστικό μήνυμα (Ελληνικά)"
            submit_info(0) = si

            sms_connector.Init("MY_VERY_SECRET_TOKEN", "mySenderID")
            res = sms_connector.SendSms(submit_info, 0)
            If res.ErrorCode <> SMS_SERVICE_ERROR_CODES.NO_ERROR Then
               Console.WriteLine("Problem sending SMS. Error message: {0}", res.ErrorMessage)
            Else
               Console.WriteLine("SMS sent sucessfully! SMSId for 1st sent message: {0}", res.SubmitInfo.FirstOrDefault().smsid)
            End If
      End Sub
   End Module

---------------------------------------------------------


APPENDIX - Classes
------------------


Models.OP_RESULT_BASE
^^^^^^^^^^^^^^^^^^^^^

.. code:: csharp

   public class OP_RESULT_BASE
   {
      public OP_RESULT_BASE()
      {
         ErrorCode = SMS_SERVICE_ERROR_CODES.NO_ERROR;
         ErrorMessage = null;
      }

      public SMS_SERVICE_ERROR_CODES ErrorCode { get; set; }
      public string ErrorMessage { get; set; }
   }

Models.OP_RESULT
^^^^^^^^^^^^^^^^

.. code:: csharp

   public class OP_RESULT : OP_RESULT_BASE
   {
      public OP_RESULT()
         :base()
      {
         SubmitInfo = null;
      }

      public SubmissionInfo[] SubmitInfo { get; set; }
   }



Models.SubmissionInfo
~~~~~~~~~~~~~~~~~~~~~

.. code:: csharp

   public class SubmissionInfo
   {
      public string destination { get; set; }
      public uint smsid { get; set; }
   }


Models.OP_RESULT_SMSLOG
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: csharp

   public class OP_RESULT_SMSLOG : OP_RESULT_BASE
   {
      public OP_RESULT_SMSLOG()
         : base()
      {
      }

      public Models.SMSLogRow[] SMSLogRows { get; set; }
   }

Models.SMSLogRow
~~~~~~~~~~~~~~~~

.. code:: csharp

   public class SMSLogRow
   {
      public uint SMS_ID { get; set; }
      public uint BatchID { get; set; }
      public string Sender_ID { get; set; }
      public string Destination { get; set; }
      public uint LastStatusUnixDatetime { get; set; }
      public DateTime LastStatusDatetime { get; set; }
      public string StatusStr { get; set; }
      public int SMS_Qty { get; set; }
      public double MessageCharge { get; set; }
      public string InstantMessageStatusStr { get; set; }
   }


Models.OP_RESULT_SMSSTAT
^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: csharp

   public class OP_RESULT_SMSSTAT : OP_RESULT_BASE
   {
      public OP_RESULT_SMSSTAT()
         :base()
      {
      }

      public SmsStatusInfo[] StatusInfo { get; set; }
   }

Models.SmsStatusInfo
~~~~~~~~~~~~~~~~~~~~

.. code:: csharp

   public class SmsStatusInfo
   {
      public uint sms_id { get; set; }
      public DateTime submitted_on { get; set; }
      public DateTime last_status_time { get; set; }
      public string recipient { get; set; }
      public DLR_CODES status_code { get; set; }
      public string status_txt { get; set; }
      public int sms_qty { get; set; }
      public double charge_amount { get; set; }
   }


Models.OP_RESULT_ACCOUNT_INFO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: csharp

   public class OP_RESULT_ACCOUNT_INFO : OP_RESULT_BASE
   {
      public OP_RESULT_ACCOUNT_INFO()
         :base()
      {
      }

      public AccountBalanceInfo AccountBalance { get; set; }
   }


Models.AccountBalanceInfo
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: csharp

   public class AccountBalanceInfo
   {
      public double Balance { get; set; }
      public int SmsRemainCount { get; set; }
      public int LCSmsRemainCount { get; set; }
   }


Models.HttpApiJSMSParts
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: csharp

   public class HttpApiJSMSParts
   {
      public string destination { get; set; }
      public string message { get; set; }
   }


Models.SMSLogParameters
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: csharp

   public class SMSLogParameters
   {
      public string submit_date { get; set; }
      public int? timezone_offset { get; set; }
      public string senderid { get; set; }
      public string destination { get; set; }
      public uint sms_id { get; set; }
      public uint batch_id { get; set; }
      public uint gt_sms_id { get; set; }
   }


Error Codes
^^^^^^^^^^^

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



.. |Add_reference| raw:: html
   
   <a href="https://msdn.microsoft.com/en-us/library/wkze6zky.aspx" target="_blank">How to: Add or Remove References By Using the Add Reference Dialog Box</a>


.. _`Terracom.Liveall.ConnectorLib`: https://www.liveall.eu/download/Terracom.Liveall.ConnectorLib_1.0.9.zip
