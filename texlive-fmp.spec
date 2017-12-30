# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fmp
# catalog-date 2007-01-04 00:44:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-fmp
Version:	20170414
Release:	1
Summary:	Include Functional MetaPost in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fmp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fmp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fmp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fmp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive fmp package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fmp/fmp.sty
%doc %{_texmfdistdir}/doc/latex/fmp/README
%doc %{_texmfdistdir}/doc/latex/fmp/fmp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fmp/fmp-doc.hs
%doc %{_texmfdistdir}/source/latex/fmp/fmp.dtx
%doc %{_texmfdistdir}/source/latex/fmp/fmp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070104-2
+ Revision: 751982
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070104-1
+ Revision: 718467
- texlive-fmp
- texlive-fmp
- texlive-fmp
- texlive-fmp

