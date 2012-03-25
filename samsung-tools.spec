Name:		samsung-tools
Version:	2.1
Release:	1
License:	GPLv2+
Group:		System/Configuration/Hardware
URL:		https://launchpad.net/samsung-tools
Source0:	http://launchpad.net/samsung-tools/trunk/2.1/+download/%{name}-%{version}.tar.gz
Summary:	Tools for Samsung laptops

%description
Tools for Samsung netbooks.
'Samsung Tools' is the successor of 'Samsung Scripts' 
provided by the 'Linux On My Samsung' project.
It allows the complete configuration and the
control in a friendly way of devices
found on Samsung netbooks (bluetooth, wireless, 
webcam, backlight, CPU fan, special keys) 
and the control of various aspects 
related to power management, 
like the CPU undervolting
(when a PHC-enabled kernel is available).


%prep
%setup -q

%build
echo "Hello Mandriva"
#make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc ChangeLog README
%{_bindir}/%{name}
%{_bindir}/%{name}-preferences
%{_sysconfdir}/%{name}
%{_sysconfdir}/dbus-1
%{_sysconfdir}/pm/
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/%{name}-preferences.desktop
%{_datadir}/dbus-1/*/*
%{_prefix}/lib/%{name}
