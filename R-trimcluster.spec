%global packname  trimcluster
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1_2
Release:          1
Summary:          Cluster analysis with trimming
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-fpc 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-fpc 

%description
Trimmed k-means clustering.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
