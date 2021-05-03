import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
olympics=pd.read_csv("players.csv")   
def teams_medals():
    filter=((olympics.Medal=='Gold')|(olympics.Medal=='Silver')|(olympics.Medal=='Bronze'))
    medal_data=olympics[filter]
    teams=list(medal_data['Team'].unique())
    medal_counts=[]
    for i in teams:
        x = medal_data[medal_data['Team'] == i]
        medalCount = len(x)
        medal_counts.append(medalCount)
    newData = pd.DataFrame({'Teams': teams,'medal_counts':medal_counts})
    new_index = (newData['medal_counts'].sort_values(ascending=False)).index.values
    sorted_data = newData.reindex(new_index)
    plt.figure(figsize = (12,10))
    sns.barplot(x = sorted_data['Teams'], y = sorted_data['medal_counts'])
    plt.xticks(rotation = 90)
    plt.xlabel('Teams')
    plt.ylabel('Total Medal Count')
    plt.title('Medal Counts by Teams')
    plt.show()
def players_age():
    filter=((olympics.Age>0))
    new_data=olympics[filter]
    age_data={}
    for i in new_data['Age']:
        if i not in age_data.keys():
            age_data[i]=1
        else:
            age_data[i]=age_data[i]+1
    age=[]
    counts=[]
    for i in age_data.keys():
        age.append(i)
    for j in age_data.values():
        counts.append(j)
    ages=pd.DataFrame({'Age':age,'No of players':counts})
    plt.figure(figsize = (10,8))
    sns.barplot(x=ages['Age'],y=ages['No of players'])
    plt.xticks(rotation = 90)
    plt.xlabel('Age')
    plt.ylabel('No of Players')
    plt.title('No of players of the paricular age')
    plt.show()
def players_teams():
    teams=list(olympics['Team'].unique())
    team_data={}
    for i in olympics['Team']:
        if i not in team_data.keys():
            team_data[i]=1
        else:
            team_data[i]=team_data[i]+1
    team_name=[]
    count=[]
    for i in team_data.keys():
        team_name.append(i)
    for j in team_data.values():
        count.append(j)
    teams=pd.DataFrame({'Teams':team_name,'No of players':count})
    plt.figure(figsize = (20,8))
    sns.barplot(x=teams['Teams'],y=teams['No of players'])
    plt.xticks(rotation = 90)
    plt.xlabel('Teams')
    plt.ylabel('No of Players')
    plt.title('No of players of the paricular team')
    plt.show()
def golds_country():
    filter=(olympics.Medal=='Gold')
    new_data=olympics[filter]
    golds={}
    for i in new_data['NOC']:
        if i not in golds.keys():
            golds[i]=1
        else:
            golds[i]=golds[i]+1
    countries=[]
    count=[]
    for i in golds.keys():
        countries.append(i)
    for j in golds.values():
        count.append(j)
    gold=pd.DataFrame({'Country':countries,'No of golds':count})
    plt.figure(figsize = (20,8))
    sns.barplot(x=gold['Country'],y=gold['No of golds'])
    plt.xticks(rotation = 90)
    plt.xlabel('Country')
    plt.ylabel('No of golds')
    plt.title('No of golds of the paricular country')
    plt.show()
def m_fem_male():
    print("THE NUMBER OF MALE AND FEMALE PARTICIPATED IN OLYMPICS ARE : ")
    olympics['Sex'].value_counts().plot(kind='bar',color='orange')
    plt.show()
def sum_win():
    print("THE HIGHEST NUMBER OF OLYMPICS OCURRED ARE : ")
    olympics['Games'].value_counts().plot(kind='bar',color='pink')
    plt.show()
def summergold_winners():
    summer_gold=[]
    x=olympics.groupby(['Medal','Games']).get_group(('Gold','Summer'))
    print("THE PLAYERS WHO WON GOLD MEDAL IN SUMMER OLYMPICS:")
    for i in x['Name']:
        summer_gold.append(i)
    for j in summer_gold:
        print(j)
def summersilver_winners():
    summer_silver=[]
    y=olympics.groupby(['Medal','Games']).get_group(('Silver','Summer'))
    print("THE PLAYERS WHO WON SILVER MEDAL IN SUMMER OLYMPICS:")
    for i in y['Name']:
        summer_silver.append(i)
    for j in summer_silver:
        print(j)
def summerbronze_winners():
    summer_bronze=[]
    z=olympics.groupby(['Medal','Games']).get_group(('Bronze','Summer'))
    print("THE PLAYERS WHO WON BRONZE MEDAL IN SUMMER OLYMPICS:")
    for i in z['Name']:
        summer_bronze.append(i)
    for j in summer_bronze:
        print(j)
