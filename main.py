#!/usr/bin/env python3


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

def get_vote_gain(county_name:str, margin: float, frac_reporting: int, current_votes: int verbose=False):
    
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
County	        Margin	   | Est. votes reported 	Total votes Absentee
-----------------------------------------------------------------------
Allegheny	    Biden +19  | 95%                    675,489	    310,796

Philadelphia	Biden +61  | 89%                    634,592	    75,220

Bucks	        Biden +3   | 94%                    375,205	    —

Delaware	    Biden +25  | 87%                    302,024	    74,110
'''

from collections import OrderedDict

Gains = {}


Gains['Allegheny   '] = get_vote_gain(county_name='Allegheny', margin=19, current_votes=675489, frac_reporting=95)
Gains['Philedelphia'] = get_vote_gain(county_name='Philedelphia', margin=61, current_votes=634592, frac_reporting=89)
Gains['Bucks       '] = get_vote_gain(county_name='Bucks', margin=3, current_votes=375205, frac_reporting=94 )
Gains['Delaware    '] = get_vote_gain(county_name='Delaware', margin=25, current_votes=302024, frac_reporting=87)

swing = 0
for cty, votes in Gains.items():
    
    print(f'In {cty} county the swing will be: {int(votes)}\t votes.')
    swing += votes
print(f'The total swing is {int(swing)} votes.')


t = 3278696
b = 3237391
print(f'current status: trump: {b}, biden: {b}; difference: {t-b}')
