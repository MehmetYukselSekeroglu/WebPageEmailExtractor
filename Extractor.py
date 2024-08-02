
import subprocess
import os
import sys
import time
import random
from urllib.parse import urlparse,unquote,urlunparse
import threading

"""
package list

beautifulsoup4
requests
colorama
argparse
pyfiglet
"""

def installPackage(package:str) -> None:
    _command = [sys.executable, "-m", "pip", "install", package]
    commandStatus = subprocess.run(_command,capture_output=True,shell=True)
    print(f"... {package} ...")
    if commandStatus.returncode != 0:
        print(f"indirme işlemi başarısız oldu!\t{package}")
        print(f"*"*100)
        print(commandStatus.stderr.decode("utf-8"))
        print(f"*"*100)
        sys.exit(2)
    else:
        print(f"Başarıyla indirildi:\t{package}")




def installRequirements():
    installPackage("beautifulsoup4")
    installPackage("requests")
    installPackage("colorama")
    installPackage("argparse")
    installPackage("HiveWebCrawler")





try:
    from bs4 import BeautifulSoup
    import requests
    import argparse
    import colorama
    from colorama import Fore
    from HiveWebCrawler.Crawler import WebCrawler
    
except ModuleNotFoundError as e:
    print(e)
    print(f"Çalıştır: pip install beautifulsoup4 requests colorama argparse HiveWebCrawler")
    sys.exit(1)





colorama.init()

__VERSION__ = "1.0"
__AUTHOR__ = "_NULL_"

C_ORANGE = "\033[38;5;208m"
C_GREEN = Fore.GREEN
C_BLUE = Fore.GREEN
C_RESET = Fore.RESET
C_YELLOW = Fore.YELLOW
C_RED = Fore.RED

T_BOLD = "\033[1m"
T_BOLD_RESET = "\033[0m"



IMAGE_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webm",
    ".tiff"
)

def is_safe_url__html(target_url,timeout_sec=10,req_headers:dict=None) -> tuple:
        try:
            request_header = {
                "User-Agent":randomUserAgent()
            }            
            if req_headers is not None:
                request_header = req_headers
                
                
            send_request = requests.head(url=target_url,timeout=timeout_sec,headers=request_header)
            if not send_request.ok:
                return False
                        
            content_type = send_request.headers.get("Content-Type")
            if "text/html" not in content_type.lower():
                return False
            
            if "text/html" in content_type.lower():
                return True
            
            return False
            
        
        except Exception as err:
            return False

            

def prepare_url(target_url:str) -> dict:
    decoded_url = unquote(target_url)
    parsed_url  = urlparse(decoded_url)
    
    
    etc = parsed_url.params 
    
    if parsed_url.query:
        etc += "?" + parsed_url.query
    
    return {
        "origin":decoded_url,
        "base_domain":parsed_url.netloc,
        "path":parsed_url.path,
        "etc":etc 
    }






