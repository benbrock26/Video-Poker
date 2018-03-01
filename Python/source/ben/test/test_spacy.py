# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:10:01 2018

@author: Ben Brock
"""

# I created some tests according to your PDF file
c1= ['10s','Js','Qs','Ks','As']   # --> Royal Flush!
c2=['4d','5d','6d','7d','8d']     # --> Straight Flush!
c3=['Qs','Qd','Qc','Qh','10s']    # --> Four of a kind!
c4=['Ks','Kd','3h','3s','3c']     # --> Full house!
c5=['Ad','Qd','6d','Jd','2d']     # --> Flush
c6=['Ks','Qd','Jc','10h','9s']
c7=['5d','Js','8h','8s','8d']
c8=['10s','Qd','7s','Qc','7h']
c9=['10s','Jd','7s','6h','6s']
c10=['7c','6d','4s','3h','2c']
c11=['2h', '2d', '2c', 'Kc', 'Qd']      # three of a kind  beginning
c12=['2h', '5h', '7d', '8c', '9s']      # high card
c13=['Ah', '2d', '3c', '4c', '5d']      # straight
c14=['2h', '3h', '2d', '3c', '2d']      # full house
c15=['2h', '7h', '2d', '3c', '3d']      # two pair
c16 =['2h','7h', '7d', '7c', '7s']      # four of a kind
c17=['9h', '10h', 'Jh', 'Qh', 'Kh']     # straigh flush 
c18=['4h', '4s', 'Ks', '5d', '10s']     # one pair
c19=['Qc', '10c', '7c', '6c', '4c']     # flush          end
c20 = ['As', 'Ac', 'Ah', 'Ad', '2c']     # four of a kind 
c21 = ['Jc', '10c', '9c', '8c', '7c']    # straight flush
c22 = ['5c', '5d', '5h', '5s', '2d']     # four of a kind
c23 = ['6s', '6h', '6d', 'Kc', 'Kh']     # full house
c24 = ['Jd', '9d','8d', '4d', '3d']      # flush
c25 = ['10d', '9s', '8h', '7d', '6c' ]   # straight
c26 = ['Qc', 'Qs', 'Qh', '9h', '2s']     # three of a kind 
c27 = ['Jh', 'Jc', '3c', '3s', '2h']    # two pair
c28 = ['10c', '10h', '8s', '7h', '4c']   # one pair
c29 = ['Kd', 'Qd', '7s', '4s', '2h']     # high card


def setCards(l):
    values=[]
    suits=[]
    for x in l:
        print x
        suits.append(x[-1])
        if x[0]=='J':
            values.append(11)
        elif x[0]=='Q':
            values.append(12)
        elif x[0]=='K':
            values.append(13)
        elif x[0]=='A':
            values.append(14)
        else:
            values.append(int(x[:len(x)-1]))#in case of two digits line '10'
            
    return sorted(values),suits  #values need to be sorted
    
    
def main():
    pass
    tests=[c1, c2, c3]

    for x in tests:
        print x
        value,suit = setCards(x)
        print value,'-->', suit

if __name__ == '__main__':
    main()