class MLH_Fellowship:
    def information(self):
        print('\tName:  Prajesh Srivastava')
        print('\tEmail: prajeshsrivastava786@gmail.com\n')
    def education(self):
        print('\tBachelor of Technology(GLA University, Mathura)\t 2022 \n')
        print('\tIntermediate(Gyandeep English School,Varanasi)\t2018 \n')
        print('\tHigh School(Gyandeep English School,Varanasi)\t 2016\n')
    def skills(self):
        print('\tTeamwork and Collaboration \n\tEffective Analytical Skill\n'
              '\tAbility to identif and solve problem\n\tListening skill\n')
    def experience(self):
        print('\tMicrosoft Learn Student Ambassador(Microsoft)\tAugust2020-Present\n'
              '\tPresident(Pi Maths Club,GLAU)\t\t\tAugust2020-Present\n'
              '\tCampus Ambassador(Coding Blocks)\t\tJuly2019-July2020\n'
              '\tMember(E-cell ,GLAU)\t\t\t\tSep.2018-sep.2019\n')

Prajesh=MLH_Fellowship()
while True:
    print('Information PRESS 1\n'
          'Education PRESS 2\n'
          'Skills PRESS 3\n'
          'Experience PRESS 4\n'
          'Quit PRESS 0')
    fetching=int(input())
    if fetching==0:
        print('Thanks , See you soon')
        break
    elif fetching==1:
        Prajesh.information()
    elif fetching==2:
        Prajesh.education()
    elif fetching==3:
        Prajesh.skills()
    elif fetching==4:
        Prajesh.experience()
    else:
        print('oohhoo , Wrong Input try again...\n')
        
        
        
