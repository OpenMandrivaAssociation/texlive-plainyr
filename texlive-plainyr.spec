Name:		texlive-plainyr
Version:	52783
Release:	2
Summary:	Plain bibliography style, sorted by year first
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plainyr
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainyr.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a version of the standard plain BibTeX style, modified
to sort chronologically (by year) first, then by author, title,
etc. (The style's name isn't what the author submitted: it was
renamed for clarity.)

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/plainyr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
