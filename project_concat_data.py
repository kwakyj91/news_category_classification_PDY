import pandas as pd
df = pd.read_csv('data/naver_news_section_po.csv')
print(df.head())

df_temp = pd.read_csv('data/naver_news_section_ec.csv')
print(df_temp.head())

df = pd.concat([df,df_temp],ignore_index=True)
print(df.head())
df_temp = pd.read_csv('data/naver_news_section_so.csv')

df = pd.concat([df,df_temp],ignore_index=True)
df_temp = pd.read_csv('data/naver_news_section_cu.csv')

df = pd.concat([df,df_temp],ignore_index=True)
df_temp = pd.read_csv('data/naver_news_section_wo.csv')
df = pd.concat([df,df_temp],ignore_index=True)

df_temp = pd.read_csv('data/naver_news_section_it.csv')
df = pd.concat([df,df_temp],ignore_index=True)

df_temp = pd.read_csv('data/news_titles.csv')
df = pd.concat([df,df_temp],ignore_index=True)

df_temp = pd.read_csv('data/naver_headline_news_20260608.csv')
df = pd.concat([df,df_temp],ignore_index=True)


df.info()
df = df.drop_duplicates()

print(df.category.value_counts())
print(df.isnull().sum())

df.info()
df.to_csv('./data/project_news_titles.csv', index=False)