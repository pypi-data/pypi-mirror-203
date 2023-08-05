#  Copyright (c) 2017-2023 Reveal Energy Services, Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License"); 
#  you may not use this file except in compliance with the License. 
#  You may obtain a copy of the License at 
#
#      http://www.apache.org/licenses/LICENSE-2.0 
#
#  Unless required by applicable law or agreed to in writing, software 
#  distributed under the License is distributed on an "AS IS" BASIS, 
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
#  See the License for the specific language governing permissions and 
#  limitations under the License. 
#
# This file is part of Orchid and related technologies.
#

import pathlib

import packaging.version as pv


def api_version():
    """
    Calculate the Python API version.

    Returns:
        The Python API version read from the `VERSION` file.
    """
    with pathlib.Path(__file__).parent.joinpath('VERSION').open() as version_file:
        text_version = version_file.read()
        result = pv.parse(text_version)
        return result
