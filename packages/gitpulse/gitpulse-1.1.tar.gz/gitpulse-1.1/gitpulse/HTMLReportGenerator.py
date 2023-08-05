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

import json
from jinja2 import Environment, FileSystemLoader


class GitHTMLReportGenerator:
    def __init__(self, commits, merges):
        self.commits = commits
        self.merges = merges

    def generate(self, output_filename):
        self.template = "report.html"
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(self.template)

        developers = {}
        for commit in self.commits:
            author_email = commit['commit_details']['author_email']
            author_name = commit['commit_details']['author_name']
            if author_email not in developers:
                developers[author_email] = {
                    'name': author_name,
                    'email': author_email,
                    'num_commits': 0,
                    'num_merges': 0
                }
            developers[author_email]['num_commits'] += 1

        for merge in self.merges:
            author_email = merge['commit_details']['author_email']
            author_name = merge['commit_details']['author_name']
            if author_email not in developers:
                developers[author_email] = {
                    'name': author_name,
                    'email': author_email,
                    'num_commits': 0,
                    'num_merges': 0
                }
            developers[author_email]['num_merges'] += 1

        rendered_report = template.render(
            commits=self.commits,
            merges=self.merges,
            developers=list(developers.values())
        )

        with open(output_filename, 'w') as f:
            f.write(rendered_report)
