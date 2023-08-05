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

import os
import uuid
from .HTMLReportGenerator import GitHTMLReportGenerator


class DynamicHTMLReportGenerator(GitHTMLReportGenerator):
    def __init__(self):
        self.template = "report.html"
        self.template_string = """
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>GitPulse Report</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
                <style>
                    table.diff {border: 1px solid black; border-collapse: collapse; font-family: Consolas, "Courier New", monospace;}
                    td.diff {border: 1px solid black; padding: 2px;}
                </style>
            </head>
            <body>

            <div class="container mt-3">
                <h2>GitPulse</h2>
                <ul class="nav nav-tabs">
                    <li class="nav-item">
                        <a class="nav-link active" data-toggle="tab" href="#dashboard">Dashboard</a>
                    </li>
                    {% for commit in commits %}
                    <li class="nav-item">
                        <a class="nav-link" data-toggle="tab" href="#commit-{{ loop.index }}">{{ commit.commit_hash[:7] }}</a>
                    </li>
                    {% endfor %}
                </ul>

                <div class="tab-content">
                    <div id="dashboard" class="container tab-pane active"><br>
                        <h3>Dashboard</h3>
                        <table class="table">
                            <thead>
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Number of Commits</th>
                                <th>Number of Merges</th>
                            </tr>
                            </thead>
                            <tbody>
                            {% for developer in developers %}
                            <tr>
                                <td>{{ developer.name }}</td>
                                <td>{{ developer.email }}</td>
                                <td>{{ developer.num_commits }}</td>
                                <td>{{ developer.num_merges }}</td>
                            </tr>
                            {% endfor %}
                            </tbody>
                        </table>
                    </div>
                    {% for commit in commits %}
                    <div id="commit-{{ loop.index }}" class="container tab-pane fade"><br>
                        <h3>{{ commit.commit_details.subject }}</h3>
                        <p><strong>Author:</strong> {{ commit.commit_details.author_name }} ({{ commit.commit_details.author_email }})</p>
                        <p><strong>Changed Files:</strong></p>
                        <ul>
                        {% for file in commit.changed_files %}
                            <li>{{ file.status }}: {{ file.filename }}</li>
                        {% endfor %}
                        </ul>
                        
                    </div>
                    {% endfor %}
                </div>
            </div>

            </body>
            </html>
        """
        with open(self.template, 'w') as f:
            f.write(self.template_string)

    def generate(self, output_file):
        super().generate(output_file)
        os.remove(self.template)
