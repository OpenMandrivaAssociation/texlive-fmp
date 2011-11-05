# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fmp
# catalog-date 2007-01-04 00:44:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-fmp
Version:	20070104
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive fmp package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
