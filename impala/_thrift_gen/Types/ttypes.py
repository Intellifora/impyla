#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TPrimitiveType(object):
  INVALID_TYPE = 0
  NULL_TYPE = 1
  BOOLEAN = 2
  TINYINT = 3
  SMALLINT = 4
  INT = 5
  BIGINT = 6
  FLOAT = 7
  DOUBLE = 8
  DATE = 9
  DATETIME = 10
  TIMESTAMP = 11
  STRING = 12
  BINARY = 13
  DECIMAL = 14
  CHAR = 15
  VARCHAR = 16

  _VALUES_TO_NAMES = {
    0: "INVALID_TYPE",
    1: "NULL_TYPE",
    2: "BOOLEAN",
    3: "TINYINT",
    4: "SMALLINT",
    5: "INT",
    6: "BIGINT",
    7: "FLOAT",
    8: "DOUBLE",
    9: "DATE",
    10: "DATETIME",
    11: "TIMESTAMP",
    12: "STRING",
    13: "BINARY",
    14: "DECIMAL",
    15: "CHAR",
    16: "VARCHAR",
  }

  _NAMES_TO_VALUES = {
    "INVALID_TYPE": 0,
    "NULL_TYPE": 1,
    "BOOLEAN": 2,
    "TINYINT": 3,
    "SMALLINT": 4,
    "INT": 5,
    "BIGINT": 6,
    "FLOAT": 7,
    "DOUBLE": 8,
    "DATE": 9,
    "DATETIME": 10,
    "TIMESTAMP": 11,
    "STRING": 12,
    "BINARY": 13,
    "DECIMAL": 14,
    "CHAR": 15,
    "VARCHAR": 16,
  }

class TTypeNodeType(object):
  SCALAR = 0
  ARRAY = 1
  MAP = 2
  STRUCT = 3

  _VALUES_TO_NAMES = {
    0: "SCALAR",
    1: "ARRAY",
    2: "MAP",
    3: "STRUCT",
  }

  _NAMES_TO_VALUES = {
    "SCALAR": 0,
    "ARRAY": 1,
    "MAP": 2,
    "STRUCT": 3,
  }

class TStmtType(object):
  QUERY = 0
  DDL = 1
  DML = 2
  EXPLAIN = 3
  LOAD = 4
  SET = 5

  _VALUES_TO_NAMES = {
    0: "QUERY",
    1: "DDL",
    2: "DML",
    3: "EXPLAIN",
    4: "LOAD",
    5: "SET",
  }

  _NAMES_TO_VALUES = {
    "QUERY": 0,
    "DDL": 1,
    "DML": 2,
    "EXPLAIN": 3,
    "LOAD": 4,
    "SET": 5,
  }

class TExplainLevel(object):
  MINIMAL = 0
  STANDARD = 1
  EXTENDED = 2
  VERBOSE = 3

  _VALUES_TO_NAMES = {
    0: "MINIMAL",
    1: "STANDARD",
    2: "EXTENDED",
    3: "VERBOSE",
  }

  _NAMES_TO_VALUES = {
    "MINIMAL": 0,
    "STANDARD": 1,
    "EXTENDED": 2,
    "VERBOSE": 3,
  }

class TFunctionType(object):
  SCALAR = 0
  AGGREGATE = 1

  _VALUES_TO_NAMES = {
    0: "SCALAR",
    1: "AGGREGATE",
  }

  _NAMES_TO_VALUES = {
    "SCALAR": 0,
    "AGGREGATE": 1,
  }

class TFunctionBinaryType(object):
  BUILTIN = 0
  HIVE = 1
  NATIVE = 2
  IR = 3

  _VALUES_TO_NAMES = {
    0: "BUILTIN",
    1: "HIVE",
    2: "NATIVE",
    3: "IR",
  }

  _NAMES_TO_VALUES = {
    "BUILTIN": 0,
    "HIVE": 1,
    "NATIVE": 2,
    "IR": 3,
  }


