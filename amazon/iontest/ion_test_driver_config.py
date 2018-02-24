# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at:
#
#    http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
import os

from amazon.iontest.ion_test_driver_util import IonBuild, NO_OP_BUILD, log_call

ION_TESTS_SOURCE = 'https://github.com/amzn/ion-tests.git'

# Tools expected to be present on the system. Key: name, value: path. Paths may be overridden using --<name>.
# Accordingly, if tool dependencies are added here, a corresponding option should be added to the CLI.
TOOL_DEPENDENCIES = {
    'cmake': 'cmake',
    'git': 'git'
}


def install_ion_c(log):
    log_call(log, (TOOL_DEPENDENCIES['cmake'], '-DCMAKE_BUILD_TYPE=Debug'))
    log_call(log, (TOOL_DEPENDENCIES['cmake'], '--build', '.'))


ION_BUILDS = {
    'ion-c': IonBuild(install_ion_c, os.path.join('tools', 'cli', 'ion')),
    'ion-tests': NO_OP_BUILD,
    # TODO add more implementations here
}

# Ion implementations hosted in Github. Local implementations may be tested using the `--implementation` argument,
# and should not be added here.
ION_IMPLEMENTATIONS = [
    'ion-c,/Users/greggt/Documents/workspace/ion-c,cli-integ-intnegzero-assertions',  # TODO -> amzn:master once cli is merged
    # TODO add more Ion implementations here
]