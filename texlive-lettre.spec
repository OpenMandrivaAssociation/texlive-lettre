%global tl_name lettre
%global tl_revision 54722

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.002
Release:	%{tl_revision}.1
Summary:	Letters and faxes in French
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lettre
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lettre.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lettre.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Developed from the ancestor of the standard letter class, at the
Observatoire de Geneve.

