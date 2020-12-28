#this is a scraper
#scraping methodology is unknown
#scraping algorithm is unknown


#database structur is unknown
#columns required:: profile_name,no_of_followers,no_of_posts,revisit_count,tag_name











from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
from selenium.webdriver.firefox.options import Options
options=Options()
options.headless=False
profile_name=''
profile = webdriver.FirefoxProfile(profile_name)

driver=webdriver.Firefox(options=options,firefox_profile=profile)
follow_button_xpath='//button[@class="oW_lN _0mzm- sqdOP yWX7d        "]'




def sleep(a,b=-1):
    if(b==-1):
        print("sleeping for "+str(a)+" seconds.....")
        time.sleep(a)
    elif(b>a):
        t=random.randint(a, b)
        print("sleeping for "+str(t)+" seconds.....")

        time.sleep(t)
    else:
        print("the sleep values are not correct")
def login():
    driver = self.driver
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
    login_button.click()
    time.sleep(2)
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    user_name_elem.clear()
    user_name_elem.send_keys('username')
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    passworword_elem.clear()
    passworword_elem.send_keys('password')
    passworword_elem.send_keys(Keys.RETURN)
    time.sleep(2)



def goto_hashtag(hashtag,scroll=1):
    print("going to #"+hashtag+" page")
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    sleep(2)

    # gathering photos
    pic_hrefs = []
    for i in range(scroll):
        try:
            print("scrolling...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            print("Check: pic href length " + str(len(pic_hrefs)))
        except Exception:
            continue
    return pic_hrefs


def goto_profile(pic_href):
    sleep(2,4)
    print("opening "+pic_href)


    driver.get(pic_href)
    
    sleep(2,4)
    try:
        url=driver.find_element_by_xpath('//img[@class="FFVAD"]').get_attribute('src')
    except:
        url='url'

    user_name=driver.find_element_by_xpath('//a[@class="FPmhX notranslate nJAzx"]').get_attribute('title')
    like="//a[@class='zV_Nj']/span"
    likes=driver.find_element_by_xpath(like).text
    # get tags
    #profile_link = driver.find_elements_by_tag_name('a')
    profile_link = driver.find_element_by_xpath("//a[@class='FPmhX notranslate nJAzx']")
    print("going to profile "+profile_link.get_attribute('href'))
    driver.get(profile_link.get_attribute('href'))
    sleep(2, 4)
    sleep(2)  
    return url,user_name,likes

def like_photo( hashtag):
    driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    time.sleep(2)

    # gathering photos
    pic_hrefs = []
    for i in range(1, 7):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            # print("Check: pic href length " + str(len(pic_hrefs)))
        except Exception:
            continue

    # Liking photos
    unique_photos = len(pic_hrefs)
    for pic_href in pic_hrefs:
        driver.get(pic_href)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            time.sleep(random.randint(2, 4))
            like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
            like_button().click()
            for second in reversed(range(0, random.randint(18, 28))):
                print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                + " | Sleeping " + str(second))
                time.sleep(1)
        except Exception as e:
            time.sleep(2)
        unique_photos -= 1
def follow():
    driver = self.driver
    driver.get("https://www.instagram.com/explore")
    time.sleep(2)
    pic_hrefs = []
    for i in range(1, 2):
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            print("Check: pic href length " + str(len(pic_hrefs)))
        except Exception:
            continue

    
    print(pic_hrefs)
    for pic_href in pic_hrefs:
        time.sleep(random.randint(2,4))
        driver.get(pic_href)
        time.sleep(random.randint(2, 4))
        follow_button = lambda: driver.find_element_by_xpath('//button[@class="oW_lN _0mzm- sqdOP yWX7d        "]').click()
        follow_button()
        time.sleep(random.randint(2, 4))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        comment_elem = driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
        comment_elem.clear()
        comment_elem.click()
        time.sleep(random.randint(4, 5))
        comment_elem = driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")

        comment_elem.send_keys("awesome!!")
        time.sleep(random.randint(2, 4))
        post_button = driver.find_element_by_xpath("//button[@class='_0mzm- sqdOP yWX7d        ']")
        post_button.click()
        # time.sleep(random.randint(2, 4))






def goto_explore(scroll=1):
    sleep(2,4)
    print("opening explore page")
    driver.get("https://www.instagram.com/explore")
    sleep(3,4)
    pic_hrefs=[]
    for i in range(scroll):
        try:
            print("scrolling")

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            # get tags
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            # finding relevant hrefs
            hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                if '.com/p/' in elem.get_attribute('href')]
            # building list of unique photos
            [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            print("Check: pic href length " + str(len(pic_hrefs)))
        except Exception:
            continue
    return pic_hrefs


def goto_home():
    sleep(2,4)
    print("opening home page")

    driver.get("https://www.instagram.com")
    sleep(3,4)



def scrape_explore():
    print("todo")
    pics=goto_explore()
    for pic in pics:
        goto_profile(pic)
        posts=driver.find_element_by_xpath('//span[@class="-nal3 "]/span')
        elems=driver.find_elements_by_xpath('//a[@class="-nal3 "]/span')
        followers=elems[0].text
        following=elems[1].text
        
        if(',' in followers):
            followers.replace(',','')

        print(followers)
        if('k' in followers):
            followers=float(followers[0:len(followers)-1])*1000
        elif('m' in followers):
            followers=float(followers[0:len(followers)-1])*1000
        else:
            followers=float(followers)
        if(',' in posts):
            posts.replace(',','')

        print(posts)
        if('k' in posts):
            posts=float(posts[0:len(posts)-1])*1000
        elif('m' in posts):
            posts=float(posts[0:len(posts)-1])*1000
        else:
            posts=float(posts)
        if(',' in following):
            following.replace(',','')

        print(following)
        if('k' in following):
            following=float(following[0:len(following)-1])*1000
        elif('m' in followers):
            following=float(following[0:len(following)-1])*1000
        else:
            following=float(following)


        follow_at_profile()
        like_n_times(3)


def scrape_profile(href='https://www.instagram.com/garyvee/',n=10):
    sleep(2,5)
    driver.get(href)
    sleep(2,4)
    path="//div[@class='v1Nh3 kIKUG  _bz0w']/a"
    element=driver.find_element_by_xpath(path)  
    print("clicking on first pic")
    driver.execute_script("arguments[0].click();",element)
    sleep(3)
    for i in range(n):
        # comment_box='//div[@class="C4VMK"]'
        # commenter='//div[@class="C4VMK"]/h3/a'# get attribute text
        # comment_time='//time[@class="FH9sR Nzb55"]'
        # view_replies='//button[@class="_0mzm- sqdOP yWX7d"]'
        # reply='//button[@class="FH9sR"]'
        # more_replies_button='//buton[@class="dCJp8 afkep _0mzm-"]'
        # comment_text='//div[@class="C4VMK"]/span'

        like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
        like_button()
        sleep(3,5)
        right_button = lambda: driver.find_element_by_xpath('//a[@class="HBoOv coreSpriteRightPaginationArrow"]').click()
        right_button()
        sleep(3,5)
    print("liked "+str(n)+" times..")

    
    


def reply_and_like_comments_on_own_pics():
    print("todo")




#class="_5f5mN       jIbKX  _6VtSN     yZn4P   "


try:
    goto_explore(3)
except Exception as e:
    print("error occurred",e)
finally:
    print('closing driver')
    driver.close()