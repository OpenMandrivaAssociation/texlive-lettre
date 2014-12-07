# revision 31879
# category Package
# catalog-ctan /macros/latex/contrib/lettre
# catalog-date 2013-10-10 10:12:24 +0200
# catalog-license lppl
# catalog-version 2.349
Name:		texlive-lettre
Version:	2.349
Release:	8
Summary:	Letters and faxes in French
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lettre
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettre.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lettre.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/lettre/default.ins
%{_texmfdistdir}/tex/latex/lettre/lettre.cls
%doc %{_texmfdistdir}/doc/latex/lettre/ALIRE
%doc %{_texmfdistdir}/doc/latex/lettre/LAST_VERSION
%doc %{_texmfdistdir}/doc/latex/lettre/LICENSE
%doc %{_texmfdistdir}/doc/latex/lettre/README
%doc %{_texmfdistdir}/doc/latex/lettre/amg.ins
%doc %{_texmfdistdir}/doc/latex/lettre/amgmono.eps
%doc %{_texmfdistdir}/doc/latex/lettre/ecusson55.ps
%doc %{_texmfdistdir}/doc/latex/lettre/institut.tpl
%doc %{_texmfdistdir}/doc/latex/lettre/letdoc.pdf
%doc %{_texmfdistdir}/doc/latex/lettre/letdoc.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letdoc2.pdf
%doc %{_texmfdistdir}/doc/latex/lettre/letdoc2.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letdocmain.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex1.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex2.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex3.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex4.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex5.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex6.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex7.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex8.tex
%doc %{_texmfdistdir}/doc/latex/lettre/lettre.tpl
%doc %{_texmfdistdir}/doc/latex/lettre/lppl.txt
%doc %{_texmfdistdir}/doc/latex/lettre/makefile
%doc %{_texmfdistdir}/doc/latex/lettre/obs.ins
%doc %{_texmfdistdir}/doc/latex/lettre/release-notes
%doc %{_texmfdistdir}/doc/latex/lettre/sondes.tex
%doc %{_texmfdistdir}/doc/latex/lettre/telefax.tpl
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxd.tex
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxe.tex
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxf.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
