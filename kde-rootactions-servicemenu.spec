%define oname	rootactions_servicemenu

Summary:	Root actions for Dolphin context menu
Name:		kde-rootactions-servicemenu
Version:	2.7.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-apps.org/content/show.php/?content=48411
Source0:	http://www.kde-apps.org/CONTENT/content-files/48411-%{oname}_%{version}.tar.gz
# adapt for kdesu in %{_libdir}/kde4/libexec/kdesu
Patch0:		rootactions-mandriva-kdesu.patch
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
%setup -q -n %{oname}_%{version}
%patch0 -p1

%install
%__rm -rf %{buildroot}
%__install -d -m755 %{buildroot}%{_bindir}
%__install -m755 Root_Actions_%{version}/*.pl %{buildroot}%{_bindir}

%__install -d -m755 %{buildroot}%{_kde_services}/ServiceMenus
%__install -m644 Root_Actions_%{version}/dolphin-KDE4/* %{buildroot}%{_kde_services}/ServiceMenus

%__install -d -m755 %{buildroot}%{_kde_appsdir}/krusader
%__install -m644 Root_Actions_%{version}/krusader-KDE4/* %{buildroot}%{_kde_appsdir}/krusader


%clean
%__rm -rf %{buildroot}

%files
%doc README changelog
%{_bindir}/rootactions-servicemenu.pl
%{_kde_services}/ServiceMenus/10-rootactionsfolders.desktop
%{_kde_services}/ServiceMenus/11-rootactionsfiles.desktop
%{_kde_appsdir}/krusader/krusader_rootactions.xml



%changelog
* Mon May 28 2012 Andrey Bondrov <abondrov@mandriva.org> 2.7.3-1mdv2012.0
+ Revision: 801007
- New version 2.7.3, re-diff patch, package Krusader actions (but user must import them from Krusader settings anyway)

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

  + Juan Luis Baptiste <juancho@mandriva.org>
    - Updated to 2.4.6.

* Wed Jul 22 2009 Anssi Hannula <anssi@mandriva.org> 2.4.3-2mdv2010.0
+ Revision: 398558
- obsoletes openasroot-kmenu

* Tue Jul 21 2009 Anssi Hannula <anssi@mandriva.org> 2.4.3-1mdv2010.0
+ Revision: 398438
- initial Mandriva release

