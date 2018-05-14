# Completed Unit 5 - built search engine that can respond to queries quickly, no matter how large the index gets.


# Getting url from the Internet
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

# Returning first link and end position of the link
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Union two arrays
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

# Extracting all links from requested page
def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# starting web crawling on a particular url
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {} #starting with empty dictionary
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index


# Adding funtions for indexing and crawled pages


# Adding word to the index
def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        # not found, add new keyword to index
        index[keyword] = [url]

# Help function that search the index for the keyword
def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

# splitting page into words and adds them to index
def add_page_to_index(index,url,content):
    words = content.split()
    for keyword in words:
        add_to_index(index,keyword,url)

# recording cliks on a particular link
def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] += 1
