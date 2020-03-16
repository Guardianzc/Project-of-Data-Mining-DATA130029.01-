#A Python script for processing the data
#More data to correct

#Train part
C_train = pd.read_csv('train_add.csv')
for i in range(C_train.shape[0]):
    C_id = C_train.iloc[i]['id']
    C_bud = C_train.iloc[i]['budget']
    train.loc[train['id'] == C_id, 'budget'] = C_bud

#Test part
C_test = pd.read_csv('test_add.csv')
for i in range(C_test.shape[0]):
    C_id = C_test.iloc[i]['id']
    C_bud = C_test.iloc[i]['budget']
    test.loc[test['id'] == C_id, 'budget'] = C_bud
	
#Work2: new_feature1:同期有多少其他电影上线
#Compute how many movies are released in the same month

SameReleaseDate = train.groupby(['release_month','release_year'])['id'].count().reset_index()
SameReleaseDate.columns = ['release_month','release_year','SameReleaseMonth']
train = train.merge(SameReleaseDate,how = 'left',on = ['release_month','release_year'])
test = test.merge(SameReleaseDate,how = 'left',on = ['release_month','release_year'])
test['SameReleaseMonth'] = test['SameReleaseMonth'].fillna(1)

#Work3: new_feature2:电影放映年的经济状况(Global GDP per person)

WorldGDP = pd.read_csv('GDP.csv')
WorldGDP = WorldGDP.loc[WorldGDP['Country Name']=='World']
WorldGDP = WorldGDP.iloc[:,4:]
WorldGDP = WorldGDP.transpose()
WorldGDP = WorldGDP.rename(columns={257:'GlobalGDP'})
WorldGDP['release_year'] = WorldGDP.index
WorldGDP['release_year'] = WorldGDP['release_year'].apply(pd.to_numeric)
WorldGDP.loc[WorldGDP['release_year'] == 2018,'GlobalGDP'] = 11370
train = pd.merge(train,WorldGDP,how='left',on=['release_year']) 
train['GlobalGDP'] = train['GlobalGDP'].fillna(0)
test = pd.merge(test,WorldGDP,how='left',on=['release_year'])
test['GlobalGDP'] = test['GlobalGDP'].fillna(0)