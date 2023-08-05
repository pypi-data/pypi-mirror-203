from bs4 import BeautifulSoup
import requests
import socket
import ipaddress





class NetPack(object):
    class ServerLocation(object):
        AFRINIC = 'whois.afrinic.net'
        ARIN = 'whois.arin.net'
        APNIC = 'whois.apnic.net'
        LACNIC = 'whois.lacnic.net'
        RIPE_NCC = 'whois.ripe.net'
        IANA = 'whois.iana.org'
        RADB = 'https://www.radb.net/query?keywords='

    FLAG_HELP = """
        For query_flags
        ARIN: https://www.arin.net/resources/registry/whois/rws/cli/#using-flags
        AFRINIC: https://www.afrinic.net/support/whois/manual
        APNIC: https://www.apnic.net/manage-ip/using-whois/searching/query-options/
        RIPR_NCC: https://apps.db.ripe.net/docs/13.Types-of-Queries/
        LACNIC & IANA, no specific instructions
    """
    WHOIS_PORT = 43
    SOCKET_TIMEOUT = 5

    @staticmethod
    def is_valid_ipv4(ip: str) -> bool:
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    @staticmethod
    def is_valid_ipv6_address(ipv6: str) -> bool:
        try:
            ipaddress.IPv6Address(ipv6)
            return True
        except ipaddress.AddressValueError:
            return False

    @staticmethod
    def is_cidr_ipv4(cidr_str: str) -> bool:
        try:
            ipaddress.IPv4Network(cidr_str, strict=False)
            return True
        except ValueError:
            return False

    @staticmethod
    def inr(server: str, ipv4v6: str, query_flags: str = None) -> str:

        try:
            # Establish a TCP connection to the whois server
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(NetPack.SOCKET_TIMEOUT)
            s.connect((server, NetPack.WHOIS_PORT))

            # Send the query string and receive the response
            s.sendall((query_flags if query_flags else '' + ' ' + ipv4v6 + ' \r\n').encode('utf-8'))

            # Receive the response from the WHOIS server
            response = b''
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data
            s.close()
        except Exception as e:
            return e.__str__()

            # Print the response
        return response.decode('utf-8')

    @staticmethod
    def radb(ip):
        # Make a request to the webpage
        url = NetPack.ServerLocation.RADB + ip
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the title tag and extract its text
        radb_information_meta = soup.find_all("pre")

        # You can extract the information by below code.
        radb_information = ''
        for item in radb_information_meta:
            radb_information += item.text + '\r\r\n\n'

        return radb_information
