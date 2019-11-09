from ctypes import *
import time


#Type redefine!
BOOL = c_int
DWORD = c_ulong
HANDLE = c_void_p
UINT = c_uint
CHAR = c_char_p
USHORT = c_ushort
LONG = c_long
INT = c_int

"""
#####################################################################################################################################################################################
#Open Device
#OpenDevice = self.rotationMotor.VCS_OpenDevice
#OpenDevice.argtypes = [CHAR, CHAR, CHAR, CHAR, POINTER(UINT)]
#OpenDevice.restype = HANDLE

#Communication Info
GetProtocolStackSettings = self.rotationMotor.VCS_GetProtocolStackSettings
GetProtocolStackSettings.argtypes = [HANDLE, POINTER(UINT), POINTER(UINT), POINTER(UINT)]
GetProtocolStackSettings.restype = BOOL

SetProtocolStackSettings = self.rotationMotor.VCS_SetProtocolStackSettings
SetProtocolStackSettings.argtypes = [HANDLE, UINT, UINT, POINTER(UINT)]
SetProtocolStackSettings.restype = BOOL

#Enable Motor
SetEnableState = self.rotationMotor.VCS_SetEnableState
SetEnableState.argtypes = [HANDLE, USHORT, POINTER(UINT)]
SetEnableState.restype = BOOL

GetEnableState = self.rotationMotor.VCS_GetEnableState
GetEnableState.argtypes = [HANDLE, USHORT, POINTER(BOOL), POINTER(UINT)]
GetEnableState.restype = BOOL

#Clear Fault
GetFaultState = self.rotationMotor.VCS_GetFaultState
GetFaultState.argtypes = [HANDLE, USHORT, POINTER(BOOL), POINTER(UINT)]
GetFaultState.restype = BOOL

ClearFault = self.rotationMotor.VCS_ClearFault
ClearFault.argtypes = [HANDLE, USHORT, POINTER(UINT)]
ClearFault.restype = BOOL

#Velocity Mode
MoveWithVelocity = self.rotationMotor.VCS_MoveWithVelocity
MoveWithVelocity.argtypes = [HANDLE, USHORT, LONG, POINTER(UINT)]
MoveWithVelocity.restype = BOOL

ActivateProfileVelocityMode = self.rotationMotor.VCS_ActivateProfileVelocityMode
ActivateProfileVelocityMode.argtypes = [HANDLE, USHORT, POINTER(UINT)]
ActivateProfileVelocityMode.restype = BOOL

HaltVelocityMovement = self.rotationMotor.VCS_HaltVelocityMovement
HaltVelocityMovement.argtypes = [HANDLE, USHORT, POINTER(UINT)]
HaltVelocityMovement.restype = BOOL

#Position Mode
ActivateProfilePositionMode = self.rotationMotor.VCS_ActivateProfilePositionMode
ActivateProfilePositionMode.argtypes = [HANDLE, USHORT, POINTER(UINT)]
ActivateProfilePositionMode.restype = BOOL

SetPositionProfile = self.rotationMotor.VCS_SetPositionProfile
SetPositionProfile.argtypes = [HANDLE, USHORT, UINT, UINT, UINT, POINTER(UINT)]
SetPositionProfile.restype = BOOL

MoveToPosition = self.rotationMotor.VCS_MoveToPosition
MoveToPosition.argtypes = [HANDLE, USHORT, LONG, INT, INT, POINTER(UINT)]
MoveToPosition.restype = BOOL

HaltPositionMovement = self.rotationMotor.VCS_HaltPositionMovement
HaltPositionMovement.argtypes = [HANDLE, USHORT, POINTER(UINT)]
HaltPositionMovement.restype = BOOL

#Max Speed
SetMaxProfileVelocity = self.rotationMotor.VCS_SetMaxProfileVelocity
SetMaxProfileVelocity.argtypes = [HANDLE, USHORT, UINT, POINTER(UINT)]
SetMaxProfileVelocity.restype = BOOL

#Motor Speed and Position Info
GetPosition = self.rotationMotor.VCS_GetPositionIs
GetPosition.argtypes = [HANDLE, USHORT, POINTER(INT), POINTER(UINT)]
GetPosition.restype = BOOL

GetVelocity = self.rotationMotor.VCS_GetVelocityIs
GetVelocity.argtypes = [HANDLE, USHORT, POINTER(INT), POINTER(UINT)]
GetVelocity.restype = BOOL

#Close Device
CloseDevice = self.rotationMotor.VCS_CloseDevice
CloseDevice.argtypes = [HANDLE, POINTER(UINT)]
CloseDevice.restype = BOOL

#Close All Device
CloseAllDevices = self.rotationMotor.VCS_CloseAllDevices
CloseAllDevices.argtypes = [POINTER(UINT)]
CloseAllDevices.restype = BOOL
"""


