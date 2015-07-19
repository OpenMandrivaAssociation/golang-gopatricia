%define debug_package   %{nil}
%define import_path     github.com/tchap/go-patricia
%define gosrc %{go_dir}/src/pkg/%{import_path}

Name:           golang-gopatricia
Version:        1.0.1
Release:        4
Summary:        A generic patricia trie (also called radix tree) implemented in Go (Golang)
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
BuildRequires:  golang
Requires:       golang
Group:		Development/Other
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/patricia) = %{version}-%{release}
BuildArch:	noarch

%description
A generic patricia trie (also called radix tree) implemented in Go (Golang)

%prep
%setup -n go-patricia-%{version}

%build

%install
for d in patricia; do
    install -d -p %{buildroot}/%{gosrc}/$d
    cp -av $d/*.go %{buildroot}/%{gosrc}/$d
done

%check

%files
%doc LICENSE README.md
%dir %attr(755,root,root) %{gosrc}/patricia
%{gosrc}/patricia/*.go
