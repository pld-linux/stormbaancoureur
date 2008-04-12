#
# TODO:
# - make it builds on 64 bits
#
Summary:	Simulated obstacle course for automobiles
Summary(pl.UTF-8):	Symulowany kurs samochodowy z przeszkodami
Name:		stormbaancoureur
Version:	2.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://bram.creative4vision.nl/sturmbahnfahrer/download/%{name}-%{version}.tar.gz
# Source0-md5:	5475c64d85d0921f446cf9fbb3b73c35
Patch0:		%{name}-dirs.patch
URL:		http://www.sturmbahnfahrer.com/
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
W tej grze zadaniem gracza jest kierowanie samochodem przez kurs z
przeszkodami. Sukces zależy od całkowitej kontroli samochodu oraz
korzystania z praw fizyki.

%prep
%setup -q
%patch0 -p1
%{__sed} -i -e 's/libode.a/libode.so/g' src-%{name}/Makefile

%build
cd src-%{name}
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -I../src-common -DGAMEVERSION=%{version}" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

cd src-%{name}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src-stormbaancoureur/{README,TODO}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
