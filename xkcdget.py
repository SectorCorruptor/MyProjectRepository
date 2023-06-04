import requests
import shutil
import sys

class ExistenceError(Exception):
    pass

def get_xkcd(no=None):
    if no is None:
        t = requests.get("https://xkcd.com").text
    else:
        t = requests.get("https://xkcd.com/%d" % no).text
    start = t.find("Image URL (for hotlinking/embedding):")
    end = t.find("\n", start)
    line = t[start:end]
    link = line[line.find("\""):line.find("\"",line.find("\"")+1)][1:]
    try:
        open(link[29:])
    except:
        response = requests.get(link, stream=True)
        with open(link[29:], 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        out_file.close()
    else:
        print("File already exists, open %s" % (__file__[:-11] + link[29:]), file=sys.stderr)
        raise ExistenceError("File already exists, open %s" % (__file__[:-11] + link[29:]))

def get_all_xkcds(begin=None):
    t = requests.get("https://xkcd.com").text
    start = t.find("Permanent link to this comic: ")
    end = t.find("\n", start)
    line = t[start:end]
    link = line[line.find("\""):line.find("\"",line.find("\"")+1)][1:]
    amt = int(link[link.rfind("/")+1:])
    for i in range(begin if begin is not None else 1, amt+1):
        if not i == 404:
            try:
                get_xkcd(i)
            except ExistenceError:
                continue
            except:
                print("Unknown error while loading xkcd %d" % i, file=sys.stderr)
            else:
                print("Successfully loaded xkcd %d" % i)
                continue
    
    
if __name__ == '__main__':
    get_xkcd()
