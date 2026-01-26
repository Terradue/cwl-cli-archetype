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

from cwl_cli_archetype import create_archetype
from pathlib import Path
from typing import List

import click

@click.command(context_settings={'show_default': True})
@click.option(
    '--clt-id',
    required=True,
    type=click.STRING,
    multiple=True,
    help="ID(s) of the CommandLineTool"
)
@click.option(
    "--target-dir",
    type=click.Path(
        path_type=Path
    ),
    required=True,
    help="The output directory path"
)
def main(
    clt_id: List[str],
    target_dir: Path
):
    create_archetype(clt_id, target_dir)