def wintergold_winners():
    winter_gold=[]
    x=olympics.groupby(['Medal','Games']).get_group(('Gold','Winter'))
    print("THE PLAYERS WHO WON GOLD MEDAL IN WINTER OLYMPICS:")
    for i in x['Name']:
        winter_gold.append(i)
    for j in winter_gold:
        print(j)
def wintersilver_winners():
    winter_silver=[]
    y=olympics.groupby(['Medal','Games']).get_group(('Silver','Winter'))
    print("THE PLAYERS WHO WON SILVER MEDAL IN WINTER OLYMPICS:")
    for i in y['Name']:
        winter_silver.append(i)
    for j in winter_silver:
        print(j)
def winterbronze_winners():
    winter_bronze=[]
    z=olympics.groupby(['Medal','Games']).get_group(('Bronze','Winter'))
    print("THE PLAYERS WHO WON BRONZE MEDAL IN WINTER OLYMPICS:")
    for i in z['Name']:
        winter_bronze.append(i)
    for j in winter_bronze:
        print(j)
def number_summergold():
    print("TOTAL NUMBER OF SUMMER OLYMPICS GOLD WINNERS:")
    x=olympics.groupby(['Medal','Games']).get_group(('Gold','Summer'))
    print(x.shape[0])
def number_summersilver():
    print("TOTAL NUMBER OF SUMMER OLYMPICS SILVER WINNERS:")
    y=olympics.groupby(['Medal','Games']).get_group(('Silver','Summer'))
    print(y.shape[0])
def number_summerbronze():
    print("TOTAL NUMBER OF SUMMER OLYMPICS BRONZE WINNERS:") 
    z=olympics.groupby(['Medal','Games']).get_group(('Bronze','Summer'))
    print(z.shape[0])
def number_wintergold():
    print("TOTAL NUMBER OF WINTER OLYMPICS GOLD WINNERS:")
    x=olympics.groupby(['Medal','Games']).get_group(('Gold','Winter'))
    print(x.shape[0])
def number_wintersilver():
    print("TOTAL NUMBER OF WINTER OLYMPICS SILVER WINNERS:")
    y=olympics.groupby(['Medal','Games']).get_group(('Silver','Winter'))
    print(y.shape[0])
def number_winterbronze():
    print("TOTAL NUMBER OF WINTER OLYMPICS BRONZE WINNERS:") 
    z=olympics.groupby(['Medal','Games']).get_group(('Bronze','Winter'))
    print(z.shape[0])
def number_summer():
    print("TOTAL NUMBER OF PLAYERS PARICIPATED IN SUMMER OLYMPICS:")
    l=olympics.groupby(['Games']).get_group(('Summer'))
    print(l.shape[0])
def number_winter():
    print("TOTAL NUMBER OF PLAYERS PARICIPATED IN WINTER OLYMPICS:")
    l=olympics.groupby(['Games']).get_group(('Winter'))
    print(l.shape[0])
def sports_summer():
    summer_sports=[]
    print("THE SPORTS CONDUCTED IN THE SUMMER OLYMPICS:")
    p=olympics.groupby(['Games']).get_group(('Summer'))
    for i in p['Sport']:
        if i not in summer_sports:
            summer_sports.append(i)
    for j in summer_sports:
        print(j)
def sports_winter():
    winter_sports=[]
    print("THE SPORTS CONDUCTED IN THE WINTER OLYMPICS:")
    k=olympics.groupby(['Games']).get_group(('Winter'))
    for i in k['Sport']:
        if i not in winter_sports:
            winter_sports.append(i)
    for j in winter_sports:
        print(j)
def summer_players():
    print("PLAYERS PARTICIPATED IN THE SUMMER OLYMPICS:")
    j=olympics.groupby(['Games']).get_group(('Summer'))
    players_summer=[]
    for i in j['Name']:
        players_summer.append(i)
    for h in players_summer:
        print(h)
def winter_players():
    print("PLAYERS PARTICIPATED IN THE WINTER OLYMPICS:")
    j=olympics.groupby(['Games']).get_group(('Winter'))
    players_winter=[]
    for i in j['Name']:
        players_winter.append(i)
    for h in players_winter:
        print(h)
def city_won():
    list_city=[]
    dict_city={}
    print("THE CITIES WHICH HAS WON MOST OF THE OLYMPIC GAMES:")
    for i in olympics['City']:
        if i not in list_city:
            list_city.append(i)
            dict_city[i]=(olympics.City==i).sum()
    itemMaxValue = max(dict_city.items(), key=lambda x: x[1])
    for key, value in dict_city.items():
        if value == itemMaxValue[1]:
            print(key)
