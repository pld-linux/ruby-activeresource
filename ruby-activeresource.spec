Summary:	Think Active Record for web resources
Name:		ruby-ActiveResource
Version:	2.0.4
Release:	1
License:	Ruby-alike
Source0:	http://rubyforge.org/frs/download.php/42551/activeresource-%{version}.tgz
# Source0-md5:	99def882b19e7d98eb759a39e42333b4
Group:		Development/Languages
URL:		http://rubyforge.org/projects/activeresource/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarc only because of ruby packaging
%define		_enable_debug_packages	0

%description
Wraps web resources in model classes that can be manipulated through
XML over REST.

%package rdoc
Summary:	Documentation files for ActiveResource
Group:		Documentation

%description rdoc
Documentation files for ActiveResource.

%prep
%setup -q -n activeresource-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{ruby_rubylibdir}/active_resource.rb
%{ruby_rubylibdir}/activeresource.rb
%{ruby_rubylibdir}/active_resource

%files rdoc
%defattr(644,root,root,755)
%{ruby_ridir}/ri/ActiveResource
