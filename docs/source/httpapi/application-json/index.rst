JSON API (application/json API)
===================================

.. figure:: ../../static/httpapi-json.png
   :alt: httpapi-json-logo

This type of `Liveall.eu`_ API offers more flexibilty when using it, since you can easily and straight-forward send messages to many recipients
with a different text for each one. With advanced API type you can send SMS and Viber messages.

The ``Content-Type`` on the request headers is set to ``application/json`` and all the data structure is a text, representing a **JSON object**.
Likewise, the response is not a delimited string but a JSON object

.. toctree::
   :caption: Below are the available actions for this type of API
   :maxdepth: 1

   sendjsms
   sendjsms_with_form
   sendviber
   

.. _`Liveall.eu`: https://www.liveall.eu
