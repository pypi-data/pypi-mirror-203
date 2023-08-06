#!/usr/bin/env python3
# Copyright 2022 David Seaward and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import click

from samosa import git


@click.command()
def validate():
    """
    Enforce a triangular Git workflow. If this is not possible, explain why.
    """

    if git.validate_path(os.getcwd()):
        exit(0)
    else:
        exit(1)