def summer_golds():
    list_team=[]
    print("THE TEAM WHICH HAS WON MORE GOLD MEDALS IN SUMMER OLYMPICS IS:")
    x=olympics.groupby(['Medal','Games']).get_group(('Gold','Summer'))
    dict_team={}
    for i in x['Team']:
        if i not in list_team:
            list_team.append(i)
            dict_team[i]=(x.Team==i).sum()
    itemMaxValue = max(dict_team.items(), key=lambda x: x[1])
    for key, value in dict_team.items():
        if value == itemMaxValue[1]:
            print(key)
def winter_golds():
    list_team=[]
    print("THE TEAM WHICH HAS WON MORE GOLD MEDALS IN WINTER OLYMPICS IS:")
    x=olympics.groupby(['Medal','Games']).get_group(('Gold','Winter'))
    dict_team={}
    for i in x['Team']:
        if i not in list_team:
            list_team.append(i)
            dict_team[i]=(x.Team==i).sum()
    itemMaxValue = max(dict_team.items(), key=lambda x: x[1])
    for key, value in dict_team.items():
        if value == itemMaxValue[1]:
            print(key)
def summer_woncity():
    list_city=[]
    dict_city={}
    x=olympics.groupby(['Games']).get_group(('Summer'))
    print("THE CITIES WHICH HAS WON MOST OF THE SUMMER OLYMPIC GAMES:")
    for i in x['City']:
        if i not in list_city:
            list_city.append(i)
            dict_city[i]=(x.City==i).sum()
    itemMaxValue = max(dict_city.items(), key=lambda x: x[1])
    for key, value in dict_city.items():
        if value == itemMaxValue[1]:
            print(key)
def winter_woncity():
    list_city=[]
    dict_city={}
    x=olympics.groupby(['Games']).get_group(('Winter'))
    print("THE CITY WHICH HAS WON MOST OF THE WINTER OLYMPIC GAMES:")
    for i in x['City']:
        if i not in list_city:
            list_city.append(i)
            dict_city[i]=(x.City==i).sum()
    itemMaxValue = max(dict_city.items(), key=lambda x: x[1])
    for key, value in dict_city.items():
        if value == itemMaxValue[1]:
            print(key)
def players_sports():
    choice=input("Enter the choice to know s for summer olympics sports or w for winter olympics sports for displaying players participated in that sport and n for quit:\n")
    while choice!='n':
        if choice=='s':
            players_list=[]
            sports_summer()
            sport=input("Choose the sport to display the players participated in that sport in summer olympics:\n")
            x=olympics.groupby(['Games','Sport']).get_group(('Summer',sport))
            for i in x['Name']:
                players_list.append(i)
            print("THE PLAYERS PARTICIPATED IN {} IN THE SUMMER OLYMICS ARE:".format(sport))
            for j in players_list:
                print(j)
        elif choice=='w':
            players_list=[]
            sports_winter()
            sport=input("Choose the sport to display the players participated in that sport in winter olympics:\n")
            x=olympics.groupby(['Games','Sport']).get_group(('Winter',sport))
            for i in x['Name']:
                players_list.append(i)
            print("\nTHE PLAYERS PARTICIPATED IN {} IN THE SUMMER OLYMICS ARE:".format(sport))
            for j in players_list:
                print(j)
        choice=input("Enter the choice to continue to know s for summer olympics sports or w for winter olympics sports for displaying players participated in that sport and n for quit:\n")
def avg_height():
    print("THE AVERAGE HEIGHT OF THE PLAYERS IS : ")
    print(olympics["Height"].mean())
def avg_weight():
    print("THE AVERAGE WEIGHT OF THE PLAYERS IS : ")
    print(olympics["Weight"].mean())
def no_fem_male():
    print(olympics["Sex"].value_counts())
def rename_col():
    ch2=input("Enter any one to change:\ni for id:0\n n for name\n s for sex\n a for age \n h for height \n w for weight \n t for team \n no for NOC\n y for year\n c for city \nc for city\n sp for sport \n e for event \n m for medal \n g for game \n")
    if ch2=='i':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"ID: 0":word},inplace=True)
    elif ch2=='n':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Name":word},inplace=True)
    elif ch2=='s':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Sex":word},inplace=True)
    elif ch2=='a':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Age":word},inplace=True)
    elif ch2=='h':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Height":word},inplace=True)
    elif ch2=='w':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Weigth":word},inplace=True)
    elif ch2=='t':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Team":word},inplace=True)
    elif ch2=='no':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"NOC":word},inplace=True)
    elif ch2=='y':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Year":word},inplace=True)
    elif ch2=='c':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"City":word},inplace=True)
    elif ch2=='sp':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Sport":word},inplace=True)
    elif ch2=='e':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Event":word},inplace=True)
    elif ch2=='m':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Medal":word},inplace=True)
    elif ch2=='g':
        word=input("To what name do u want to change it\n")
        olympics.rename(columns={"Game":word},inplace=True)
def sort_name():
    print(olympics.sort_values(by='Name'))
