import pathlib

import piig
import piig.examples.vicecenter

from piig import function
from piig import ptest


test_vice_center = piig.ptest.example_compare(piig.examples.vicecenter.vicecenter)
