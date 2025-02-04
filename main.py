# https://github.com/public-apis/public-apis/tree/master
from apiify.GetContent import GetContent
# from apiify.BuildSoup import BuildSoup
from apiify.Driver import Driver
# from new_folder.dynamic_methods import dynamic_method

def main(url, names):
    gc = GetContent(names, url)
    res = gc.extract()
    res_dicts = [metadata.model_dump() for metadata in res]
    print(res_dicts)
    driver = Driver(res_dicts, url)
    driver.run()

if __name__ == '__main__':
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    names = ['Movie Title', 'Tomatometer']
    main(url, names)