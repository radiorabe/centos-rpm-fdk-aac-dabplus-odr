#
# spec file for package libfdk-dabplus-odr
# and subpackages libfdk-dabplus-odr and libtoolame-dab-odr
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
%define reponame fdk-aac-dabplus

# Names and versions of the (sub)packages
# See https://www.redhat.com/archives/rpm-list/2000-October/msg00216.html
%define main_name fdk-aac-dabplus-odr
%define main_version 1.1.0 

%define libfdk_dabplus_name libfdk-dabplus-odr
# Version relates to libFDK/src/FDK_core.cpp (FDK tools library info)
%define libfdk_dabplus_version 2.3.2.odr 
%define libfdk_dabplus_license FraunhoferFDK

%define libtoolame_dab_name libtoolame-dab-odr
# Version relates to libtoolame-dab/HISTORY
%define libtoolame_dab_version 0.2l.odr
%define libtoolame_dab_license LGPLv2+

# Conditional build support
# add --without alsa option, i.e. enable alsa by default
%bcond_without alsa
# add --without imagemagick option, i.e. enable imagemagick by default
%bcond_without imagemagick
# add --with jack option, i.e. disable jack by default
%bcond_with jack
# add --with vlc option, i.e. disable vlc by default
%bcond_with vlc

Name:           %{main_name}
Version:        %{main_version}
Release:        1%{?dist}
Summary:        Opendigitalradio's fork of the standalone library of the Fraunhofer FDK AAC code from Android

License:        ASL 2.0 GPLv3+
URL:            https://github.com/Opendigitalradio/%{reponame}
Source0:        https://github.com/Opendigitalradio/%{reponame}/archive/v%{main_version}.tar.gz#/%{main_name}-%{main_version}.tar.gz


BuildRequires:  chrpath
BuildRequires:  libfec-odr-devel
BuildRequires:  libtool
BuildRequires:  zeromq-devel
Requires:       %{libfdk_dabplus_name}
Requires:       libfec-odr
Requires:       %{libtoolame_dab_name}
Requires:       zeromq

%if %{with alsa}
BuildRequires:  alsa-lib-devel
Requires:       alsa-lib
%endif

%if %{with imagemagick}
BuildRequires:  imagemagick-devel
Requires:       imagemagick-lib
%endif

%if %{with jack}
BuildRequires:  jack-audio-connection-kit-devel
Requires:       jack-audio-connection-kit
%endif

%if %{with vlc}
BuildRequires:  vlc-devel
Requires:       vlc
%endif

%description
This package contains a DAB and DAB+ encoder that integrates into the
ODR-mmbTools.
The DAB encoder is based on toolame. The DAB+ encoder uses a modified library
of the Fraunhofer FDK AAC code from Android, patched for 960-transform to do
DAB+ broadcast encoding.
The main tool is the dabplus-enc encoder, which can read audio from a file
(raw or wav), from an ALSA source, from JACK or using libVLC, and encode to a
file, a pipe, or to a ZeroMQ output compatible with ODR-DabMux.


%package -n     %{libfdk_dabplus_name}
Version:        %{libfdk_dabplus_version}
Summary:        Opendigitalradio's fork of the Fraunhofer FDK AAC Codec Library for Android
License:        %{libfdk_dabplus_license}

%description -n %{libfdk_dabplus_name}
The Fraunhofer FDK AAC Codec Library for Android ("FDK AAC Codec") is software
that implements the MPEG Advanced Audio Coding ("AAC") encoding and decoding
scheme for digital audio.


%package -n     %{libfdk_dabplus_name}-devel
Version:        %{libfdk_dabplus_version}
Summary:        Development files for %{libfdk_dabplus_name}
License:        %{libfdk_dabplus_license}
Requires:       %{libfdk_dabplus_name}%{?_isa} = %{libfdk_dabplus_version}-%{release}

%description -n %{libfdk_dabplus_name}-devel
The %{libfdk_dabplus_name}-devel package contains libraries and header files for
developing applications that use %{libfdk_dabplus_name}.


%package -n     %{libtoolame_dab_name}
Version:        %{libtoolame_dab_version}
Summary:        Opendigitalradio's fork of tooLAME
License:        %{libtoolame_dab_license}

%description -n %{libtoolame_dab_name}
tooLAME is an optimized Mpeg Audio 1/2 Layer 2 encoder. It is based heavily on
- the ISO dist10 code - improvement to algorithms as part of the LAME project,
in form of a library to be used with the encoder for the ODR-mmbTools


%package -n     %{libtoolame_dab_name}-devel
Version:        %{libtoolame_dab_version}
Summary:        Development files for %{libtoolame_dab_name}
License:        %{libtoolame_dab_license}
Requires:       %{libtoolame_dab_name}%{?_isa} = %{libtoolame_dab_version}-%{release}

%description -n %{libtoolame_dab_name}-devel
The %{libtoolame_dab_name}-devel package contains libraries and header files for
developing applications that use %{libtoolame_dab_name}.


%prep
%setup -q -n %{reponame}-%{main_version}


%build
autoreconf -fi
%configure --disable-static \
           %{?with_alsa:--enable-alsa} \
           %{?with_jack:--enable-jack} \
           %{?with_vlc:--enable-vlc}
           
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Remove Rpath to get rid of hardcoded library paths
# and pass the check-rpaths tests:
# ERROR   0002: file '/usr/bin/dabplus-enc' contains an invalid rpath
#
# Unfortunately, passing --disable-rpath to configure is not supported,
# that's why chrpath is used. This should be fixed within the buildsystem
# someday.
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/dabplus-enc


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc ChangeLog NOTICE README.md
%{_bindir}/*


%files -n %{libfdk_dabplus_name}
%{_libdir}/libfdk-dabplus.so.*

%files -n %{libfdk_dabplus_name}-devel
%{_libdir}/pkgconfig/fdk-dabplus.pc
%{_includedir}/fdk-dabplus/*
%{_libdir}/libfdk-dabplus.so


%files -n %{libtoolame_dab_name}
%{_libdir}/libtoolame-dab.so.*

%files -n %{libtoolame_dab_name}-devel
%doc libtoolame-dab/HISTORY libtoolame-dab/README.md
%{_libdir}/pkgconfig/fdk-dabplus.pc
%{_includedir}/libtoolame-dab/*
%{_libdir}/libtoolame-dab.so


%changelog
* Sat Aug 20 2016 Christian Affolter <c.affolter@purplehaze.ch> - 1.1.0-1
- Initial release