def drop_col():
    olympics_copy=olympics.copy()
    ch2=input("Enter any one to change:\ni for id:0\n n for name\n s for sex\n a for age \n h for height \n w for weight \n t for team \n no for NOC\n y for year\n c for city \nc for city\n sp for sport \n e for event \n m for medal \n g for game \n")
    if ch2=='i':
        print(olympics_copy.drop(['ID'],axis=1))
        
    elif ch2=='n':
        print(olympics_copy.drop(['Name'],axis=1))
        
    elif ch2=='s':
        print(olympics_copy.drop(['Sex'],axis=1))
       
    elif ch2=='a':
        print(olympics_copy.drop(['Age'],axis=1))
        
       
    elif ch2=='h':
        print(olympics_copy.drop(['Height'],axis=1))
        
    elif ch2=='w':
        print(olympics_copy.drop(['Weight'],axis=1))
        
    elif ch2=='t':
        print(olympics_copy.drop(['Team'],axis=1))
        
        
    elif ch2=='no':
        print(olympics_copy.drop(['NOC'],axis=1))
        
        
    elif ch2=='y':
        print(olympics_copy.drop(['YEAR'],axis=1))
       
    elif ch2=='c':
        print(olympics_copy.drop(['Country'],axis=1))
        
       
    elif ch2=='sp':
        print(olympics_copy.drop(['Sport'],axis=1))
       
       
    elif ch2=='e':
        print(olympics_copy.drop(['Event'],axis=1))
       
    elif ch2=='m':
        print(olympics_copy.drop(['Medal'],axis=1))
        
    elif ch2=='g':
        print(olympics_copy.drop(['Game'],axis=1))
def remove_nan():
    olympics_copyw=olympics.copy() 
    print(olympics_copyw.dropna())
def calculate_BMI():
    dict_bmi={}
    names=[]
    height=[]
    weight=[]
    k=0
    olympics_copyb=olympics.copy()
    olympics_copyb=olympics_copyb.dropna(subset=['Height','Weight'])
    for i in olympics_copyb['Name']:
        names.append(i)
    for i in olympics_copyb['Height']:
        height.append(i)
    for i in olympics_copyb['Weight']:
        weight.append(i)
    for i,j in zip(height,weight):
        dict_bmi[names[k]]=(j/((i/100)**2))
        k=k+1
    for i,j in dict_bmi.items():
        print("{} has {} bmi ".format(i,j))
def players_not_medal():
    olympics_copym=olympics.copy()
    cols=['ID','Sex','Event','Games','Age','Height','Weight','Team','NOC','Year','City','Sport']
    print(olympics_copym.drop(cols,axis=1))
    #print(olympics_copym)    
    
def sum_gold_sil_bro():
    data=olympics[olympics['Games']=='Summer']
    data.Medal.value_counts()
    labels=data.Medal.value_counts().index
    colors=['red','gold','silver']
    explode=[0,0,0]
    sizes=data.Medal.value_counts().values
    plt.figure(figsize=(7,7))
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%')
    print("THE HIGHEST MEDAL WON IN SUMMER IS : ")
    plt.show()
    
def new_row_end():
    olympics.loc[len(olympics)]=[352,'Aathmika','F',23,173,64,'India','IND',2012,'Coimbatore','Hockey','Hockey','Silver','Winter']
    print(olympics)


def append():
    a={'ID':1,'Name':'A Dijiang','Sex':'M','Age':24,'Height':180,'Weight':80,'Team':'China','NOC':'CHN','Year':1992,'City':'Barcelona','Sport':'Basketball','Event':'Basketball','Medal':'Gold','Games':'Summer'}
    b={'ID':2,'Name':'A Lamusi','Sex':'M','Age':23,'Height':170,'Weight':60,'Team':'China','NOC':'CHN','Year':2012,'City':'London','Sport':'Judo','Event':'Judo Mens','Medal':'Silver','Games':'Summer'}
    df1 = pd.DataFrame(a, index=[0])
    df2 = pd.DataFrame(b, index=[1])
    d1 = pd.DataFrame()
    d1 = d1.append(df1)
    d1 = d1.append(df2).fillna(0)
    print(d1)
    
def concat():
    a={'ID':1,'Name':'A Dijiang','Sex':'M','Age':24,'Height':180,'Weight':80,'Team':'China','NOC':'CHN','Year':1992,'City':'Barcelona','Sport':'Basketball','Event':'Basketball','Medal':'Gold','Games':'Summer'}
    b={'ID':2,'Name':'A Lamusi','Sex':'M','Age':23,'Height':170,'Weight':60,'Team':'China','NOC':'CHN','Year':2012,'City':'London','Sport':'Judo','Event':'Judo Mens','Medal':'Silver','Games':'Summer'}
    df1 = pd.DataFrame(a, index=[0])
    df2 = pd.DataFrame(b, index=[1])
    d2 = pd.concat([df1, df2]).fillna(0)
    print(d2)
    
