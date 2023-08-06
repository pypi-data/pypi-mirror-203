from pyrogram.types import ForceReply
import asyncio
import logging

class errors:
   class timeout:
     code,text,cancel,unknown,alert,basic = 101,None,False,False,False,False 
     timeout = error = "[100] Time Out ..!"
   class cancel:
     code,text,timeout,unknown,alert,basic = 102,None,False,False,False,False 
     cancel = error = "[102] Listening cancelled...!"
   class unknown:
     code,text,timeout,cancel,alert,basic = 103,None,False,False,False,False 
     error = unknown = "[103] Unknown Error...!"
   class alert:
     code,text,timeout,cancel,unknown,basic = 104,None,False,False,False,False 
     error = alert = "[104] Expected a callback query...!"
   class basic:
      error = basic = "Parameter type Invalid check again...!"
      code,text,timeout,cancel,alert,unknown = 105,None,False,False,False,False
         
