from ast import Return
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
  
    df=pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_count()




    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean()


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =(df[df['education'] =='Bachelors'].shape[0]/df.shape[0])*100
    print("The precnetage of the people {percentage_bachelors:.2f}%.")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?


data = {'education': ['High School', 'High School', 'High School', 'High School', 'High School',
                       'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor', 'Bachelor',
                       'Master', 'Master', 'Master', 'Master',
                       'Doctorate', 'Doctorate', 'Doctorate', 'Doctorate', 'Doctorate'],
        'income': ['50K or more', 'less than 50K', '50K or more', 'less than 50K', '50K or more',
                    '50K or more', 'less than 50K', '50K or more', 'less than 50K', '50K or more',
                    '50K or more', 'less than 50K', '50K or more', 'less than 50K', '50K or more',
                    'less than 50K', '50K or more', 'less than 50K', '50K or more', 'less than 50K']}

df = pd.DataFrame(data)

advanced_education = ['Bachelor', 'Master', 'Doctorate']

# percentage of people with advanced education who make more than 50K
higher_education = df[df['education'].isin(advanced_education) & (df['income'] == '50K or more')]
print(f"The percentage of people with advanced education who make more than 50K is {(higher_education.shape[0] / df[df['education'].isin(advanced_education)].shape[0]) * 100:.2f}%.")

# percentage of people without advanced education who make more than 50K
lower_education = df[~df['education'].isin(advanced_education) & (df['income'] == '50K or more')]
print(f"The percentage of people without advanced education who make more than 50K is {(lower_education.shape[0] / df[~df['education'].isin(advanced_education)].shape[0]) * 100:.2f}%.")

    # percentage with salary >50K
lower_education_rich =df[~df['education'].isin(advanced_education) & (df['income'] == '50K or more')]
print(f"The percentage of people with lower education who make more than 50K is {(lower_education_rich.shape[0] / df[~df['education'].isin(advanced_education)].shape[0]) * 100:.2f}%.")
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df[df['hours-per-week'].isin(range(15,21))& (df['income']=='50k or more')]
print("the precnetage of such type of people is {(num_min_workers.shape[0] / df[df['hours-per-week'].isin(range(15, 21))].shape[0]) * 100:.2f}%.")

rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
# First, ensure that the 'income' column is a categorical data type
df['income'] = df['income'].astype('category')

# Calculate the percentage of people earning >50K in each country
df['income_pct'] = df.groupby('country')['income'].transform(lambda x: x.eq('50k or more').sum() / len(x) * 100)

# Identify the country with the highest percentage of people earning >50K
highest_earning_country = df[df['income_pct'] == df['income_pct'].max()]['country'].values[0]
highest_earning_country_percentage = df[df['income_pct'] == df['income_pct'].max()]['income_pct'].values[0]

print(f"The country with the highest percentage of people earning >50K is {highest_earning_country} with a percentage of {highest_earning_country_percentage:.2f}%.")

    # Identify the most popular occupation for those who earn >50K in India.


# Assuming 'df' is your DataFrame and it contains columns 'occupation', 'income', and 'country'
df = df[df['income'] == '50k or more']    # Filter the DataFrame to only include rows where income is >50K
df = df[df['country'] == 'India']        # Filter the DataFrame to only include rows where country is India

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df['occupation'].value_counts().idxmax()

print(f"The most popular occupation for those who earn >50K in India is {top_IN_occupation}.")
    # DO NOT MODIFY BELOW THIS LINE

if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

return
{
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
