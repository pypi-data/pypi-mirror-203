# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: Copyright 2022 David Seaward and contributors

from samosa import git


def test_valid_suffix():
    assert git.valid_suffix("hotmail.com")


def test_invalid_suffix():
    assert not git.valid_suffix("example.com")