USER_AGENT_ARRAY = [
"Opera/8.51 (Windows NT 5.0; U; en)"
,"Opera/8.51 (Windows NT 5.1; U; de)"
,"Opera/8.51 (Windows NT 5.1; U; en)"
,"Opera/8.51 (Windows NT 5.1; U; fr)"
,"Opera/8.51 (Windows NT 5.1; U; nb)"
,"Opera/8.51 (Windows NT 5.1; U; pl)"
,"Opera/8.51 (X11; Linux i686; U; en)"
,"Opera/8.51 (X11; Linux x86_64; U; en)"
,"Opera/8.51 (X11; U; Linux i686; en-US; rv:1.8)"
,"Opera/8.52 (Windows ME; U; en)"
,"Opera/8.52 (Windows NT 5.0; U; en)"
,"Opera/8.52 (Windows NT 5.1; U; en)"
,"Opera/8.52 (Windows NT 5.1; U; ru)"
,"Opera/8.52 (X11; Linux i686; U; en)"
,"Opera/8.52 (X11; Linux x86_64; U; en)"
,"Opera/8.53 (Windows 98; U; en)"
,"Opera/8.53 (Windows NT 5.0; U; en)"
,"Opera/8.53 (Windows NT 5.1; U; de)"
,"Opera/8.53 (Windows NT 5.1; U; en)"
,"Opera/8.53 (Windows NT 5.1; U; pt)"
,"Opera/8.53 (Windows NT 5.2; U; en)"
,"Opera/8.54 (Windows 98; U; en)"
,"Opera/8.54 (Windows NT 4.0; U; zh-cn)"
,"Opera/8.54 (Windows NT 5.0; U; de)"
,"Opera/8.54 (Windows NT 5.0; U; en)"
,"Opera/8.54 (Windows NT 5.1; U; en)"
,"Opera/8.54 (Windows NT 5.1; U; pl)"
,"Opera/8.54 (Windows NT 5.1; U; ru)"
,"Opera/8.54 (X11; Linux i686; U; de)"
,"Opera/8.54 (X11; Linux i686; U; pl)"
,"Opera/9.00 (Macintosh; PPC Mac OS X; U; es)"
,"Opera/9.80 (X11; Linux i686; U; en) Presto/2.5.27 Version/10.60"
,"Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.6.30 Version/10.61"
,"Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11"
,"Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01"
,"Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50"
,"Opera/9.80 (X11; Linux i686; U; it) Presto/2.5.24 Version/10.54"
,"Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00"
,"Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01"
,"Opera/9.80 (X11; Linux i686; U; nb) Presto/2.2.15 Version/10.00"
,"Opera/9.80 (X11; Linux i686; U; pl) Presto/2.2.15 Version/10.00"
,"Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61"
,"Opera/9.80 (X11; Linux i686; U; pt-BR) Presto/2.2.15 Version/10.00"
,"Opera/9.80 (X11; Linux i686; U; ru) Presto/2.2.15 Version/10.00"
,"Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11"
,"Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10"
,"Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"
,"Opera/9.80 (X11; Linux x86_64; U; en-GB) Presto/2.2.15 Version/10.01"
,"Opera/9.80 (X11; Linux x86_64; U; en) Presto/2.2.15 Version/10.00"
,"Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50"
,"Opera/9.80 (X11; Linux x86_64; U; it) Presto/2.2.15 Version/10.10"
,"Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00"
,"Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01"
,"Opera/9.80 (X11; U; Linux i686; en-US; rv:1.9.2.3) Presto/2.2.15 Version/10.10"
,"Opera/9.99 (Windows NT 5.1; U; pl) Presto/9.9.9"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.3a3pre) Gecko/20100306 Firefox3.6 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:2.0b10) Gecko/20110126 Firefox/4.0b10"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB7.0 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; es-ES; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB7.1"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; et; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2 GTB7.0"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.8) Gecko/20100722 Firefox 3.6.8 GTB7.1"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; hu; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; hu; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB7.1"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; hu; rv:1.9.2.7) Gecko/20100713 Firefox/3.6.7 GTB7.1"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6 (.NET CLR 3.5.30729)"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; it; rv:1.9.2.8) Gecko/20100722 AskTbADAP/3.9.1.14019 Firefox/3.6.8"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; ja; rv:1.9.2.4) Gecko/20100611 Firefox/3.6.4 GTB7.1"
,"Mozilla/5.0 (Windows; U; Windows NT 6.1; lt; rv:1.9.2) Gecko/20100115 Firefox/3.6"

]


def randomUserAgent() -> str:
    return str(random.choice(USER_AGENT_ARRAY))



# For url handler

GOOGLE_BOT_IMAGE = "Googlebot-Image/1.0"
GOOGLE_BOT_VIDEO ="Googlebot-Video/1.0"
GOOGLE_BOT_STORE = "Mozilla/5.0 (X11; Linux x86_64; Storebot-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
GOOGLE_BOT_INSPECTION_ADVANCED_SEARCH = "Mozilla/5.0 (compatible; Google-InspectionTool/1.0;)"
GOOGLE_BOT_ADS = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
GOOGLE_ADSENSE = "Mediapartners-Google"
GOOGLE_SAFE_SEARCH = "Google-Safety"

def _GetTime():
    """
    herhangi parametre almadan sisteme ait güncel zamanı 
    str: day/mount/year hour:min:sec olarak döndürür

    Returns:
        str: day/mount/year hour:min:sec
    """
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    day_is = current_time.tm_mday
    mount_is = current_time.tm_mon
    year_is = current_time.tm_year
    
    formatted_time = f"{day_is}/{mount_is}/{year_is} {hour:02d}:{minute:02d}:{second:02d}"
    return formatted_time





# BILGILENDIRMELER ICIN 
def p_info(mesages:str, locations:str=None):
    sys.stdout.write(f"{C_GREEN}[{_GetTime()}]{T_BOLD}[INFO]: {T_BOLD_RESET}{mesages}\n")
    sys.stdout.flush()
    
# HATA MESAJLARI ICIN 
def p_error(mesages:str,locations:str=None):
    sys.stderr.write(f"{C_RED}[{_GetTime()}]{T_BOLD}[ERR]: {T_BOLD_RESET}{mesages}\n")
    sys.stdout.flush()
    
# Uyarıları için
def p_warn(mesages:str,locations:str=None):
    print(f"{C_ORANGE}[{_GetTime()}]{T_BOLD}[WARN]: {T_BOLD_RESET}{mesages}")

#Log mesajları için
def p_log(mesages:str,locations:str=None):
    print(f"{C_BLUE}[{_GetTime()}][log]: {mesages}")

def p_title(your_title:str,locations:str=None):
    
        print(f"{T_BOLD}{C_BLUE}>> {your_title}{C_RESET}{T_BOLD_RESET}")     

















