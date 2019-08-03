# This package could be noarch except that it needs to install scripts
# into /usr/lib{64,}/
%define debug_package %{nil}

Name:		samsung-tools
Version:	2.3.1
Release:	%mkrel 7
Summary:	Tools for Samsung laptops
License:	GPLv2+
Group:		System/Configuration
URL:		https://launchpad.net/samsung-tools
Source0:	http://launchpad.net/samsung-tools/trunk/%{version}/+download/%{name}-%{version}.tar.gz
ExclusiveArch:	%ix86 x86_64
BuildRequires:	locales
Requires:	pm-utils
Requires:	dbus-python
Requires:	pygtk2.0
Requires:	python-notify
Requires:	rfkill
Requires:	xbindkeys
Requires:	vbetool
Requires(post):	rpm-helper >= 0.24.8-1
Requires(preun):rpm-helper >= 0.24.8-1

%description
'Samsung Tools' is the successor of 'Samsung Scripts' provided by the 'Linux
On My Samsung' project. It allows the complete configuration and the control
in a friendly way of devices found on Samsung netbooks (bluetooth, wireless,
webcam, backlight, CPU fan, special keys) and the control of various aspects
related to power management, like the CPU undervolting (when a PHC-enabled
kernel is available).

%prep
%setup -q

#fix rights
chmod 644 ChangeLog

%build
#nothing

%install
#without this build throws a bunch of warnings
LC_ALL=UTF-8 %makeinstall_std

#move files to a correct location
%ifarch x86_64
	mkdir -p %{buildroot}%{_libdir}
	mv %{buildroot}%{_prefix}/lib/pm-utils %{buildroot}%{_libdir}/pm-utils
%endif

rm -rf %{buildroot}/usr/lib/systemd/

mkdir -p %{buildroot}%{_unitdir}/
cat <<EOF > %{buildroot}%{_unitdir}/%{name}.service
[Unit]
Description=Tools for Samsung laptops

[Service]
ExecStart=/bin/dbus-send --system --print-reply=literal --dest=org.voria.SamsungTools.System / org.voria.SamsungTools.System.SetInitialDevicesStatus
Type=forking

[Install]
WantedBy=multi-user.target
EOF

%find_lang %{name}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files -f %{name}.lang
%doc ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}-preferences
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/scripts/
%config(noreplace) %{_sysconfdir}/%{name}/session.conf
%config(noreplace) %{_sysconfdir}/%{name}/system.conf
%config(noreplace) %{_sysconfdir}/%{name}/scripts/*
%{_sysconfdir}/dbus-1/system.d/org.voria.SamsungTools.System.conf
%{_sysconfdir}/xdg/autostart/%{name}-session-service.desktop
%{_libdir}/pm-utils/power.d/%{name}*
%{_libdir}/pm-utils/sleep.d/20_%{name}
%{_datadir}/applications/%{name}-preferences.desktop
%{_datadir}/dbus-1/*/org.voria.SamsungTools.*.service
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service