#####################################################################################################################################################################################
#Rotation Motor Class
class MaxonMotor(object):

    BOOL = c_int
    DWORD = c_ulong
    HANDLE = c_void_p
    UINT = c_uint
    CHAR = c_char_p
    USHORT = c_ushort
    LONG = c_long
    INT = c_int
    
    """rotation motor"""
    def __init__(self, RMNodeId, pDeviceName, pProtocolStackName, pInterfaceName, pPortName, lBaudrate):
        #Type redefine!
        
        self.RMNodeId = USHORT(RMNodeId)
        self.pDeviceName = CHAR(pDeviceName)
        self.pProtocolStackName = CHAR(pProtocolStackName)
        self.pInterfaceName = CHAR(pInterfaceName)
        self.pPortName = CHAR(pPortName)
        self.lBaudrate = UINT(lBaudrate)
        self.RMHandle = HANDLE(0)
        self.errorCode = UINT(0)
        self.lTimeout = UINT(0)

        #self.relativePosition = LONG(relativePosition)
        self.rmPosition = INT(0)
        self.rmVelosity = INT(0)

        self.rotationMotor = cdll.LoadLibrary("libEposCmd.so")

        #Open Device
        self.OpenDevice = self.rotationMotor.VCS_OpenDevice
        self.OpenDevice.argtypes = [CHAR, CHAR, CHAR, CHAR, POINTER(UINT)]
        self.OpenDevice.restype = HANDLE

        #Communication Info
        self.GetProtocolStackSettings = self.rotationMotor.VCS_GetProtocolStackSettings
        self.GetProtocolStackSettings.argtypes = [HANDLE, POINTER(UINT), POINTER(UINT), POINTER(UINT)]
        self.GetProtocolStackSettings.restype = BOOL

        self.SetProtocolStackSettings = self.rotationMotor.VCS_SetProtocolStackSettings
        self.SetProtocolStackSettings.argtypes = [HANDLE, UINT, UINT, POINTER(UINT)]
        self.SetProtocolStackSettings.restype = BOOL

        #Enable Motor
        self.SetEnableState = self.rotationMotor.VCS_SetEnableState
        self.SetEnableState.argtypes = [HANDLE, USHORT, POINTER(UINT)]
        self.SetEnableState.restype = BOOL

        self.GetEnableState = self.rotationMotor.VCS_GetEnableState
        self.GetEnableState.argtypes = [HANDLE, USHORT, POINTER(BOOL), POINTER(UINT)]
        self.GetEnableState.restype = BOOL

        #Clear Fault
        self.GetFaultState = self.rotationMotor.VCS_GetFaultState
        self.GetFaultState.argtypes = [HANDLE, USHORT, POINTER(BOOL), POINTER(UINT)]
        self.GetFaultState.restype = BOOL

        self.ClearFault = self.rotationMotor.VCS_ClearFault
        self.ClearFault.argtypes = [HANDLE, USHORT, POINTER(UINT)]
        self.ClearFault.restype = BOOL

        #Velocity Mode
        self.MoveWithVelocity = self.rotationMotor.VCS_MoveWithVelocity
        self.MoveWithVelocity.argtypes = [HANDLE, USHORT, LONG, POINTER(UINT)]
        self.MoveWithVelocity.restype = BOOL

        self.ActivateProfileVelocityMode = self.rotationMotor.VCS_ActivateProfileVelocityMode
        self.ActivateProfileVelocityMode.argtypes = [HANDLE, USHORT, POINTER(UINT)]
        self.ActivateProfileVelocityMode.restype = BOOL

        self.HaltVelocityMovement = self.rotationMotor.VCS_HaltVelocityMovement
        self.HaltVelocityMovement.argtypes = [HANDLE, USHORT, POINTER(UINT)]
        self.HaltVelocityMovement.restype = BOOL

        #Position Mode
        self.ActivateProfilePositionMode = self.rotationMotor.VCS_ActivateProfilePositionMode
        self.ActivateProfilePositionMode.argtypes = [HANDLE, USHORT, POINTER(UINT)]
        self.ActivateProfilePositionMode.restype = BOOL

        self.SetPositionProfile = self.rotationMotor.VCS_SetPositionProfile
        self.SetPositionProfile.argtypes = [HANDLE, USHORT, UINT, UINT, UINT, POINTER(UINT)]
        self.SetPositionProfile.restype = BOOL

        self.MoveToPosition = self.rotationMotor.VCS_MoveToPosition
        self.MoveToPosition.argtypes = [HANDLE, USHORT, LONG, INT, INT, POINTER(UINT)]
        self.MoveToPosition.restype = BOOL

        self.HaltPositionMovement = self.rotationMotor.VCS_HaltPositionMovement
        self.HaltPositionMovement.argtypes = [HANDLE, USHORT, POINTER(UINT)]
        self.HaltPositionMovement.restype = BOOL
        
        #Max Speed
        self.SetMaxProfileVelocity = self.rotationMotor.VCS_SetMaxProfileVelocity
        self.SetMaxProfileVelocity.argtypes = [HANDLE, USHORT, UINT, POINTER(UINT)]
        self.SetMaxProfileVelocity.restype = BOOL

        #Motor Speed and Position Info
        self.GetPosition = self.rotationMotor.VCS_GetPositionIs
        self.GetPosition.argtypes = [HANDLE, USHORT, POINTER(INT), POINTER(UINT)]
        self.GetPosition.restype = BOOL

        self.GetVelocity = self.rotationMotor.VCS_GetVelocityIs
        self.GetVelocity.argtypes = [HANDLE, USHORT, POINTER(INT), POINTER(UINT)]
        self.GetVelocity.restype = BOOL

        #Close Device
        self.CloseDevice = self.rotationMotor.VCS_CloseDevice
        self.CloseDevice.argtypes = [HANDLE, POINTER(UINT)]
        self.CloseDevice.restype = BOOL

        #Close All Device
        self.CloseAllDevices = self.rotationMotor.VCS_CloseAllDevices
        self.CloseAllDevices.argtypes = [POINTER(UINT)]
        self.CloseAllDevices.restype = BOOL
            
        self.open_device()
        
    
    #Open Device
    def open_device(self):
        Result = 0
        oIsFault = BOOL(0)
        oIsEnabled = BOOL(0)

        print "Open Device-----"
        self.RMHandle = self.OpenDevice(self.pDeviceName, self.pProtocolStackName, self.pInterfaceName, self.pPortName, byref(self.errorCode))
        #self.RMHandle = OpenDevice(CHAR(2), CHAR("EPOS2"), CHAR("MAXON SERIAL V2"), CHAR("USB"), CHAR("USB0"), byref(self.errorCode))

        print self.RMHandle, self.errorCode.value
        if self.max_speed() == 0:
           return Result

        self.ClearFault(self.RMHandle, self.RMNodeId, byref(self.errorCode))
        self.SetEnableState(self.RMHandle, self.RMNodeId, byref(self.errorCode))
        
        #Set Max Speed

