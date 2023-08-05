# Python 3 server example
# https://pythonbasics.org/webserver/
# mod by 44xtc44
import os

import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

try:
    import eisenmp
    import eisenmp.eisenmp_exa_multi_srv_each_cpu as multi_on_each_cpu
    import eisenmp.eisenmp_exa_each_flask_orm_srv_one_cpu as single_on_each_cpu
    import eisenmp.eisenmp_exa_prime as prime
    import eisenmp.eisenmp_exa_web_csv as web_csv
    import eisenmp.eisenmp_exa_http as http_srv
    import eisenmp.eisenmp_exa_double_q as double_q
    import eisenmp.eisenmp_exa_bruteforce as bruteforce

except ImportError:
    import eisenmp_examples
    import eisenmp_examples.eisenmp_exa_multi_srv_each_cpu as multi_on_each_cpu
    import eisenmp_examples.eisenmp_exa_each_flask_orm_srv_one_cpu as single_on_each_cpu
    import eisenmp_examples.eisenmp_exa_prime as prime
    import eisenmp_examples.eisenmp_exa_web_csv as web_csv
    import eisenmp_examples.eisenmp_exa_http as http_srv
    import eisenmp_examples.eisenmp_exa_double_q as double_q
    import eisenmp_examples.eisenmp_exa_bruteforce as bruteforce

hostName = "localhost"
serverPort = 12_321
dir_name = os.path.dirname(__file__)


class Menu:
    example_menu = [
        'Multiple server in each process/CPU core - share a port range - share a DB. Worker Green, Yellow and Blue',
        'Prime Number calculation',
        'Every Flask server in a different process - share a port range - share a DB. Worker Yellow and Blue',
        'Web CSV large list. Average for each chunk of a large list column to simply calc the results later.',
        'One simple http server presents a radio on every process. "Unemployed" worker exit.',
        'Each process has two Queues feed audio and video. Merge in a fake production.',
        'Brute force attack with dictionary and itertools generator'
    ]

    exa_tpl_lst = [
        (0, example_menu[0], multi_on_each_cpu.main),
        (1, example_menu[1], prime.main),
        (2, example_menu[2], single_on_each_cpu.main),
        (3, example_menu[3], web_csv.main),
        (4, example_menu[4], http_srv.main),
        (5, example_menu[5], double_q.main),
        (6, example_menu[6], bruteforce.main)
    ]


def run_http():
    """Blocked, no loop here
    """
    global serverPort

    while 1:
        try:
            webServer = HTTPServer((hostName, serverPort), MyServer)
            break
        except OSError:
            print(f'serverPort in use {serverPort}\n\tadd one to port number')
            serverPort += 1  # port already in use

    print(f"Examples http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        """"""
        # print(self.headers)
        length = int(self.headers.get_all('content-length')[0])
        print(self.headers.get_all('content-length'))
        data_string = self.rfile.read(length)
        example_fun = Menu.exa_tpl_lst[int(data_string)][2]
        ret_val = example_fun()
        # print(data_string)
        self.send_response(200)
        # self.send_header("Content-type", "text/plain")
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.flush_headers()
        json_string = json.dumps(str(ret_val))
        self.wfile.write(bytes(json_string, "utf-8"))
        return True

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        da_html_lst = [

            "<!doctype html><html><html lang='en'>",
            "<head>",
            "<meta charset='UTF-8'>",
            "<meta X-Content-Type-Options='nosniff'>",
            "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
            "<style>",
            "@font-face {font-family: 'PT Sans';font-style: normal;font-weight: normal;",
            "src: local('PT Sans'), local('PTSans-Regular'),",
            "url(data:application/font-woff2;charset=utf-8;base64,d09GRgABAAAAAHowABMAAAAA+OAA) format('woff2');}",

            "body{font-family:PT Sans, arial; color:black;background-color:#ccc;}",
            "h1 {color:brown;text-align:center;}",
            ".container {display: flex;}",
            ".middle {display: flex;flex-direction: column;margin: auto;color:brown;}",
            ".pMid {color: black; text-align:center;}",
            "</style>",
            f"<title>Examples</title>",
            "</head>",

            "<body>",
            f"<h1> Welcome to eisenmp_examples</h1>",
            f"<p class=pMid> Examples run in the terminal window. </p>",
            f"<div class='container'>",
            f"<div class='middle'>",
            '_o__example_buttons____',
            "</div></div>",
            "send: <p id=pRspReturn class=pInOut> </p>",
            f"resp: <p id=pMsg class=pInOut> </p>",
            "</body></html>",

            "<script>",
            "function getExa(radio_btn_id) {",
            "document.getElementById('pMsg').innerHTML='';",
            "const xhr = new XMLHttpRequest();",
            "xhr.open('POST', '/');",
            "xhr.onload = function () {console.log('xhr r ', xhr.response); ",
            "document.getElementById('pMsg').innerHTML=xhr.response;}; ",
            "xhr.send(radio_btn_id);",
            "let pRspReturn = document.getElementById('pRspReturn');",
            "pRspReturn.innerText=radio_btn_id;",
            "}",
            "</script>",
            "</body></html>"
        ]

        for _ in da_html_lst:
            if _ == '_o__example_buttons____':
                for i, _ in enumerate(Menu.exa_tpl_lst):
                    idx = Menu.exa_tpl_lst[i][0]
                    show = Menu.exa_tpl_lst[i][1]
                    exa_html_line = f"<div><label><input type='radio' name='da'" \
                                    f"id='{idx}' onclick='getExa(id)'>{show}</label></div>"
                    self.wfile.write(bytes(exa_html_line, "utf-8"))
                continue
            self.wfile.write(bytes(_, "utf-8"))


def main():
    """
    """
    start = time.perf_counter()

    run_http()

    print('Time in sec: ', round((time.perf_counter() - start)))


if __name__ == '__main__':
    main()
