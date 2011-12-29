# revision 21400
# category Package
# catalog-ctan /macros/latex/contrib/lettre
# catalog-date 2007-01-08 22:21:56 +0100
# catalog-license lppl
# catalog-version 2.346
Name:		texlive-lettre
Version:	2.346
Release:	1
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
%{_texmfdistdir}/tex/latex/lettre/lettre.cls_2.346
%{_texmfdistdir}/tex/latex/lettre/obs.ins
%doc %{_texmfdistdir}/doc/latex/lettre/2.346-release-notes
%doc %{_texmfdistdir}/doc/latex/lettre/ALIRE
%doc %{_texmfdistdir}/doc/latex/lettre/LAST_VERSION_IS_2.346
%doc %{_texmfdistdir}/doc/latex/lettre/LICENSE
%doc %{_texmfdistdir}/doc/latex/lettre/README
%doc %{_texmfdistdir}/doc/latex/lettre/institut.tpl
%doc %{_texmfdistdir}/doc/latex/lettre/letdoc.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex1.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex1.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex1.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex2.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex2.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex2.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex3.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex3.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex3.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex4.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex4.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex4.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex5.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex5.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex5.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex6.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex6.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex6.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex7.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex7.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex71.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex72.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex8.odt
%doc %{_texmfdistdir}/doc/latex/lettre/letex8.tex
%doc %{_texmfdistdir}/doc/latex/lettre/letex81.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex82.ps
%doc %{_texmfdistdir}/doc/latex/lettre/letex83.ps
%doc %{_texmfdistdir}/doc/latex/lettre/lettre.tpl
%doc %{_texmfdistdir}/doc/latex/lettre/lppl.txt
%doc %{_texmfdistdir}/doc/latex/lettre/telefax.tpl
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxd.odt
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxd.ps
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxd.tex
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxe.odt
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxe.ps
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxe.tex
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxf.odt
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxf.tex
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxf1.ps
%doc %{_texmfdistdir}/doc/latex/lettre/testfaxf2.ps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
