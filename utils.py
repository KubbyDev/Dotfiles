from pathlib import Path
from typing import Dict


Aliases = Dict[str, str]


class Platform:

    def update_aliases(self, aliases: Aliases):
        pass

    def aliases_yaml_path(self) -> Path:
        pass
