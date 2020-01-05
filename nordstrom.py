from selenium import webdriver
import random
import pandas as pd
import sys


names_df = []
prices_df = []
colors_df = []
sizes_df = []

driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
driver.get('https://shop.nordstrom.com/c/mens-clothing?origin=topnav&breadcrumb=Home%2fMen%2fClothing')

#To get sizes of products from product link
def get_sizes(sizeurl):
    driver1 = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    driver1.get(sizeurl)
    t = True
    ct = 1
    sizes = []
    while t:
        try:
            size = driver1.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/ul/li[{}]/div/div[1]/span'.format(ct)).get_attribute('innerHTML')
            ct += 1
            sizes.append(size)
        except:
            t = False
    driver1.close()
    return sizes

random.seed(20)
prod = random.sample(range(1,15), 3)


for i in prod:
    t = True
    ct = 1
    color = []
    try:
        markdown = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/div[3]/span'.format(i)).text
        name = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/h3/a'.format(i))
        price = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/div[4]/div[2]/span[2]'.format(i))
        print("first block")


    except:
        if driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/div[3]/div[1]/span[1]'.format(i)).get_attribute('innerHTML') == 'Was:':
            name = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/h3/a'.format(i))
            price = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/div[3]/div[2]/span[2]'.format(i))
            print("Second block")
        else:
            name = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/h3/a'.format(i))
            price = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/div[3]/div/span[2]'.format(i))
            print("Third block")
    while t:
        try:
            col = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/div[2]/div/ul/li[{}]/button/span'.format(i, ct))
            ct += 1
            color.append(col.get_attribute('innerHTML'))
        except:
            t = False
    sizeurl = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[5]/div/div/div/section/div/div/div/div/article[{}]/h3/a'.format(i)).get_attribute('href')

    sizes = get_sizes(sizeurl)
    print("Details about article {}".format(i))
    names = name.get_attribute('innerHTML')
    prices = price.get_attribute('innerHTML')
    print(color)
    print(sizes)
    print('\n\n')
    colors_df.append(color)
    sizes_df.append(sizes)
    names_df.append(names)
    prices_df.append(prices)
columns = ['Name of product', 'Price', 'Colors available', 'Size available']

df = pd.DataFrame(list(zip(names_df, prices_df, colors_df, sizes_df)), columns=columns)
df['Sl No.'] = list(range(1,len(df)+1))
df.set_index('Sl No.', inplace=True)
print(df)
df.to_csv('answer.csv')
driver.close()
sys.exit()
