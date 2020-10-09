import time

from selenium import webdriver


coockies = [
            {
              "name": "_ga",
              "value": "GA1.2.1919241072.1590922528",
              
            },
            {
              "name": "LF_ID",
              "value": "1590922527689-6611590-1782987",
              
            },
            {
              "name": "GCID",
              "value": "70f4b7c-6a68312-181ec14-7643480",

            },
            {
              "name": "GRID",
              "value": "70f4b7c-6a68312-181ec14-7643480",
              
              
            },
            {
              "name": "GCESS",
              "value": "BQwBAQsCBQADBNeM014IAQMFBAAAAAAEBAAvDQAJAQEHBEXekQ8CBNeM014KBAAAAAAGBOY4LysBCMygHAAAAAAA",
              
              
            },
            {
              "name": "_gid",
              "value": "GA1.2.946170054.1591426860",
              
              
            },
            {
              "name": "Hm_lvt_59c4ff31a9ee6263811b23eb921a5083",
              "value": "1590922528,1591426862,1591434423,1591493676",
              
              
            },
            {
              "name": "_gat",
              "value": "1",
              
              
            },
            {
              "name": "gk_process_ev",
              "value": "{%22count%22:5%2C%22target%22:%22%22}",
              
              
            },
            {
              "name": "Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083",
              "value": "1591494576",
              
              
            }
          ]


def get_html():
    driver = webdriver.Chrome()
    # for coockie in coockies:
    #     driver.add_cookie(coockie)
    driver.implicitly_wait(10)
    driver.get('https://time.geekbang.org/column/article/96570')
    driver.execute_script("(function(){ if(!window.jQuery){ var s = document.createElement('script'); s.type = "
                          "'text/javascript'; s.src = 'https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js'; "
                          "document.body.appendChild(s); } } )();")
    print(driver.get_cookies())
    time.sleep(5)
    ret = driver.execute_script("return typeof jQuery;")

    print(ret)
    ret = driver.execute_script("return (function(){var a = $('div[data-slate-editor]').innerText;return {'text':a};})()")
    print(ret)


get_html()


