from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd  # 파일 저장을 위해 판다스 추가
import time

options = ChromeOptions()
options.add_argument('lang=ko_KR')
# 브라우져 안보이게 하기
options.add_argument('headless')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = 'https://news.naver.com/section/105'
driver.get(url)
button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]/a'

for i in range(30):
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(0.5)

# 수집한 기사 제목들을 담을 빈 리스트 생성
titles = []

for i in range(1, 180):
    for j in range(1, 7):
        try:
            title_xpath = '//*[@id="newsct"]/div[4]/div/div[1]/div[{}]/ul/li[{}]/div/div/div[2]/a/strong'.format(i, j)
            title = driver.find_element(By.XPATH, title_xpath).text
            print(title)

            # 수집된 제목이 빈 글자가 아니면 리스트에 추가합니다.
            if title:
                titles.append(title)
        except:
            print('error', i, j)

# -------------------------------------------------------------
# ★ 여기서부터 요청하신 저장 코드 구간입니다.
# -------------------------------------------------------------

# 1. 수집한 리스트를 표(DataFrame) 형태로 변환 (컬럼명: titles)
df_politics = pd.DataFrame(titles, columns=['titles'])

# 2. 카테고리(category) 컬럼을 만들고 'Politics'로 고정 채우기
df_politics['category'] = 'IT'

# 3. 셀레늄 크롬 브라우저 안전하게 종료
driver.quit()

# 4. 지정하신 파일명으로 깔끔하게 저장 (한글 깨짐 방지 인코딩 적용)
df_politics.to_csv('./data/naver_news_section_it.csv', index=False, encoding='utf-8-sig')
print("naver_news_section.csv 파일로 수집 및 저장 완료! 🚀")