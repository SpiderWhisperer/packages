Name:           ft2-clone
Version:        v2.29
Release:        1%?dist
Summary:        A package example
URL:            https://16-bits.org/ft2.php
Source0:        https://github.com/8bitbubsy/ft2-clone/archive/refs/tags/%{version}.tar.gz
Source0:        https://github.com/some/repo/archive/%{version}.tar.gz
# You should change the above link to the source tarball you got from the preparation section
License:        BSD-3-Clause
BuildRequires:  some dependencies >= 3.2.1 another-dep
Requires:       SDL2-devel
Requires:       gcc
Requires:       gcc-c++
Requires:       alsa-lib-devel
# We require you to add yourself as the packager here (if this is an issue for you, let us know):
Packager:       Summer Cordaella <summer.cordaella@pm.me>

%description
This is a description of the package that literally does nothing.

%prep
%autosetup -n %{version}
# if you are not using a tarball, simply use normal shell commands to extract the sources
echo "hai"

%build
echo "this will run when building pkg"

%install
echo "this will also run when building pkg but for installing it into %{buildroot} so that anda (mock) can package it"

%files
# This macro expands to `/usr/bin`. To see what macros expand to, you can run `rpm --eval %{MACRO}`
%{_bindir}/pkgname-binary
/path/to/more/files/*/package

%changelog
* Wed Jan 11 2006 your-username-here <your_email@idk.xyz>
- Description on what you've done
