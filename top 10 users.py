'''
List the top 10 users who accumulated the most sessions where they had more streaming sessions than viewing. Return the user_id, number of streaming sessions, and number of viewing sessions.

user_id:intsession_start:datetimesession_end:datetimesession_id:intsession_type:varchar

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column         Non-Null Count  Dtype         
---  ------         --------------  -----         
 0   user_id        10 non-null     int64         
 1   session_start  10 non-null     datetime64[ns]
 2   session_end    10 non-null     datetime64[ns]
 3   session_id     10 non-null     int64         
 4   session_type   10 non-null     object        
dtypes: datetime64[ns](2), int64(2), object(1)
memory usage: 532.0+ bytes

'''

# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions.head()

df = twitch_sessions

dfs = df[df['session_type'] == 'streamer']
dfv = df[df['session_type'] == 'viewer']

dfsn = dfs.groupby('user_id')['session_type'].size().reset_index(name='s_cnt')
dfvn = dfv.groupby('user_id')['session_type'].size().reset_index(name='v_cnt')
me = pd.merge(dfsn,dfvn,how = 'outer')

me[me['s_cnt'] > me['v_cnt']]


# ==========================================================

session_counts = df.groupby(['user_id', 'session_type']).size().unstack(fill_value=0)
session_counts.columns = ['number_of_viewing_sessions', 'number_of_streaming_sessions']

# Now, we'll filter out users with more streaming sessions than viewing sessions
more_streaming = session_counts[session_counts['number_of_streaming_sessions'] > session_counts['number_of_viewing_sessions']]

# Finally, we'll sort the users by the number of streaming sessions and return the top 10
top_users = more_streaming.sort_values(by='number_of_streaming_sessions', ascending=False).head(10)
top_users = top_users[['number_of_streaming_sessions', 'number_of_viewing_sessions']]
top_users.reset_index(inplace=True)
top_users