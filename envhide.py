import os
import string 
from pprint import pprint
import random # to get a random string 


# make a list of all the windows environment variables 
# GET ALL THESE FROM  : https://www.computerhope.com/issues/ch000088.html
env_var = [
    "ALLUSERSPROFILE",
    "CommonProgramFiles",  
    "CommonProgramW6432", 
    "ComSpec", 
    "PATHEXT", 
    "ProgramData", 
    "ProgramFiles",  
    "ProgramW6432",  
    "PSModulePath", 
    "PUBLIC", 
    "SystemDrive", 
    "SystemRoot",
    "windir",
    
]

'''
TESTING PART ==> 
# get our -user name , cuz we dont want someone to see it 
current_username = os.getenv('USERNAME')

# check each of them 
for each_var in env_var:
    # get the value wrt key(each env variable)
    value = os.getenv(each_var)
    
    # skip our name 
    if current_username in value or any(keyword in each_var for keyword in ["LOGONSERVER", "USERDOMAIN", "COMPUTERNAME"]):
        continue
    
    # if value exists 
    if value:
        print(f"{each_var} = {value}")
        
'''

# ex:   { 'e': {PUBLIC : [5]}   }  ==> for prinatable 'e' ==> in the value of PUBLIC -- path ==> 
# C:\Users\Public , we have 5 TH INDEX AS 'e' , we are tracking the index of all such occurence of e in PUBLIC 

env_mapping = {}

# check all the strings in string module available s
# A printable string is any sequence of four or more printable characters terminated by a new line or NULL 
# character. ==> env_mapping

for character in string.printable:
    env_mapping[character] = {}  # creating a nested-dictionary 
    # print(character)  ==> each cahracter 0-9 and some special symbols in printable 
    for var in env_var:
        value = os.getenv(var)
        # print(value) ==> to get the path of each environment varibale 
        
        # check if that printable character in path 
        if character in value:
            # if yes , map the character, variable with a empty list for future tracking 
            env_mapping[character][var] = []  
            
            # i is index , c is value  , enumerate() ==> to continuously iterate based on path 
            for i, c in enumerate(value):
                # if we found match for printable-character and actual environment variable , then add it to index i  in dictionary 
                if character == c:
                    env_mapping[character][var].append(i)
                    
# pprint(env_mapping)

# Obfuscate means to make something unclear or hard to understand, especially on purpose. 
def envhide_obfuscate(string):
    obf_code = []
    for c in string:
        # get the curr string   , get only the keys (a, b , A , C , ' ..) , since it is iterable , convert it into a list 
        possible_vars = list(env_mapping[c].keys())
        
        # if possible_vars is {} ==> empty ==> not present , ==> {'' : {} } ==> empty spaces  
        # just add cahracter itself  ['']
        if not possible_vars :
            obf_code.append(f'[char]{ord(c)}')  # char 65 ==> A (ascii value -65)
            continue
            
        chosen_var = random.choice(possible_vars)
        
        # get the index for random choosen , chck possible and chosen both 
        possible_indices = env_mapping[c][chosen_var]
        
        # testing purpose for choosen-var , possible-indices  , 
        # chosen_var='SystemRoot' possible_indices=[3, 8] 
        # print(f"{chosen_var=} {possible_indices=}")
        
        chosen_index = random.choice(possible_indices)
        
        # now buuld our new character - randomly choosen + existing 
        new_character = os.getenv(chosen_var)[chosen_index]
        
        # add the powershell syntax 
        pwsh_syntax = f'$env:{chosen_var}[{chosen_index}]'  # this is a bash script 
        obf_code.append(pwsh_syntax)
        
    return  obf_code  

# invoke a new iex 
def pwsh_obfuscate(string):
    iex = envhide_obfuscate('iex') # pass iex tool globally as prefix 
    pieces = envhide_obfuscate(string)
    iex_stage = f'({",".join(iex)} -Join ${random.randint(1, 99999)})'
    payload_stage= f'({",".join(pieces)} -Join ${random.randint(1, 99999)})'
    return f'& {iex_stage} {payload_stage}'
    
powershell_command = "Write-Output 420"
# pprint(envhide_obfuscate(powershell_command))  == testing purpose 
print(pwsh_obfuscate(powershell_command))