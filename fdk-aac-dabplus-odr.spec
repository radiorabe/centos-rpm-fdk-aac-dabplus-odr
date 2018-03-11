#
# spec file for package fdk-aac-dabplus-odr
#
# Copyright (c) 2016 - 2018 Radio Bern RaBe
#                           http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-fdk-aac-dabplus-odr
#


# Name of the GitHub repository
%define reponame fdk-aac

# Note, that at the time of writing there was no official release available.
# To get a stable reproducable build, a specific Git commit is used instead.
%global commit0 3eab23670d4d9fb2a8ee01c1be7b4acfc14c1552
%global shortcommit0 3eab236


Name:           fdk-aac-dabplus-odr
# The Version is made up out of the fdk-aac upstream version, according to
# the ChangeLog and the last origin repo tag, with the short commit hash
# from the ODR git repositry appended.
Version:        0.1.6.odr.%{shortcommit0}
Release:        1%{?dist}
Summary:        Opendigitalradio's fork of the standalone library of the Fraunhofer FDK AAC code from Android

License:        FraunhoferFDK
URL:            https://github.com/Opendigitalradio/%{reponame}
Source0:        https://github.com/Opendigitalradio/%{reponame}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz


%description
The Fraunhofer FDK AAC Codec Library for Android ("FDK AAC Codec") is software
that implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.
This package contains a a modified version of this library, patched for
960-transform to do DAB+ broadcast encoding.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{reponame}-%{commit0}


%build
autoreconf -fi
%configure --disable-static
           
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc ChangeLog NOTICE README.md
%{_libdir}/*.so.*

%files devel
%doc documentation/*.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc


%changelog
* Sun Mar 11 2018 Christian Affolter <c.affolter@purplehaze.ch> - 0.1.6.odr.3eab236-1
- Version bump to 0.1.6 Git 3eab236

* Tue Aug 22 2017 Christian Affolter <c.affolter@purplehaze.ch> - 0.1.5.odr.89639e3-1
- Version bump to 0.1.5 Git 89639e3
- Including README.md

* Fri Feb 17 2017 Lucas Bickel <hairmare@rabe.ch> - 0.1.4.odr.7257135-2
- Bump https://github.com/Opendigitalradio/fdk-aac/pull/21

* Fri Sep 23 2016 Christian Affolter <c.affolter@purplehaze.ch> - 0.1.4.odr.aad197a-1
- New release, according to the ODR project reorganisation
