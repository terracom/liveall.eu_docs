Old API (obsolete)
==================
We maintain the old http api for backwards compatibility (there are no improvements on this api), because Liveall.eu has an ecosystem of 3rd party applications-sites that haven’t switched to our new API yet. Apart from that, old api does not provide security (if you use GET requests), because all parameters are on the url and not in the request’s body.
All newcomers to the service cannot use that API. They **must** use newer versions of API