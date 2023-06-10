# PORTSWIGGER Web Security Academy Scripts

![WebSecurityAcademy](Portswigger.png)

FOR EDUCATIONAL PURPOSE ONLY

Written in python3, these scripts would probably have been cleaner.
Feel free to hack and improve them to your liking. 


**Usages:**

```bash
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net <YOUR_PAYLOAD>
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net SOLUTION
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net "SOLUTION1"
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net 'SOLUTION2'
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net $(cat <YOUR_PAYLOAD_FILE>)

python3 exploit-lab01.py <TARGET> <ATTACKER>
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net https://xxxxxxxxxx.exploit-server.net
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net https://xxxxxxxxxx.exploit-server.net SOLUTION
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net https://xxxxxxxxxx.exploit-server.net $(cat <YOUR_PAYLOAD_FILE>)

python3 exploit-lab01.py <TARGET> <ATTACKER> <COLLABORATOR>
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net https://xxxxxxxxxx.exploit-server.net xxxxxxxxxx.oastify.com
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net https://xxxxxxxxxx.exploit-server.net xxxxxxxxxx.oastify.com SOLUTION
python3 exploit-lab01.py https://xxxxxxxxxx.web-security-academy.net https://xxxxxxxxxx.exploit-server.net xxxxxxxxxx.oastify.com $(cat <YOUR_PAYLOAD_FILE>)
```



