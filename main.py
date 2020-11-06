#!/usr/bin/env python3

print('='*80+'\n\t\t\tPennsylvania Projection')
'''
Joseph R. Biden Jr.
Democrat
3,307,724	49.5%
Donald J. Trump*
Republican
3,295,334	49.3
'''
#trump & biden current vote totals
b = 3307724
t = 3295334

print(f'current status: \n\tTrump: {b} votes\n\tBiden: {b} votes\n\tDifference: {b-t} +Biden\n')

def get_vote_diff(trump:int , biden: int) -> int:

    
    print(f'''
            Trump has {trump} votes and Biden has {biden} votes.
            The difference to make up is {abs(trump-biden)} votes.
           ''')
    return abs(trump-biden)


def get_fractions(margin: int) -> tuple: # Tup(float, float)
    '''
    larger + smaller = 100
    larger - smaller = margin
    '''
    larger           = ( 100 + margin )/2
    smaller          = 100 - larger
    return (larger, smaller)

def get_vote_gain(county_name:str, margin: float, frac_reporting: int, current_votes: int, verbose=False):
    
    final_total_votes = current_votes/(frac_reporting/100)
    #print(final_total_votes, current_votes, frac_reporting)
    remaining_votes   = final_total_votes - current_votes

    big, small        = get_fractions(margin)

    big_vote_delta    = big*remaining_votes/100
    small_vote_delta  = small*remaining_votes/100
    
    gain              = big_vote_delta - small_vote_delta

    gain_message = f'The gain will be: {int(gain):,} votes'
    message = f'The gain will be: {int(gain):,} votes'
    if county_name: 
        message = f'In {county_name} county, ' + message
    
    
    return gain
    
    
'''
source: https://www.nytimes.com/interactive/2020/11/03/us/elections/results-pennsylvania-president.html

County	        Margin	   | Est. votes reported 	Total votes Absentee
-----------------------------------------------------------------------

County	Margin	2016 margin	Est. votes reported	Total votes	Absentee
Philadelphia	Biden +62	D+67	
96%
685,791	75,220
Allegheny	Biden +19	D+16.5	
94%
675,489	310,796

'''

from collections import OrderedDict

Gains = {}


Gains['Allegheny   '] = get_vote_gain(county_name='Allegheny', margin=19, current_votes=675489, frac_reporting=95)
Gains['Philedelphia'] = get_vote_gain(county_name='Philedelphia', margin=94, current_votes=685791, frac_reporting=94)
#Gains['Bucks       '] = get_vote_gain(county_name='Bucks', margin=3, current_votes=375205, frac_reporting=94 )
#Gains['Delaware    '] = get_vote_gain(county_name='Delaware', margin=25, current_votes=302024, frac_reporting=87)

print('='*80)
print('\t\t\t\tResults\n')
swing = 0
for cty, votes in Gains.items():
    
    print(f'In {cty} county the swing will be:\n\t{int(votes)}\tvotes.')
    swing += votes
print(f'The total swing is {int(swing)} votes.')
print(f'The final vote differential will be {b-t} + {swing} = {b-t+swing} votes.')
print('='*80)

'''
================================================================================
			Pennsylvania Projection
current status:
	Trump: 3307724 votes
	Biden: 3307724 votes
	Difference: 12390 +Biden

================================================================================
				Results

In Allegheny    county the swing will be:
	6754	votes.
In Philedelphia county the swing will be:
	41147	votes.
The total swing is 47902 votes.
The final vote differential will be 12390 + 47902.35 = 60292.35 votes.
================================================================================
'''
