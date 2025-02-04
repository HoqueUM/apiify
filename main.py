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
    driver = Driver()
    driver.build_soup()
    # print(dynamic_method(res_dicts))
    # bs = BuildSoup(url, gc)
    # bs.add_dynamic_methods(res_dicts)
    # for name in names:
    #     method_name = name.replace(" ", "_").lower()
    #     method = getattr(bs, method_name)
    #     result = method()
    #     if not len(result):
    #         gc.retry()
    #     else:
    #         print(f"{name}: {method()}")

if __name__ == '__main__':
    url = 'https://www.rottentomatoes.com/m/heart_eyes'
    names = ['Movie Title', 'Tomatometer']
    main(url, names)