#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
<영화 데이터 전체 수집하기>
 - 공통으로 사용되는 기능들을 class(클래스)화 하여 사용
"""


# In[8]:


### 설치 필요 : pip install selenium
# 동적 웹페이지 처리를 위한 라이브러리
from selenium import webdriver

# 웹페이지 내에 데이터 추출을 위한 라이브러리
from selenium.webdriver.common.by import By

# 대기시간 설정
import time

### 웹 데이터 정보 수집을 위한 기능 정의를 위해 클래스 생성
class WebControl :
    
    ### 클래스 생성자
    def __init__(self) : 
        self.driver = self.getDriverChrome()

    # ------------------[Driver Control]-----------------------
    ### 웹드라이버 크롬 클래스 생성하기
    # - 크롬 브라우저가 Open됨
    # - 드라이버 정보를 메모리에 저장함
    def getDriverChrome(self) :
        return webdriver.Chrome()

    ### 크롬 브라우저 닫기
    # - 드라이버 정보가 메모리에서 삭제됨
    def closeDriver(self) :
        self.driver.quit()

    # ------------------[Page Control]-----------------------
    ### URL을 이용하여 페이지 전환하기
    def setUrlPageControl(self, url) :
        self.driver.get(url)

    ### 페이지 내에서 Click 이벤트에 따른 페이지 전환하기
    def setClickEvent(self, event, before=-1) :
        ### 페이지 내에 클릭할 태그정보를 이용하여 click 수행
        event.click()

        ### click 후 페이지 전환 처리
        page_handle = self.driver.window_handles[before]

        ### click 후 전환된 페이지의 모든 tag 정보 추출하기
        self.driver.switch_to.window(page_handle)

        ### 페이지 전환 후에는 페이지 로딩이 완료 될 수 있도록 대기 시간 주기(1초)
        time.sleep(1)

    ### 페이지 내에서 Click 이벤트에 따른 페이지 전환하기
    def setMoreClickEvent(self, event, before=-1) :
        ### - 펼친 횟수 확인 변수
        cnt = 0
        
        while True : 
            try : 
                ### 페이지 내에 클릭할 태그정보를 이용하여 click 수행
                event.click()
        
                ### click 후 페이지 전환 처리
                page_handle = self.driver.window_handles[before]
        
                ### click 후 전환된 페이지의 모든 tag 정보 추출하기
                self.driver.switch_to.window(page_handle)
        
                ### 페이지 전환 후에는 페이지 로딩이 완료 될 수 있도록 대기 시간 주기(1초)
                time.sleep(1)

                ### 더보기 클릭 횟수 확인을 위해 1씩 증가
                cnt += 1
                
            except Exception as e :
                # print(f"Error : {e}")
                break

        self.more_view_cnt = cnt

    ### 현재 페이지의 URL 추출하기
    def getCurrentUrl(self) :
        return self.driver.current_url

    ### 현재 드라이브에 저장된 페이지 이동 히스토리 정보 추출하기
    # - 리스트로 반환됨
    def getWindowHandles(self) :
        return self.driver.window_handles

    ### 이전 페이지로 이동하기
    def setBeforePage(self, num=-2) :
        self.driver.execute_script(f"window.history.go({num})")
        time.sleep(1)

    # ------------------[Tag에 해당하는 정보 추출하기]-----------------------
    ### 여러 건의 태크 정보 추출하기
    # - 리스트로 반환됨
    def getElements(self, tag) :
        try :
            elements = self.driver.find_elements(By.CSS_SELECTOR, tag)
            if len(elements) > 0 :
                return elements
            else : 
                return []
        except Exception as e: 
            return []
        
    ### 한 건의 태크 요소 추출하기
    def getElement(self, tag) :
        try : 
            element = self.driver.find_element(By.CSS_SELECTOR, tag)
            if element  is not None :
                return element
            else : 
                return ""
            
        except Exception as e:
            return ""
        

    ### 한 건의 태크 정보 추출하기
    # - 문자열로 반환됨
    def getElementText(self, tag) :
        try : 
            element = self.driver.find_element(By.CSS_SELECTOR, tag)
            if element  is not None :
                return element.text
            else : 
                return ""
            
        except Exception as e:
            return ""


# In[6]:


"""
<주피터 파일을 -> 파이썬 파일로 변환하기>
 - File > Save and Export Notebook As.. > Executable Script 선택
 - 주피터 노트북 파일명과 동일한, *.py 파일이 다운로드됨
 - 파일명 변경 : webcontorl.py
 - 위치 이동 : lib 폴더 생성 후 > lib 하위에 파일 위치 시키기
"""


# In[ ]:




