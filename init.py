# 自动预装相应库
try:
    from urllib import response
    import requests
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    import pandas as pd
    import json
    import smtplib
    from email.mime.text import MIMEText
    from random import *
except ImportError:
    import pip
    pip.main(["install","--user","urllib","requests","fake_useragent","bs4","pandas","json","smtplib","random"])
    from urllib import response
    import requests
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    import pandas as pd
    import json
    import smtplib
    from email.mime.text import MIMEText