def threadFunction(targetAddress, self_crawler:WebCrawler,self_targetList:list,scannedList:list):        
    _temp_list = []
    
    
    getCrawl = self_crawler.send_request(target_url=targetAddress,timeout_sec=10,req_headers={
        "User-Agent":randomUserAgent()
        })
    
    targetAddress_parsed = prepare_url(targetAddress)

    if not getCrawl["success"]:
        p_error(f"{targetAddress} -> {getCrawl['message']}")
        return
                
    
    links_from_url = self_crawler.crawl_links_from_pesponse_href(targetAddress_parsed["base_domain"],getCrawl["data"])
            
    #print(f">> Scanning: {targetAddress_parsed['path']}", end="\r")

    if len(links_from_url["data_array"]) < 1 :
        p_warn(f">> No link detected on -> {targetAddress}","startCrawl")      
        return                      
    
    for single_link_list in links_from_url["data_array"]:
        _url = str(single_link_list[0])
        _title = single_link_list[1]
    
        if _url.startswith(f"#"):
            pass
    
        _url = unquote(_url)
        if _url not in self_targetList:
            parsed_url = urlparse(_url)
            _url = urlunparse(parsed_url._replace(fragment=""))
        
            if not _url.startswith("http://") and not _url.startswith("https://"):
                if _url.startswith(targetAddress_parsed["base_domain"]) or _url.startswith("www.") :
                    _url = "http" + "://" + _url
                else:
                    if _url.startswith("#/"):
                        _url = _url[2:]
                    _url ="https://"+ targetAddress_parsed["base_domain"] + "/" + _url                        

            if str(parsed_url.path).endswith(IMAGE_EXTENSIONS) and targetAddress_parsed["base_domain"] in _url:        
                continue
        
            if targetAddress_parsed["base_domain"] in _url or str(targetAddress_parsed["base_domain"]).replace("www.","") in _url:        
                if _url not in self_targetList and _url not in scannedList:
                    self_targetList.append(_url)
                    _temp_list.append(_url)
            else:
                continue
            
    
    emails_list = self_crawler.crawl_email_address_from_response_href(getCrawl["data"])

    if len(emails_list["data_array"]) != 0:
        for element in emails_list["data_array"]:
            p_info(f"Found email: {element[1]} on {targetAddress}")





class ExtractorClass():
    
    def __init__(self, targetUrl:str,thread=4):
        self.targetUrl = targetUrl
        self.threadCount = thread
        self.scannedList = []

        self.targetList = []
        self.targetUrl = unquote(self.targetUrl)
        self.targetList.append(self.targetUrl)
        
        self.Crawler_is = WebCrawler()
        
        
        
    def startExtract(self):
        while True:
            self.targetList = list(set(self.targetList))
            if len(self.targetList) == 0:
                print()
                p_info("Tüm adresler tarandı, threadların bitmesi bekleniyor...")

                while threading.active_count() != 1:
                    time.sleep(0.2)
                    
                print()
                p_info("Threadlar bitti, sistemden çıkılıyor...")
                break
            
            
            targetAddress = self.targetList.pop(0)
            
            if targetAddress not in self.scannedList:
                self.scannedList.append(targetAddress)
            else:
                continue



            if len(self.targetList) > 10:
                while threading.active_count() > self.threadCount:
                    time.sleep(0.1)            
                threading.Thread(target=threadFunction, args=(targetAddress,self.Crawler_is,self.targetList,self.scannedList), daemon=True).start()
            else:
                threadFunction(targetAddress=targetAddress,self_crawler=self.Crawler_is,self_targetList=self.targetList,scannedList=self.scannedList)
            

            
        while threading.active_count() != 1:
            time.sleep(1)   
        
        
        
    


print("""
EEEEE M   M   A   III L     FFFFF III N   N DDDD  EEEEE RRRR  
E     MM MM  A A   I  L     F      I  NN  N D   D E     R   R 
EEEE  M M M AAAAA  I  L     FFFF   I  N N N D   D EEEE  RRRR  
E     M   M A   A  I  L     F      I  N  NN D   D E     R  R  
EEEEE M   M A   A III LLLLL F     III N   N DDDD  EEEEE R   R 
                                                              
""")
    
    
argParser = argparse.ArgumentParser()

argParser.add_argument("--url",required=True,type=str,help="Hedef Web Sitesinin adresi")

argDict = vars(argParser.parse_args())

targetURL = str(argDict["url"])



if not targetURL.startswith("http://") and not targetURL.startswith("https://"):
    targetURL = "https://" + targetURL
    
p_info(f"Starting scan for: {targetURL}")
print()
dorkExtarctor = ExtractorClass(targetUrl=targetURL,thread=4)
dorkExtarctor.startExtract()




    
    
    
    