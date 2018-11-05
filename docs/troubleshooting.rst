Troubleshooting
===============

 
How to check a read of DRM registers
------------------------------------

You can do a basic check on read DRM register callbacks by reading the known value of HDK version register of the DRM controller.

This can be done using the read/write callback functions :

   * write value 0x0 to register at offset 0x0 : this will set the register page number to the Page 0 of registers
   * read value from register at offset 0x68 : this correspond to the version register, it will contain the version of the HDK used to integrate the DRM controller. For version 2.3.0 of the HDK this register will contain value 0x20300.


How to check the correct license duration on Metering mode
----------------------------------------------------------

To be sure that the license duration is in line with the frequency applied in your design:

   * launch your FPGA accelerator: (imply to do a metering auto_start_session (MeteringSessionManager class))
   * just after, disconnect the network. By consequence, the next license will not be provided to the Hardware.
   * check that the FPGA accelerator is locked after 2x the license duration (at the session begin, 2 licenses are applied, so the first license duration is 2x the license duration)
   * if the duration is not correct, please check the frequency applied to the DRM Controller clock (DRM_aCLK)

If the duration is still not correct, you can contact Accelize support: `support@accelize.com <mailto:support@accelize.com>`_
