 
Operation validation
====================

Create AccelStore account and access key
----------------------------------------

   *   Create a free account on AccelStore: https://accelstore.accelize.com/user/register
   *   Create an access key from your AccelStore account: https://accelstore.accelize.com/user/applications


Create cred.json
----------------

.. code-block:: json

   {
      "client_id": "## your client id from Accelstore ##",
      "client_secret": "## your client secret from Accelstore ##"
   }

Activation validation
----------------------

   * Start a design in default (metered/floating) DRM mode with valid credentials in the cred.json file
      * the design works fine and returns the following message
       
.. code-block:: bash

   [INFO] Starting metering session...
   [INFO] Started new metering session with sessionId A876FD1EDE47765B and set first license with duration of 15 seconds
   [INFO] Stopping metering session...
   [INFO] Stopped metering session with sessionId A876FD1EDE47765B and uploaded last metering data

|
   * Update the cred.json file with wrong credentials and restart the design in default DRM mode
      * the design must fail with the following error message:


.. code-block:: bash

   [INFO] Resuming metering session...
   [ERROR] WSOAuth HTTP response code : 401({"error": "invalid_client"}) [errCode=10002]
   Error auto_starting metering sessiona


Metering validation
-------------------


For each protected IP, depending on the pricing defined for this IP (say, C coins per D MB processed - please refer to :ref:`Metering Control` chapter for more information):

   * Stimulate the design so as to process an amount of data corresponding to an expected amount of coins as defined by your business rule (say, 10xD MB corresponding to 10xC coins)
   * Check the coins consumption on AccelStore: `https://accelstore.accelize.com/user/metering <https://accelstore.accelize.com/user/metering>`_

 

Optional: floating validation
-----------------------------

   * Contact Accelize and request 2 floating licenses
   * Run 2 instances of the fpga design in parallel to use the 2 floating licenses
      * the 2 instances must work fine
   * Run 3 instances of the fpga design in parallel

  * only 2 instances must work

 
Optional: node locked validation
--------------------------------


* Contact Accelize and request 1 node locked license
* Start the fpga design and use the node locked license
* Kill the SDK

  * the design must still run
