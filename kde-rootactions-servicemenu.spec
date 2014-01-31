%define oname	rootactions_servicemenu

Summary:	Root actions for Dolphin context menu
Name:		kde-rootactions-servicemenu
Version:	2.8.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://www.kde-apps.org/content/show.php/?content=48411
Source0:	http://www.kde-apps.org/CONTENT/content-files/48411-%{oname}_%{version}.tar.gz
# adapt for kdesu in %{_libdir}/kde4/libexec/kdesu
Patch0:		rootactions-mandriva-kdesu.patch
BuildRequires:	kde4-macros
Requires:	kdebase4-workspace
BuildArch:	noarch

%description
Root Actions servicemenu provides a convenient way to perform
several actions 'as root', from the right-click context menu in KDE
filemanager.

%files
%doc README changelog
%{_bindir}/rootactions-servicemenu.pl
%{_kde_services}/ServiceMenus/10-rootactionsfolders.desktop
%{_kde_services}/ServiceMenus/11-rootactionsfiles.desktop
%{_kde_appsdir}/krusader/krusader_rootactions.xml

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}_%{version}
%patch0 -p1

%build

%install
install -d -m755 %{buildroot}%{_bindir}
install -m755 Root_Actions_%{version}/*.pl %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_kde_services}/ServiceMenus
install -m644 Root_Actions_%{version}/dolphin-KDE4/* %{buildroot}%{_kde_services}/ServiceMenus

install -d -m755 %{buildroot}%{_kde_appsdir}/krusader
install -m644 Root_Actions_%{version}/krusader-KDE4/* %{buildroot}%{_kde_appsdir}/krusader


