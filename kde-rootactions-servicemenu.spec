%define name kde-rootactions-servicemenu
%define oname rootactions_servicemenu
%define version 2.9.1
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Graphical desktop/KDE
Summary: Root actions for Dolphin context menu
Url: https://www.kde-look.org/content/show.php/Root+Actions+Servicemenu?content=48411
Source:%{oname}_%version.tar.gz
BuildRoot: %{_tmppath}/%{oname}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Root Actions servicemenu provides a convenient way to perform
several actions 'as root', from the right-click context menu in Dolphin
filemanager..

%prep
%setup -n %{oname}_%version/Root_Actions_2.9.1

%install
rm -rf %{buildroot}

mkdir %buildroot
mkdir %buildroot/usr
mkdir %buildroot%_bindir
mkdir %buildroot%_datadir
mkdir %buildroot%_datadir/kservices5/
mkdir %buildroot%_datadir/kservices5/ServiceMenus
install -Dm 755 rootactions-servicemenu.pl %buildroot%_bindir
install -Dm 755 dolphin-KDE4/*desktop %buildroot%_datadir/kservices5/ServiceMenus/

%clean
rm -rf %{buildroot}

%files
%_bindir/rootactions-servicemenu.pl
%_datadir/kservices5/ServiceMenus/*desktop