##        
##        if self.RMHandle != 0 and self.errorCode.value == 0:
##            if self.GetProtocolStackSettings(self.RMHandle, byref(self.lBaudrate), byref(self.lTimeout), byref(self.errorCode)) != BOOL(0):
##                if self.SetProtocolStackSettings(self.RMHandle, self.lBaudrate, self.lTimeout, byref(self.errorCode)) != BOOL(0):
##                    if self.GetProtocolStackSettings(self.RMHandle, byref(self.lBaudrate), byref(self.lTimeout), byref(self.errorCode)) != BOOL(0):
##                        Result = 1
##        else:
##            self.RMHandle = HANDLE(0)
##        if self.GetFaultState(self.RMHandle, self.RMNodeId, byref(oIsFault), byref(self.errorCode)) == BOOL(0):
##            Result = 0
##        if Result:
##            if oIsFault != BOOL(0):
##                if self.ClearFault(self.RMHandle, self.RMNodeId, byref(self.errorCode)) == BOOL(0):
##                    Result = 0
##            if self.GetEnableState(self.RMHandle, self.RMNodeId, byref(oIsEnabled), byref(self.errorCode)) == BOOL(0):
##                Result = 0
##            if oIsEnabled == BOOL(0):
##                if self.SetEnableState(self.RMHandle, self.RMNodeId, byref(self.errorCode)) == BOOL(0):
##                    Result = 0

        
        return Result
        

    #Max Speed
    def max_speed(self):
        Result = 0
        if self.SetMaxProfileVelocity(self.RMHandle, self.RMNodeId, UINT(90), byref(self.errorCode)) != BOOL(0):
            Result = 1
        return Result

    #Position Mode
    def rm_move_to_position(self, positionModeSpeed, targetRelativePosition):
        Result = 1
