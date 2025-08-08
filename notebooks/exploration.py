#!/usr/bin/env python
# coding: utf-8

# In[54]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
import numpy as np
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_dir)

from src.loader import load_csv
import pandas as pd
import math


# In[55]:


df = load_csv("../data/raw/gapminder_full.csv")
df.head()


# In[56]:


from src.summary_stats import print_basic_info
print_basic_info(df)


# In[57]:


from src.cleaning import convert_column_to_datetime, standardize_text_column

df = convert_column_to_datetime(df, 'year', '%Y')
print(df.head())


# In[58]:


life_exp_describtion = df['life_exp'].describe()
gdp_cap_describtion = df['gdp_cap'].describe()


# In[59]:


df['gdp_total'] = df['gdp_cap'] * df['population']
df['life_exp_bin'] = pd.cut(df["life_exp"], bins= [life_exp_describtion["min"], life_exp_describtion["25%"], life_exp_describtion["50%"], life_exp_describtion["75%"], life_exp_describtion["max"]], labels=["Low", "Medium", "High", "Very High"])
df['gdp_cap_bin'] = pd.cut(df["gdp_cap"], bins= [gdp_cap_describtion["min"], gdp_cap_describtion["25%"], gdp_cap_describtion["50%"], gdp_cap_describtion["75%"], gdp_cap_describtion["max"]], labels=["Low", "Medium", "High", "Very High"])
print(df.head())


# In[60]:


df = standardize_text_column(df, ["country", "continent"], False)


# In[61]:


print(df.head())


# In[62]:


df_summery = df.groupby('continent').agg({
    'life_exp' : ['mean', 'median', 'std'],
    'gdp_cap' : ['mean', 'median', 'std'],
    'population' : ['mean', 'median', 'std']
})

print(df_summery)



# In[63]:


import src.plotter as plotter
plotter.plot_life_expectancy_distribution(df, 'output/Distribution of Life Expectancy Measured by Number of Records in the Dataset (1972–2007)')


# In[64]:


life_exp_bin_counts = df.groupby(['year', 'life_exp_bin']).nunique().reset_index()
life_exp_bin_counts.rename(columns={'country': 'number_of_countries'}, inplace=True)


# In[65]:


plotter.plot_life_expectancy_bins_over_time(life_exp_bin_counts, 'output/Number of Countries in Each Life Expectancy Category Over Time')


# In[66]:


gdp_cap_bin_counts = df.groupby(['year', 'gdp_cap_bin']).nunique().reset_index()
gdp_cap_bin_counts.rename(columns={'country': 'number_of_countries'}, inplace=True)


# In[67]:


plotter.plot_gdp_cap_bins_over_time(gdp_cap_bin_counts, 'output/Number of Countries in GDP per capital Category Over Time')


# In[68]:


df["decade"] = (df['year'].dt.year // 10) *10
decades = sorted(df['decade'].unique())


# In[69]:


plotter.plot_gdp_share_by_continent_per_decade(df, decades, 'output/Total GDP Share by Continent in Each Decade')


# In[70]:


plotter.plot_avg_life_expectancy_by_continent_and_decade(df, 'output/avg_life_expectancy_by_continent_and_decade.png')


# In[71]:


plotter.plot_population_by_continent_over_time(df, output_path='output/population_by_continent_over_time.png')


# In[73]:


plotter.plot_gapminder_2007_bubble_chart(df, output_path='output/gapminder_2007_bubble_chart.png')


# In[28]:


cols = df.columns.tolist()
cols.insert(2, cols.pop(cols.index('decade')))
df = df[cols]


# In[29]:


print(df)


# In[30]:


cols = df.columns.tolist()
cols.insert(6, cols.pop(cols.index('life_exp_bin')))
cols.insert(8, cols.pop(cols.index('gdp_cap_bin')))
df = df[cols]


# In[31]:


print(df)


# In[32]:


df.to_csv('World_development_Gapminder_1954_2007.csv', index=False)