def combine_first():
    a={'ID':1,'Name':'A Dijiang','Sex':'M','Age':24,'Height':180,'Weight':80,'Team':'China','NOC':'CHN','Year':1992,'City':'Barcelona','Sport':'Basketball','Event':'Basketball','Medal':'Gold','Games':'Summer'}
    b={'ID':2,'Name':'A Lamusi','Sex':'M','Age':23,'Height':170,'Weight':60,'Team':'China','NOC':'CHN','Year':2012,'City':'London','Sport':'Judo','Event':'Judo Mens','Medal':'Silver','Games':'Summer'}
    df1 = pd.DataFrame(a, index=[0])
    df2 = pd.DataFrame(b, index=[1])
    d3 = pd.DataFrame()
    d3 = d3.combine_first(df1).combine_first(df2).fillna(0)
    print(d3)
    
def nsmallest():
    print(olympics.nsmallest(1,['Weight']))
    
def nlargest():
    print(olympics.nlargest(1,['Height']))
    
def mean_weight():
    mean=olympics["Weight"].mean()
    print(mean)

def mean_height():
    mean=olympics["Height"].mean()
    print(mean)
def mode():
    mode=olympics.loc[:,"Weight"].mode()
    print(mode)
    
def median():
    median=olympics["Weight"].median()
    print(median)
    
def dicti():
    data=({'ID':[0,1],'Name':['Advaitha','A Dijiang'],'Sex':['F','M'],'Age':[25,24],'Height':[170,180],'Weight':[59,80],'Team':['India','China'],'NOC':['IND','CHN'],'Year':[2000,1992],'City':['New Delhi','Barcelona'],'Sport':['Baketball','Basketball'],'Event':['Basketball','Basketball'],'Medal':['Gold','Gold'],'Games':['Summer','Summer']})
    dicti=pd.DataFrame(data)
    print(dicti)
    
def num_gold_basketball():
    x=olympics.groupby(['Medal','Sport']).get_group(('Gold','Basketball'))
    print(x.shape[0])
    
def num_silver_Swimming():
    y=olympics.groupby(['Medal','Sport']).get_group(('Silver','Swimming'))
    print(y.shape[0])
    
def num_bronze_icehockey():
    z=olympics.groupby(['Medal','Sport']).get_group(('Bronze','Ice Hockey'))
    print(z.shape[0])
    
def male_data():
    print(olympics.loc[olympics['Sex'].isin(['M'])])
    
def female_data():
    print(olympics.loc[olympics['Sex'].isin(['F'])])
    
def num_males():
    b=olympics.groupby(['Sex']).get_group(('M'))
    print(b.shape[0])
    
def num_females():
    a=olympics.groupby(['Sex']).get_group(('F'))
    print(a.shape[0])

def top_5_event():
    events = olympics["Event"].value_counts()
    plt.figure(figsize = (20, 7))
    sns.barplot(x = events[:5].index, y = events[:5].values)
    plt.ylabel('Number of event')
    plt.xlabel('Events')

    plt.title('Top Events', color = 'blue', fontsize = 15)
    plt.show()

def per_medals_2012():
    data2012 = olympics[olympics['Year'] == 2012]
    data2012.Medal.value_counts()
    labels = data2012.Medal.value_counts().index
    colors = ['red', 'gold', 'silver']
    explode = [0, 0, 0]
    sizes = data2012.Medal.value_counts().values
    
    plt.figure(figsize = (7, 7))
    plt.pie(sizes, explode = explode, labels = labels, colors = colors , autopct='%1.1f%%')
    plt.title('Medals according to 2012', color = 'blue', fontsize = 15)
    plt.show()

def top_bb_team():
    dataBasketballWithMedals = olympics[(olympics["Sport"] == "Basketball") & (olympics["Medal"] == "Gold")]
    dataBasketballWithMedals.Team.value_counts()
    plt.figure(figsize = (10, 7))
    sns.countplot(x = dataBasketballWithMedals.Team)
    plt.ylabel('Number of gold medals')
    plt.title('Top Basketball Teams', color = 'blue', fontsize = 15)
    plt.show()
    
def top_10_sport():
    sports = olympics.Sport.value_counts()
    plt.figure(figsize = (17, 7))
    sns.barplot(x = sports[:10].index, y = sports[:10].values)
    plt.ylabel('Number of Sport')
    plt.xlabel('Sport Types')
    plt.title('Top Sports', color = 'blue', fontsize=15)
    plt.show()
    
