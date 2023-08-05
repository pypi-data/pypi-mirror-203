#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import codechecker_api_shared.ttypes

from thrift.transport import TTransport
all_structs = []


class HandshakeInformation(object):
    """
    Attributes:
     - requiresAuthentication
     - sessionStillActive
    """


    def __init__(self, requiresAuthentication=None, sessionStillActive=None,):
        self.requiresAuthentication = requiresAuthentication
        self.sessionStillActive = sessionStillActive

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.requiresAuthentication = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.sessionStillActive = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('HandshakeInformation')
        if self.requiresAuthentication is not None:
            oprot.writeFieldBegin('requiresAuthentication', TType.BOOL, 1)
            oprot.writeBool(self.requiresAuthentication)
            oprot.writeFieldEnd()
        if self.sessionStillActive is not None:
            oprot.writeFieldBegin('sessionStillActive', TType.BOOL, 2)
            oprot.writeBool(self.sessionStillActive)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthorisationList(object):
    """
    Attributes:
     - users
     - groups
    """


    def __init__(self, users=None, groups=None,):
        self.users = users
        self.groups = groups

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.users = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.users.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.groups = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.groups.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AuthorisationList')
        if self.users is not None:
            oprot.writeFieldBegin('users', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.users))
            for iter12 in self.users:
                oprot.writeString(iter12.encode('utf-8') if sys.version_info[0] == 2 else iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.groups is not None:
            oprot.writeFieldBegin('groups', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.groups))
            for iter13 in self.groups:
                oprot.writeString(iter13.encode('utf-8') if sys.version_info[0] == 2 else iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PermissionFilter(object):
    """
    Attributes:
     - given
     - canManage
    """


    def __init__(self, given=None, canManage=None,):
        self.given = given
        self.canManage = canManage

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.given = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.canManage = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('PermissionFilter')
        if self.given is not None:
            oprot.writeFieldBegin('given', TType.BOOL, 1)
            oprot.writeBool(self.given)
            oprot.writeFieldEnd()
        if self.canManage is not None:
            oprot.writeFieldBegin('canManage', TType.BOOL, 2)
            oprot.writeBool(self.canManage)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class SessionTokenData(object):
    """
    Attributes:
     - token
     - description
     - lastAccess
    """


    def __init__(self, token=None, description=None, lastAccess=None,):
        self.token = token
        self.description = description
        self.lastAccess = lastAccess

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.lastAccess = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('SessionTokenData')
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 1)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 2)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        if self.lastAccess is not None:
            oprot.writeFieldBegin('lastAccess', TType.STRING, 3)
            oprot.writeString(self.lastAccess.encode('utf-8') if sys.version_info[0] == 2 else self.lastAccess)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Permissions(object):
    """
    Attributes:
     - user
     - group
    """


    def __init__(self, user=None, group=None,):
        self.user = user
        self.group = group

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.MAP:
                    self.user = {}
                    (_ktype15, _vtype16, _size14) = iprot.readMapBegin()
                    for _i18 in range(_size14):
                        _key19 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val20 = []
                        (_etype24, _size21) = iprot.readListBegin()
                        for _i25 in range(_size21):
                            _elem26 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                            _val20.append(_elem26)
                        iprot.readListEnd()
                        self.user[_key19] = _val20
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.group = {}
                    (_ktype28, _vtype29, _size27) = iprot.readMapBegin()
                    for _i31 in range(_size27):
                        _key32 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val33 = []
                        (_etype37, _size34) = iprot.readListBegin()
                        for _i38 in range(_size34):
                            _elem39 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                            _val33.append(_elem39)
                        iprot.readListEnd()
                        self.group[_key32] = _val33
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Permissions')
        if self.user is not None:
            oprot.writeFieldBegin('user', TType.MAP, 1)
            oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.user))
            for kiter40, viter41 in self.user.items():
                oprot.writeString(kiter40.encode('utf-8') if sys.version_info[0] == 2 else kiter40)
                oprot.writeListBegin(TType.STRING, len(viter41))
                for iter42 in viter41:
                    oprot.writeString(iter42.encode('utf-8') if sys.version_info[0] == 2 else iter42)
                oprot.writeListEnd()
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.group is not None:
            oprot.writeFieldBegin('group', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.group))
            for kiter43, viter44 in self.group.items():
                oprot.writeString(kiter43.encode('utf-8') if sys.version_info[0] == 2 else kiter43)
                oprot.writeListBegin(TType.STRING, len(viter44))
                for iter45 in viter44:
                    oprot.writeString(iter45.encode('utf-8') if sys.version_info[0] == 2 else iter45)
                oprot.writeListEnd()
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AccessControl(object):
    """
    Attributes:
     - globalPermissions
     - productPermissions
    """


    def __init__(self, globalPermissions=None, productPermissions=None,):
        self.globalPermissions = globalPermissions
        self.productPermissions = productPermissions

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.globalPermissions = Permissions()
                    self.globalPermissions.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.productPermissions = {}
                    (_ktype47, _vtype48, _size46) = iprot.readMapBegin()
                    for _i50 in range(_size46):
                        _key51 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val52 = Permissions()
                        _val52.read(iprot)
                        self.productPermissions[_key51] = _val52
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AccessControl')
        if self.globalPermissions is not None:
            oprot.writeFieldBegin('globalPermissions', TType.STRUCT, 1)
            self.globalPermissions.write(oprot)
            oprot.writeFieldEnd()
        if self.productPermissions is not None:
            oprot.writeFieldBegin('productPermissions', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.productPermissions))
            for kiter53, viter54 in self.productPermissions.items():
                oprot.writeString(kiter53.encode('utf-8') if sys.version_info[0] == 2 else kiter53)
                viter54.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(HandshakeInformation)
HandshakeInformation.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'requiresAuthentication', None, None, ),  # 1
    (2, TType.BOOL, 'sessionStillActive', None, None, ),  # 2
)
all_structs.append(AuthorisationList)
AuthorisationList.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'users', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.LIST, 'groups', (TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(PermissionFilter)
PermissionFilter.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'given', None, None, ),  # 1
    (2, TType.BOOL, 'canManage', None, None, ),  # 2
)
all_structs.append(SessionTokenData)
SessionTokenData.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'token', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'description', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'lastAccess', 'UTF8', None, ),  # 3
)
all_structs.append(Permissions)
Permissions.thrift_spec = (
    None,  # 0
    (1, TType.MAP, 'user', (TType.STRING, 'UTF8', TType.LIST, (TType.STRING, 'UTF8', False), False), None, ),  # 1
    (2, TType.MAP, 'group', (TType.STRING, 'UTF8', TType.LIST, (TType.STRING, 'UTF8', False), False), None, ),  # 2
)
all_structs.append(AccessControl)
AccessControl.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'globalPermissions', [Permissions, None], None, ),  # 1
    (2, TType.MAP, 'productPermissions', (TType.STRING, 'UTF8', TType.STRUCT, [Permissions, None], False), None, ),  # 2
)
fix_spec(all_structs)
del all_structs