**Categories:**
- [SQL Injection](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/SQLInjection#sql-injection): 17/17
- [XSS (Cross-Site Scripting)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/XSS#xss): 30/30
- [CSRF (Cross-Site Request Forgery)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/CSRF#csrf): 12/12
- [ClickJacking](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/ClickJacking#clickjacking): 5/5
- [DOM-Based XSS](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/DOMBasedXSS#dombasedxss): 7/7
- [CORS (Cross-Origin Resource Sharing)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/CORS#cors): 3/4
- [XXE (XML External Entity injection)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/XXE#xxe): 9/9
- [SSRF (Server-Side Request Forgery)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/SSRF#ssrf): 7/7
- [HTTP Request Smuggling](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/RequestSmuggling#http-request-smuggling): 22/22
- [OS Command Injection](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/OSCommandInjection/#os-command-injection) 5/5
- [SSTI (Server-Side Template Injection)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/SSTI/#ssti) 7/7
- [Directory Traversal](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/DirectoryTraversal/#directory-traversal) 6/6
- [Access Control Vulnerabilities](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/AccessControl/#access-control) 13/13
- [Authentication](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/Authentication/#authentication) 14/14
- [Websockets](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/Websockets/#websockets) 3/3
- [Web Cache Poisoning](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/WebCachePoisoning/#web-cache-poisoning) 13/13
- [Insecure Deserialization](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/InsecureDeserialization/#insecure-deserialization) 10/10
- [Information Disclosure](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/InformationDisclosure/#information-disclosure) 5/5
- [Business Logic](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/BusinessLogic/#business-logic) 11/11
- [Host Header](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/HostHeader/#host-header) 7/7
- [OAuth](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/OAuth/#oauth) 6/6
- [File Upload](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/FileUpload/#file-upload) 7/7
- [JWT (JSON Web Token)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/JWT/#jwt) 2/8


## [SQL Injection](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/SQLInjection#sql-injection)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab01.py)

Lab: [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab02.py)

Lab: [SQL injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab03.py)
Lab: [SQL injection UNION attack, determining the number of columns returned by the query](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab04.py)

Lab: [SQL injection UNION attack, finding a column containing text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab05.py)

Lab: [SQL injection UNION attack, retrieving data from other tables](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab06.py)

Lab: [SQL injection UNION attack, retrieving multiple values in a single column](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab07.py)

Lab: [SQL injection attack, querying the database type and version on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab08.py)

Lab: [SQL injection attack, querying the database type and version on MySQL and Microsoft](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft)

Difficulty: PRACTITIONER


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab09.py)

Lab: [SQL injection attack, listing the database contents on non-Oracle databases](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)

Difficulty: PRACTITIONER


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab10.py)

Lab: [SQL injection attack, listing the database contents on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab11.py)

Lab: [Blind SQL injection with conditional responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)

Difficulty: PRACTITIONER


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab12.py)

Lab: [Blind SQL injection with conditional errors](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors)

Difficulty: PRACTITIONER


### [**Script 13**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab13.py)

Lab: [Visible error-based SQL injection](https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based)

Difficulty: PRACTITIONER


### [**Script 14**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab14.py)

Lab: [Blind SQL injection with time delays](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays)

Difficulty: PRACTITIONER


### [**Script 15**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab15.py)

Lab: [Blind SQL injection with time delays and information retrieval](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)

Difficulty: PRACTITIONER


### [**Script 16**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab16.py)

Lab: [Blind SQL injection with out-of-band interaction](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band)

Difficulty: PRACTITIONER

- Requires Burp Collaborator (BurpSuite Pro)


### [**Script 17**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab17.py)

Lab: [Blind SQL injection with out-of-band data exfiltration](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration)

Difficulty: PRACTITIONER

- Requires Burp Collaborator (BurpSuite Pro)


### [**Script 18**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SQLInjection/exploit-lab18.py)

Lab: [SQL injection with filter bypass via XML encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)

Difficulty: PRACTITIONER



## [XSS (Cross-Site Scripting)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/XSS#xss)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab01.py)

Lab: [Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab02.py)

Lab: [Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab03.py)

Lab: [DOM XSS in document.write sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)

Difficulty: APPRENTICE


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab04.py)

Lab: [DOM XSS in innerHTML sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)

Difficulty: APPRENTICE


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab05.py)

Lab: [DOM XSS in jQuery anchor href attribute sink using location.search source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)

Difficulty: APPRENTICE


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab06.py)

Lab: [DOM XSS in jQuery selector sink using a hashchange event](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)

Difficulty: APPRENTICE


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab07.py)

Lab: [Reflected XSS into attribute with angle brackets HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)

Difficulty: APPRENTICE


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab08.py)

Lab: [Stored XSS into anchor href attribute with double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)

Difficulty: APPRENTICE


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab09.py)

Lab: [Reflected XSS into a JavaScript string with angle brackets HTML encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)

Difficulty: APPRENTICE


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab10.py)

Lab: [DOM XSS in document.write sink using source location.search inside a select element](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab11.py)

Lab: [DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression)

Difficulty: PRACTITIONER


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab12.py)

Lab: [Reflected DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected)

Difficulty: PRACTITIONER


### [**Script 13**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab13.py)

Lab: [Stored DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored)

Difficulty: PRACTITIONER


### [**Script 14**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab14.py)

Lab: [Exploiting cross-site scripting to steal cookies](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-stealing-cookies)

Difficulty: PRACTITIONER

- Requires Burp Collaborator (BurpSuite Pro)


### [**Script 15**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab15.py)

Lab: [Exploiting cross-site scripting to capture passwords](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-capturing-passwords)

Difficulty: PRACTITIONER

- Requires Burp Collaborator (BurpSuite Pro)


### [**Script 16**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab16.py)

Lab: [Exploiting XSS to perform CSRF](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-perform-csrf)

Difficulty: PRACTITIONER


### [**Script 17**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab17.py)

Lab: [Reflected XSS into HTML context with most tags and attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked)

Difficulty: PRACTITIONER


### [**Script 18**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab18.py)

Lab: [Reflected XSS into HTML context with all tags blocked except custom ones](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked)

Difficulty: PRACTITIONER


### [**Script 19**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab19.py)

Lab: [Reflected XSS with some SVG markup allowed](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed)

Difficulty: PRACTITIONER


### [**Script 20**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab20.py)

Lab: [Reflected XSS in canonical link tag](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-canonical-link-tag)

Difficulty: PRACTITIONER


### [**Script 21**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab21.py)

Lab: [Reflected XSS into a JavaScript string with single quote and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped)

Difficulty: PRACTITIONER


### [**Script 22**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab22.py)

Lab: [Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped)

Difficulty: PRACTITIONER


### [**Script 23**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab23.py)

Lab: [Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped)

Difficulty: PRACTITIONER


### [**Script 24**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab24.py)

Lab: [Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-template-literal-angle-brackets-single-double-quotes-backslash-backticks-escaped)

Difficulty: PRACTITIONER


### [**Script 25**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab25.py)

Lab: [Reflected XSS with event handlers and href attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-event-handlers-and-href-attributes-blocked)

Difficulty: EXPERT


### [**Script 26**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab26.py)

Lab: [Reflected XSS in a JavaScript URL with some characters blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-url-some-characters-blocked)

Difficulty: EXPERT


### [**Script 27**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab27.py)

Lab: [Reflected XSS with AngularJS sandbox escape without strings](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-without-strings)

Difficulty: EXPERT


### [**Script 28**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab28.py)

Lab: [Reflected XSS with AngularJS sandbox escape and CSP](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-and-csp)

Difficulty: EXPERT


### [**Script 29**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab29.py)

Lab: [Reflected XSS protected by very strict CSP, with dangling markup attack](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-very-strict-csp-with-dangling-markup-attack)

Difficulty: EXPERT

- Requires Burp Collaborator (BurpSuite Pro)


### [**Script 30**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XSS/exploit-lab30.py)

Lab: [Reflected XSS protected by CSP, with CSP bypass](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-csp-bypass)

Difficulty: EXPERT




## [CSRF (Cross-Site Request Forgery)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/CSRF#csrf)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab01.py)

Lab: [CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab02.py)

Lab: [CSRF where token validation depends on request method](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-request-method)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab03.py)

Lab: [CSRF where token validation depends on token being present](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-token-being-present)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab04.py)

Lab: [CSRF where token is not tied to user session](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-not-tied-to-user-session)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab05.py)

Lab: [CSRF where token is tied to non-session cookie](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-tied-to-non-session-cookie)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab06.py)

Lab: [CSRF where token is duplicated in cookie](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-duplicated-in-cookie)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab07.py)

Lab: [SameSite Lax bypass via method override](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-lax-bypass-via-method-override)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab08.py)

Lab: [SameSite Strict bypass via client-side redirect](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-client-side-redirect)

Difficulty: PRACTITIONER


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab09.py)

Lab: [SameSite Strict bypass via sibling domain](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-sibling-domain)

Difficulty: PRACTITIONER


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab10.py)

Lab: [SameSite Lax bypass via cookie refresh](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-cookie-refresh)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab11.py)

Lab: [CSRF where Referer validation depends on header being present](https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-depends-on-header-being-present)

Difficulty: PRACTITIONER


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab12.py)

Lab: [CSRF with broken Referer validation](https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-broken)

Difficulty: PRACTITIONER




## [ClickJacking](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/ClickJacking#clickjacking)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/ClickJacking/exploit-lab01.py)

Lab: [Basic clickjacking with CSRF token protection](https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/ClickJacking/exploit-lab02.py)

Lab: [Clickjacking with form input data prefilled from a URL parameter](https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/ClickJacking/exploit-lab03.py)

Lab: [Clickjacking with a frame buster script](https://portswigger.net/web-security/clickjacking/lab-frame-buster-script)

Difficulty: APPRENTICE


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab04.py)

Lab: [Exploiting clickjacking vulnerability to trigger DOM-based XSS](https://portswigger.net/web-security/clickjacking/lab-exploiting-to-trigger-dom-based-xss)

Difficulty: PRACTITIONER

### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CSRF/exploit-lab05.py)

Lab: [Multistep clickjacking](https://portswigger.net/web-security/clickjacking/lab-multistep)

Difficulty: PRACTITIONER




## [DOM-Based XSS](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/DOMBasedXSS#dombasedxss)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab01.py)

Lab: [DOM XSS using web messages](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages)

Difficulty: PRACTITIONER


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab02.py)

Lab: [DOM XSS using web messages and a JavaScript URL](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-a-javascript-url)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab03.py)

Lab: [DOM XSS using web messages and JSON.parse](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab04.py)

Lab: [DOM-based open redirection](https://portswigger.net/web-security/dom-based/open-redirection/lab-dom-open-redirection)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab05.py)

Lab: [DOM-based cookie manipulation](https://portswigger.net/web-security/dom-based/cookie-manipulation/lab-dom-cookie-manipulation)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab06.py)

Lab: [Exploiting DOM clobbering to enable XSS](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering)

Difficulty: EXPERT


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DOMBasedXSS/exploit-lab07.py)

Lab: [Clobbering DOM attributes to bypass HTML filters](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters)

Difficulty: EXPERT




## [CORS (Cross-origin Resource Sharing)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/CORS#cors)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CORS/exploit-lab01.py)

Lab: [CORS vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CORS/exploit-lab02.py)

Lab: [CORS vulnerability with trusted null origin](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/CORS/exploit-lab03.py)

Lab: [CORS vulnerability with trusted insecure protocols](https://portswigger.net/web-security/cors/lab-breaking-https-attack)

Difficulty: PRACTITIONER


### **Script 04** **W.I.P.**

Lab: [CORS vulnerability with internal network pivot attack](https://portswigger.net/web-security/cors/lab-internal-network-pivot-attack)

Difficulty: EXPERT




## [XXE (XML External Entity injection)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/XXE#xxe)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab01.py)

Lab: [Exploiting XXE using external entities to retrieve files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab02.py)

Lab: [Exploiting XXE to perform SSRF attacks](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-perform-ssrf)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab03.py)

Lab: [Blind XXE with out-of-band interaction](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab04.py)

Lab: [Blind XXE with out-of-band interaction via XML parameter entities](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction-using-parameter-entities)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab05.py)

Lab: [Exploiting blind XXE to exfiltrate data using a malicious external DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab06.py)

Lab: [Exploiting blind XXE to retrieve data via error messages](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-data-retrieval-via-error-messages)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab07.py)

Lab: [Exploiting XInclude to retrieve files](https://portswigger.net/web-security/xxe/lab-xinclude-attack)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab08.py)

Lab: [Exploiting XXE via image file upload](https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload)

Difficulty: PRACTITIONER

- Requires shutil & pytesseract 

```bash
python3 -m pip install pytest-shutil pytesseract
```


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/XXE/exploit-lab09.py)

Lab: [Exploiting XXE to retrieve data by repurposing a local DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-trigger-error-message-by-repurposing-local-dtd)

Difficulty: EXPERT




## [SSRF (Server-Side Request Forgery)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/SSRF#ssrf)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab01.py)

Lab: [Basic SSRF against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab02.py)

Lab: [Basic SSRF against another back-end system](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab03.py)

Lab: [SSRF with blacklist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-blacklist-filter)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab04.py)

Lab: [SSRF with filter bypass via open redirection vulnerability](https://portswigger.net/web-security/ssrf/lab-ssrf-filter-bypass-via-open-redirection)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab05.py)

Lab: [Blind SSRF with out-of-band detection](https://portswigger.net/web-security/ssrf/blind/lab-out-of-band-detection)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab06.py)

Lab: [SSRF with whitelist-based input filter](https://portswigger.net/web-security/ssrf/lab-ssrf-with-whitelist-filter)

Difficulty: EXPERT


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSRF/exploit-lab07.py)

Lab: [Blind SSRF with Shellshock exploitation](https://portswigger.net/web-security/ssrf/blind/lab-shellshock-exploitation)

Difficulty: EXPERT

- Requires Burp Collaborator (BurpSuite Pro)    NOT TESTED <!>




## [HTTP Request Smuggling](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/RequestSmuggling#http-request-smuggling)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab01.py)

Lab: [HTTP request smuggling, basic CL.TE vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te)

Difficulty: PRACTITIONER


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab02.py)

Lab: [HTTP request smuggling, basic TE.CL vulnerability](https://portswigger.net/web-security/request-smuggling/lab-basic-te-cl)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab03.py)

Lab: [HTTP request smuggling, obfuscating the TE header](https://portswigger.net/web-security/request-smuggling/lab-obfuscating-te-header)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab04.py)

Lab: [HTTP request smuggling, confirming a CL.TE vulnerability via differential responses](https://portswigger.net/web-security/request-smuggling/finding/lab-confirming-cl-te-via-differential-responses)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab05.py)

Lab: [HTTP request smuggling, confirming a TE.CL vulnerability via differential responses](https://portswigger.net/web-security/request-smuggling/finding/lab-confirming-te-cl-via-differential-responses)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab06.py)

Lab: [Exploiting HTTP request smuggling to bypass front-end security controls, CL.TE vulnerability](https://portswigger.net/web-security/request-smuggling/exploiting/lab-bypass-front-end-controls-cl-te)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab07.py)

Lab: [Exploiting HTTP request smuggling to bypass front-end security controls, TE.CL vulnerability](https://portswigger.net/web-security/request-smuggling/exploiting/lab-bypass-front-end-controls-te-cl)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab08.py)

Lab: [Exploiting HTTP request smuggling to reveal front-end request rewriting](https://portswigger.net/web-security/request-smuggling/exploiting/lab-reveal-front-end-request-rewriting)

Difficulty: PRACTITIONER


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab09.py)

Lab: [Exploiting HTTP request smuggling to capture other users' requests](https://portswigger.net/web-security/request-smuggling/exploiting/lab-capture-other-users-requests)

Difficulty: PRACTITIONER


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab10.py)

Lab: [Exploiting HTTP request smuggling to deliver reflected XSS](https://portswigger.net/web-security/request-smuggling/exploiting/lab-deliver-reflected-xss)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab11.py)

Lab: [Response queue poisoning via H2.TE request smuggling](https://portswigger.net/web-security/request-smuggling/advanced/response-queue-poisoning/lab-request-smuggling-h2-response-queue-poisoning-via-te-request-smuggling)

Difficulty: PRACTITIONER


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab12.py)

Lab: [H2.CL request smuggling](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-cl-request-smuggling)

Difficulty: PRACTITIONER


### [**Script 13**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab13.py)

Lab: [HTTP/2 request smuggling via CRLF injection](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-request-smuggling-via-crlf-injection)

Difficulty: PRACTITIONER


### [**Script 14**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab14.py)

Lab: [HTTP/2 request splitting via CRLF injection](https://portswigger.net/web-security/request-smuggling/advanced/lab-request-smuggling-h2-request-splitting-via-crlf-injection)

Difficulty: PRACTITIONER


### [**Script 15**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab15.py)

Lab: [CL.0 request smuggling](https://portswigger.net/web-security/request-smuggling/browser/cl-0/lab-cl-0-request-smuggling)

Difficulty: PRACTITIONER


### [**Script 16**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab16.py)

Lab: [Exploiting HTTP request smuggling to perform web cache poisoning](https://portswigger.net/web-security/request-smuggling/exploiting/lab-perform-web-cache-poisoning)

Difficulty: EXPERT


### [**Script 17**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab17.py)

Lab: [Exploiting HTTP request smuggling to perform web cache deception](https://portswigger.net/web-security/request-smuggling/exploiting/lab-perform-web-cache-deception)

Difficulty: EXPERT


### [**Script 18**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab18.py)

Lab: [Bypassing access controls via HTTP/2 request tunnelling](https://portswigger.net/web-security/request-smuggling/advanced/request-tunnelling/lab-request-smuggling-h2-bypass-access-controls-via-request-tunnelling)

Difficulty: EXPERT


### [**Script 19**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab19.py)

Lab: [Web cache poisoning via HTTP/2 request tunnelling](https://portswigger.net/web-security/request-smuggling/advanced/request-tunnelling/lab-request-smuggling-h2-web-cache-poisoning-via-request-tunnelling)

Difficulty: EXPERT


### [**Script 20**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab20.py)

Lab: [Client-side desync](https://portswigger.net/web-security/request-smuggling/browser/client-side-desync/lab-client-side-desync)

Difficulty: EXPERT


### [**Script 21**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab21.py)

Lab: [Browser cache poisoning via client-side desync](https://portswigger.net/web-security/request-smuggling/browser/client-side-desync/lab-browser-cache-poisoning-via-client-side-desync)

Difficulty: EXPERT


### [**Script 22**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/RequestSmuggling/exploit-lab22.py)

Lab: [Server-side pause-based request smuggling](https://portswigger.net/web-security/request-smuggling/browser/pause-based-desync/lab-server-side-pause-based-request-smuggling)

Difficulty: EXPERT






## [OS Command Injection](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/OSCommandInjection/#os-command-injection)




### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OSCommandInjection/exploit-lab01.py)

Lab: [OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OSCommandInjection/exploit-lab02.py)

Lab: [Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OSCommandInjection/exploit-lab03.py)

Lab: [Blind OS command injection with output redirection](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OSCommandInjection/exploit-lab04.py)

Lab: [Blind OS command injection with out-of-band interaction](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OSCommandInjection/exploit-lab05.py)

Lab: [Blind OS command injection with out-of-band data exfiltration](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration)

Difficulty: PRACTITIONER

- Requires Burp Collaborator (BurpSuite Pro)    NOT TESTED <!>





## [SSTI (Server-Side Template Injection)](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/SSTI/#ssti)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab01.py)

Lab: [Basic server-side template injection](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic)

Difficulty: PRACTITIONER


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab02.py)

Lab: [Basic server-side template injection (code context)](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic-code-context)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab03.py)

Lab: [Server-side template injection using documentation](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-using-documentation)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab04.py)

Lab: [Server-side template injection in an unknown language with a documented exploit](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-in-an-unknown-language-with-a-documented-exploit)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab05.py)

Lab: [Server-side template injection with information disclosure via user-supplied objects](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-with-information-disclosure-via-user-supplied-objects)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab06.py)

Lab: [Server-side template injection in a sandboxed environment](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-in-a-sandboxed-environment)

Difficulty: EXPERT


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/SSTI/exploit-lab07.py)

Lab: [Server-side template injection with a custom exploit](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-with-a-custom-exploit)

Difficulty: EXPERT




## [Directory Traversal](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/DirectoryTraversal/#directory-traversal)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DirectoryTraversal/exploit-lab01.py)

Lab: [File path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DirectoryTraversal/exploit-lab02.py)

Lab: [File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DirectoryTraversal/exploit-lab03.py)

Lab: [File path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DirectoryTraversal/exploit-lab04.py)

Lab: [File path traversal, traversal sequences stripped with superfluous URL-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DirectoryTraversal/exploit-lab05.py)

Lab: [File path traversal, validation of start of path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/DirectoryTraversal/exploit-lab06.py)

Lab: [File path traversal, validation of file extension with null byte bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)

Difficulty: PRACTITIONER




## [Access Control Vulnerabilities](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/AccessControl/#access-control)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab01.py)

Lab: [Unprotected admin functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab02.py)

Lab: [Unprotected admin functionality with unpredictable URL](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab03.py)

Lab: [User role controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)

Difficulty: APPRENTICE


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab04.py)

Lab: [User role can be modified in user profile](https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile)

Difficulty: APPRENTICE


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab05.py)

Lab: [User ID controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)

Difficulty: APPRENTICE


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab06.py)

Lab: [User ID controlled by request parameter, with unpredictable user IDs](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids)

Difficulty: APPRENTICE


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab07.py)

Lab: [User ID controlled by request parameter with data leakage in redirect](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect)

Difficulty: APPRENTICE


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab08.py)

Lab: [User ID controlled by request parameter with password disclosure](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure)

Difficulty: APPRENTICE


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab09.py)

Lab: [Insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)

Difficulty: APPRENTICE


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab10.py)

Lab: [URL-based access control can be circumvented](https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab11.py)

Lab: [Method-based access control can be circumvented](https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented)

Difficulty: PRACTITIONER


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab12.py)

Lab: [Multi-step process with no access control on one step](https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step)

Difficulty: PRACTITIONER


### [**Script 13**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/AccessControl/exploit-lab13.py)

Lab: [Referer-based access control](https://portswigger.net/web-security/access-control/lab-referer-based-access-control)

Difficulty: PRACTITIONER




## [Authentication](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/Authentication/#authentication)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab01.py)

Lab: [Username enumeration via different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab02.py)

Lab: [2FA simple bypass](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab03.py)

Lab: [Password reset broken logic](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-broken-logic)

Difficulty: APPRENTICE


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab04.py)

Lab: [Username enumeration via subtly different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab05.py)

Lab: [Username enumeration via response timing](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab06.py)

Lab: [Broken brute-force protection, IP block](https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab07.py)

Lab: [Username enumeration via account lock](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab08.py)

Lab: [2FA broken logic](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-broken-logic)

Difficulty: PRACTITIONER


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab09.py)

Lab: [Brute-forcing a stay-logged-in cookie](https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie)

Difficulty: PRACTITIONER


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab10.py)

Lab: [Offline password cracking](https://portswigger.net/web-security/authentication/other-mechanisms/lab-offline-password-cracking)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab11.py)

Lab: [Password reset poisoning via middleware](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware)

Difficulty: PRACTITIONER


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab12.py)

Lab: [Password brute-force via password change](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-brute-force-via-password-change)

Difficulty: PRACTITIONER


### [**Script 13**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab13.py)

Lab: [Broken brute-force protection, multiple credentials per request](https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request)

Difficulty: EXPERT


### [**Script 14**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Authentication/exploit-lab14.py)

Lab: [2FA bypass using a brute-force attack](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-bypass-using-a-brute-force-attack)

Difficulty: EXPERT




## [Websockets](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/Websockets/#websockets)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Websockets/exploit-lab01.py)

Lab: [Manipulating WebSocket messages to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Websockets/exploit-lab02.py)

Lab: [Manipulating the WebSocket handshake to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/Websockets/exploit-lab03.py)

Lab: [Cross-site WebSocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab)

Difficulty: PRACTITIONER






## [Web Cache Poisoning](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/WebCachePoisoning/#web-cache-poisoning)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab01.py)

Lab: [Web cache poisoning with an unkeyed header](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header)

Difficulty: PRACTITIONER


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab02.py)

Lab: [Web cache poisoning with an unkeyed cookie](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-cookie)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab03.py)

Lab: [Web cache poisoning with multiple headers](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-multiple-headers)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab04.py)

