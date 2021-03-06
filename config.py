import ConfigParser

class Config:
    "Configuration parser"

    def __init__(self, fname):
        self.parser = ConfigParser.ConfigParser()
        self.parser.read( fname )

        self.rpms = self._opt_break( "rpms" )
        self.local_rpms = self._opt_break( "local_rpms" )
        self.files = self._opt_break( "files" )
        self.exclude_paths = self._opt_break( "exclude_paths" )
        self.library_dirs = self._opt_break( "library_dirs" )
        self.path = self._opt_break( "path" )
        self.use_audit = self.parser.getboolean( "dynpk", "use_audit" )
        self.fakechroot_lib = self._get_opt_opt( "fakechroot_lib", "/usr/lib/fakechroot/libfakechroot.so" )

    def _opt_break(self, name):
        "Break up a space separated config option into a list"
        try:
            return self._break_up( self.parser.get( "dynpk", name ) )
        except ConfigParser.NoOptionError:
            return []

    def _break_up(self, s):
        "Break up a space separated string into a list"
        l = [x.strip() for x in s.split()]
        return l
        
    def _get_opt_opt(self, name, default):
        try:
            return self.parser.get( "dynpk", name )
        except ConfigParser.NoOptionError:
            return default
