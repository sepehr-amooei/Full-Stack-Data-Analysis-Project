import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
import math

# 1. Histogram: Distribution of life expectancy across the dataset
def plot_life_expectancy_distribution(df, output_path='output/life_expectancy_distribution.png'):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='life_exp', bins=30, kde=True)
    plt.title('Distribution of Life Expectancy Measured by Number of Records in the Dataset (1972–2007)')
    plt.xlabel('Life Expectancy')
    plt.ylabel('Frequency')
    plt.tight_layout()
    # plt.savefig(output_path)
    plt.show()


# 2. Line plot: Number of countries in each life expectancy bin over time
def plot_life_expectancy_bins_over_time(life_exp_bin_counts, output_path='output/life_expectancy_bins_over_time.png'):
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=life_exp_bin_counts,
        x='year',
        y='number_of_countries',
        hue='life_exp_bin',
        marker='o'
    )
    plt.title('Number of Countries in Each Life Expectancy Category Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Countries')
    plt.legend(title='Life Expectancy Category')
    plt.grid(True)
    plt.tight_layout()
    # plt.savefig(output_path)
    plt.show()


# 3. Line plot: Number of countries in each GDP per capita bin over time
def plot_gdp_cap_bins_over_time(gdp_cap_bin_counts, output_path='output/gdp_cap_bins_over_time.png'):
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=gdp_cap_bin_counts,
        x='year',
        y='number_of_countries',
        hue='gdp_cap_bin',
        marker='o'
    )
    plt.title('Number of Countries in GDP per Capita Category Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Countries')
    plt.legend(title='GDP per Capita Category')
    plt.grid(True)
    plt.tight_layout()
    # plt.savefig(output_path)
    plt.show()


# 4. Pie charts: GDP share by continent across different decades
def plot_gdp_share_by_continent_per_decade(df, decades, output_path='output/gdp_share_by_continent_per_decade.png'):
    num_charts = len(decades)
    n_rows = 2
    n_cols = math.ceil(num_charts / n_rows)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 8))
    axes = axes.flatten()

    for i, decade in enumerate(decades):
        data = df[df['decade'] == decade].groupby('continent')['gdp_total'].sum()
        plt.sca(axes[i])
        plt.pie(data, labels=data.index, autopct='%1.1f%%')
        axes[i].set_title(f"GDP Share by Continent ({decade}s)")

    plt.suptitle("Total GDP Share by Continent in Each Decade", fontsize=14)
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    # plt.savefig(output_path)
    plt.show()


# 5. Point plot: Average life expectancy by continent and decade
def plot_avg_life_expectancy_by_continent_and_decade(df, output_path='output/avg_life_expectancy_by_continent_and_decade.png'):
    sns.pointplot(
        data=df,
        x='continent',
        y='life_exp',
        hue='decade',
        dodge=True,
        markers='o',
        capsize=0.1,
        palette='bright'
    )
    plt.title("Average Life Expectancy by Continent and Decade")
    plt.ylabel("Life Expectancy")
    plt.xlabel("Continent")
    plt.legend(title='Decade', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    # plt.savefig(output_path)
    plt.show()


# 6. Stacked bar chart: Total population per continent over time
def plot_population_by_continent_over_time(df, output_path='output/population_by_continent_over_time.png'):
    df_pivot = df.groupby(['decade', 'continent'])['population'].sum().unstack()

    df_pivot.plot(kind='bar', stacked=True, figsize=(18, 8))

    plt.title("Stacked Bar Chart of Population by Continent Over Time")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(title='Continent')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig(output_path)
    plt.show()

    return df_pivot


# 7. Bubble chart: GDP vs Life Expectancy in 2007 (Gapminder-style)
def plot_gapminder_2007_bubble_chart(df, output_path='output/gapminder_2007_bubble_chart.png'):
    df_2007 = df[df['year'].dt.year == 2007]

    continent_colors = {
        'Asia': 'green',
        'Europe': 'red',
        'Americas': 'orange',
        'Africa': 'blue',
        'Oceania': 'purple'
    }

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df_2007['gdp_cap'], df_2007['life_exp'],
        s=df_2007['population'] / 1e6,
        c=df_2007['continent'].map(continent_colors),
        alpha=0.8
    )

    legend_handles = [Patch(color=color, label=continent) for continent, color in continent_colors.items()]
    plt.legend(handles=legend_handles, title='Continent', loc='upper left', frameon=True)

    plt.xscale('log')
    plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])
    plt.xlabel('GDP per Capita (PPP$, log scale)')
    plt.ylabel('Life Expectancy (years)')
    plt.title('World Development in 2007 (Gapminder)')

    # Optional: hardcoded country labels
    plt.text(4959.114854, 72.961, 'China', fontsize=9, ha='center', va='center')
    plt.text(2452.210407, 64.698, 'India', fontsize=9, ha='center', va='center')
    plt.text(42951.65309, 78.242, 'USA', fontsize=9, ha='center', va='center', color='white')

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    # plt.savefig(output_path)
    plt.show()