Lab: [Targeted web cache poisoning using an unknown header](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-targeted-using-an-unknown-header)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab05.py)

Lab: [Web cache poisoning via an unkeyed query string](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-unkeyed-query)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab06.py)

Lab: [Web cache poisoning via an unkeyed query parameter](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-unkeyed-param)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab07.py)

Lab: [Parameter cloaking](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-param-cloaking)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab08.py)

Lab: [Web cache poisoning via a fat GET request](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-fat-get)

Difficulty: PRACTITIONER


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab09.py)

Lab: [URL normalization](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-normalization)

Difficulty: PRACTITIONER


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab10.py)

Lab: [Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-to-exploit-a-dom-vulnerability-via-a-cache-with-strict-cacheability-criteria)

Difficulty: EXPERT


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab11.py)

Lab: [Combining web cache poisoning vulnerabilities](https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-combining-vulnerabilities)

Difficulty: EXPERT


### [**Script 12**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab12.py)

Lab: [Cache key injection](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-cache-key-injection)

Difficulty: EXPERT


### [**Script 13**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/WebCachePoisoning/exploit-lab13.py)

Lab: [Internal cache poisoning](https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws/lab-web-cache-poisoning-internal)

Difficulty: EXPERT





## [Insecure Deserialization](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/InsecureDeserialization/#insecure-deserialization)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab01.py)

