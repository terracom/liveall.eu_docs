FORM API (x-www-form-urlencoded API)
======================================

.. figure:: ../../static/httpapi.png
   :alt: httpapi-logo

This type of `Liveall.eu`_ API is based on the form x-www-form-urlencoded type of web-requests (**POST**) as described here: `POST HTTP - MDN Web Docs`_

The ``Content-Type`` on the request headers is set to ``application/x-www-form-urlencoded``

.. note::
   If you like to send multiple SMS with one request you are advised to use the **application/json** API, which offers more flexibility.

.. toctree::
   :caption: Actions
   :maxdepth: 1

   smssendout
   checksmsstatus
   checkaccountbalance
   getmessagelogforadate
   operationresultcodes



.. _`POST HTTP - MDN Web Docs`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST/
.. _`Liveall.eu`: https://www.liveall.eu
