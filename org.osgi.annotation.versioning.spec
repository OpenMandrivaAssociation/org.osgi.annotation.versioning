Name: org.osgi.annotation.versioning
Version: 1.1.0
Release: 2
Group: Development/Java
Summary: An implementation of the org.osgi.annotation.versioning API
Source0: https://repo1.maven.org/maven2/org/osgi/org.osgi.annotation.versioning/%{version}/org.osgi.annotation.versioning-%{version}-sources.jar
Source1: https://repo1.maven.org/maven2/org/osgi/org.osgi.annotation.versioning/%{version}/org.osgi.annotation.versioning-%{version}.pom
License: BSD
BuildRequires: jdk-current
BuildRequires: javapackages-local
BuildArch: noarch

%description
OSGi Companion Code for org.osgi.annotation.versioning

%package javadoc
Summary: Javadoc documentation for org.osgi.annotation.versioning
Group: Development/Java

%description javadoc
Javadoc documentation for org.osgi.annotation.versioning

%prep
%autosetup -p1 -c %{name}-%{version}

%build
. %{_sysconfdir}/profile.d/90java.sh
export PATH=$JAVA_HOME/bin:$PATH

cat >module-info.java <<'EOF'
module org.osgi.annotation.versioning {
	exports org.osgi.annotation.versioning;
}
EOF
find . -name "*.java" |xargs javac
find . -name "*.class" -o -name "*.properties" |xargs jar cf org.osgi.annotation.versioning-%{version}.jar META-INF
javadoc -d docs -sourcepath . org.osgi.annotation.versioning
cp %{S:1} .

%install
mkdir -p %{buildroot}%{_javadir}/modules %{buildroot}%{_mavenpomdir} %{buildroot}%{_javadocdir}
cp org.osgi.annotation.versioning-%{version}.jar %{buildroot}%{_javadir}
cp *.pom %{buildroot}%{_mavenpomdir}/
%add_maven_depmap org.osgi.annotation.versioning-%{version}.pom org.osgi.annotation.versioning-%{version}.jar
cp -a docs %{buildroot}%{_javadocdir}/%{name}
mv %{buildroot}%{_javadir}/*.jar %{buildroot}%{_javadir}/modules/
ln -s modules/org.osgi.annotation.versioning-%{version}.jar %{buildroot}%{_javadir}
ln -s modules/org.osgi.annotation.versioning-%{version}.jar %{buildroot}%{_javadir}/org.osgi.annotation.versioning.jar

%files -f .mfiles
%{_javadir}/*.jar
%{_javadir}/modules/*.jar

%files javadoc
%{_javadocdir}/%{name}
