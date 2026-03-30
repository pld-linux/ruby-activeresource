%define pkgname activeresource
Summary:	Think Active Record for web resources
Name:		ruby-%{pkgname}
Version:	6.2.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7b0de1613a561da41fb461082f593684
URL:		https://rubyonrails.org
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-activemodel >= 7.0
Requires:	ruby-activemodel-serializers-xml >= 1.0
Requires:	ruby-activesupport >= 7.0
Provides:	ruby-ActiveResource
Obsoletes:	ruby-ActiveResource
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wraps web resources in model classes that can be manipulated through
XML over REST.

%package rdoc
Summary:	Documentation files for ActiveResource
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActiveResource.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}

# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MIT-LICENSE README.md
%{ruby_vendorlibdir}/active_resource.rb
%{ruby_vendorlibdir}/active_resource
%{ruby_vendorlibdir}/activeresource.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ActiveResource
%{ruby_ridir}/ThreadsafeAttributes