Lab: [Modifying serialized objects](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-objects)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab02.py)

Lab: [Modifying serialized data types](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-data-types)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab03.py)

Lab: [Using application functionality to exploit insecure deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-application-functionality-to-exploit-insecure-deserialization)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab04.py)

Lab: [Arbitrary object injection in PHP](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-arbitrary-object-injection-in-php)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab05.py)

Lab: [Exploiting Java deserialization with Apache Commons](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-java-deserialization-with-apache-commons)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab06.py)

Lab: [Exploiting PHP deserialization with a pre-built gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-php-deserialization-with-a-pre-built-gadget-chain)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab07.py)

Lab: [Exploiting Ruby deserialization using a documented gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-exploiting-ruby-deserialization-using-a-documented-gadget-chain)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab08.py)

Lab: [Developing a custom gadget chain for Java deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-java-deserialization)

Difficulty: EXPERT


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab09.py)

Lab: [Developing a custom gadget chain for PHP deserialization](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-php-deserialization)

Difficulty: EXPERT


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InsecureDeserialization/exploit-lab10.py)

Lab: [Using PHAR deserialization to deploy a custom gadget chain](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-using-phar-deserialization-to-deploy-a-custom-gadget-chain)

Difficulty: EXPERT






## [Information Disclosure](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/InformationDisclosure/#information-disclosure)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InformationDisclosure/exploit-lab01.py)

