import streamlit as st
import numpy as np
import m at pl ot li b . pyplot as plt
from sklearn . neighbors import K N e i g h b o r s C l a s s i f i e r
st . s e t _ p a g e _ c o n f i g ( pag e_ ti tl e = " KNN Weather Cla ss if ie r " )
st . title ( " KNN Weather C l a s s i f i c a t i o n " )
X = np . array ([[50 , 70] , [25 , 80] , [27 , 60] , [31 , 65] , [23 , 85] , [20 , 75]])
y = np . array ([0 , 1 , 0 , 0 , 1 , 1])
label_map = {0: " Sunny " , 1: " Rainy " }
st . sidebar . header ( " Input Features " )
temp = st . sidebar . slider ( " T e m p e r a t u r e " , 10 , 60 , 26)
hum = st . sidebar . slider ( " Humidity " , 50 , 95 , 78)
knn = K N e i g h b o r s C l a s s i f i e r ( n _ n e i g h b o r s =3)
knn . fit (X , y )
new_data = np . array ([[ temp , hum ]])
pr ed ic ti on = knn . predict ( new_data ) [0]
st . write ( f " Predicted Weather : **{ label_map [ pr edi ct io n ]}** " )
fig , ax = plt . subplots ()
ax . scatter ( X [ y ==0 , 0] , X [ y ==0 , 1] , color = ’ orange ’ , label = ’ Sunny ’ , s =100 ,
edgecolor = ’k ’)
ax . scatter ( X [ y ==1 , 0] , X [ y ==1 , 1] , color = ’ blue ’ , label = ’ Rainy ’ , s =100 ,
edgecolor = ’k ’)
ax . scatter ( temp , hum , color = ’ red ’ if pre di ct io n ==1 else ’ orange ’ , marker = ’* ’
,
s =300 , edgecolor = ’ black ’ , label = f ’ New Day : { label_map [ pr ed ic ti on ]} ’)
ax . set _x la be l ( ’ T e m p e r a t u r e ’)
ax . set _y la be l ( ’ Humidity ’)
ax . set_title ( ’ KNN Weather C l a s s i f i c a t i o n ’)
ax . legend ()
ax . grid ( True )
st . pyplot ( fig )
