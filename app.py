import streamlit as st
from sklearn . f e a t u r e _ e x t r a c t i o n . text import T f i d f V e c t o r i z e r
from sklearn . svm import LinearSVC
from sklearn . m o d e l _ s e l e c t i o n import t r a i n _ t e s t _ s p l i t
from sklearn . metrics import a c c u r a c y _ s c o r e
st . title ( " Spam Email Detector " )
emails = [ " Win a free iPhone now "
,
" Meeting at 11 am tomorrow "
,
"
C o n g r a t u l a t i o n s you won lottery "
,
" Project di sc us si on with team "
,
" Claim your prize i m m e d i a t e l y "
,
"
Please find the attached report "
,
" Limited offer buy now "
,
" Urgent offer expires today "
,
" Schedule
the meeting for Monday "
,
" You have won a cash prize "
,
" Monthly p e r f o r m a n c e report attached "
,
" Exclusive deal just for you " ]
labels = [1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 1]
ve ct or iz er = T f i d f V e c t o r i z e r ( lowercase = True , s top _w or ds = " english "
,
n g r a m _ r a n g e =(1 , 2) , max_df =0.9 , min_df =1)
X = ve ct or iz er . f i t _ t r a n s f o r m ( emails )
X_train , X_test , y_train , y_test = t r a i n _ t e s t _ s p l i t (X , labels , test_size
=0.25 , r a n d o m _ s t a t e =42 , stratify = labels )
model = LinearSVC ( C =1.0 , r a n d o m _ s t a t e =42)
model . fit ( X_train , y_train )
st . write ( f " Model Accuracy : { a c c u r a c y _ s c o r e ( y_test , model . predict ( X_test ) ) } " )
user_msg = st . text_area ( " Enter Email Message " )
if st . button ( " Check " ) :
msg_vec = ve cto ri ze r . transform ([ user_msg ])
pred = model . predict ( msg_vec ) [0]
st . write ( " Result : ** Spam Email ** " if pred == 1 else " Result : ** Not Spam
Email ** " )
