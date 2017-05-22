Summary:	XMMS plugin that uses XMP library to play music modules
Summary(pl.UTF-8):	Wtyczka dla XMMS-a odtwarzająca moduły dźwiękowe z użyciem XMP
Name:		xmms-input-xmp
Version:	3.5.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/xmp/xmp-%{version}.tar.gz
# Source0-md5:	47e54e6dfa88ce37370054d4a3ea955f
Patch0:		xmp-xmms_plugin_update.patch
URL:		http://xmp.sourceforge.net/
BuildRequires:	libxmp-devel >= 4
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.0.0
Requires:	libxmp >= 4
Requires:	xmms >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS plugin that uses XMP library to play music modules.

%description -l pl.UTF-8
Wtyczka dla XMMS-a odtwarzająca moduły dźwiękowe z użyciem biblioteki
XMP.

%prep
%setup -q -n xmp-%{version}
%patch0 -p1

%build
%{__cc} %{rpmcflags} %{rpmcppflags} $(xmms-config --cflags) -fPIC -DVERSION='"%{version}"' -o xmms.o -c src/plugin/xmms.c
%{__cc} %{rpmldflags} %{rpmcflags} -shared -o xmp-xmms.so xmms.o $(xmms-config --libs) -lxmp -pthread

%install
rm -rf $RPM_BUILD_ROOT

install -D xmp-xmms.so $RPM_BUILD_ROOT%{xmms_input_plugindir}/xmp-xmms.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_input_plugindir}/xmp-xmms.so
