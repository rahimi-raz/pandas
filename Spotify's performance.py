"""


Market penetration is an important metric for understanding Spotify's performance and growth potential in different regions.

You are part of the analytics team at Spotify and are tasked with calculating the active user penetration rate in specific markets.

For this task, 'active_users' are defined based on the  following criterias:

•	last_active_date: The user must have interacted with Spotify within the last 30 days.

•	monthly_active_sessions_thousands: The user must have engaged with Spotify for at least 5000 sessions in the past month.(monthly_active_sessions_thousands = 5)

•	listening_hours: The user must have spent at least 10 hours listening on Spotify in the past month.

Based on the condition above, calculate the active 'user_penetration_rate' by using the following formula.

•	Active User Penetration Rate = (Number of Active Spotify Users in the Market / Total Population of the Market)

Total Population of the market is based on both active and passive users.

​

The output should contain 'country' and 'active_user_penetration_rate'.

Let's assume the current_day is 2024-01-31.
DataFrame: penetration_analysis


"""

# Import your libraries
import pandas as pd
from datetime import datetime

# Start writing code
penetration_analysis.head()

cd = pd.to_datetime('2024-01-31')
df = penetration_analysis

df['last_active_date'] = pd.to_datetime(df['last_active_date'])
au = df[
    ((cd - pd.to_datetime(df['last_active_date'])).dt.days <= 30) &
    (df['monthly_active_sessions_thousands'] >= 5) &
    (df['listening_hours'] >= 10 )
    ]
    
au = au.groupby('country').size().reset_index(name='active_user_count')   

tp = df[['total_population_mil','country']].drop_duplicates()

me = pd.merge(au,tp,on='country')

me['percent'] = me['active_user_count']/me['total_population_mil'] * 100

me[['percent','country']]


