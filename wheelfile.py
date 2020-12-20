# We do not target python2.
# Which python3 versions should we target? 3.6+ seems like a good idea.

from typing import List, IO
import zipfile


# Implements dict-style indices.
# Should ensure that the contents are always correct.
# Should rewrite itself to the zipfile on the fly? This would mean it has to
# take one, which might not be the best usecase for it.
# Meta-Version should not be changeable.
class PackageMeta:
    pass


# Implements dict-style indices.
# Should ensure that the contents are always correct.
# Should rewrite itself to the zipfile on the fly? This would mean it has to
# take one, which might not be the best usecase for it.
# Wheel-Version should not be changeable.
class WheelMeta:
    pass


# This should take a zipfile and write itself into it on each recalculation.
# Recalculation should be also done on __str__() or __bytes__().
# That way changing any file inside the zip will change the record on the fly.
class WheelRecord:
    # Argument name is a placeholder, come up with a better one.
    # What return type should this be?
    def hash_of(self, archive_filename) -> str:
        pass

    def _recalculate(self) -> None:
        pass


class WheelFile:
    # This should check if the zip name conforms to the wheel standard
    # Semantics to define for 'w' and 'a' modes:
    #   - the file does not exist, create a new empty one
    #   - the file exists, but is not a zip
    #   - the file exists, is a zip, but not a wheel
    #   - the file exists, is a wheel
    # Everything else should error out.
    # TODO: use ZipFile.testzip()
    def __init__(self) -> None:
        pass

    # This should take file objects too
    def add(self, path: str) -> None:
        pass

    # This should take file objects too
    # Change argnames to something better: "zip_path" does not carry the right
    # idea, "target_path" might be too descriptive.
    def extract(self, zip_path, target_path):
        pass

    # Adding metadata file from filesystem is one thing, it should also be
    # possible to add metadata from memory without FS acting as a middleman.
    # arcname argument maybe?
    def add_meta(self, filename: str) -> None:
        pass

    # Same as with add_meta, there should be a way to add from memory.
    # arcname argument maybe?
    def add_data(self, filename: str) -> None:
        pass

    # Argument name is lacking here.
    # Does this class even need this?
    # Might be better to provide WheelInfo objects, which would inherit from
    # ZipInfo but also cointain the hash from the RECORD. It would simplify the
    # whole implementation.
    # Having this method makes it possible to add comments to files.
    def getinfo(self, name: str) -> zipfile.ZipInfo:
        pass

    # Does this class even need this?
    def infolist(self) -> List[zipfile.ZipInfo]:
        pass

    # The name of this method comes from zipfile, but its... misleading.
    # It returns full paths from the archive tree. Not "names". Or is "name"
    # what you would call the archive path in PKZIP?
    def namelist(self) -> List[str]:
        pass

    # Do we actually want to have the open → close semantics?
    # Open → close semantics might be required in order to ensure a given file
    # comes last in the binary representation.
    # This should do a final recalculation of RECORD
    def close(self) -> None:
        pass

    @property
    def closed(self) -> bool:
        pass

    # Might not be needed. There's no good usecase for it, and ensuring RECORD
    # is valid becomes way harder.
    def open(self, path) -> IO:
        pass

    # This has little use when it returns bytes.
    # Might not be needed.
    def read(self, name) -> bytes:
        pass

    # Might not be needed. We have "add".
    def write(self) -> None:
        pass

    # This could be the replacement for "add from memory", a counterpart for
    # add().
    def writestr(self, arcname, data):
        pass

    # This makes it impossible to ensure that RECORD is valid. But without it,
    # the class is much less flexible.
    @property
    def zipfile(self) -> zipfile.ZipFile:
        pass

    # This name is kinda verbose and can still be conflated with
    # "package_metadata".
    @property
    def wheel_metadata(self) -> WheelMeta:
        pass

    # Too verbpose?
    # Maybe "pkg_info"?
    @property
    def package_metadata(self) -> PackageMeta:
        pass

    @property
    def record(self) -> WheelRecord:
        pass

    # TODO: properties for data that is included in the naming
    # TODO: compression level arguments - is compression even supported by Pip?
    # TODO: comment property
    # TODO: debug propery, as with ZipFile.debug

    raise NotImplementedError("Implement those below!")

    def __del__(self):
        raise NotImplementedError("Implement me!")
        self.close()

    def __enter__(self):
        raise NotImplementedError("Implement me!")

    def __exit__(self):
        raise NotImplementedError("Implement me!")
