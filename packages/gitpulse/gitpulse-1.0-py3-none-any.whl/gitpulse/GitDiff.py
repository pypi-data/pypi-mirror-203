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
import shutil
import subprocess
import json
import subprocess
import difflib
from .HTMLReportGenerator import GitHTMLReportGenerator
from .DynamicHTMLReportGenerator import DynamicHTMLReportGenerator


class GitDiff:

    def get_default_branch_name(self):
        result = self.run_command('git symbolic-ref refs/remotes/origin/HEAD')
        return result.strip().split('/')[-1]

    def run_command(self, command):
        result = subprocess.run(command, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode != 0:
            raise Exception(f'Command failed: {command}\n{result.stderr}')
        return result.stdout.strip()

    def get_commit_hashes(self):
        log_output = self.run_command(
            f'git log -n {self.num_commits} --pretty=format:"%H"')
        return log_output.split('\n')

    def get_merge_commits(self):
        default_branch = self.get_default_branch_name()
        log_command = f'git log -n {self.merge_count} --merges --first-parent --pretty=format:"%H" {default_branch}'
        log_output = self.run_command(log_command)
        return log_output.splitlines()

    def get_commit_details(self, commit_hash):
        output = self.run_command(
            f'git show --pretty=format:"%an|%ae|%s" -s {commit_hash}')

        if '|' not in output:
            raise ValueError(f'Unexpected output format: {output}')

        author_name, author_email, subject = output.split('|')
        return {
            'author_name': author_name,
            'author_email': author_email,
            'subject': subject
        }

    def get_changed_files(self, commit_hash):
        output = self.run_command(
            f'git show --pretty="" --name-status {commit_hash}')
        lines = output.split('\n')

        changed_files = []
        for line in lines:
            if '\t' not in line:
                continue
            status, filename = line.split('\t', 1)
            changed_files.append({
                'filename': filename,
                'status': status
            })
        return changed_files

    def get_side_by_side_diff(self, commit1, commit2):
        diff_command = f"git diff {commit1} {commit2}"
        output = subprocess.check_output(
            diff_command.split(), universal_newlines=True)
        file_diffs = output.split("diff --git")

        for file_diff in file_diffs[1:]:
            file_lines = file_diff.split("\n")
            file_header = file_lines[0].strip().split()
            file1 = file_header[1][2:]
            file2 = file_header[2][2:]

            content1 = subprocess.check_output(
                ["git", "show", f"{commit1}:{file1}"], universal_newlines=True, stderr=subprocess.DEVNULL)
            content2 = subprocess.check_output(
                ["git", "show", f"{commit2}:{file2}"], universal_newlines=True, stderr=subprocess.DEVNULL)

            lines1 = content1.splitlines()
            lines2 = content2.splitlines()

            diff = difflib.HtmlSideBySideDiff(lines1, lines2)
            diff_table = diff.make_table()

            return file1, file2, diff_table

    def generate_report(self, output_file="gitpulse_report.html"):
        commit_hashes = self.get_commit_hashes()
        merge_hashes = self.get_merge_commits()
        commits = []
        merges = []

        # self.get_side_by_side_diff(commit1, commit2)

        for i in range(len(commit_hashes)):
            commit_details = self.get_commit_details(commit_hashes[i])
            changed_files = self.get_changed_files(commit_hashes[i])

            commits.append({
                'commit_hash': commit_hashes[i],
                'commit_details': commit_details,
                'changed_files': changed_files
            })

        for i in range(len(merge_hashes)):
            merge_details = self.get_commit_details(merge_hashes[i])
            changed_files = self.get_changed_files(merge_hashes[i])

            merges.append({
                'commit_hash': merge_hashes[i],
                'commit_details': merge_details,
                'changed_files': changed_files
            })

        with open('git_commits.json', 'w') as f:
            json.dump(commits, f, indent=2)

        report_generator = GitHTMLReportGenerator(commits, merges)
        report_generator.generate(output_file)

    def check_dependencies(self):
        required_commands = ['git']

        for command in required_commands:
            if not shutil.which(command):
                raise Exception(f'Required command not found: {command}')

    def __init__(self, output_directory="output", merge_count=5):
        DynamicHTMLReportGenerator()
        self.num_commits = merge_count
        self.repo_directory = os.getcwd()
        self.output_directory = output_directory
        self.merge_count = merge_count
        self.check_dependencies()
