# ------------------------------------------------------------------------------
#  es7s/core
#  (c) 2022-2023 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import io
import os

import pkg_resources

from .path import RESOURCE_DIR
from .. import APP_NAME


class DemoText:
    @classmethod
    def open(cls) -> io.StringIO:
        return io.StringIO(
            pkg_resources.resource_string(
                APP_NAME, os.path.join(RESOURCE_DIR, "demo-text.txt")
            ).decode()
        )