def main():
    choice=int(input("Enter the choice needed:\n0.QUIT\n1.PLAYERS LIST WON GOLD IN SUMMER OLYMPICS\n2.PLAYERS LIST WON SILVER IN SUMMER OLYMPICS\n3.PLAYERS LIST WON BRONZE IN SUMMER OLYMPICS\n4.PLAYERS LIST WON GOLD IN WINTER OLYMPICS\n5.PLAYERS LIST WON SILVER IN WINTER OLYMPICS\n6.PLAYERS LIST WON BRONZE IN WINTER OLYMPICS\n7.NUMBER OF PLAYERS WHO GOLD IN SUMMER OLYMPICS\n8.NUMBER OF PLAYERS WON SILVER IN SUMMER OLYMPICS\n9.NUMBER OF PLAYERS WON BRONZE IN SUMMER OLYMPICS\n10.NUMBER OF PLAYERS WON GOLD IN WINTER OLYMPICS\n11.NUMBER OF PLAYERS WON SILVER IN WINTER OLYMPICS\n12.NUMBER OF PLAYERS WON BRONZE IN WINTER OLYMPICS\n13.NUMBER OF PLAYERS PARTICIPATED IN SUMMER OLYMPICS\n14.NUMBER OF PLAYERS PARTICIPATED IN WINTER OLYMPICS\n15.SPORTS CONDUCTED IN SUMMER OLYMPICS\n16.SPORTS CONDUCTED IN WINTER OLYMPICS\n17.PLAYERS LIST WHO PARTICIPATED IN SUMMER OLYMPICS\n18.PLAYERS LIST WHO PARTICIPATED IN WINTER OLYMPICS\n19.CITY WHICH HAS WON MOST OF SUMMER AND WINTER OLYMPICS\n20.TEAM WHICH HAS WON MORE GOLDS IN SUMMEROLYMPICS\n21.TEAM WHICH HAS WON MORE GOLDS IN WINTER OLYMPICS\n22.WHICH CITY HAS WON MOST OF SUMMER OLYMPICS\n23.WHICH CITY HAS WON MOST OF WINTER OLYMPICS\n24.PLAYERS LIST BASED ON THE SPORT PARTICIPATED\n25.TO FIND THE AVERAGE OF THE HEIGHT OF THE PLAYERS\n26.TO FIND THE AVERAGE OF THE WEIGHT OF THE PLAYERS\n27.TO FIND THE NUMBER OF MALE AND FEMALE PARTICIPANTS\n28.DO YOU WANT TO RENAME COLOUMN\n29.TO SORT THE DATA ACCORDING TO THE NAMES OF THE PLAYERS\n30.TO REMOVE ANY COLOUMN\n31.TO REMOVE THE 'NA' VALUES\n32.TO CALCULATE BMI OF THE PLAYERS\n33.TO DISPLAY THE PLAYERS WHO HAVE NOT WON ANY MEDALS\n34.TOTAL MEDAL COUNTS WON BY EACH TEAM GRAPH\n35.GRAPH OF NUMBER OF PLAYERS OF PARTICULAR AGE\n36.GRAPH FOR NUMBER OF PLAYERS OF PARTICULAR TEAM\n37.GRAPH OF NUMBER OF GOLDS WON BY PARTICULAR COUNTRY\n38.GRAPH FOR NUMBER OF MALES AND FEMALES PARTICIPATED IN OLYMPICS\n39.GRAPH FOR NUMBER OF OLYMPICS OCCURED IN YEARS ARE\n40.GRAPH FOR HIGHEST MEDAL WON IN SUMMER IS\n41.ADD A NEW DATA IN THE END OF THE DATASET\n42.TAKE FIRST TWO DATA AND PERFORM APPEND OPERATION\n43.TAKE FIRST TWO DATA AND PERFORM CONCAT OPERATION\n44.TAKE FIRST TWO DATA AND PERFORM COMBINE FIRST OPERATION\n45.THE DATA OF THE PERSON WITH SMALLEST WEIGHT\n46.THE DATA OF THE PERSON WITH LARGEST HEIGHT\n47.AVERAGE OF THE WEIGHTS OF THE PERSONS\n48.AVERAGE OF THE HEIGHTS OF THE PERSONS\n49.FIND THE MODE OF THE WEIGHTS\n50.FIND THE MEDIAN OF THE WEIGHTS\n51.STORE TWO DATA IN A DICTIONARY AND CONVERT IT INTO A DATAFRAME\n52.NUMBER OF PLAYERS WHO WON GOLD IN BASKETBALL\n53.NUMBER OF PLAYERS WHO WON SILVER IN SWIMMING\n54.NUMBER OF PLAYERS WHO WON BROZE IN ICEHOCKEY\n55.PRINT ALL THE DATA OF THE MALE PARTICIPANTS\n56.PRINT ALL THE DATA OF THE FEMALE PARTICIPANTS\n57.NUMBER OF MALE PARTICIPANTS IN OLYMPICS\n58.NUMBER OF FEMALE PARTICIPANTS IN OLYMPICS\n59.GRAPH FOR TOP FIVE EVENTS IN THE OLYMPICS\n60.PERCENTAGE OF MEDALS IN THE YEAR 2012 IS\n61.TOP BASKETBALL TEAMS ARE\n62.TOP TEN SPORTS OF OLYMPICS IS\n"))
    while choice>0:
        if choice==1:
            summergold_winners()
            print("\n") 
        elif choice==2:
            summersilver_winners()
            print("\n")
        elif choice==3:
            summerbronze_winners()
            print("\n")
        elif choice==4:
            wintergold_winners()
            print("\n")
        elif choice==5:
            wintersilver_winners()
            print("\n")
        elif choice==6:
            winterbronze_winners()
            print("\n")
        elif choice==7:
            number_summergold()
            print("\n")
        elif choice==8:
            number_summersilver()
            print("\n")
        elif choice==9:
            number_summerbronze()
            print("\n")
        elif choice==10:
            number_wintergold()
            print("\n")
        elif choice==11:
            number_wintersilver()
            print("\n")
        elif choice==12:
            number_winterbronze()
            print("\n")
        elif choice==13:
            number_summer()
            print("\n")
        elif choice==14:
            number_winter()
            print("\n")
        elif choice==15:
            sports_summer()
            print("\n")
        elif choice==16:
            sports_winter()
            print("\n")
        elif choice==17:
            summer_players()
            print("\n")
        elif choice==18:
            winter_players()
            print("\n")
        elif choice==19:
            city_won()
            print("\n")
        elif choice==20:
            summer_golds()
            print("\n")
        elif choice==21:
            winter_golds()
            print("\n")
        elif choice==22:
            summer_woncity()
            print("\n")
        elif choice==23:
            winter_woncity()
            print("\n")
        elif choice==24:
            players_sports()
            print("\n") 
        elif choice==25:
            avg_height()
            print("\n")
        elif choice==26:
            avg_weight()
            print("\n")
        elif choice==27:
            no_fem_male()
            print("\n")
        elif choice==28:
            rename_col()
            print("\n")
        elif choice==29:
            sort_name()
            print("\n")
        elif choice==30:
            drop_col()
            print("\n")
        elif choice==31:
            remove_nan()
            print("\n")
        elif choice==32:
            calculate_BMI()
            print("\n")
        elif choice==33:
            players_not_medal()
            print("\n")
        elif choice==34:
            teams_medals()
            print("\n")
        elif choice==35:
            players_age()
            print("\n")
        elif choice==36:
            players_teams()
            print("\n")
        elif choice==37:
            golds_country()
            print("\n")
        elif choice==38:
            m_fem_male()
            print("\n")
        elif choice==39:
            sum_win()
            print("\n")
        elif choice==40:
            sum_gold_sil_bro()
            print("\n")
        elif choice==41:
            new_row_end()
            print("\n")
        elif choice==42:
            append()
            print("\n")
        elif choice==43:
            concat()
            print("\n")
        elif choice==44:
            combine_first()
            print("\n")
        elif choice==45:
            nsmallest()
            print("\n")
        elif choice==46:
            nlargest()
            print("\n")
        elif choice==47:
            mean_weight()
            print("\n")
        elif choice==48:
            mean_height()
            print("\n")
        elif choice==49:
            mode()
            print("\n")
        elif choice==50:
            median()
            print("\n")
        elif choice==51:
            dicti()
            print("\n")
        elif choice==52:
            num_gold_basketball()
            print("\n")
        elif choice==53:
            num_silver_Swimming()
            print("\n")
        elif choice==54:
            num_bronze_icehockey()
            print("\n")
        elif choice==55:
            male_data()
            print("\n")
        elif choice==56:
            female_data()
            print("\n")
        elif choice==57:
            num_males()
            print("\n")
        elif choice==58:
            num_females()
            print("\n")
        elif choice==59:
            top_5_event()
            print("\n")
        elif choice==60:
            per_medals_2012()
            print("\n")
        elif choice==61:
            top_bb_team()
            print("\n")
        elif choice==62:
            top_10_sport()
            print("\n")
        choice=int(input("Enter the choice to continue:\n0.QUIT\n1.PLAYERS LIST WON GOLD IN SUMMER OLYMPICS\n2.PLAYERS LIST WON SILVER IN SUMMER OLYMPICS\n3.PLAYERS LIST WON BRONZE IN SUMMER OLYMPICS\n4.PLAYERS LIST WON GOLD IN WINTER OLYMPICS\n5.PLAYERS LIST WON SILVER IN WINTER OLYMPICS\n6.PLAYERS LIST WON BRONZE IN WINTER OLYMPICS\n7.NUMBER OF PLAYERS WHO GOLD IN SUMMER OLYMPICS\n8.NUMBER OF PLAYERS WON SILVER IN SUMMER OLYMPICS\n9.NUMBER OF PLAYERS WON BRONZE IN SUMMER OLYMPICS\n10.NUMBER OF PLAYERS WON GOLD IN WINTER OLYMPICS\n11.NUMBER OF PLAYERS WON SILVER IN WINTER OLYMPICS\n12.NUMBER OF PLAYERS WON BRONZE IN WINTER OLYMPICS\n13.NUMBER OF PLAYERS PARTICIPATED IN SUMMER OLYMPICS\n14.NUMBER OF PLAYERS PARTICIPATED IN WINTER OLYMPICS\n15.SPORTS CONDUCTED IN SUMMER OLYMPICS\n16.SPORTS CONDUCTED IN WINTER OLYMPICS\n17.PLAYERS LIST WHO PARTICIPATED IN SUMMER OLYMPICS\n18.PLAYERS LIST WHO PARTICIPATED IN WINTER OLYMPICS\n19.CITY WHICH HAS WON MOST OF SUMMER AND WINTER OLYMPICS\n20.TEAM WHICH HAS WON MORE GOLDS IN SUMMEROLYMPICS\n21.TEAM WHICH HAS WON MORE GOLDS IN WINTER OLYMPICS\n22.WHICH CITY HAS WON MOST OF SUMMER OLYMPICS\n23.WHICH CITY HAS WON MOST OF WINTER OLYMPICS\n24.PLAYERS LIST BASED ON THE SPORT PARTICIPATED\n25.TO FIND THE AVERAGE HEIGHT OF THE PLAYERS\n26.TO FIND THE AVERAGE WEIGHT OF THE PLAYERS \n27.TO FIND THE NUMBER OF MALE AND FEMALE PARTICIPANTS\n28.DO YOU WANT TO RENAME COLOUMN\n29.TO SORT THE DATA ACCORDING TO THE PLAYERS NMAE\n30.TO REMOVE ANY COLOUMN\n31.TO REMOVE 'NA' VALUES\n32.TO CALCULATE THE BMI OF THE PLAYERS\n33.TO DISPLAY THE PLAYERS WHO HAVE NOT WON ANY MEDALS\n34.TOTAL MEDALS WON BY EACH TEAM GRAPH\n35.GRAPH OF NUMBER OF PLAYERS OF PARTICULAR AGE\n36.GRAPH FOR NUMBER OF PLAYERS OF PARTICULAR TEAM\n37.GRAPH OF NUMBER OF GOLDS WON BY PARTICULAR COUNTRY\n38.GRAPH FOR NUMBER OF MALES AND FEMALES PARTICIPATED IN OLYMPICS\n39.GRAPH FOR NUMBER OF OLYMPICS OCCURED IN YEARS ARE\n40.GRAPH FOR HIGHEST MEDAL WON IN SUMMER IS\n41.ADD A NEW DATA IN HE END OF THE DATASET\n42.TAKE FIRST TWO TWO DATA AND PERFORM APPEND OPERATION\n43.TAKE FIRST TWO DATA AND PERFORM CONCAT OPERATION\n44.TAKE FIRST TWO DATA AND PERFORM COMBINE FIRST OPERATION\n45.THE DATA OF THE PERSON WITH SMALLEST WEIGHT\n46.THE DATA OF THE PERSON WITH THE LARGEST HEIGHT\n47.AVERAGE OF THE WEIGHTS OF THE PERSONS\n48.AVERAGE OF THE HEIGHTS OF THE PERSONS\n49.FIND THE MODE OF THE WEIGHTS\n50.FIND THE MEDIAN OF THE WEIGHTS\n51.STORE TWO DATA IN DICTIONARY AND CONVERT IT INTO A DATAFRAME\n52.NUMBER OF PLAYERS WHO WON GOLD IN BASKETBALL\n53.NUMBER OF PLAYERS WHO WON SILVER IN SWIMMING\n54.NUMBER OF PLAYERS  WHO WON BRONZE IN ICEHOCKEY\n55.PRINT ALL THE DATA OF THE MALE PARTICIPANTS\n56.PRINT ALL THE DATA OF THE FEMALE PARTICIPANTS\n57.NUMBER OF MALE PARTICIPANTS IN THE OLYMPICS\n58.NUMBER OF FEMALE PARTICIPANTS IN THE OLYMPICS\n59.GRAPH FOR TOP 5 EVENTS IN THE OLYMPICS\n60.THE PERCENTAGE OF MEDALS IN YEAR 2012 IS\n61.TOP BASKETBALL TEAMS ARE\n62.TOP TEN SPORTS OF OLYMPICS IS\n"))
main()
