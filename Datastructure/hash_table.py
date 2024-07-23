import string
import secrets

voted = {}
def check_voter(name):
    if(voted.get(name)):
        print("Kick them out")
    else:
        voted[name] = True
        print("Let them vote")


cache = {}
def get_page(url):
    if(cache.get(url)):
        print(f'Cache Hit : {url}')
        return cache[url] # cache hit
    else:
        data = url_generator() # fetch data
        cache[url] = data  # save in cache
        print(data)
        return data

alphabet = string.ascii_letters + string.digits
def url_generator():
    domain = "http://www.example.com/"
    page_path = ''.join(secrets.choice(alphabet) for i in range(15))
    return domain+page_path


get_page("http://www.example.com/LHpooXt721TJqyT")
get_page("http://www.example.com/LHpooXt721TJqyT")
get_page("http://www.example.com/LHposdd721TJqlu")

check_voter("tom")
check_voter("tom")

book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.45

s = "avocado"

