# Copyright 2026 Terradue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from importlib.metadata import version, PackageNotFoundError
from jinja2 import Environment, PackageLoader
from pathlib import Path
from typing import Any, List, Mapping

import time


def _to_mapping(functions: List[Any]) -> Mapping[str, Any]:
    mapping: Mapping[str, Any] = {}

    for function in functions:
        mapping[function.__name__[1:]] = function

    return mapping


_jinja_environment = Environment(loader=PackageLoader(package_name="cwl_cli_archetype"))
_jinja_environment.filters.update(_to_mapping([]))
_jinja_environment.tests.update(_to_mapping([]))


def _get_version() -> str:
    try:
        return version("cwl_cli_archetype")
    except PackageNotFoundError:
        return "N/A"


def _serialize_template(
    clt_id: str, clt_ids: List[str], template_name: str, output_file: Path
):
    output_file.parent.mkdir(parents=True, exist_ok=True)

    template = _jinja_environment.get_template(template_name)

    with output_file.open("w") as output_stream:
        output_stream.write(
            template.render(
                version=_get_version(),
                timestamp=datetime.fromtimestamp(time.time()).isoformat(
                    timespec="milliseconds"
                ),
                clt_id=clt_id,
                clt_ids=clt_ids,
            )
        )


def create_archetype(clt_ids: List[str], target_dir: Path):
    _serialize_template(
        "", clt_ids, "clt.cwl", Path(target_dir, "cwl-workflow/clts.cwl")
    )

    for clt_id in clt_ids:
        _serialize_template(
            clt_id, clt_ids, "Dockerfile", Path(target_dir, f"{clt_id}/Dockerfile")
        )
