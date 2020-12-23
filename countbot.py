from selenium import webdriver


PATH = "./assets/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(PATH, options=options)

# xpath for dm group
aya_dm_Xpath = '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/*'
dms_el_list = driver.find_elements_by_xpath(aya_dm_Xpath)
print(len(dms_el_list))






















# commented out 
'''
body_el = driver.find_element_by_css_selector('body')

path = '//article/div/div/p/a[text()="Log in"]
dm_Xpath = '/html/body/div[1]/section/div/div[2]/div/div/div[2]'
dm_elem = driver.find_element_by_xpath(dm_Xpath)
login_el = driver.find_element_by_xpath(path)

<input aria-label="Phone number, username, or email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name= type="text" class="_2hvTZ pexuQ zyHYP" value="">

<inutoput aria-label="Password" aria-required="true" acapitalize="off" autocorrect="off" name="password" type="password" class="_2hvTZ pexuQ zyHYP" value="">

driver.find_element_by_xpath(username_field).send_keys(USERNAME)
driver.find_element_by_xpath(password_field).send_keys(PASSWORD)

driver.find_elements_by_css_selector('button[type=submit]').click()

class = "VUU41"

[div._lz6s.Hz2lF, span._2dbep.qNELH, div.oNO81, div.S-mcP, div.N9abW, div..Igw0E.rBNOH.eGOV_.ybXk5._4EzTm., div..Igw0E.IwRSH.eGOV_._4EzTm.yC0tu., div..Igw0E.IwRSH.eGOV_._4EzTm.NUiEW., span._2dbep., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#fdadc332e432c4..Igw0E.IwRSH.eGOV_._4EzTm., div#f253c1307bb59d4..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f380e1ea13fb5a8..Igw0E.IwRSH.eGOV_._4EzTm., div#f911abb463314..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., div..Igw0E.rBNOH.eGOV_.ybXk5._4EzTm., div..Igw0E.IwRSH.eGOV_._4EzTm.yC0tu., div..Igw0E.IwRSH.eGOV_._4EzTm.NUiEW., span._2dbep., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f2c784d29ceaaf8..Igw0E.IwRSH.eGOV_._4EzTm., div#f154edff34f3c3c..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., div..Igw0E.rBNOH.eGOV_.ybXk5._4EzTm., div..Igw0E.IwRSH.eGOV_._4EzTm.yC0tu., div..Igw0E.IwRSH.eGOV_._4EzTm.NUiEW., span._2dbep., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f7db9ffdda237..Igw0E.IwRSH.eGOV_._4EzTm., div#f24db346c9cfa5..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f2476b60eec182c..Igw0E.IwRSH.eGOV_._4EzTm., div#f14d21aa8ff3128..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., div..Igw0E.rBNOH.eGOV_.ybXk5._4EzTm., div..Igw0E.IwRSH.eGOV_._4EzTm.yC0tu., div..Igw0E.IwRSH.eGOV_._4EzTm.NUiEW., span._2dbep., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#fce67f7885971..Igw0E.IwRSH.eGOV_._4EzTm., div#f2ba9e7673b1d5c..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f98bbedd886adc..Igw0E.IwRSH.eGOV_._4EzTm., div#f5137ece626ccc..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f12e1bd3cf2f6c4..Igw0E.IwRSH.eGOV_._4EzTm., div#f28d1917e46b2e..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f1f13b54a470834..Igw0E.IwRSH.eGOV_._4EzTm., div#f24b620a6e83ee8..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., span._2dbep., div..Igw0E.IwRSH.YBx95.vwCYk., div#f35ca7a9cdfe554..Igw0E.IwRSH.eGOV_._4EzTm., div#f3e52725e5c41ac..Igw0E.IwRSH.eGOV_._4EzTm.DhRcB., div.S-mcP, span._2dbep., div..Igw0E.IwRSH.eGOV_.ybXk5._4EzTm., div.frMpI.-sxBV, div..Igw0E.IwRSH.eGOV_._4EzTm.FBi-h._49XvD., a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., div..Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.soMvl.JI_ht.DhRcB., a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, a._2dbep.qNELH.kIKUG, …]



while dm_elem:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs = dm_elem.text
    if 'End of Results' in Divs:
        print('end')
        break
    else:
        continue
'''
