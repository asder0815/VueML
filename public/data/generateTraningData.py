import csv
import random
 
class Options: 
    reultModifierMultiplier = 15
    ageThreshold = 10
    sizeThreshold = 15
    genders = ['male', 'female', 'diverse']
    countries = ['Germany', 'France', 'Poland', 'England']
    ethnicities = ['German', 'French', 'Polish', 'Russian', 'English', 'Arab']
    industries = ['Software', 'Marketing', 'Retail', 'Automotive', 'Machines', 'Fashion', 'Architecture']
    results = ['success', 'failure']

class SalesRep:
    def __init__(self, name, preferredAge, preferredGender, preferredCountry, preferredEthnicity, preferredSize, preferredIndustry): 
        self.name = name
        self.preferredAge = preferredAge
        self.preferredGender = preferredGender
        self.preferredCountry = preferredCountry, 
        self.preferredEthnicity = preferredEthnicity
        self.preferredSize = preferredSize
        self.preferredIndustry = preferredIndustry

    def generateSale(self):
        salesRep = self.name
        leadScore = round(random.uniform(0,100), 2)
        customerAge = random.randint(29, 76)
        customerGender = random.choice(Options.genders)
        customerCountry = random.choice(Options.countries)
        customerEthnicity = random.choice(Options.ethnicities)
        companySize = random.randint(3, 100)
        companyIndustry = random.choice(Options.industries)
        result = ''
        resultModifier = 0
        if self.preferredAge - Options.ageThreshold <= customerAge <= self.preferredAge + Options.ageThreshold:
            resultModifier = resultModifier + 1
        else:
            resultModifier = resultModifier - 1
        if self.preferredGender == customerGender:
            resultModifier = resultModifier + 1
        else:
            resultModifier = resultModifier - 1
        if self.preferredCountry == customerCountry:
            resultModifier = resultModifier + 1
        else:
            resultModifier = resultModifier - 1
        if self.preferredEthnicity == customerEthnicity:
            resultModifier = resultModifier + 1
        else:
            resultModifier = resultModifier - 1
        if self.preferredSize / Options.sizeThreshold <= companySize <= self.preferredSize * Options.sizeThreshold:
            resultModifier = resultModifier + 1
        else:
            resultModifier = resultModifier - 1
        if self.preferredIndustry == companyIndustry:
            resultModifier = resultModifier + 1
        else:
            resultModifier = resultModifier - 1
        if(random.random() * 100 < leadScore + (resultModifier * Options.reultModifierMultiplier)):
            result = 'success'
        else: 
            result = 'failure'
        return [salesRep,leadScore,customerAge,customerGender,customerCountry,customerEthnicity,companySize,companyIndustry,result]

salesreps = [
    SalesRep('Max', 30, 'male', 'Germany', 'German', 50, 'Software'),
    SalesRep('Erika', 26, 'female', 'France', 'French', 20, 'Marketing'),
    SalesRep('Frank', 26, 'male', 'England', 'English', 250, 'Retail'),
    SalesRep('Andre', 26, 'male', 'Germany', 'German', 100, 'Automotive')
]

header = ['salesRep','leadScore','customerAge','customerGender','customerCountry','customerEthnicity','companySize','companyIndustry','result']
rows = []

for rep in salesreps: 
    x = 0
    for x in range (30): 
        rows.append(rep.generateSale())

with open('public/data/trainingdata.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rows: 
        print(row)
        writer.writerow(row)