#        positionModeSpeed = UINT(20)
        positionModeAcceleration = UINT(1000)
        positionModeDeceleration = UINT(1000)

        #self.ActivateProfileVelocityMode(self.RMHandle, self.RMNodeId, byref(self.errorCode))

        #self.MoveWithVelocity(self.RMHandle, self.RMNodeId, LONG(TargetVelocity), byref(self.errorCode))
        #time.sleep(1)

        self.ActivateProfilePositionMode(self.RMHandle, self.RMNodeId, byref(self.errorCode))
        self.SetPositionProfile(self.RMHandle, self.RMNodeId, UINT(positionModeSpeed), positionModeAcceleration, positionModeDeceleration, byref(self.errorCode))
        self.MoveToPosition(self.RMHandle, self.RMNodeId, LONG(targetRelativePosition), INT(0), INT(1), byref(self.errorCode))
        
        #if self.ActivateProfilePositionMode(self.RMHandle, self.RMNodeId, byref(self.errorCode)) != 0:
            #if self.SetPositionProfile(self.RMHandle, self.RMNodeId, positionModeSpeed, positionModeAcceleration, positionModeDeceleration, byref(self.errorCode)) != 0:
                #print self.SetPositionProfile(self.RMHandle, self.RMNodeId, positionModeSpeed, positionModeAcceleration, positionModeDeceleration, byref(self.errorCode))
                #Result = 0
                #print self.MoveToPosition(self.RMHandle, self.RMNodeId, LONG(targetRelativePosition), INT(0), INT(1), byref(self.errorCode))
                #time.sleep(3)
                #if self.MoveToPosition(self.RMHandle, self.RMNodeId, LONG(targetRelativePosition), INT(0), INT(1), byref(self.errorCode)) == 0:
                    #Result = 0
        return Result

    #Halt Position Mode
    def rm_halt_position_mode(self):
        Result = 1
        if self.HaltPositionMovement(self.RMHandle, self.RMNodeId, byref(self.errorCode)) == BOOL(0):
            Result = 0
        return Result

    #Get Position and Speed Info
    def rm_speed_and_position(self):
        Result = 0
        if self.GetPosition(self.RMHandle, self.RMNodeId, byref(self.rmPosition), byref(self.errorCode)) != BOOL(0):
            if self.GetVelocity(self.RMHandle, self.RMNodeId, byref(self.rmVelosity), byref(self.errorCode)) != BOOL(0):
                Result = 1
        return Result

    #Close Device
    def close_device(self):
        Result = 0
        if self.CloseDevice(self.RMHandle, byref(self.errorCode)) != BOOL(0):
            Result = 1
        return Result


    def rm_move(self, TargetVelocity):
        Result = 1
#        positionModeSpeed = UINT(20)
        positionModeAcceleration = UINT(1000)
        positionModeDeceleration = UINT(1000)
        self.ActivateProfileVelocityMode(self.RMHandle, self.RMNodeId, byref(self.errorCode))

        self.MoveWithVelocity(self.RMHandle, self.RMNodeId, LONG(TargetVelocity), byref(self.errorCode))
       
	#if self.ActivateProfilePositionMode(self.RMHandle, self.RMNodeId, byref(self.errorCode)) != 0:
            #if self.SetPositionProfile(self.RMHandle, self.RMNodeId, positionModeSpeed, positionModeAcceleration, positionModeDeceleration, byref(self.errorCode)) != 0:
                #print self.SetPositionProfile(self.RMHandle, self.RMNodeId, positionModeSpeed, positionModeAcceleration, positionModeDeceleration, byref(self.errorCode))
                #Result = 0
		#print self.MoveToPosition(self.RMHandle, self.RMNodeId, LONG(targetRelativePosition), INT(0), INT(1), byref(self.errorCode))
                #time.sleep(3)
                #if self.MoveToPosition(self.RMHandle, self.RMNodeId, LONG(targetRelativePosition), INT(0), INT(1), byref(self.errorCode)) == 0:
                    #Result = 0
        return Result        

##################################################################################################################################################################################

#test maxon motor to move on position mode
#guidewireRotateMotor = MaxonMotor(2, "EPOS2", "MAXON SERIAL V2", "USB", "USB0", 1000000)
#guidewireRotateMotor.rm_move_to_position(40,-8000)
#time.sleep(6)
#guidewireRotateMotor.close_device()

