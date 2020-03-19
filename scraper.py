import requests, re, sys

if __name__ == "__main__": 
    # argv[1] target_url
    # argv[2] regex
    # argv[3] output_file
    print('requesting: ' + sys.argv[1])
    resp = requests.get(sys.argv[1])
    resp_text = resp.text
    regex = sys.argv[2]
    print('matching: ' + resp_text[0:100] + ' ...' + '\nwith ' + regex)
    result = re.search(regex, resp_text)

    if result:
        print("Search successful: " + result.group(0))
        f = open(sys.argv[3], "w+")
        f.write(result.group(0))
    else:
        print("search unsuccessful.")


