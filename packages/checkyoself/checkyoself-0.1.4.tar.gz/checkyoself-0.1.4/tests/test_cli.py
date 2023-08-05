# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: Copyright 2020 David Seaward and contributors

from checkyoself import chikkity


def test_invoke():
    result = chikkity.check()
    assert result is None
