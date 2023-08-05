# -----------------------------------------------------------------------------
# Copyright (C) 2023 Naveen Alok
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------
#
# Author: Naveen Alok (naveenalok@gmail.com)
# Maintainer: Naveen Alok (naveenalok@gmail.com)
# Created: 15-04-2023
#
# -----------------------------------------------------------------------------

from gitpulse.GitDiff import GitDiff


def main():
    git_diff = GitDiff()
    git_diff.generate_report()


if __name__ == '__main__':
    main()
