# centos-rpm-fdk-aac-dabplus-odr
CentOS 7 RPM Specfile for [Opendigitalradio's fork of the standalone library of the Fraunhofer FDK AAC code from Android (fdk-aac-dabplus)](https://github.com/Opendigitalradio/fdk-aac-dabplus) which is part of [RaBe's DAB / DAB+ broadcasting package collection](https://build.opensuse.org/project/show/home:radiorabe:dab).

The Specfile consists out of the main package <code>fdk-aac-dabplus-odr</code> and the subpackages <code>libfdk-dabplus-odr</code> and <code>libtoolame-dab-odr</code> as well as the related <code>*-devel</code> packages.

The package supports [conditional builds](http://www.rpm.org/wiki/PackagerDocs/ConditionalBuilds) with the following default parameters (see the [FDK-AAC-DABplus package description](https://github.com/Opendigitalradio/fdk-aac-dabplus/blob/master/README.md) for further information):
```bash
 rpmbuild -ba fdk-aac-dabplus-odr.spec --with alsa --with imagemagick --without jack --without vlc
```

## Usage
There are pre-built binary packages for CentOS 7 available on [Radio RaBe's OBS DAB / DAB+ broadcasting package repository](https://build.opensuse.org/project/show/home:radiorabe:dab), which can be installed as follows:

```bash
curl -o /etc/yum.repos.d/home:radiorabe:dab.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/dab/CentOS_7/home:radiorabe:dab.repo
     
yum install @TODO
```
