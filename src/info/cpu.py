import time
from win32 import win32pdh

#Essentially an hack
def GetPerformanceAttributesSleep(object, counter, instance = None, inum=-1,
                             format = win32pdh.PDH_FMT_LONG, machine=None, interval=0.5):
    # NOTE: Many counters require 2 samples to give accurate results,
    # including "% Processor Time" (as by definition, at any instant, a
    # thread's CPU usage is either 0 or 100).  To read counters like this,
    # you should copy this function, but keep the counter open, and call
    # CollectQueryData() each time you need to know.
    # See http://support.microsoft.com/default.aspx?scid=kb;EN-US;q262938
    # and http://msdn.microsoft.com/library/en-us/dnperfmo/html/perfmonpt2.asp
    # My older explanation for this was that the "AddCounter" process forced
    # the CPU to 100%, but the above makes more sense :)
    path = win32pdh.MakeCounterPath( (machine,object,instance, None, inum,counter) )
    hq = win32pdh.OpenQuery()
    try:
        hc = win32pdh.AddCounter(hq, path)
        try:
            win32pdh.CollectQueryData(hq)
            time.sleep(interval)
            win32pdh.CollectQueryData(hq)
            type, val = win32pdh.GetFormattedCounterValue(hc, format)
            return val
        finally:
            win32pdh.RemoveCounter(hc)
    finally:
        win32pdh.CloseQuery(hq)

def createCounter(object, counter, instance = None, inum=-1,
                             format = win32pdh.PDH_FMT_LONG, machine=None):
    path = win32pdh.MakeCounterPath( (machine,object,instance, None, inum,counter) )
    hq = win32pdh.OpenQuery()

def GetPerformanceAttributesWithout(object, counter, instance = None, inum=-1,
                             format = win32pdh.PDH_FMT_LONG, machine=None, interval=0.5):
    # NOTE: Many counters require 2 samples to give accurate results,
    # including "% Processor Time" (as by definition, at any instant, a
    # thread's CPU usage is either 0 or 100).  To read counters like this,
    # you should copy this function, but keep the counter open, and call
    # CollectQueryData() each time you need to know.
    # See http://support.microsoft.com/default.aspx?scid=kb;EN-US;q262938
    # and http://msdn.microsoft.com/library/en-us/dnperfmo/html/perfmonpt2.asp
    # My older explanation for this was that the "AddCounter" process forced
    # the CPU to 100%, but the above makes more sense :)
    path = win32pdh.MakeCounterPath( (machine,object,instance, None, inum,counter) )
    hq = win32pdh.OpenQuery()
    try:
        hc = win32pdh.AddCounter(hq, path)
        try:
            win32pdh.CollectQueryData(hq)
            time.sleep(interval)
            win32pdh.CollectQueryData(hq)
            type, val = win32pdh.GetFormattedCounterValue(hc, format)
            return val
        finally:
            win32pdh.RemoveCounter(hc)
    finally:
        win32pdh.CloseQuery(hq)

def getRunningTotal():
    pass

def getTotal():
    return int(100 - GetPerformanceAttributesSleep("Processor(_Total)", "% Idle Time"))

def getNodeN(n):
    return int(100 - GetPerformanceAttributesSleep("Processor("+ str(int(n)) +")", "% Idle Time"))