Lab: [Information disclosure in error messages](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InformationDisclosure/exploit-lab02.py)

Lab: [Information disclosure on debug page](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InformationDisclosure/exploit-lab03.py)

Lab: [Source code disclosure via backup files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files)

Difficulty: APPRENTICE


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InformationDisclosure/exploit-lab04.py)

Lab: [Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)

Difficulty: APPRENTICE


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/InformationDisclosure/exploit-lab05.py)

Lab: [Information disclosure in version control history](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history)

Difficulty: PRACTITIONER





## [Business Logic](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/BusinessLogic/#business-logic)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab01.py)

Lab: [Excessive trust in client-side controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab02.py)

Lab: [High-level logic vulnerability](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab03.py)

Lab: [High-level logic vulnerability](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level)

Difficulty: APPRENTICE


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab04.py)

Lab: [Flawed enforcement of business rules](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-flawed-enforcement-of-business-rules)

Difficulty: APPRENTICE


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab05.py)

Lab: [Low-level logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-low-level)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab06.py)

Lab: [Inconsistent handling of exceptional input](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-handling-of-exceptional-input)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab07.py)

Lab: [Weak isolation on dual-use endpoint](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint)

Difficulty: PRACTITIONER


### [**Script 08**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab08.py)

