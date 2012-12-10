%define __prefix /usr/local


Name: sayhi
Version: %{version}
Release: %{release}%{?dist}
Summary: sayhi
License: LGPL
Url: http://mail.ru
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python2.7 = 2.7.3

Requires: python2.7 = 2.7.3


%description
Just an example how to make python packages for CentOS right.

%prep
if [ -d %{buildroot}%{__prefix}/%{name} ];
then
    echo "Cleaning out stale build directory" 1>&2
    %{__rm} -rf %{buildroot}%{__prefix}/%{name}
fi

rm -rf %{name}-%{version}

git clone --depth=1 --branch=master \
    git://github.com/pzinovkin/sayhi.git \
    %{name}-%{version}
%setup -T -D -n %{name}-%{version}

%build

# creating virtual environment
virtualenv --distribute %{buildroot}%{__prefix}/%{name}

# install
%{buildroot}%{__prefix}/%{name}/bin/pip install \
    --index-url=http://pypi.mail.ru/simple \
    .

# do not include *.pyc in rpm
find %{buildroot}%{__prefix}/%{name}/ -type f -name "*.py[co]" -delete

# fix python path
find %{buildroot}%{__prefix}/%{name}/ -type f \
    -exec sed -i 's:'%{buildroot}'::' {} \;

%install
# compile py files
%{buildroot}%{__prefix}/%{name}/bin/python \
    -m compileall -qf %{buildroot}%{__prefix}/%{name}/

mkdir -p %{buildroot}%{__prefix}/bin/
ln -s %{__prefix}/%{name}/bin/%{name} %{buildroot}%{__prefix}/bin/%{name}

%post
ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{__prefix}/bin/%{name}
%{__prefix}/%{name}/
