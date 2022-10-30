# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_jplephem', [dirname(__file__)])
        except ImportError:
            import _jplephem
            return _jplephem
        if fp is not None:
            try:
                _mod = imp.load_module('_jplephem', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _jplephem = swig_import_helper()
    del swig_import_helper
else:
    import _jplephem
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def set_ephemeris_dir(*args):
  return _jplephem.set_ephemeris_dir(*args)
set_ephemeris_dir = _jplephem.set_ephemeris_dir

def object_track(*args):
  return _jplephem.object_track(*args)
object_track = _jplephem.object_track

def object_doppler(*args):
  return _jplephem.object_doppler(*args)
object_doppler = _jplephem.object_doppler

def doppler_fraction(*args):
  return _jplephem.doppler_fraction(*args)
doppler_fraction = _jplephem.doppler_fraction

def observer_position_velocity(*args):
  return _jplephem.observer_position_velocity(*args)
observer_position_velocity = _jplephem.observer_position_velocity

def pulse_delay(*args):
  return _jplephem.pulse_delay(*args)
pulse_delay = _jplephem.pulse_delay

def utc_to_tdb(*args):
  return _jplephem.utc_to_tdb(*args)
utc_to_tdb = _jplephem.utc_to_tdb

def utc_to_last(*args):
  return _jplephem.utc_to_last(*args)
utc_to_last = _jplephem.utc_to_last

def last_to_utc(*args):
  return _jplephem.last_to_utc(*args)
last_to_utc = _jplephem.last_to_utc

def epoch_to_j2000(*args):
  return _jplephem.epoch_to_j2000(*args)
epoch_to_j2000 = _jplephem.epoch_to_j2000

def j2000_to_epoch(*args):
  return _jplephem.j2000_to_epoch(*args)
j2000_to_epoch = _jplephem.j2000_to_epoch

def add_aberration(*args):
  return _jplephem.add_aberration(*args)
add_aberration = _jplephem.add_aberration

def remove_aberration(*args):
  return _jplephem.remove_aberration(*args)
remove_aberration = _jplephem.remove_aberration

def set_observer_coordinates(*args):
  return _jplephem.set_observer_coordinates(*args)
set_observer_coordinates = _jplephem.set_observer_coordinates

def geocentric_observer_track(*args):
  return _jplephem.geocentric_observer_track(*args)
geocentric_observer_track = _jplephem.geocentric_observer_track

def barycentric_observer_track(*args):
  return _jplephem.barycentric_observer_track(*args)
barycentric_observer_track = _jplephem.barycentric_observer_track

def barycentric_earth_track(*args):
  return _jplephem.barycentric_earth_track(*args)
barycentric_earth_track = _jplephem.barycentric_earth_track

def barycentric_object_track(*args):
  return _jplephem.barycentric_object_track(*args)
barycentric_object_track = _jplephem.barycentric_object_track
# This file is compatible with both classic and new-style classes.


