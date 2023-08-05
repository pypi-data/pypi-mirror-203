# Copyright (c) 2023 Maxwell G <gotmax@e.email>
# SPDX-License-Identifier: GPL-2.0-or-later

from __future__ import annotations

import datetime
import subprocess
from collections.abc import Sequence
from pathlib import Path
from shutil import copy2
from unittest import mock

import pytest
import pytest_mock
import specfile
import specfile.changelog
import specfile.macros

from fclogr.cli import Bumper, main

DEFAULT_PACKAGER = "Perry the Packager <perry@example.com>"
DATE_STR = datetime.datetime.now(tz=datetime.timezone.utc).strftime("%a %b %d %Y")


@pytest.mark.parametrize(
    "value,expected",
    [
        # REL_MATCHER
        pytest.param("1", "2", id="simple"),
        pytest.param("33", "34", id="simple double"),
        # PRE_REL_MATCHER
        pytest.param("0.1", "0.2", id="prerel"),
        # POST_REL_MATCHER
        pytest.param("abcdefgh.1", "abcdefgh.2", id="postrel"),
        # fallback
        pytest.param("abcdefgh", "abcdefgh.1", id="fallback"),
    ],
)
def test_bumper_handle_release(value: str, expected: str) -> None:
    assert Bumper._handle_release2(value) == expected


def get_entry_obj(
    evr: str,
    lines: list[str],
    following_lines: list[str],
    date_str: str = DATE_STR,
    packager: str = DEFAULT_PACKAGER,
):
    header = f"* {date_str} {packager} - {evr}"
    return specfile.changelog.ChangelogEntry(header, lines, following_lines)


INITIAL_ENTRY = get_entry_obj(
    "1-1",
    ["- Initial package"],
    [],
    "Fri Mar 03 2023",
    "Packager <example@example.com>",
)


@pytest.mark.parametrize(
    "args, changelog, version, raw_release, subprocess_calls",
    [
        pytest.param(
            [],
            [INITIAL_ENTRY, get_entry_obj("1-2", ["- bump"], [""])],
            "1",
            "2%{?dist}",
            [],
            id="no-arguments",
        ),
        pytest.param(
            ["--new", "3"],
            [INITIAL_ENTRY, get_entry_obj("3-1", ["- Update to 3."], [""])],
            "3",
            "1%{?dist}",
            [],
            id="new-version-no-arguments",
        ),
        pytest.param(
            ["--new", "3", "--commit"],
            [INITIAL_ENTRY, get_entry_obj("3-1", ["- Update to 3."], [""])],
            "3",
            "1%{?dist}",
            [
                lambda p: mock.call(
                    ["add", p],
                    check=True,
                    stdout=subprocess.DEVNULL,
                ),
                lambda _: mock.call(["commit", "-m", "Update to 3."], check=True),
            ],
            id="new-version-commit",
        ),
        pytest.param(
            ["--comment", "abc"],
            [INITIAL_ENTRY, get_entry_obj("1-2", ["- abc"], [""])],
            "1",
            "2%{?dist}",
            [],
            id="comment",
        ),
        pytest.param(
            ["--comment", "- abc", "-c", "xyz", "--new", "5", "-S"],
            [INITIAL_ENTRY, get_entry_obj("5-1", ["- abc", "- xyz"], [""])],
            "5",
            "1%{?dist}",
            [
                lambda p: mock.call(
                    ["add", p],
                    check=True,
                    stdout=subprocess.DEVNULL,
                ),
                lambda _: mock.call(
                    ["commit", "-m", "abc", "-m", "xyz", "--gpg-sign"], check=True
                ),
            ],
            id="new-version-with-multiple-comments",
        ),
    ],
)
def test_bumper_full(
    test_data: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mocker: pytest_mock.MockerFixture,
    args: Sequence[str],
    changelog: list[specfile.changelog.ChangelogEntry],
    version: str,
    raw_release: str,
    subprocess_calls: Sequence[mock.call],
):
    monkeypatch.setenv("RPM_PACKAGER", DEFAULT_PACKAGER)
    subprocess_mock: mock.MagicMock = mocker.patch.object(Bumper, "_git")
    name = "package.spec"
    path = tmp_path / name
    copy2(test_data / name, path)
    args = ["bump", *args, str(path)]
    assert main(args) == 0
    specfile.macros.Macros.reinit()

    with specfile.Specfile(path) as spec:
        assert spec.raw_release == raw_release
        assert spec.version == version
        with spec.changelog() as spec_changelog:
            assert list(spec_changelog) == changelog
    assert subprocess_mock.call_args_list == [call(path) for call in subprocess_calls]
