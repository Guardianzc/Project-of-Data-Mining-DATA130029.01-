#work3: new_feature3，4:前5位演员的popularity和前5位crew的popularity
pop = pd.read_csv('pop.csv')
temp_train = pd.read_csv('train.csv')
#temp_train.index = temp_train['id']
temp_train['5cast_pop'] = 0
temp_train['5crew_pop'] = 0
temp_test = pd.read_csv('test.csv')
#temp_test = temp_test['id']
temp_test['5cast_pop'] = 0
temp_test['5crew_pop'] = 0
for i in range(temp_train.shape[0]):
    print(i)
    cast_pop = 0
    crew_pop = 0
    try:
        temp = eval(temp_train.iloc[i]['cast'])
    except:
        temp = []
    temp = temp[:5]
    for cast in temp:
        temp_id = cast['id']
        #print(temp_id,float(pop.loc[pop['id'] == temp_id]['popularity']))
        cast_pop = cast_pop + float(pop.loc[pop['id'] == temp_id]['popularity']) 
    try:
        temp = eval(temp_train.iloc[i]['crew'])
    except:
        temp = []
    temp = temp[:5]
    for crew in temp:
        temp_id = crew['id']
        crew_pop = crew_pop + float(pop.loc[pop['id'] == temp_id]['popularity'])
    #print(cast_pop, crew_pop)
    temp_train.iloc[i,-2] = cast_pop
    temp_train.iloc[i,-1] = crew_pop
    #print(temp_train.iloc[i]['5cast_pop'],temp_train.iloc[i]['5crew_pop'])
    
for i in range(temp_test.shape[0]):
    print(i)
    cast_pop = 0
    crew_pop = 0
    try:
        temp = eval(temp_test.iloc[i]['cast'])
    except:
        temp = []
    temp = temp[:5]
    for cast in temp:
        temp_id = cast['id']
        cast_pop = cast_pop + float(pop.loc[pop['id'] == temp_id]['popularity'])
    try:
        temp = eval(temp_test.iloc[i]['crew'])
    except:
        temp = []
    temp = temp[:5]
    for crew in temp:
        temp_id = crew['id']
        crew_pop = crew_pop + float(pop.loc[pop['id'] == temp_id]['popularity'])
    temp_test.iloc[i,-2] = cast_pop
    temp_test.iloc[i,-1] = crew_pop
temp_train.index = temp_train['id']
temp_test.index = temp_test['id']
train = pd.concat([train,temp_train['5cast_pop']],axis = 1)
train = pd.concat([train,temp_train['5crew_pop']],axis = 1)
test = pd.concat([test,temp_test['5cast_pop']],axis = 1)
test = pd.concat([test,temp_test['5crew_pop']],axis = 1)