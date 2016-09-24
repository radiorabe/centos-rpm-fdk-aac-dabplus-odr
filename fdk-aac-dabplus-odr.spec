#
# spec file for package fdk-aac-dabplus-odr
#
# Copyright (c) 2016 Radio Bern RaBe
#                    http://www.rabe.ch
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
%global commit0 aad197a2a2e3b8897279a34778946355589b02fa
%global shortcommit0 aad197a


Name:           fdk-aac-dabplus-odr
# The Version is made up out of the fdk-aac upstream version, according to
# the ChangeLog and the last origin repo tag, with the short commit hash
# from the ODR git repositry appended.
Version:        0.1.4.odr.%{shortcommit0}
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
%doc ChangeLog NOTICE
%{_libdir}/*.so.*

%files devel
%doc documentation/*.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc


%changelog
* Fri Sep 23 2016 Christian Affolter <c.affolter@purplehaze.ch> - 0.1.4.odr.aad197a-1
- New release, according to the ODR project reorganisation
