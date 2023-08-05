# This specfile is licensed under:
#
# Copyright (C) 2023 Maxwell G <gotmax@e.email>
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html

Name:           fclogr
Version:        0.2.0
Release:        1%{?dist}
Summary:        A tool for managing RPM changelogs and updates

License:        GPL-2.0-or-later
URL:            https://sr.ht/~gotmax23/fclogr
%global furl    https://git.sr.ht/~gotmax23/fclogr
Source0:        %{furl}/refs/download/v%{version}/fclogr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  python3-devel

BuildRequires:  %{py3_dist pytest}
BuildRequires:  rpmdevtools

# This is currently used for `fclogr bump`.
# TODO: Remove once https://github.com/packit/specfile/pull/220
# is merged.
Recommends:     rpmdevtools


%description
fclogr is a tool for managing RPM changelogs and updates.


%prep
%autosetup -p1 -n fclogr-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fclogr


%check
%pytest


%files -f %{pyproject_files}
%license LICENSES/*.txt
%doc README.md
%doc NEWS.md
%{_bindir}/fclogr*


%changelog
* Sat Mar 18 2023 Maxwell G <maxwell@gtmx.me> - 0.2.0-1
- Initial package
