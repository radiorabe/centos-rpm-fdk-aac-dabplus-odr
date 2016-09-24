# centos-rpm-fdk-aac-dabplus-odr
CentOS 7 RPM Specfile for [Opendigitalradio's fork of the standalone library of the Fraunhofer FDK AAC code from Android (fdk-aac)](https://github.com/Opendigitalradio/fdk-aac) which is part of [RaBe's DAB / DAB+ broadcasting package collection](https://build.opensuse.org/project/show/home:radiorabe:dab).

The Specfile consists out of the main package <code>fdk-aac-dabplus-odr</code> and the related <code>*-devel</code> package.

## Usage
There are pre-built binary packages for CentOS 7 available on [Radio RaBe's OBS DAB / DAB+ broadcasting package repository](https://build.opensuse.org/project/show/home:radiorabe:dab), which can be installed as follows:

```bash
curl -o /etc/yum.repos.d/home:radiorabe:dab.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/dab/CentOS_7/home:radiorabe:dab.repo
     
yum install fdk-aac-dabplus-odr
```
