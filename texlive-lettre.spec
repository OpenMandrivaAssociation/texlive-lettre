Name:		texlive-lettre
Version:	54722
Release:	2
Summary:	Letters and faxes in French
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lettre
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettre.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettre.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Developed from the ancestor of the standard letter class, at
the Observatoire de Geneve.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lettre
%doc %{_texmfdistdir}/doc/latex/lettre

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
