
%define name	kde-rootactions-servicemenu
%define oname	rootactions_servicemenu
%define version	2.4.6
%define rel	2

Summary:	Root actions for Dolphin context menu
Name:		%{name}
Version:	%{version}
Release:	%mkrel %rel
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-apps.org/content/show.php/?content=48411
Source0:	http://www.kde-apps.org/CONTENT/content-files/48411-%{oname}_%{version}.tar.gz
# adapt for kdesu in %{_libdir}/kde4/libexec/kdesu
Patch0:		rootactions-mandriva-kdesu.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
BuildRequires:	kde4-macros
Requires:	kdebase4-workspace
Obsoletes:	kde_servicemenu_rootactions < %{version}
Obsoletes:	openasroot-kmenu < 1.0-7
Provides:	openasroot-kmenu = 1.1

%description
Root Actions servicemenu provides a convenient way to perform
several actions 'as root', from the right-click context menu in KDE
filemanager.

%prep
%setup -q -n %{oname}_%version
%patch0 -p1

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 Root_Actions_%{version}/*.pl %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_kde_services}/ServiceMenus
install -m644 Root_Actions_%{version}/dolphin-KDE4/* %{buildroot}%{_kde_services}/ServiceMenus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README changelog
%{_bindir}/rootactions-servicemenu.pl
%{_kde_services}/ServiceMenus/10-rootactionsfolders.desktop
%{_kde_services}/ServiceMenus/11-rootactionsfiles.desktop
