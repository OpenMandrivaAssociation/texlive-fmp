Name:		texlive-fmp
Version:	20190228
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
%{_texmfdistdir}/tex/latex/fmp
%doc %{_texmfdistdir}/doc/latex/fmp
#- source
%doc %{_texmfdistdir}/source/latex/fmp

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