Lab: [Insufficient workflow validation](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-insufficient-workflow-validation)

Difficulty: PRACTITIONER


### [**Script 09**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab09.py)

Lab: [Authentication bypass via flawed state machine](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine)

Difficulty: PRACTITIONER


### [**Script 10**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab10.py)

Lab: [Infinite money logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money)

Difficulty: PRACTITIONER


### [**Script 11**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab11.py)

Lab: [Authentication bypass via encryption oracle](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-encryption-oracle)

Difficulty: PRACTITIONER




## [Host Header](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/HostHeader/#host-header)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab01.py)

Lab: [Basic password reset poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-basic-password-reset-poisoning)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab02.py)

Lab: [Host header authentication bypass](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-authentication-bypass)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab03.py)

Lab: [Web cache poisoning via ambiguous requests](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-web-cache-poisoning-via-ambiguous-requests)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab04.py)

Lab: [Routing-based SSRF](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-routing-based-ssrf)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab05.py)

Lab: [SSRF via flawed request parsing](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-ssrf-via-flawed-request-parsing)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab06.py)

Lab: [Host validation bypass via connection state attack](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-host-validation-bypass-via-connection-state-attack)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/BusinessLogic/exploit-lab07.py)

Lab: [Password reset poisoning via dangling markup](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-password-reset-poisoning-via-dangling-markup)

