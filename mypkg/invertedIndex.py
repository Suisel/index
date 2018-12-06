parser = 'html.parser'
page = requests.get(path_to_document).text
soup = BeautifulSoup(page, parser)