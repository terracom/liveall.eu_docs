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
   ``Array`` of `Models.HttpApiJSMSParts`_ that contains every destination/message pair to be sent

:guilabel:`price_category`
   ``(optional) - int`` it is the price category to use. Default value: 0. 1 for low-cost where applicable

:guilabel:`send_on`
   ``(optional) - DateTime?`` It is the DateTime for the SMS batch to be sent

**Return value**

Data type: `Models.OP_RESULT`_

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
   ``Array`` of `Models.HttpApiJSMSParts`_ that contains every destination/message pair to be sent

:guilabel:`price_category`
   ``(optional) - int`` it is the price category to use. Default value: 0. 1 for low-cost where applicable

:guilabel:`send_on`
   ``(optional) - DateTime?`` It is the DateTime for the SMS batch to be sent

**Return value**

Data type: `Models.OP_RESULT`_

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
   `Models.SMSLogParameters`_ it contains all the available properties as parameters

**Return value**

Data type: `Models.OP_RESULT_SMSLOG`_

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

Data type: `Models.OP_RESULT_SMSSTAT`_

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

Data type: :hoverxref:`OP_RESULT_ACCOUNT_INFO <index:Models.OP_RESULT_ACCOUNT_INFO>`


Data type2: :hoverxref:`OP_RESULT_ACCOUNT_INFO <Models.OP_RESULT_ACCOUNT_INFO>`

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

Error codes
^^^^^^^^^^^

Test 


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



.. |Add_reference| raw:: html
   
   <a href="https://msdn.microsoft.com/en-us/library/wkze6zky.aspx" target="_blank">How to: Add or Remove References By Using the Add Reference Dialog Box</a>


.. _`Terracom.Liveall.ConnectorLib`: https://www.liveall.eu/download/Terracom.Liveall.ConnectorLib_1.0.8.zip
