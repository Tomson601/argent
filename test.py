code = 200

main_header = f'HTTP/1.0 {code} OK\r\nContent-type: text/html\r\n\r\n'
headers = [
    "Content-Type: text/html; charset=UTF-8",
    "Cache-Control: max-age=3600, public",
    "Content-Type: text/html; charset=UTF-8",
    "Last-Modified: Sat, 28 Nov 2009 03:50:37 GMT",
    "X-Pingback: https://code.tutsplus.com/xmlrpc.php",
    "Content-Encoding: gzip",
    "Vary: Accept-Encoding, Cookie, User-Agent"]


def __create_combined_headers(main_header, headers):
    combined_header = main_header
    for header in headers:
        combined_header += header + "\n"
    return bytes(combined_header, 'utf-8')


headers = __create_combined_headers(main_header, headers)

print(headers)