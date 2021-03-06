#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rails-dom-testing
Version  : 1.0.7
Release  : 11
URL      : https://rubygems.org/downloads/rails-dom-testing-1.0.7.gem
Source0  : https://rubygems.org/downloads/rails-dom-testing-1.0.7.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-minitest
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rails-deprecated_sanitizer
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
# Rails::Dom::Testing
[![Build Status](https://travis-ci.org/rails/rails-dom-testing.svg)](https://travis-ci.org/rails/rails-dom-testing)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rails-dom-testing-1.0.7
gem spec %{SOURCE0} -l --ruby > rubygem-rails-dom-testing.gemspec

%build
gem build rubygem-rails-dom-testing.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rails-dom-testing-1.0.7.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/rails-dom-testing-1.0.6  && sed -i "/\.test_order/ s/^/#/" test/test_helper.rb && ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rails-dom-testing-1.0.7.gem
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails-dom-testing.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions/dom_assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions/selector_assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions/selector_assertions/count_describable.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions/selector_assertions/html_selector.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions/selector_assertions/substitution_context.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/assertions/tag_assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/lib/rails/dom/testing/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/test/dom_assertions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/test/selector_assertions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/test/tag_assertions_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-dom-testing-1.0.7/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rails-dom-testing-1.0.7.gemspec
