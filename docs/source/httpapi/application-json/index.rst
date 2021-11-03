Advanced API (application/json API)
===================================

This type of API offers more flexibilty when using it, since you can easily and straight-forward send messages to many recipients
with a different text for each one. With advanced API type you can send SMS and Viber messages.

The ``Content-Type`` on the request headers is set to ``application/json`` and all the data structure is a text, representing a **JSON object**.
Likewise, the response is not a delimited string but a JSON object

.. toctree::
   :caption: Options
   :maxdepth: 1

   sendjsms
   