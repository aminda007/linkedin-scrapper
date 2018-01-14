import json


class Extractor:

    profile_data = {}

    def extract_info(self, data):

        intro = data['included'][-1]
        included = data['included']
        print(intro)
        print(included[0])

        firstName = intro['firstName']
        lastName = intro['lastName']
        occupation = intro['occupation']

        skills = []
        experience = []

        for index, i in enumerate(included):
            if 'name' in i.keys():
                print(i)
                print(index)
                if (len(i) == 9):
                    print(i['name'] + 'company')
                    experience.append(i['name'])
                if (len(i) == 4):
                    skills.append(i['name'])

        skillsList = ''
        for i in skills:
            skillsList += (i + ', ');

        experienceList = ''
        for i in experience:
            experienceList += (i + ', ');

        print('\n' + 'Name:       ' + firstName + ' ' + lastName + '\n'
                'Occupation: ' + occupation + '\n'
                'Skills:     ' + skillsList[:-2] + '\n'
                'Experience: ' + experienceList[:-2])

