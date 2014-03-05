Name:           luajit
Version:        2.0.2
Release:        0
License:        MIT
Summary:        Just-In-Time Compiler for Lua
Url:            http://luajit.org/git/luajit-2.0.git
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make

%description
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language.

%package devel
Summary:    Just-In-Time Compiler for Lua -- development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language.

%prep
%setup -q


%build
make %{?jobs:-j%jobs} V=1 PREFIX="/usr"

%install
make install \
  PREFIX="/usr" \
  DPREFIX="%{buildroot}/usr" \
  INSTALL_BIN="%{buildroot}/%{_bindir}" \
  INSTALL_LIB="%{buildroot}/%{_libdir}" \
  #eol

rm -f %{buildroot}${bindir}/lib${name}*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%license COPYRIGHT
%{_bindir}/%{name}*
%{_libdir}/lib%{name}*
%{_datadir}/*


%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}*/*
%{_libdir}/pkgconfig/%{name}*.pc
%{_mandir}/*
