class Rep:

    Path = '/Users/apple/PycharmProjects/OPS_Portal/features/Config_Folder/chromedriver'

    Url="https://ops.youplus.com/signin"
    result_path="/Users/apple/PycharmProjects/OPS_Portal/features/Results/test.png"

    # login page Details
    login_page_email_id="//input[@name='email']"
    login_page_pwd="//input[@name='password']"
    Login_page_Sign_In_Button="//*[@id='root']/div/div[2]/form/button"

    # Select or Add Taxonomy Page

    manage_site_lnk="//*[@id='root']/section/header/ul/li[4]/a"

    # Select Domain Page

    cross_sign_btn = "//span[@class='ant-input-suffix']//i"

    ent_domain_= "//*[@id='selectValue']"

    select_domain = "//*[@id='root']/section/main/div/div/div[1]/div[2]/ul/div/li/span/span"

    eye_icon = "//*[@class='ant-table-row ant-table-row-level-0' and @data-row-key='0' ]//i[@aria-label='icon: eye']"

    # Check and Approve page

    # Question with confidence score

    ent_quest = "//div[@class='css-151xaom-placeholder']"

    input_txt = "//input[@id='react-select-2-input']"

    set1 ="//div[@id='react-select-2-option-7']"

        #"//*[@id='root']/section/main/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/span/div/div[2]"

    duration="//*[@id='root']/section/main/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/form/div/div[2]/div/span/span/input"


    mins = "(// li)[21]"

    secs = "(// li)[81]"

    opinion_Sentiment = "//span[text()='Positive']"

    apprve = "//span[text()='Approve']"

    save = "//*[@id='root']/section/main/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[4]/button/span"








