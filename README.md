# <p align="center">Log4shell command generator</p>
<p align="center">
Generate commands for CVE-2021-44228.<br>
<img src="https://i.imgur.com/ziLtORE.png" />
</p>

## Description

This simple script helps to generate command payloads for testing the log4shell vulnerability. 


## How Log4shell works

1. Attacker sets up an LDAP and an HTTP server. 

2. Attacker sends a specially crafted JNDI injection payload, that Log4j (a widely used logging system that Minecraft also uses) understands and executes automatically, as soon as the logger logs a message containing the payload. 

3. The vulnerable system running Log4j then sends a query to the attacker’s LDAP server. The LDAP server tells Log4j to download the Java class file from the attacker’s w

4.Log4j then executes the downloaded Java class.

The vulnerability exists due to the Log4j processor's handling of log messages. Apache Log4j2 versions between 2.0 and 2.14.1 do not protect against attacker-controlled LDAP (Lightweight Directory Access Protocol) and other JNDI (Java Naming and Directory Interface) related endpoints. If an attacker sends a specially crafted message, this may result in the loading of an external code class and the execution of that code (RCE). [via picussecurity](https://www.picussecurity.com/resource/blog/log4j-vulnerability-remediation-with-waf-and-ips-cve-2021-44228#:~:text=The%20CVE%2D2021%2D44228%20is,can%20be%20exploited%20without%20authentication.&text=If%20an%20attacker%20sends%20a,of%20that%20code%20(RCE).)

## Usage

`python log4shell.py --help`
