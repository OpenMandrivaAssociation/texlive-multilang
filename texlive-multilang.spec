Name:		texlive-multilang
Version:	49065
Release:	2
Summary:	A LaTeX package for maintaining multiple translations of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multilang
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multilang.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multilang.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multilang.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Maintaining a LaTeX document with translations for multiple
languages can be cumbersome and error-prone. This package
provides a set of macros for defining macros and environments
as wrappers around existing macros and environments. These
wrappers allow one to clearly specify multiple translations for
the arguments to the wrapped macros and environments while only
the translation of the document's language is actually shown.
Choosing a translation then is as simple as choosing the
document's language via babel or polyglossia.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/multilang
%{_texmfdistdir}/tex/latex/multilang
%doc %{_texmfdistdir}/doc/latex/multilang

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
