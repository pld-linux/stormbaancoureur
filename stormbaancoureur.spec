#
# TODO:
# - make it build on 64 bits
#
Summary:	Simulated obstacle course for automobiles
Summary(pl.UTF-8):	Symulowany rajd samochodowy z przeszkodami
Name:		stormbaancoureur
Version:	2.1.5
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://bram.creative4vision.nl/stormbaancoureur/download/%{name}-%{version}.tar.gz
# Source0-md5:	18aa9e5f34ede655d6530e6f022a455e
Patch0:		%{name}-dirs.patch
URL:		http://bram.creative4vision.nl/stormbaancoureur/
BuildRequires:	OpenGL-glut-devel
BuildRequires:	ode-devel >= 0.8
BuildRequires:	plib-devel >= 1.8.4
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In this game, your objective is to drive your car along an obstacle
course. Success depends on total control of the car, and making use of
the laws of physics.

%description -l pl.UTF-8
W tej grze zadaniem gracza jest kierowanie samochodem podczas rajdu z
przeszkodami. Sukces zależy od całkowitej kontroli samochodu oraz
korzystania z praw fizyki.

%prep
%setup -q
%patch0 -p1
%{__sed} -i -e 's/libode.a/libode.so/g' src-%{name}/Makefile

%build
%{__make} -C src-%{name} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -I../src-common -DGAMEVERSION=%{version}" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src-%{name} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src-stormbaancoureur/{README,TODO}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
