# PORTSWIGGER Web Security Academy Scripts

![WebSecurityAcademy](Portswigger.png)

FOR EDUCATIONAL PURPOSE ONLY

Written in python3, these scripts would probably have been cleaner.
Feel free to hack and improve them to your liking. 


**Usage:**
```bash
python3 exploit-lab01.py https://xxxxxxxxxxxxx.web-security-academy.net <YOUR_PAYLOAD>
python3 exploit-lab01.py https://xxxxxxxxxxxxx.web-security-academy.net SOLUTION
python3 exploit-lab01.py https://xxxxxxxxxxxxx.web-security-academy.net SOLUTION1
python3 exploit-lab01.py https://xxxxxxxxxxxxx.web-security-academy.net SOLUTION2

python3 exploit-lab01.py <TARGET> <ATTACKER>
python3 exploit-lab01.py https://xxxxxxxxxxxxx.web-security-academy.net https://xxxxxxxxxxxxx.exploit-server.net

python3 exploit-lab01.py <TARGET> <ATTACKER> <COLLABORATOR>
python3 exploit-lab01.py https://xxxxxxxxxxxxx.web-security-academy.net https://xxxxxxxxxxxxx.exploit-server.net xxxxxxxxxx.oastify.com
```

## SQL Injection

**Script 01**
[SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)
Difficulty: APPRENTICE

**Script 02**
[SQL injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)
Difficulty: APPRENTICE

**Script 03**
[SQL injection UNION attack, determining the number of columns returned by the query](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)
Difficulty: PRACTITIONER

**Script 04**
[SQL injection UNION attack, finding a column containing text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)
Difficulty: PRACTITIONER

**Script 05**
[SQL injection UNION attack, retrieving data from other tables](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables)
Difficulty: PRACTITIONER

**Script 06**
[SQL injection UNION attack, retrieving multiple values in a single column](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column)
Difficulty: PRACTITIONER

**Script 07**
[SQL injection attack, querying the database type and version on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)
Difficulty: PRACTITIONER

**Script 08**
[SQL injection attack, querying the database type and version on MySQL and Microsoft](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft)
Difficulty: PRACTITIONER

**Script 09**
[SQL injection attack, listing the database contents on non-Oracle databases](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)
Difficulty: PRACTITIONER

**Script 10**
[SQL injection attack, listing the database contents on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)
Difficulty: PRACTITIONER

**Script 11**
[Blind SQL injection with conditional responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)
Difficulty: PRACTITIONER

**Script 12**
[Blind SQL injection with conditional errors](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors)
Difficulty: PRACTITIONER

**Script 13**
[Blind SQL injection with time delays](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays)
Difficulty: PRACTITIONER

**Script 14**
[Blind SQL injection with time delays and information retrieval](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)
Difficulty: PRACTITIONER

**Script 15**
[Blind SQL injection with out-of-band interaction](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band)
Difficulty: PRACTITIONER

**Script 16**
[Blind SQL injection with out-of-band data exfiltration](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration)
Difficulty: PRACTITIONER

**Script 17**
[SQL injection with filter bypass via XML encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)
Difficulty: PRACTITIONER



## XSS

**Script 01**
[Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)
Difficulty: APPRENTICE

**Script 02**
[Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)
Difficulty: APPRENTICE

**Script 03**
[DOM XSS in document.write sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)
Difficulty: APPRENTICE

**Script 04**
[DOM XSS in innerHTML sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)
Difficulty: APPRENTICE

**Script 05**
[DOM XSS in jQuery anchor href attribute sink using location.search source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)
Difficulty: APPRENTICE

**Script 06**
[DOM XSS in jQuery selector sink using a hashchange event](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)
Difficulty: APPRENTICE

**Script 07**
[Reflected XSS into attribute with angle brackets HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)
Difficulty: APPRENTICE

**Script 08**
[Stored XSS into anchor href attribute with double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)
Difficulty: APPRENTICE

**Script 09**
[Reflected XSS into a JavaScript string with angle brackets HTML encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)
Difficulty: APPRENTICE

**Script 10**
[DOM XSS in document.write sink using source location.search inside a select element](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)
Difficulty: PRACTITIONER

**Script 11**
[DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-angularjs-expression)
Difficulty: PRACTITIONER

**Script 12**
[Reflected DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected)
Difficulty: PRACTITIONER

**Script 13**
[Stored DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored)
Difficulty: PRACTITIONER

**Script 14**
[Exploiting cross-site scripting to steal cookies](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-stealing-cookies)
Difficulty: PRACTITIONER

**Script 15**
[Exploiting cross-site scripting to capture passwords](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-capturing-passwords)
Difficulty: PRACTITIONER

**Script 16**
[Exploiting XSS to perform CSRF](https://portswigger.net/web-security/cross-site-scripting/exploiting/lab-perform-csrf)
Difficulty: PRACTITIONER

**Script 17**
[Reflected XSS into HTML context with most tags and attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked)
Difficulty: PRACTITIONER

**Script 18**
[Reflected XSS into HTML context with all tags blocked except custom ones](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked)
Difficulty: PRACTITIONER

**Script 19**
[Reflected XSS with some SVG markup allowed](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed)
Difficulty: PRACTITIONER

**Script 20**
[Reflected XSS in canonical link tag](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-canonical-link-tag)
Difficulty: PRACTITIONER

**Script 21**
[Reflected XSS into a JavaScript string with single quote and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped)
Difficulty: PRACTITIONER

**Script 22**
[Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped)
Difficulty: PRACTITIONER

**Script 23**
[Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped)
Difficulty: PRACTITIONER

**Script 24**
[Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-template-literal-angle-brackets-single-double-quotes-backslash-backticks-escaped)
Difficulty: PRACTITIONER

**Script 25**
[Reflected XSS with event handlers and href attributes blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-event-handlers-and-href-attributes-blocked)
Difficulty: EXPERT

**Script 26**
[Reflected XSS in a JavaScript URL with some characters blocked](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-url-some-characters-blocked)
Difficulty: EXPERT

**Script 27**
[Reflected XSS with AngularJS sandbox escape without strings](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-without-strings)
Difficulty: EXPERT

**Script 28**
[Reflected XSS with AngularJS sandbox escape and CSP](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-and-csp)
Difficulty: EXPERT

**Script 29**
[Reflected XSS protected by very strict CSP, with dangling markup attack](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-very-strict-csp-with-dangling-markup-attack)
Difficulty: EXPERT

**Script 30**
[Reflected XSS protected by CSP, with CSP bypass](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-csp-bypass)
Difficulty: EXPERT