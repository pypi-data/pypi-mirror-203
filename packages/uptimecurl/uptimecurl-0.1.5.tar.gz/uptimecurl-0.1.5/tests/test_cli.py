# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: Copyright 2020 David Seaward and contributors

from uptimecurl import cli


def test_invoke():
    result = cli.invoke()
    assert result is None