Difficulty: EXPERT




## [OAuth](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/OAuth/#oauth)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OAuth/exploit-lab01.py)

Lab: [Authentication bypass via OAuth implicit flow](https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OAuth/exploit-lab02.py)

Lab: [Forced OAuth profile linking](https://portswigger.net/web-security/oauth/lab-oauth-forced-oauth-profile-linking)

Difficulty: PRACTITIONER


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OAuth/exploit-lab03.py)

Lab: [OAuth account hijacking via redirect_uri](https://portswigger.net/web-security/oauth/lab-oauth-account-hijacking-via-redirect-uri)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OAuth/exploit-lab04.py)

Lab: [Stealing OAuth access tokens via an open redirect](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-an-open-redirect)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OAuth/exploit-lab05.py)

Lab: [SSRF via OpenID dynamic client registration](https://portswigger.net/web-security/oauth/openid/lab-oauth-ssrf-via-openid-dynamic-client-registration)

Difficulty: PRACTITIONER


### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/OAuth/exploit-lab06.py)

Lab: [Stealing OAuth access tokens via a proxy page](https://portswigger.net/web-security/oauth/lab-oauth-stealing-oauth-access-tokens-via-a-proxy-page)

Difficulty: EXPERT





## [File Upload](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/FileUpload/#file-upload)



### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab01.py)

Lab: [Remote code execution via web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab02.py)

Lab: [Web shell upload via Content-Type restriction bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass)

Difficulty: APPRENTICE


### [**Script 03**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab03.py)

Lab: [Web shell upload via path traversal](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-path-traversal)

Difficulty: PRACTITIONER


### [**Script 04**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab04.py)

Lab: [Web shell upload via extension blacklist bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass)

Difficulty: PRACTITIONER


### [**Script 05**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab05.py)

Lab: [Web shell upload via obfuscated file extension](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension)

Difficulty: PRACTITIONER



### [**Script 06**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab06.py)

Lab: [Remote code execution via polyglot web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-polyglot-web-shell-upload)

Difficulty: PRACTITIONER


### [**Script 07**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/FileUpload/exploit-lab07.py)

Lab: [Web shell upload via race condition](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition)

Difficulty: EXPERT






## [JWT](https://github.com/gwyomarch/WebSecurityAcademy/tree/main/JWT/#jwt)


### [**Script 01**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/JWT/exploit-lab01.py)

Lab: [JWT authentication bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)

Difficulty: APPRENTICE


### [**Script 02**](https://github.com/gwyomarch/WebSecurityAcademy/blob/main/JWT/exploit-lab02.py)

Lab: [JWT authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)

Difficulty: APPRENTICE



...

