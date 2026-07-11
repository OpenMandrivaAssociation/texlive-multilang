%global tl_name multilang
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9b
Release:	%{tl_revision}.1
Summary:	A LaTeX package for maintaining multiple translations of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multilang
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multilang.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multilang.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multilang.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Maintaining a LaTeX document with translations for multiple languages
can be cumbersome and error-prone. This package provides a set of macros
for defining macros and environments as wrappers around existing macros
and environments. These wrappers allow one to clearly specify multiple
translations for the arguments to the wrapped macros and environments
while only the translation of the document's language is actually shown.
Choosing a translation then is as simple as choosing the document's
language via babel or polyglossia.

