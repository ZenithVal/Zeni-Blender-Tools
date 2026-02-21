# operators/__init__.py

from . import ShapeKeysOps
from . import ModelOps

classes = (
    ShapeKeysOps.classes
    + ModelOps.classes
    #+ lorum ipsum.classes
)