class TScalarType(object):
  """
  Attributes:
   - type
   - len
   - precision
   - scale
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.I32, 'len', None, None, ), # 2
    (3, TType.I32, 'precision', None, None, ), # 3
    (4, TType.I32, 'scale', None, None, ), # 4
  )

  def __init__(self, type=None, len=None, precision=None, scale=None,):
    self.type = type
    self.len = len
    self.precision = precision
    self.scale = scale

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.len = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.precision = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.scale = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TScalarType')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.len is not None:
      oprot.writeFieldBegin('len', TType.I32, 2)
      oprot.writeI32(self.len)
      oprot.writeFieldEnd()
    if self.precision is not None:
      oprot.writeFieldBegin('precision', TType.I32, 3)
      oprot.writeI32(self.precision)
      oprot.writeFieldEnd()
    if self.scale is not None:
      oprot.writeFieldBegin('scale', TType.I32, 4)
      oprot.writeI32(self.scale)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TStructField(object):
  """
  Attributes:
   - name
   - comment
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'comment', None, None, ), # 2
  )

  def __init__(self, name=None, comment=None,):
    self.name = name
    self.comment = comment

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.comment = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TStructField')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.comment is not None:
      oprot.writeFieldBegin('comment', TType.STRING, 2)
      oprot.writeString(self.comment)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TTypeNode(object):
  """
  Attributes:
   - type
   - scalar_type
   - struct_fields
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRUCT, 'scalar_type', (TScalarType, TScalarType.thrift_spec), None, ), # 2
    (3, TType.LIST, 'struct_fields', (TType.STRUCT,(TStructField, TStructField.thrift_spec)), None, ), # 3
  )

  def __init__(self, type=None, scalar_type=None, struct_fields=None,):
    self.type = type
    self.scalar_type = scalar_type
    self.struct_fields = struct_fields

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.scalar_type = TScalarType()
          self.scalar_type.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.struct_fields = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TStructField()
            _elem5.read(iprot)
            self.struct_fields.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TTypeNode')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.scalar_type is not None:
      oprot.writeFieldBegin('scalar_type', TType.STRUCT, 2)
      self.scalar_type.write(oprot)
      oprot.writeFieldEnd()
    if self.struct_fields is not None:
      oprot.writeFieldBegin('struct_fields', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.struct_fields))
      for iter6 in self.struct_fields:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TColumnType(object):
  """
  Attributes:
   - types
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'types', (TType.STRUCT,(TTypeNode, TTypeNode.thrift_spec)), None, ), # 1
  )

  def __init__(self, types=None,):
    self.types = types

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.types = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = TTypeNode()
            _elem12.read(iprot)
            self.types.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TColumnType')
    if self.types is not None:
      oprot.writeFieldBegin('types', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.types))
      for iter13 in self.types:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TNetworkAddress(object):
  """
  Attributes:
   - hostname
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'hostname', None, None, ), # 1
    (2, TType.I32, 'port', None, None, ), # 2
  )

  def __init__(self, hostname=None, port=None,):
    self.hostname = hostname
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.hostname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TNetworkAddress')
    if self.hostname is not None:
      oprot.writeFieldBegin('hostname', TType.STRING, 1)
      oprot.writeString(self.hostname)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 2)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.hostname is None:
      raise TProtocol.TProtocolException(message='Required field hostname is unset!')
    if self.port is None:
      raise TProtocol.TProtocolException(message='Required field port is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TUniqueId(object):
  """
  Attributes:
   - hi
   - lo
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'hi', None, None, ), # 1
    (2, TType.I64, 'lo', None, None, ), # 2
  )

  def __init__(self, hi=None, lo=None,):
    self.hi = hi
    self.lo = lo

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.hi = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.lo = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TUniqueId')
    if self.hi is not None:
      oprot.writeFieldBegin('hi', TType.I64, 1)
      oprot.writeI64(self.hi)
      oprot.writeFieldEnd()
    if self.lo is not None:
      oprot.writeFieldBegin('lo', TType.I64, 2)
      oprot.writeI64(self.lo)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.hi is None:
      raise TProtocol.TProtocolException(message='Required field hi is unset!')
    if self.lo is None:
      raise TProtocol.TProtocolException(message='Required field lo is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TFunctionName(object):
  """
  Attributes:
   - db_name
   - function_name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'db_name', None, None, ), # 1
    (2, TType.STRING, 'function_name', None, None, ), # 2
  )

  def __init__(self, db_name=None, function_name=None,):
    self.db_name = db_name
    self.function_name = function_name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.db_name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.function_name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TFunctionName')
    if self.db_name is not None:
      oprot.writeFieldBegin('db_name', TType.STRING, 1)
      oprot.writeString(self.db_name)
      oprot.writeFieldEnd()
    if self.function_name is not None:
      oprot.writeFieldBegin('function_name', TType.STRING, 2)
      oprot.writeString(self.function_name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.function_name is None:
      raise TProtocol.TProtocolException(message='Required field function_name is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TScalarFunction(object):
  """
  Attributes:
   - symbol
   - prepare_fn_symbol
   - close_fn_symbol
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'symbol', None, None, ), # 1
    (2, TType.STRING, 'prepare_fn_symbol', None, None, ), # 2
    (3, TType.STRING, 'close_fn_symbol', None, None, ), # 3
  )

  def __init__(self, symbol=None, prepare_fn_symbol=None, close_fn_symbol=None,):
    self.symbol = symbol
    self.prepare_fn_symbol = prepare_fn_symbol
    self.close_fn_symbol = close_fn_symbol

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.prepare_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.close_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TScalarFunction')
    if self.symbol is not None:
      oprot.writeFieldBegin('symbol', TType.STRING, 1)
      oprot.writeString(self.symbol)
      oprot.writeFieldEnd()
    if self.prepare_fn_symbol is not None:
      oprot.writeFieldBegin('prepare_fn_symbol', TType.STRING, 2)
      oprot.writeString(self.prepare_fn_symbol)
      oprot.writeFieldEnd()
    if self.close_fn_symbol is not None:
      oprot.writeFieldBegin('close_fn_symbol', TType.STRING, 3)
      oprot.writeString(self.close_fn_symbol)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.symbol is None:
      raise TProtocol.TProtocolException(message='Required field symbol is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TAggregateFunction(object):
  """
  Attributes:
   - intermediate_type
   - update_fn_symbol
   - init_fn_symbol
   - serialize_fn_symbol
   - merge_fn_symbol
   - finalize_fn_symbol
   - ignores_distinct
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'intermediate_type', (TColumnType, TColumnType.thrift_spec), None, ), # 1
    (2, TType.STRING, 'update_fn_symbol', None, None, ), # 2
    (3, TType.STRING, 'init_fn_symbol', None, None, ), # 3
    (4, TType.STRING, 'serialize_fn_symbol', None, None, ), # 4
    (5, TType.STRING, 'merge_fn_symbol', None, None, ), # 5
    (6, TType.STRING, 'finalize_fn_symbol', None, None, ), # 6
    (7, TType.BOOL, 'ignores_distinct', None, None, ), # 7
  )

  def __init__(self, intermediate_type=None, update_fn_symbol=None, init_fn_symbol=None, serialize_fn_symbol=None, merge_fn_symbol=None, finalize_fn_symbol=None, ignores_distinct=None,):
    self.intermediate_type = intermediate_type
    self.update_fn_symbol = update_fn_symbol
    self.init_fn_symbol = init_fn_symbol
    self.serialize_fn_symbol = serialize_fn_symbol
    self.merge_fn_symbol = merge_fn_symbol
    self.finalize_fn_symbol = finalize_fn_symbol
    self.ignores_distinct = ignores_distinct

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.intermediate_type = TColumnType()
          self.intermediate_type.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.update_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.init_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.serialize_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.merge_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.finalize_fn_symbol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.ignores_distinct = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TAggregateFunction')
    if self.intermediate_type is not None:
      oprot.writeFieldBegin('intermediate_type', TType.STRUCT, 1)
      self.intermediate_type.write(oprot)
      oprot.writeFieldEnd()
    if self.update_fn_symbol is not None:
      oprot.writeFieldBegin('update_fn_symbol', TType.STRING, 2)
      oprot.writeString(self.update_fn_symbol)
      oprot.writeFieldEnd()
    if self.init_fn_symbol is not None:
      oprot.writeFieldBegin('init_fn_symbol', TType.STRING, 3)
      oprot.writeString(self.init_fn_symbol)
      oprot.writeFieldEnd()
    if self.serialize_fn_symbol is not None:
      oprot.writeFieldBegin('serialize_fn_symbol', TType.STRING, 4)
      oprot.writeString(self.serialize_fn_symbol)
      oprot.writeFieldEnd()
    if self.merge_fn_symbol is not None:
      oprot.writeFieldBegin('merge_fn_symbol', TType.STRING, 5)
      oprot.writeString(self.merge_fn_symbol)
      oprot.writeFieldEnd()
    if self.finalize_fn_symbol is not None:
      oprot.writeFieldBegin('finalize_fn_symbol', TType.STRING, 6)
      oprot.writeString(self.finalize_fn_symbol)
      oprot.writeFieldEnd()
    if self.ignores_distinct is not None:
      oprot.writeFieldBegin('ignores_distinct', TType.BOOL, 7)
      oprot.writeBool(self.ignores_distinct)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.intermediate_type is None:
      raise TProtocol.TProtocolException(message='Required field intermediate_type is unset!')
    if self.update_fn_symbol is None:
      raise TProtocol.TProtocolException(message='Required field update_fn_symbol is unset!')
    if self.init_fn_symbol is None:
      raise TProtocol.TProtocolException(message='Required field init_fn_symbol is unset!')
    if self.merge_fn_symbol is None:
      raise TProtocol.TProtocolException(message='Required field merge_fn_symbol is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TFunction(object):
  """
  Attributes:
   - name
   - binary_type
   - arg_types
   - ret_type
   - has_var_args
   - comment
   - signature
   - hdfs_location
   - scalar_fn
   - aggregate_fn
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'name', (TFunctionName, TFunctionName.thrift_spec), None, ), # 1
    (2, TType.I32, 'binary_type', None, None, ), # 2
    (3, TType.LIST, 'arg_types', (TType.STRUCT,(TColumnType, TColumnType.thrift_spec)), None, ), # 3
    (4, TType.STRUCT, 'ret_type', (TColumnType, TColumnType.thrift_spec), None, ), # 4
    (5, TType.BOOL, 'has_var_args', None, None, ), # 5
    (6, TType.STRING, 'comment', None, None, ), # 6
    (7, TType.STRING, 'signature', None, None, ), # 7
    (8, TType.STRING, 'hdfs_location', None, None, ), # 8
    (9, TType.STRUCT, 'scalar_fn', (TScalarFunction, TScalarFunction.thrift_spec), None, ), # 9
    (10, TType.STRUCT, 'aggregate_fn', (TAggregateFunction, TAggregateFunction.thrift_spec), None, ), # 10
  )

  def __init__(self, name=None, binary_type=None, arg_types=None, ret_type=None, has_var_args=None, comment=None, signature=None, hdfs_location=None, scalar_fn=None, aggregate_fn=None,):
    self.name = name
    self.binary_type = binary_type
    self.arg_types = arg_types
    self.ret_type = ret_type
    self.has_var_args = has_var_args
    self.comment = comment
    self.signature = signature
    self.hdfs_location = hdfs_location
    self.scalar_fn = scalar_fn
    self.aggregate_fn = aggregate_fn

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.name = TFunctionName()
          self.name.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.binary_type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.arg_types = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = TColumnType()
            _elem19.read(iprot)
            self.arg_types.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.ret_type = TColumnType()
          self.ret_type.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.has_var_args = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.comment = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.signature = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.hdfs_location = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRUCT:
          self.scalar_fn = TScalarFunction()
          self.scalar_fn.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRUCT:
          self.aggregate_fn = TAggregateFunction()
          self.aggregate_fn.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TFunction')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRUCT, 1)
      self.name.write(oprot)
      oprot.writeFieldEnd()
    if self.binary_type is not None:
      oprot.writeFieldBegin('binary_type', TType.I32, 2)
      oprot.writeI32(self.binary_type)
      oprot.writeFieldEnd()
    if self.arg_types is not None:
      oprot.writeFieldBegin('arg_types', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.arg_types))
      for iter20 in self.arg_types:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ret_type is not None:
      oprot.writeFieldBegin('ret_type', TType.STRUCT, 4)
      self.ret_type.write(oprot)
      oprot.writeFieldEnd()
    if self.has_var_args is not None:
      oprot.writeFieldBegin('has_var_args', TType.BOOL, 5)
      oprot.writeBool(self.has_var_args)
      oprot.writeFieldEnd()
    if self.comment is not None:
      oprot.writeFieldBegin('comment', TType.STRING, 6)
      oprot.writeString(self.comment)
      oprot.writeFieldEnd()
    if self.signature is not None:
      oprot.writeFieldBegin('signature', TType.STRING, 7)
      oprot.writeString(self.signature)
      oprot.writeFieldEnd()
    if self.hdfs_location is not None:
      oprot.writeFieldBegin('hdfs_location', TType.STRING, 8)
      oprot.writeString(self.hdfs_location)
      oprot.writeFieldEnd()
    if self.scalar_fn is not None:
      oprot.writeFieldBegin('scalar_fn', TType.STRUCT, 9)
      self.scalar_fn.write(oprot)
      oprot.writeFieldEnd()
    if self.aggregate_fn is not None:
      oprot.writeFieldBegin('aggregate_fn', TType.STRUCT, 10)
      self.aggregate_fn.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    if self.binary_type is None:
      raise TProtocol.TProtocolException(message='Required field binary_type is unset!')
    if self.arg_types is None:
      raise TProtocol.TProtocolException(message='Required field arg_types is unset!')
    if self.ret_type is None:
      raise TProtocol.TProtocolException(message='Required field ret_type is unset!')
    if self.has_var_args is None:
      raise TProtocol.TProtocolException(message='Required field has_var_args is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)