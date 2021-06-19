years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]

def annual_births_average(years=years, births=births):
   '''Return a list of tuples with each entry in this format
       (year, birth, running_average)
       Round the running_average to the nearest integer. 
   '''  
   results = []
   sum_ = 0

   for index, (year, birth) in enumerate(zip(years, births), start=1):
      sum_ += birth
      results.append((year, birth, round(sum_ / index)))

   return results


print(*annual_births_average(years, births), sep='\n')
'''
(2010, 723165, 723165)
(2011, 723913, 723539)
(2012, 729674, 725584)
(2013, 698512, 718816)
(2014, 695233, 714099)
(2015, 697852, 711392)
(2016, 696271, 709231)
(2017, 679106, 705466)
(2018, 657076, 700089)
(2019, 640370, 694117)
'''
