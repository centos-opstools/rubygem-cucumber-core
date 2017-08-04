# Generated from cucumber-core-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-core

Name: rubygem-%{gem_name}
Version: 1.5.0
Release: 1%{?dist}
Summary: Core library for the Cucumber BDD app
Group: Development/Languages
License: MIT
URL: http://cukes.info
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
Requires: rubygem(backports) >= 3.6
Requires: rubygem(backports) < 4
Requires: rubygem(gherkin) >= 4.0
Requires: rubygem(gherkin) < 5
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(rspec) >= 3
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(unindent) >= 1.0
# BuildRequires: rubygem(kramdown) >= 1.4.2
# BuildRequires: rubygem(kramdown) < 1.5
# BuildRequires: rubygem(yard)
# BuildRequires: rubygem(coveralls) >= 0.7
# BuildRequires: rubygem(coveralls) < 1
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Core library for the Cucumber BDD app.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.coveralls.yml
%{gem_instdir}/.rspec
%{gem_instdir}/.ruby-gemset
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber-core.gemspec
%{gem_instdir}/spec

%changelog
* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 1.5.0-1
- still need version 1.5.0 for deps
