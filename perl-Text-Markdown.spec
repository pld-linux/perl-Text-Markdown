#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Text
%define		pnam	Markdown
Summary:	Text::Markdown - Convert Markdown syntax to (X)HTML
Summary(pl.UTF-8):	Text::Markdown - konwersja składni Markdown do (X)HTML-a
Name:		perl-Text-Markdown
Version:	1.000031
Release:	2
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/Text-Markdown-%{version}.tar.gz
# Source0-md5:	88ace17b0debebe88f0ea45a76c397ed
URL:		http://search.cpan.org/dist/Text-Markdown/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Tidy
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format
is most similar to that of plain text email, and supports features
such as headers, *emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use
span-level HTML tags anywhere in a Markdown document, and you can use
block level HTML tags (like <div> and <table> as well).

%description -l pl.UTF-8
Markdown to filtr tekstu do HTML-a. Tłumaczy łatwy w czytaniu i
pisaniu strukturalny format tekstowy do HTML-a. Format tekstowy
Markdown jest dosyć podobny do czysto tekstowych wiadomości
elektronicznych i obsługuje właściwości takie jak nagłówki,
*wyróżnienia*, bloki kodu, bloki cytatów i odnośniki.

Składnia Markdown została zaprojektowana nie jako ogólny język
znaczników, ale tak, żeby służyła za frontend dla (X)HTML-a. Można
używać w dowolnym miejscu dokumentu Markdown znaczników HTML poziomu
linii, a także znaczników HTML poziomu bloków (w tym takich jak <div>
czy <table>).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/Markdown.pl
%{_mandir}/man1/Markdown.pl.1p*
%{_mandir}/man3/Text::Markdown.3pm*
%{perl_vendorlib}/Text/Markdown.pm
