# https://github.com/public-apis/public-apis/tree/master
from apiify.GetContent import GetContent
# from apiify.BuildSoup import BuildSoup
from apiify.Driver import Driver
# from new_folder.dynamic_methods import dynamic_method

def main(url, names):
    gc = GetContent(names, url)
    res = gc.extract()
    before = gc.result
    res_dicts = [metadata.model_dump() for metadata in res]
    print(res_dicts)
    driver = Driver(res_dicts, url, gc.result)
    driver.run()
if __name__ == '__main__':
    """
    Allowed types:
    - string
    - int
    - float
    - bool
    - list (this will be a special case, we will compback to it)
    """
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    names = ['Movie Title', 'Tomatometer']
    nems = {'Movie Title': 'string', 'Tomatometer': 'string', 'In Theaters': 'bool'}
    main(url, nems)