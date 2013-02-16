%define		pkg	config-chain
Summary:	Handle configuration once and for all
Name:		nodejs-%{pkg}
Version:	1.1.5
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		http://github.com/dominictarr/config-chain
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	aa6b0be8d0564a06ef7638fb301ecef0
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-ini < 2
Requires:	nodejs-ini >= 1.0.0
Requires:	nodejs-proto-list < 1.3.0
Requires:	nodejs-proto-list >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The semantic version comparison library for the Node.js package
manager (npm).

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json index.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.markdown LICENCE
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/index.js
