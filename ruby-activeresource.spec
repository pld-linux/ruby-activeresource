%define pkgname activeresource
Summary:	Think Active Record for web resources
Name:		ruby-%{pkgname}
Version:	2.3.5
Release:	1
License:	Ruby-alike
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	d66534fe7c40498d6fa7229122f74f23
Group:		Development/Languages
URL:		http://rubyforge.org/projects/activeresource/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-ActiveResource
Provides:	ruby-ActiveResource
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Wraps web resources in model classes that can be manipulated through
XML over REST.

%package rdoc
Summary:	Documentation files for ActiveResource
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActiveResource.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{ruby_rubylibdir}/active_resource.rb
%{ruby_rubylibdir}/activeresource.rb
%{ruby_rubylibdir}/active_resource

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}
%{ruby_ridir}/ActiveResource
