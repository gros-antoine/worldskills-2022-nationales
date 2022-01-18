# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from test/IMU.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class IMU(genpy.Message):
  _md5sum = "b6894b4d9810ae1193e5899d0d32ce57"
  _type = "test/IMU"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 angle_x
float32 angle_y
float32 angle_z
float32 gyr_x
float32 gyr_y
float32 gyr_z
float32 acc_x
float32 acc_y
float32 acc_z
"""
  __slots__ = ['angle_x','angle_y','angle_z','gyr_x','gyr_y','gyr_z','acc_x','acc_y','acc_z']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       angle_x,angle_y,angle_z,gyr_x,gyr_y,gyr_z,acc_x,acc_y,acc_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(IMU, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.angle_x is None:
        self.angle_x = 0.
      if self.angle_y is None:
        self.angle_y = 0.
      if self.angle_z is None:
        self.angle_z = 0.
      if self.gyr_x is None:
        self.gyr_x = 0.
      if self.gyr_y is None:
        self.gyr_y = 0.
      if self.gyr_z is None:
        self.gyr_z = 0.
      if self.acc_x is None:
        self.acc_x = 0.
      if self.acc_y is None:
        self.acc_y = 0.
      if self.acc_z is None:
        self.acc_z = 0.
    else:
      self.angle_x = 0.
      self.angle_y = 0.
      self.angle_z = 0.
      self.gyr_x = 0.
      self.gyr_y = 0.
      self.gyr_z = 0.
      self.acc_x = 0.
      self.acc_y = 0.
      self.acc_z = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_9f().pack(_x.angle_x, _x.angle_y, _x.angle_z, _x.gyr_x, _x.gyr_y, _x.gyr_z, _x.acc_x, _x.acc_y, _x.acc_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 36
      (_x.angle_x, _x.angle_y, _x.angle_z, _x.gyr_x, _x.gyr_y, _x.gyr_z, _x.acc_x, _x.acc_y, _x.acc_z,) = _get_struct_9f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_9f().pack(_x.angle_x, _x.angle_y, _x.angle_z, _x.gyr_x, _x.gyr_y, _x.gyr_z, _x.acc_x, _x.acc_y, _x.acc_z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 36
      (_x.angle_x, _x.angle_y, _x.angle_z, _x.gyr_x, _x.gyr_y, _x.gyr_z, _x.acc_x, _x.acc_y, _x.acc_z,) = _get_struct_9f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_9f = None
def _get_struct_9f():
    global _struct_9f
    if _struct_9f is None:
        _struct_9f = struct.Struct("<9f")
    return _struct_9f
