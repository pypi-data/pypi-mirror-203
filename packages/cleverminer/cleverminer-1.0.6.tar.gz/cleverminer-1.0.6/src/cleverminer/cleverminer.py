import sys #line:31
import time #line:32
import copy #line:33
from time import strftime #line:35
from time import gmtime #line:36
import pandas as pd #line:38
import numpy #line:39
from pandas .api .types import CategoricalDtype #line:40
import progressbar #line:42
class cleverminer :#line:44
    version_string ="1.0.6"#line:46
    def __init__ (O0OOOOO0O0O0000OO ,**O0OO00OO0O00OOO00 ):#line:48
        O0OOOOO0O0O0000OO ._print_disclaimer ()#line:49
        O0OOOOO0O0O0000OO .stats ={'total_cnt':0 ,'total_ver':0 ,'total_valid':0 ,'control_number':0 ,'start_prep_time':time .time (),'end_prep_time':time .time (),'start_proc_time':time .time (),'end_proc_time':time .time ()}#line:58
        O0OOOOO0O0O0000OO .options ={'max_categories':100 ,'max_rules':None ,'optimizations':True ,'automatic_data_conversions':True ,'progressbar':True }#line:65
        O0OOOOO0O0O0000OO .kwargs =None #line:66
        if len (O0OO00OO0O00OOO00 )>0 :#line:67
            O0OOOOO0O0O0000OO .kwargs =O0OO00OO0O00OOO00 #line:68
        O0OOOOO0O0O0000OO .verbosity ={}#line:69
        O0OOOOO0O0O0000OO .verbosity ['debug']=False #line:70
        O0OOOOO0O0O0000OO .verbosity ['print_rules']=False #line:71
        O0OOOOO0O0O0000OO .verbosity ['print_hashes']=True #line:72
        O0OOOOO0O0O0000OO .verbosity ['last_hash_time']=0 #line:73
        O0OOOOO0O0O0000OO .verbosity ['hint']=False #line:74
        if "opts"in O0OO00OO0O00OOO00 :#line:75
            O0OOOOO0O0O0000OO ._set_opts (O0OO00OO0O00OOO00 .get ("opts"))#line:76
        if "opts"in O0OO00OO0O00OOO00 :#line:77
            if "verbose"in O0OO00OO0O00OOO00 .get ('opts'):#line:78
                O0O00OO0OO0OO0O00 =O0OO00OO0O00OOO00 .get ('opts').get ('verbose')#line:79
                if O0O00OO0OO0OO0O00 .upper ()=='FULL':#line:80
                    O0OOOOO0O0O0000OO .verbosity ['debug']=True #line:81
                    O0OOOOO0O0O0000OO .verbosity ['print_rules']=True #line:82
                    O0OOOOO0O0O0000OO .verbosity ['print_hashes']=False #line:83
                    O0OOOOO0O0O0000OO .verbosity ['hint']=True #line:84
                    O0OOOOO0O0O0000OO .options ['progressbar']=False #line:85
                elif O0O00OO0OO0OO0O00 .upper ()=='RULES':#line:86
                    O0OOOOO0O0O0000OO .verbosity ['debug']=False #line:87
                    O0OOOOO0O0O0000OO .verbosity ['print_rules']=True #line:88
                    O0OOOOO0O0O0000OO .verbosity ['print_hashes']=True #line:89
                    O0OOOOO0O0O0000OO .verbosity ['hint']=True #line:90
                    O0OOOOO0O0O0000OO .options ['progressbar']=False #line:91
                elif O0O00OO0OO0OO0O00 .upper ()=='HINT':#line:92
                    O0OOOOO0O0O0000OO .verbosity ['debug']=False #line:93
                    O0OOOOO0O0O0000OO .verbosity ['print_rules']=False #line:94
                    O0OOOOO0O0O0000OO .verbosity ['print_hashes']=True #line:95
                    O0OOOOO0O0O0000OO .verbosity ['last_hash_time']=0 #line:96
                    O0OOOOO0O0O0000OO .verbosity ['hint']=True #line:97
                    O0OOOOO0O0O0000OO .options ['progressbar']=False #line:98
                elif O0O00OO0OO0OO0O00 .upper ()=='DEBUG':#line:99
                    O0OOOOO0O0O0000OO .verbosity ['debug']=True #line:100
                    O0OOOOO0O0O0000OO .verbosity ['print_rules']=True #line:101
                    O0OOOOO0O0O0000OO .verbosity ['print_hashes']=True #line:102
                    O0OOOOO0O0O0000OO .verbosity ['last_hash_time']=0 #line:103
                    O0OOOOO0O0O0000OO .verbosity ['hint']=True #line:104
                    O0OOOOO0O0O0000OO .options ['progressbar']=False #line:105
        O0OOOOO0O0O0000OO ._is_py310 =sys .version_info [0 ]>=4 or (sys .version_info [0 ]>=3 and sys .version_info [1 ]>=10 )#line:106
        if not (O0OOOOO0O0O0000OO ._is_py310 ):#line:107
            print ("Warning: Python 3.10+ NOT detected. You should upgrade to Python 3.10 or greater to get better performance")#line:108
        else :#line:109
            if (O0OOOOO0O0O0000OO .verbosity ['debug']):#line:110
                print ("Python 3.10+ detected.")#line:111
        O0OOOOO0O0O0000OO ._initialized =False #line:112
        O0OOOOO0O0O0000OO ._init_data ()#line:113
        O0OOOOO0O0O0000OO ._init_task ()#line:114
        if len (O0OO00OO0O00OOO00 )>0 :#line:115
            if "df"in O0OO00OO0O00OOO00 :#line:116
                O0OOOOO0O0O0000OO ._prep_data (O0OO00OO0O00OOO00 .get ("df"))#line:117
            else :#line:118
                print ("Missing dataframe. Cannot initialize.")#line:119
                O0OOOOO0O0O0000OO ._initialized =False #line:120
                return #line:121
            O00O0O00O00O000OO =O0OO00OO0O00OOO00 .get ("proc",None )#line:122
            if not (O00O0O00O00O000OO ==None ):#line:123
                O0OOOOO0O0O0000OO ._calculate (**O0OO00OO0O00OOO00 )#line:124
            else :#line:126
                if O0OOOOO0O0O0000OO .verbosity ['debug']:#line:127
                    print ("INFO: just initialized")#line:128
        O0OOOOO0O0O0000OO ._initialized =True #line:129
    def _set_opts (O0OOO0OO000000OO0 ,O00O0OOO000OO0O00 ):#line:131
        if "no_optimizations"in O00O0OOO000OO0O00 :#line:132
            O0OOO0OO000000OO0 .options ['optimizations']=not (O00O0OOO000OO0O00 ['no_optimizations'])#line:133
            print ("No optimization will be made.")#line:134
        if "disable_progressbar"in O00O0OOO000OO0O00 :#line:135
            O0OOO0OO000000OO0 .options ['progressbar']=False #line:136
            print ("Progressbar will not be shown.")#line:137
        if "max_rules"in O00O0OOO000OO0O00 :#line:138
            O0OOO0OO000000OO0 .options ['max_rules']=O00O0OOO000OO0O00 ['max_rules']#line:139
        if "max_categories"in O00O0OOO000OO0O00 :#line:140
            O0OOO0OO000000OO0 .options ['max_categories']=O00O0OOO000OO0O00 ['max_categories']#line:141
            if O0OOO0OO000000OO0 .verbosity ['debug']==True :#line:142
                print (f"Maximum number of categories set to {O0OOO0OO000000OO0.options['max_categories']}")#line:143
        if "no_automatic_data_conversions"in O00O0OOO000OO0O00 :#line:144
            O0OOO0OO000000OO0 .options ['automatic_data_conversions']=not (O00O0OOO000OO0O00 ['no_automatic_data_conversions'])#line:145
            print ("No automatic data conversions will be made.")#line:146
    def _init_data (OOOO0000000OO0OO0 ):#line:149
        OOOO0000000OO0OO0 .data ={}#line:151
        OOOO0000000OO0OO0 .data ["varname"]=[]#line:152
        OOOO0000000OO0OO0 .data ["catnames"]=[]#line:153
        OOOO0000000OO0OO0 .data ["vtypes"]=[]#line:154
        OOOO0000000OO0OO0 .data ["dm"]=[]#line:155
        OOOO0000000OO0OO0 .data ["rows_count"]=int (0 )#line:156
        OOOO0000000OO0OO0 .data ["data_prepared"]=0 #line:157
    def _init_task (O00OO00OOOO000OOO ):#line:159
        if "opts"in O00OO00OOOO000OOO .kwargs :#line:161
            O00OO00OOOO000OOO ._set_opts (O00OO00OOOO000OOO .kwargs .get ("opts"))#line:162
        O00OO00OOOO000OOO .cedent ={'cedent_type':'none','defi':{},'num_cedent':0 ,'trace_cedent':[],'trace_cedent_asindata':[],'traces':[],'generated_string':'','rule':{},'filter_value':int (0 )}#line:172
        O00OO00OOOO000OOO .task_actinfo ={'proc':'','cedents_to_do':[],'cedents':[]}#line:176
        O00OO00OOOO000OOO .rulelist =[]#line:177
        O00OO00OOOO000OOO .stats ['total_cnt']=0 #line:179
        O00OO00OOOO000OOO .stats ['total_valid']=0 #line:180
        O00OO00OOOO000OOO .stats ['control_number']=0 #line:181
        O00OO00OOOO000OOO .result ={}#line:182
        O00OO00OOOO000OOO ._opt_base =None #line:183
        O00OO00OOOO000OOO ._opt_relbase =None #line:184
        O00OO00OOOO000OOO ._opt_base1 =None #line:185
        O00OO00OOOO000OOO ._opt_relbase1 =None #line:186
        O00OO00OOOO000OOO ._opt_base2 =None #line:187
        O00OO00OOOO000OOO ._opt_relbase2 =None #line:188
        O0OOOO0OOO00O00OO =None #line:189
        if not (O00OO00OOOO000OOO .kwargs ==None ):#line:190
            O0OOOO0OOO00O00OO =O00OO00OOOO000OOO .kwargs .get ("quantifiers",None )#line:191
            if not (O0OOOO0OOO00O00OO ==None ):#line:192
                for OO0OO0OO0OOO0OOO0 in O0OOOO0OOO00O00OO .keys ():#line:193
                    if OO0OO0OO0OOO0OOO0 .upper ()=='BASE':#line:194
                        O00OO00OOOO000OOO ._opt_base =O0OOOO0OOO00O00OO .get (OO0OO0OO0OOO0OOO0 )#line:195
                    if OO0OO0OO0OOO0OOO0 .upper ()=='RELBASE':#line:196
                        O00OO00OOOO000OOO ._opt_relbase =O0OOOO0OOO00O00OO .get (OO0OO0OO0OOO0OOO0 )#line:197
                    if (OO0OO0OO0OOO0OOO0 .upper ()=='FRSTBASE')|(OO0OO0OO0OOO0OOO0 .upper ()=='BASE1'):#line:198
                        O00OO00OOOO000OOO ._opt_base1 =O0OOOO0OOO00O00OO .get (OO0OO0OO0OOO0OOO0 )#line:199
                    if (OO0OO0OO0OOO0OOO0 .upper ()=='SCNDBASE')|(OO0OO0OO0OOO0OOO0 .upper ()=='BASE2'):#line:200
                        O00OO00OOOO000OOO ._opt_base2 =O0OOOO0OOO00O00OO .get (OO0OO0OO0OOO0OOO0 )#line:201
                    if (OO0OO0OO0OOO0OOO0 .upper ()=='FRSTRELBASE')|(OO0OO0OO0OOO0OOO0 .upper ()=='RELBASE1'):#line:202
                        O00OO00OOOO000OOO ._opt_relbase1 =O0OOOO0OOO00O00OO .get (OO0OO0OO0OOO0OOO0 )#line:203
                    if (OO0OO0OO0OOO0OOO0 .upper ()=='SCNDRELBASE')|(OO0OO0OO0OOO0OOO0 .upper ()=='RELBASE2'):#line:204
                        O00OO00OOOO000OOO ._opt_relbase2 =O0OOOO0OOO00O00OO .get (OO0OO0OO0OOO0OOO0 )#line:205
            else :#line:206
                print ("Warning: no quantifiers found. Optimization will not take place (1)")#line:207
        else :#line:208
            print ("Warning: no quantifiers found. Optimization will not take place (2)")#line:209
    def mine (O0000O0O00OOOO00O ,**O00O00O0OOO0000O0 ):#line:212
        if not (O0000O0O00OOOO00O ._initialized ):#line:213
            print ("Class NOT INITIALIZED. Please call constructor with dataframe first")#line:214
            return #line:215
        O0000O0O00OOOO00O .kwargs =None #line:216
        if len (O00O00O0OOO0000O0 )>0 :#line:217
            O0000O0O00OOOO00O .kwargs =O00O00O0OOO0000O0 #line:218
        O0000O0O00OOOO00O ._init_task ()#line:219
        if len (O00O00O0OOO0000O0 )>0 :#line:220
            O00OOO000O0OOO000 =O00O00O0OOO0000O0 .get ("proc",None )#line:221
            if not (O00OOO000O0OOO000 ==None ):#line:222
                O0000O0O00OOOO00O ._calc_all (**O00O00O0OOO0000O0 )#line:223
            else :#line:224
                print ("Rule mining procedure missing")#line:225
    def _get_ver (OO000000OOOO000O0 ):#line:228
        return OO000000OOOO000O0 .version_string #line:229
    def _print_disclaimer (O0OO0O0000O000OO0 ):#line:231
        print (f"Cleverminer version {O0OO0O0000O000OO0._get_ver()}.")#line:233
    def _automatic_data_conversions (OOOOO0000OOOO00OO ,O0O00O0OO00O0000O ):#line:239
        print ("Automatically reordering numeric categories ...")#line:240
        for O0O0O0O0O0OOOOO00 in range (len (O0O00O0OO00O0000O .columns )):#line:241
            if OOOOO0000OOOO00OO .verbosity ['debug']:#line:242
                print (f"#{O0O0O0O0O0OOOOO00}: {O0O00O0OO00O0000O.columns[O0O0O0O0O0OOOOO00]} : {O0O00O0OO00O0000O.dtypes[O0O0O0O0O0OOOOO00]}.")#line:243
            try :#line:244
                O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]]=O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]].astype (str ).astype (float )#line:245
                if OOOOO0000OOOO00OO .verbosity ['debug']:#line:246
                    print (f"CONVERTED TO FLOATS #{O0O0O0O0O0OOOOO00}: {O0O00O0OO00O0000O.columns[O0O0O0O0O0OOOOO00]} : {O0O00O0OO00O0000O.dtypes[O0O0O0O0O0OOOOO00]}.")#line:247
                O0OOO00O0OOO0O000 =pd .unique (O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]])#line:248
                OOOO00OOOO00OOOOO =True #line:249
                for O0O0OO0O0O0OO00O0 in O0OOO00O0OOO0O000 :#line:250
                    if O0O0OO0O0O0OO00O0 %1 !=0 :#line:251
                        OOOO00OOOO00OOOOO =False #line:252
                if OOOO00OOOO00OOOOO :#line:253
                    O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]]=O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]].astype (int )#line:254
                    if OOOOO0000OOOO00OO .verbosity ['debug']:#line:255
                        print (f"CONVERTED TO INT #{O0O0O0O0O0OOOOO00}: {O0O00O0OO00O0000O.columns[O0O0O0O0O0OOOOO00]} : {O0O00O0OO00O0000O.dtypes[O0O0O0O0O0OOOOO00]}.")#line:256
                OO00OO00000OO00O0 =pd .unique (O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]])#line:257
                OO00OO0O0OOO0O0OO =CategoricalDtype (categories =OO00OO00000OO00O0 .sort (),ordered =True )#line:258
                O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]]=O0O00O0OO00O0000O [O0O00O0OO00O0000O .columns [O0O0O0O0O0OOOOO00 ]].astype (OO00OO0O0OOO0O0OO )#line:259
                if OOOOO0000OOOO00OO .verbosity ['debug']:#line:260
                    print (f"CONVERTED TO CATEGORY #{O0O0O0O0O0OOOOO00}: {O0O00O0OO00O0000O.columns[O0O0O0O0O0OOOOO00]} : {O0O00O0OO00O0000O.dtypes[O0O0O0O0O0OOOOO00]}.")#line:261
            except :#line:263
                if OOOOO0000OOOO00OO .verbosity ['debug']:#line:264
                    print ("...cannot be converted to int")#line:265
        print ("Automatically reordering numeric categories ...done")#line:266
    def _prep_data (OOO00OO000O00OO00 ,OOO00O000OO0000O0 ):#line:268
        print ("Starting data preparation ...")#line:269
        OOO00OO000O00OO00 ._init_data ()#line:270
        OOO00OO000O00OO00 .stats ['start_prep_time']=time .time ()#line:271
        if OOO00OO000O00OO00 .options ['automatic_data_conversions']:#line:272
            OOO00OO000O00OO00 ._automatic_data_conversions (OOO00O000OO0000O0 )#line:273
        OOO00OO000O00OO00 .data ["rows_count"]=OOO00O000OO0000O0 .shape [0 ]#line:274
        for OO0OO000O0OO0OO0O in OOO00O000OO0000O0 .select_dtypes (exclude =['category']).columns :#line:275
            OOO00O000OO0000O0 [OO0OO000O0OO0OO0O ]=OOO00O000OO0000O0 [OO0OO000O0OO0OO0O ].apply (str )#line:276
        try :#line:277
            OO000O0OOOOO0OOOO =pd .DataFrame .from_records ([(OO0OOO00O0OO00OO0 ,OOO00O000OO0000O0 [OO0OOO00O0OO00OO0 ].nunique ())for OO0OOO00O0OO00OO0 in OOO00O000OO0000O0 .columns ],columns =['Column_Name','Num_Unique']).sort_values (by =['Num_Unique'])#line:279
        except :#line:280
            print ("Error in input data, probably unsupported data type. Will try to scan for column with unsupported type.")#line:281
            O0OO0O00000O0O0O0 =""#line:282
            try :#line:283
                for OO0OO000O0OO0OO0O in OOO00O000OO0000O0 .columns :#line:284
                    O0OO0O00000O0O0O0 =OO0OO000O0OO0OO0O #line:285
                    print (f"...column {OO0OO000O0OO0OO0O} has {int(OOO00O000OO0000O0[OO0OO000O0OO0OO0O].nunique())} values")#line:286
            except :#line:287
                print (f"... detected : column {O0OO0O00000O0O0O0} has unsupported type: {type(OOO00O000OO0000O0[OO0OO000O0OO0OO0O])}.")#line:288
                exit (1 )#line:289
            print (f"Error in data profiling - attribute with unsupported type not detected. Please profile attributes manually, only simple attributes are supported.")#line:290
            exit (1 )#line:291
        if OOO00OO000O00OO00 .verbosity ['hint']:#line:294
            print ("Quick profile of input data: unique value counts are:")#line:295
            print (OO000O0OOOOO0OOOO )#line:296
            for OO0OO000O0OO0OO0O in OOO00O000OO0000O0 .columns :#line:297
                if OOO00O000OO0000O0 [OO0OO000O0OO0OO0O ].nunique ()<OOO00OO000O00OO00 .options ['max_categories']:#line:298
                    OOO00O000OO0000O0 [OO0OO000O0OO0OO0O ]=OOO00O000OO0000O0 [OO0OO000O0OO0OO0O ].astype ('category')#line:299
                else :#line:300
                    print (f"WARNING: attribute {OO0OO000O0OO0OO0O} has more than {OOO00OO000O00OO00.options['max_categories']} values, will be ignored.\r\n If you haven't set maximum number of categories and you really need more categories and you know what you are doing, please use max_categories option to increase allowed number of categories.")#line:301
                    del OOO00O000OO0000O0 [OO0OO000O0OO0OO0O ]#line:302
        print ("Encoding columns into bit-form...")#line:303
        O0O0OO0OOOO000O0O =0 #line:304
        OO00000OOO0O0OO0O =0 #line:305
        for OOOOO00O00OO0OO00 in OOO00O000OO0000O0 :#line:306
            if OOO00OO000O00OO00 .verbosity ['debug']:#line:308
                print ('Column: '+OOOOO00O00OO0OO00 )#line:309
            OOO00OO000O00OO00 .data ["varname"].append (OOOOO00O00OO0OO00 )#line:310
            OO0O000OOOOOOO0O0 =pd .get_dummies (OOO00O000OO0000O0 [OOOOO00O00OO0OO00 ])#line:311
            OOO00OOOO0O00OO0O =0 #line:312
            if (OOO00O000OO0000O0 .dtypes [OOOOO00O00OO0OO00 ].name =='category'):#line:313
                OOO00OOOO0O00OO0O =1 #line:314
            OOO00OO000O00OO00 .data ["vtypes"].append (OOO00OOOO0O00OO0O )#line:315
            OOO00O00OO00O00O0 =0 #line:318
            OO0OO0O0O0O000O0O =[]#line:319
            O00OOO0000OO00000 =[]#line:320
            for OO000O0OO000O0O00 in OO0O000OOOOOOO0O0 :#line:322
                if OOO00OO000O00OO00 .verbosity ['debug']:#line:324
                    print ('....category : '+str (OO000O0OO000O0O00 )+" @ "+str (time .time ()))#line:325
                OO0OO0O0O0O000O0O .append (OO000O0OO000O0O00 )#line:326
                O000O00O0O000OO0O =int (0 )#line:327
                OO0000OO0OOO0OOO0 =OO0O000OOOOOOO0O0 [OO000O0OO000O0O00 ].values #line:328
                O0O00O0O0000O0000 =numpy .packbits (OO0000OO0OOO0OOO0 ,bitorder ='little')#line:330
                O000O00O0O000OO0O =int .from_bytes (O0O00O0O0000O0000 ,byteorder ='little')#line:331
                O00OOO0000OO00000 .append (O000O00O0O000OO0O )#line:332
                OOO00O00OO00O00O0 +=1 #line:350
                OO00000OOO0O0OO0O +=1 #line:351
            OOO00OO000O00OO00 .data ["catnames"].append (OO0OO0O0O0O000O0O )#line:353
            OOO00OO000O00OO00 .data ["dm"].append (O00OOO0000OO00000 )#line:354
        print ("Encoding columns into bit-form...done")#line:356
        if OOO00OO000O00OO00 .verbosity ['hint']:#line:357
            print (f"List of attributes for analysis is: {OOO00OO000O00OO00.data['varname']}")#line:358
            print (f"List of category names for individual attributes is : {OOO00OO000O00OO00.data['catnames']}")#line:359
        if OOO00OO000O00OO00 .verbosity ['debug']:#line:360
            print (f"List of vtypes is (all should be 1) : {OOO00OO000O00OO00.data['vtypes']}")#line:361
        OOO00OO000O00OO00 .data ["data_prepared"]=1 #line:363
        print ("Data preparation finished.")#line:364
        if OOO00OO000O00OO00 .verbosity ['debug']:#line:365
            print ('Number of variables : '+str (len (OOO00OO000O00OO00 .data ["dm"])))#line:366
            print ('Total number of categories in all variables : '+str (OO00000OOO0O0OO0O ))#line:367
        OOO00OO000O00OO00 .stats ['end_prep_time']=time .time ()#line:368
        if OOO00OO000O00OO00 .verbosity ['debug']:#line:369
            print ('Time needed for data preparation : ',str (OOO00OO000O00OO00 .stats ['end_prep_time']-OOO00OO000O00OO00 .stats ['start_prep_time']))#line:370
    def _bitcount (O0000O0O000OO0000 ,O00OO00O0OO000OO0 ):#line:372
        O000O00O0O0O0O00O =None #line:373
        if (O0000O0O000OO0000 ._is_py310 ):#line:374
            O000O00O0O0O0O00O =O00OO00O0OO000OO0 .bit_count ()#line:375
        else :#line:376
            O000O00O0O0O0O00O =bin (O00OO00O0OO000OO0 ).count ("1")#line:377
        return O000O00O0O0O0O00O #line:378
    def _verifyCF (OO0O0OO00OOOOOOOO ,_OO0O0O0O0OO0O0000 ):#line:381
        O00O0000OO0OO0OO0 =OO0O0OO00OOOOOOOO ._bitcount (_OO0O0O0O0OO0O0000 )#line:382
        O0000O00OOOO0OO0O =[]#line:383
        O00OO0O0OO0OOOO00 =[]#line:384
        O0OO000OOOOO0OOO0 =0 #line:385
        OOO0OO0OOOOO0O0O0 =0 #line:386
        OO0OOOOOO0000OOOO =0 #line:387
        OOOO000O0000000O0 =0 #line:388
        O00OOO00OOOOOO0O0 =0 #line:389
        OO00O00000O00OOO0 =0 #line:390
        O00OOO000O0O0O000 =0 #line:391
        OOO0OO0OO000000O0 =0 #line:392
        O0OO00O00000OOOO0 =0 #line:393
        OOO000000000OOO0O =0 #line:394
        OO0OOO0O0O00O0000 =0 #line:395
        OOOOO00OOO0OO0O00 =[]#line:396
        if ('aad_weights'in OO0O0OO00OOOOOOOO .quantifiers ):#line:397
            OOO000000000OOO0O =1 #line:398
            OO0O0O00OOO00OOO0 =[]#line:399
            OOOOO00OOO0OO0O00 =OO0O0OO00OOOOOOOO .quantifiers .get ('aad_weights')#line:400
        OO00OOOO0000000OO =OO0O0OO00OOOOOOOO .data ["dm"][OO0O0OO00OOOOOOOO .data ["varname"].index (OO0O0OO00OOOOOOOO .kwargs .get ('target'))]#line:401
        for O00OO0O0000000000 in range (len (OO00OOOO0000000OO )):#line:402
            OOO0OO0OOOOO0O0O0 =O0OO000OOOOO0OOO0 #line:404
            O0OO000OOOOO0OOO0 =OO0O0OO00OOOOOOOO ._bitcount (_OO0O0O0O0OO0O0000 &OO00OOOO0000000OO [O00OO0O0000000000 ])#line:405
            O0000O00OOOO0OO0O .append (O0OO000OOOOO0OOO0 )#line:406
            if O00OO0O0000000000 >0 :#line:407
                if (O0OO000OOOOO0OOO0 >OOO0OO0OOOOO0O0O0 ):#line:408
                    if (OO0OOOOOO0000OOOO ==1 ):#line:409
                        OOO0OO0OO000000O0 +=1 #line:410
                    else :#line:411
                        OOO0OO0OO000000O0 =1 #line:412
                    if OOO0OO0OO000000O0 >OOOO000O0000000O0 :#line:413
                        OOOO000O0000000O0 =OOO0OO0OO000000O0 #line:414
                    OO0OOOOOO0000OOOO =1 #line:415
                    OO00O00000O00OOO0 +=1 #line:416
                if (O0OO000OOOOO0OOO0 <OOO0OO0OOOOO0O0O0 ):#line:417
                    if (OO0OOOOOO0000OOOO ==-1 ):#line:418
                        O0OO00O00000OOOO0 +=1 #line:419
                    else :#line:420
                        O0OO00O00000OOOO0 =1 #line:421
                    if O0OO00O00000OOOO0 >O00OOO00OOOOOO0O0 :#line:422
                        O00OOO00OOOOOO0O0 =O0OO00O00000OOOO0 #line:423
                    OO0OOOOOO0000OOOO =-1 #line:424
                    O00OOO000O0O0O000 +=1 #line:425
                if (O0OO000OOOOO0OOO0 ==OOO0OO0OOOOO0O0O0 ):#line:426
                    OO0OOOOOO0000OOOO =0 #line:427
                    O0OO00O00000OOOO0 =0 #line:428
                    OOO0OO0OO000000O0 =0 #line:429
            if (OOO000000000OOO0O ):#line:431
                OO00O0OO0OOOO0OOO =OO0O0OO00OOOOOOOO ._bitcount (OO00OOOO0000000OO [O00OO0O0000000000 ])#line:432
                OO0O0O00OOO00OOO0 .append (OO00O0OO0OOOO0OOO )#line:433
        if (OOO000000000OOO0O &sum (O0000O00OOOO0OO0O )>0 ):#line:435
            for O00OO0O0000000000 in range (len (OO00OOOO0000000OO )):#line:436
                if OO0O0O00OOO00OOO0 [O00OO0O0000000000 ]>0 :#line:437
                    if O0000O00OOOO0OO0O [O00OO0O0000000000 ]/sum (O0000O00OOOO0OO0O )>OO0O0O00OOO00OOO0 [O00OO0O0000000000 ]/sum (OO0O0O00OOO00OOO0 ):#line:439
                        OO0OOO0O0O00O0000 +=OOOOO00OOO0OO0O00 [O00OO0O0000000000 ]*((O0000O00OOOO0OO0O [O00OO0O0000000000 ]/sum (O0000O00OOOO0OO0O ))/(OO0O0O00OOO00OOO0 [O00OO0O0000000000 ]/sum (OO0O0O00OOO00OOO0 ))-1 )#line:440
        O000000O0O0O0O00O =True #line:443
        for O00O00O0OO0O0OO00 in OO0O0OO00OOOOOOOO .quantifiers .keys ():#line:444
            if O00O00O0OO0O0OO00 .upper ()=='BASE':#line:445
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=O00O0000OO0OO0OO0 )#line:446
            if O00O00O0OO0O0OO00 .upper ()=='RELBASE':#line:447
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=O00O0000OO0OO0OO0 *1.0 /OO0O0OO00OOOOOOOO .data ["rows_count"])#line:448
            if O00O00O0OO0O0OO00 .upper ()=='S_UP':#line:449
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=OOOO000O0000000O0 )#line:450
            if O00O00O0OO0O0OO00 .upper ()=='S_DOWN':#line:451
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=O00OOO00OOOOOO0O0 )#line:452
            if O00O00O0OO0O0OO00 .upper ()=='S_ANY_UP':#line:453
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=OOOO000O0000000O0 )#line:454
            if O00O00O0OO0O0OO00 .upper ()=='S_ANY_DOWN':#line:455
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=O00OOO00OOOOOO0O0 )#line:456
            if O00O00O0OO0O0OO00 .upper ()=='MAX':#line:457
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=max (O0000O00OOOO0OO0O ))#line:458
            if O00O00O0OO0O0OO00 .upper ()=='MIN':#line:459
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=min (O0000O00OOOO0OO0O ))#line:460
            if O00O00O0OO0O0OO00 .upper ()=='RELMAX':#line:461
                if sum (O0000O00OOOO0OO0O )>0 :#line:462
                    O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=max (O0000O00OOOO0OO0O )*1.0 /sum (O0000O00OOOO0OO0O ))#line:463
                else :#line:464
                    O000000O0O0O0O00O =False #line:465
            if O00O00O0OO0O0OO00 .upper ()=='RELMAX_LEQ':#line:466
                if sum (O0000O00OOOO0OO0O )>0 :#line:467
                    O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )>=max (O0000O00OOOO0OO0O )*1.0 /sum (O0000O00OOOO0OO0O ))#line:468
                else :#line:469
                    O000000O0O0O0O00O =False #line:470
            if O00O00O0OO0O0OO00 .upper ()=='RELMIN':#line:471
                if sum (O0000O00OOOO0OO0O )>0 :#line:472
                    O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=min (O0000O00OOOO0OO0O )*1.0 /sum (O0000O00OOOO0OO0O ))#line:473
                else :#line:474
                    O000000O0O0O0O00O =False #line:475
            if O00O00O0OO0O0OO00 .upper ()=='RELMIN_LEQ':#line:476
                if sum (O0000O00OOOO0OO0O )>0 :#line:477
                    O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )>=min (O0000O00OOOO0OO0O )*1.0 /sum (O0000O00OOOO0OO0O ))#line:478
                else :#line:479
                    O000000O0O0O0O00O =False #line:480
            if O00O00O0OO0O0OO00 .upper ()=='AAD':#line:481
                O000000O0O0O0O00O =O000000O0O0O0O00O and (OO0O0OO00OOOOOOOO .quantifiers .get (O00O00O0OO0O0OO00 )<=OO0OOO0O0O00O0000 )#line:482
        O00OOO0OO0OOOO000 ={}#line:484
        if O000000O0O0O0O00O ==True :#line:485
            OO0O0OO00OOOOOOOO .stats ['total_valid']+=1 #line:487
            O00OOO0OO0OOOO000 ["base"]=O00O0000OO0OO0OO0 #line:488
            O00OOO0OO0OOOO000 ["rel_base"]=O00O0000OO0OO0OO0 *1.0 /OO0O0OO00OOOOOOOO .data ["rows_count"]#line:489
            O00OOO0OO0OOOO000 ["s_up"]=OOOO000O0000000O0 #line:490
            O00OOO0OO0OOOO000 ["s_down"]=O00OOO00OOOOOO0O0 #line:491
            O00OOO0OO0OOOO000 ["s_any_up"]=OO00O00000O00OOO0 #line:492
            O00OOO0OO0OOOO000 ["s_any_down"]=O00OOO000O0O0O000 #line:493
            O00OOO0OO0OOOO000 ["max"]=max (O0000O00OOOO0OO0O )#line:494
            O00OOO0OO0OOOO000 ["min"]=min (O0000O00OOOO0OO0O )#line:495
            if sum (O0000O00OOOO0OO0O )>0 :#line:498
                O00OOO0OO0OOOO000 ["rel_max"]=max (O0000O00OOOO0OO0O )*1.0 /sum (O0000O00OOOO0OO0O )#line:499
                O00OOO0OO0OOOO000 ["rel_min"]=min (O0000O00OOOO0OO0O )*1.0 /sum (O0000O00OOOO0OO0O )#line:500
            else :#line:501
                O00OOO0OO0OOOO000 ["rel_max"]=0 #line:502
                O00OOO0OO0OOOO000 ["rel_min"]=0 #line:503
            O00OOO0OO0OOOO000 ["hist"]=O0000O00OOOO0OO0O #line:504
            if OOO000000000OOO0O :#line:505
                O00OOO0OO0OOOO000 ["aad"]=OO0OOO0O0O00O0000 #line:506
                O00OOO0OO0OOOO000 ["hist_full"]=OO0O0O00OOO00OOO0 #line:507
                O00OOO0OO0OOOO000 ["rel_hist"]=[O0OOOOOO00OO0O0OO /sum (O0000O00OOOO0OO0O )for O0OOOOOO00OO0O0OO in O0000O00OOOO0OO0O ]#line:508
                O00OOO0OO0OOOO000 ["rel_hist_full"]=[OOOO00OO00OOOO0O0 /sum (OO0O0O00OOO00OOO0 )for OOOO00OO00OOOO0O0 in OO0O0O00OOO00OOO0 ]#line:509
        return O000000O0O0O0O00O ,O00OOO0OO0OOOO000 #line:511
    def _verifyUIC (O000000OOO000O00O ,_OO0OOO000OOOOOOOO ):#line:513
        O0O0OOO0O0OOOOOOO ={}#line:514
        OOOO000O00OO00O0O =0 #line:515
        for OO000O00O00OOO00O in O000000OOO000O00O .task_actinfo ['cedents']:#line:516
            O0O0OOO0O0OOOOOOO [OO000O00O00OOO00O ['cedent_type']]=OO000O00O00OOO00O ['filter_value']#line:518
            OOOO000O00OO00O0O =OOOO000O00OO00O0O +1 #line:519
        O00000000O000O000 =O000000OOO000O00O ._bitcount (_OO0OOO000OOOOOOOO )#line:521
        O0OOO0000OO00O0O0 =[]#line:522
        OOOOO00OO000OO0OO =0 #line:523
        OOO00000000O00OO0 =0 #line:524
        O000OOO000O0O00O0 =0 #line:525
        OO0OOO00OO0O0OOO0 =[]#line:526
        OOO0O00OOO000OO0O =[]#line:527
        if ('aad_weights'in O000000OOO000O00O .quantifiers ):#line:528
            OO0OOO00OO0O0OOO0 =O000000OOO000O00O .quantifiers .get ('aad_weights')#line:529
            OOO00000000O00OO0 =1 #line:530
        O000OOOO0O00O0O0O =O000000OOO000O00O .data ["dm"][O000000OOO000O00O .data ["varname"].index (O000000OOO000O00O .kwargs .get ('target'))]#line:531
        for OOOOO00O0OO0O00OO in range (len (O000OOOO0O00O0O0O )):#line:532
            O00OOO00O0O000000 =OOOOO00OO000OO0OO #line:534
            OOOOO00OO000OO0OO =O000000OOO000O00O ._bitcount (_OO0OOO000OOOOOOOO &O000OOOO0O00O0O0O [OOOOO00O0OO0O00OO ])#line:535
            O0OOO0000OO00O0O0 .append (OOOOO00OO000OO0OO )#line:536
            O0O00000OO0O0OOOO =O000000OOO000O00O ._bitcount (O0O0OOO0O0OOOOOOO ['cond']&O000OOOO0O00O0O0O [OOOOO00O0OO0O00OO ])#line:539
            OOO0O00OOO000OO0O .append (O0O00000OO0O0OOOO )#line:540
        if (OOO00000000O00OO0 &sum (O0OOO0000OO00O0O0 )>0 ):#line:542
            for OOOOO00O0OO0O00OO in range (len (O000OOOO0O00O0O0O )):#line:543
                if OOO0O00OOO000OO0O [OOOOO00O0OO0O00OO ]>0 :#line:544
                    if O0OOO0000OO00O0O0 [OOOOO00O0OO0O00OO ]/sum (O0OOO0000OO00O0O0 )>OOO0O00OOO000OO0O [OOOOO00O0OO0O00OO ]/sum (OOO0O00OOO000OO0O ):#line:546
                        O000OOO000O0O00O0 +=OO0OOO00OO0O0OOO0 [OOOOO00O0OO0O00OO ]*((O0OOO0000OO00O0O0 [OOOOO00O0OO0O00OO ]/sum (O0OOO0000OO00O0O0 ))/(OOO0O00OOO000OO0O [OOOOO00O0OO0O00OO ]/sum (OOO0O00OOO000OO0O ))-1 )#line:547
        OO00O00OO0O0O0OO0 =True #line:550
        for OOO00OOO00O0O0000 in O000000OOO000O00O .quantifiers .keys ():#line:551
            if OOO00OOO00O0O0000 .upper ()=='BASE':#line:552
                OO00O00OO0O0O0OO0 =OO00O00OO0O0O0OO0 and (O000000OOO000O00O .quantifiers .get (OOO00OOO00O0O0000 )<=O00000000O000O000 )#line:553
            if OOO00OOO00O0O0000 .upper ()=='RELBASE':#line:554
                OO00O00OO0O0O0OO0 =OO00O00OO0O0O0OO0 and (O000000OOO000O00O .quantifiers .get (OOO00OOO00O0O0000 )<=O00000000O000O000 *1.0 /O000000OOO000O00O .data ["rows_count"])#line:555
            if OOO00OOO00O0O0000 .upper ()=='AAD_SCORE':#line:556
                OO00O00OO0O0O0OO0 =OO00O00OO0O0O0OO0 and (O000000OOO000O00O .quantifiers .get (OOO00OOO00O0O0000 )<=O000OOO000O0O00O0 )#line:557
        O0O0OO0O0OOO0OO0O ={}#line:559
        if OO00O00OO0O0O0OO0 ==True :#line:560
            O000000OOO000O00O .stats ['total_valid']+=1 #line:562
            O0O0OO0O0OOO0OO0O ["base"]=O00000000O000O000 #line:563
            O0O0OO0O0OOO0OO0O ["rel_base"]=O00000000O000O000 *1.0 /O000000OOO000O00O .data ["rows_count"]#line:564
            O0O0OO0O0OOO0OO0O ["hist"]=O0OOO0000OO00O0O0 #line:565
            O0O0OO0O0OOO0OO0O ["aad_score"]=O000OOO000O0O00O0 #line:567
            O0O0OO0O0OOO0OO0O ["hist_cond"]=OOO0O00OOO000OO0O #line:568
            O0O0OO0O0OOO0OO0O ["rel_hist"]=[OO0O0OO00O000OO0O /sum (O0OOO0000OO00O0O0 )for OO0O0OO00O000OO0O in O0OOO0000OO00O0O0 ]#line:569
            O0O0OO0O0OOO0OO0O ["rel_hist_cond"]=[OO00O0O00OO0O00O0 /sum (OOO0O00OOO000OO0O )for OO00O0O00OO0O00O0 in OOO0O00OOO000OO0O ]#line:570
        return OO00O00OO0O0O0OO0 ,O0O0OO0O0OOO0OO0O #line:572
    def _verify4ft (OOOO0OOO00OO0O00O ,_O0OO0O0OOOO0OOO00 ):#line:574
        O000O0O00OOOOOOOO ={}#line:575
        OO00OO00000000000 =0 #line:576
        for O0OO0O0OO0OOO00O0 in OOOO0OOO00OO0O00O .task_actinfo ['cedents']:#line:577
            O000O0O00OOOOOOOO [O0OO0O0OO0OOO00O0 ['cedent_type']]=O0OO0O0OO0OOO00O0 ['filter_value']#line:579
            OO00OO00000000000 =OO00OO00000000000 +1 #line:580
        O0OO0O0O0OOO00OO0 =OOOO0OOO00OO0O00O ._bitcount (O000O0O00OOOOOOOO ['ante']&O000O0O00OOOOOOOO ['succ']&O000O0O00OOOOOOOO ['cond'])#line:582
        OOO000O0O0OO0OOO0 =None #line:583
        OOO000O0O0OO0OOO0 =0 #line:584
        if O0OO0O0O0OOO00OO0 >0 :#line:593
            OOO000O0O0OO0OOO0 =OOOO0OOO00OO0O00O ._bitcount (O000O0O00OOOOOOOO ['ante']&O000O0O00OOOOOOOO ['succ']&O000O0O00OOOOOOOO ['cond'])*1.0 /OOOO0OOO00OO0O00O ._bitcount (O000O0O00OOOOOOOO ['ante']&O000O0O00OOOOOOOO ['cond'])#line:594
        OOOOO000O0O00OO00 =1 <<OOOO0OOO00OO0O00O .data ["rows_count"]#line:596
        O00OOOOO0OOOOOOO0 =OOOO0OOO00OO0O00O ._bitcount (O000O0O00OOOOOOOO ['ante']&O000O0O00OOOOOOOO ['succ']&O000O0O00OOOOOOOO ['cond'])#line:597
        OOOOOO0OO0OO00OOO =OOOO0OOO00OO0O00O ._bitcount (O000O0O00OOOOOOOO ['ante']&~(OOOOO000O0O00OO00 |O000O0O00OOOOOOOO ['succ'])&O000O0O00OOOOOOOO ['cond'])#line:598
        O0OO0O0OO0OOO00O0 =OOOO0OOO00OO0O00O ._bitcount (~(OOOOO000O0O00OO00 |O000O0O00OOOOOOOO ['ante'])&O000O0O00OOOOOOOO ['succ']&O000O0O00OOOOOOOO ['cond'])#line:599
        O00O000000O0OOO0O =OOOO0OOO00OO0O00O ._bitcount (~(OOOOO000O0O00OO00 |O000O0O00OOOOOOOO ['ante'])&~(OOOOO000O0O00OO00 |O000O0O00OOOOOOOO ['succ'])&O000O0O00OOOOOOOO ['cond'])#line:600
        O0000O00O0OO00OOO =0 #line:601
        if (O00OOOOO0OOOOOOO0 +OOOOOO0OO0OO00OOO )*(O00OOOOO0OOOOOOO0 +O0OO0O0OO0OOO00O0 )>0 :#line:602
            O0000O00O0OO00OOO =O00OOOOO0OOOOOOO0 *(O00OOOOO0OOOOOOO0 +OOOOOO0OO0OO00OOO +O0OO0O0OO0OOO00O0 +O00O000000O0OOO0O )/(O00OOOOO0OOOOOOO0 +OOOOOO0OO0OO00OOO )/(O00OOOOO0OOOOOOO0 +O0OO0O0OO0OOO00O0 )-1 #line:603
        else :#line:604
            O0000O00O0OO00OOO =None #line:605
        O00OO0O0OO0O00000 =0 #line:606
        if (O00OOOOO0OOOOOOO0 +OOOOOO0OO0OO00OOO )*(O00OOOOO0OOOOOOO0 +O0OO0O0OO0OOO00O0 )>0 :#line:607
            O00OO0O0OO0O00000 =1 -O00OOOOO0OOOOOOO0 *(O00OOOOO0OOOOOOO0 +OOOOOO0OO0OO00OOO +O0OO0O0OO0OOO00O0 +O00O000000O0OOO0O )/(O00OOOOO0OOOOOOO0 +OOOOOO0OO0OO00OOO )/(O00OOOOO0OOOOOOO0 +O0OO0O0OO0OOO00O0 )#line:608
        else :#line:609
            O00OO0O0OO0O00000 =None #line:610
        O0O0OOOOO000000O0 =True #line:611
        for OOOO0000OOOO00000 in OOOO0OOO00OO0O00O .quantifiers .keys ():#line:612
            if OOOO0000OOOO00000 .upper ()=='BASE':#line:613
                O0O0OOOOO000000O0 =O0O0OOOOO000000O0 and (OOOO0OOO00OO0O00O .quantifiers .get (OOOO0000OOOO00000 )<=O0OO0O0O0OOO00OO0 )#line:614
            if OOOO0000OOOO00000 .upper ()=='RELBASE':#line:615
                O0O0OOOOO000000O0 =O0O0OOOOO000000O0 and (OOOO0OOO00OO0O00O .quantifiers .get (OOOO0000OOOO00000 )<=O0OO0O0O0OOO00OO0 *1.0 /OOOO0OOO00OO0O00O .data ["rows_count"])#line:616
            if (OOOO0000OOOO00000 .upper ()=='PIM')or (OOOO0000OOOO00000 .upper ()=='CONF'):#line:617
                O0O0OOOOO000000O0 =O0O0OOOOO000000O0 and (OOOO0OOO00OO0O00O .quantifiers .get (OOOO0000OOOO00000 )<=OOO000O0O0OO0OOO0 )#line:618
            if OOOO0000OOOO00000 .upper ()=='AAD':#line:619
                if O0000O00O0OO00OOO !=None :#line:620
                    O0O0OOOOO000000O0 =O0O0OOOOO000000O0 and (OOOO0OOO00OO0O00O .quantifiers .get (OOOO0000OOOO00000 )<=O0000O00O0OO00OOO )#line:621
                else :#line:622
                    O0O0OOOOO000000O0 =False #line:623
            if OOOO0000OOOO00000 .upper ()=='BAD':#line:624
                if O00OO0O0OO0O00000 !=None :#line:625
                    O0O0OOOOO000000O0 =O0O0OOOOO000000O0 and (OOOO0OOO00OO0O00O .quantifiers .get (OOOO0000OOOO00000 )<=O00OO0O0OO0O00000 )#line:626
                else :#line:627
                    O0O0OOOOO000000O0 =False #line:628
            OO000O0000O0OOO0O ={}#line:629
        if O0O0OOOOO000000O0 ==True :#line:630
            OOOO0OOO00OO0O00O .stats ['total_valid']+=1 #line:632
            OO000O0000O0OOO0O ["base"]=O0OO0O0O0OOO00OO0 #line:633
            OO000O0000O0OOO0O ["rel_base"]=O0OO0O0O0OOO00OO0 *1.0 /OOOO0OOO00OO0O00O .data ["rows_count"]#line:634
            OO000O0000O0OOO0O ["conf"]=OOO000O0O0OO0OOO0 #line:635
            OO000O0000O0OOO0O ["aad"]=O0000O00O0OO00OOO #line:636
            OO000O0000O0OOO0O ["bad"]=O00OO0O0OO0O00000 #line:637
            OO000O0000O0OOO0O ["fourfold"]=[O00OOOOO0OOOOOOO0 ,OOOOOO0OO0OO00OOO ,O0OO0O0OO0OOO00O0 ,O00O000000O0OOO0O ]#line:638
        return O0O0OOOOO000000O0 ,OO000O0000O0OOO0O #line:642
    def _verifysd4ft (O0O0OO00OOOO000O0 ,_OOOO000OO0OO0OOO0 ):#line:644
        O0000OO000O00OOO0 ={}#line:645
        O00OOOO00OOOO00OO =0 #line:646
        for OOOO0OO0O0O0OO0O0 in O0O0OO00OOOO000O0 .task_actinfo ['cedents']:#line:647
            O0000OO000O00OOO0 [OOOO0OO0O0O0OO0O0 ['cedent_type']]=OOOO0OO0O0O0OO0O0 ['filter_value']#line:649
            O00OOOO00OOOO00OO =O00OOOO00OOOO00OO +1 #line:650
        OO00OO0O00O00O00O =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])#line:652
        OOOOOOOOO0O0O0O0O =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])#line:653
        OO0OOOO00O0O0O00O =None #line:654
        O0OOO0O00O0000OOO =0 #line:655
        O00OO0OOO000O000O =0 #line:656
        if OO00OO0O00O00O00O >0 :#line:665
            O0OOO0O00O0000OOO =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])*1.0 /O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])#line:666
        if OOOOOOOOO0O0O0O0O >0 :#line:667
            O00OO0OOO000O000O =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])*1.0 /O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])#line:668
        OO000OOOOO0OOO0O0 =1 <<O0O0OO00OOOO000O0 .data ["rows_count"]#line:670
        O0O00O00O000OO00O =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])#line:671
        OOOOOOOOOOOOOO0OO =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['succ'])&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])#line:672
        O0OO00O0O000OO00O =O0O0OO00OOOO000O0 ._bitcount (~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['ante'])&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])#line:673
        O0OOO00OO000OOOO0 =O0O0OO00OOOO000O0 ._bitcount (~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['ante'])&~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['succ'])&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['frst'])#line:674
        O0O00O0O0OO00O00O =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])#line:675
        O00000OOO0O00O0O0 =O0O0OO00OOOO000O0 ._bitcount (O0000OO000O00OOO0 ['ante']&~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['succ'])&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])#line:676
        OO000O00O0OO00OO0 =O0O0OO00OOOO000O0 ._bitcount (~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['ante'])&O0000OO000O00OOO0 ['succ']&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])#line:677
        OO0OO000O00OO00OO =O0O0OO00OOOO000O0 ._bitcount (~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['ante'])&~(OO000OOOOO0OOO0O0 |O0000OO000O00OOO0 ['succ'])&O0000OO000O00OOO0 ['cond']&O0000OO000O00OOO0 ['scnd'])#line:678
        O0000000OOO0O0OO0 =True #line:679
        for OO0O0O0OO00O000O0 in O0O0OO00OOOO000O0 .quantifiers .keys ():#line:680
            if (OO0O0O0OO00O000O0 .upper ()=='FRSTBASE')|(OO0O0O0OO00O000O0 .upper ()=='BASE1'):#line:681
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=OO00OO0O00O00O00O )#line:682
            if (OO0O0O0OO00O000O0 .upper ()=='SCNDBASE')|(OO0O0O0OO00O000O0 .upper ()=='BASE2'):#line:683
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=OOOOOOOOO0O0O0O0O )#line:684
            if (OO0O0O0OO00O000O0 .upper ()=='FRSTRELBASE')|(OO0O0O0OO00O000O0 .upper ()=='RELBASE1'):#line:685
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=OO00OO0O00O00O00O *1.0 /O0O0OO00OOOO000O0 .data ["rows_count"])#line:686
            if (OO0O0O0OO00O000O0 .upper ()=='SCNDRELBASE')|(OO0O0O0OO00O000O0 .upper ()=='RELBASE2'):#line:687
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=OOOOOOOOO0O0O0O0O *1.0 /O0O0OO00OOOO000O0 .data ["rows_count"])#line:688
            if (OO0O0O0OO00O000O0 .upper ()=='FRSTPIM')|(OO0O0O0OO00O000O0 .upper ()=='PIM1')|(OO0O0O0OO00O000O0 .upper ()=='FRSTCONF')|(OO0O0O0OO00O000O0 .upper ()=='CONF1'):#line:689
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=O0OOO0O00O0000OOO )#line:690
            if (OO0O0O0OO00O000O0 .upper ()=='SCNDPIM')|(OO0O0O0OO00O000O0 .upper ()=='PIM2')|(OO0O0O0OO00O000O0 .upper ()=='SCNDCONF')|(OO0O0O0OO00O000O0 .upper ()=='CONF2'):#line:691
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=O00OO0OOO000O000O )#line:692
            if (OO0O0O0OO00O000O0 .upper ()=='DELTAPIM')|(OO0O0O0OO00O000O0 .upper ()=='DELTACONF'):#line:693
                O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=O0OOO0O00O0000OOO -O00OO0OOO000O000O )#line:694
            if (OO0O0O0OO00O000O0 .upper ()=='RATIOPIM')|(OO0O0O0OO00O000O0 .upper ()=='RATIOCONF'):#line:697
                if (O00OO0OOO000O000O >0 ):#line:698
                    O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )<=O0OOO0O00O0000OOO *1.0 /O00OO0OOO000O000O )#line:699
                else :#line:700
                    O0000000OOO0O0OO0 =False #line:701
            if (OO0O0O0OO00O000O0 .upper ()=='RATIOPIM_LEQ')|(OO0O0O0OO00O000O0 .upper ()=='RATIOCONF_LEQ'):#line:702
                if (O00OO0OOO000O000O >0 ):#line:703
                    O0000000OOO0O0OO0 =O0000000OOO0O0OO0 and (O0O0OO00OOOO000O0 .quantifiers .get (OO0O0O0OO00O000O0 )>=O0OOO0O00O0000OOO *1.0 /O00OO0OOO000O000O )#line:704
                else :#line:705
                    O0000000OOO0O0OO0 =False #line:706
        O000000OOOO0O00OO ={}#line:707
        if O0000000OOO0O0OO0 ==True :#line:708
            O0O0OO00OOOO000O0 .stats ['total_valid']+=1 #line:710
            O000000OOOO0O00OO ["base1"]=OO00OO0O00O00O00O #line:711
            O000000OOOO0O00OO ["base2"]=OOOOOOOOO0O0O0O0O #line:712
            O000000OOOO0O00OO ["rel_base1"]=OO00OO0O00O00O00O *1.0 /O0O0OO00OOOO000O0 .data ["rows_count"]#line:713
            O000000OOOO0O00OO ["rel_base2"]=OOOOOOOOO0O0O0O0O *1.0 /O0O0OO00OOOO000O0 .data ["rows_count"]#line:714
            O000000OOOO0O00OO ["conf1"]=O0OOO0O00O0000OOO #line:715
            O000000OOOO0O00OO ["conf2"]=O00OO0OOO000O000O #line:716
            O000000OOOO0O00OO ["deltaconf"]=O0OOO0O00O0000OOO -O00OO0OOO000O000O #line:717
            if (O00OO0OOO000O000O >0 ):#line:718
                O000000OOOO0O00OO ["ratioconf"]=O0OOO0O00O0000OOO *1.0 /O00OO0OOO000O000O #line:719
            else :#line:720
                O000000OOOO0O00OO ["ratioconf"]=None #line:721
            O000000OOOO0O00OO ["fourfold1"]=[O0O00O00O000OO00O ,OOOOOOOOOOOOOO0OO ,O0OO00O0O000OO00O ,O0OOO00OO000OOOO0 ]#line:722
            O000000OOOO0O00OO ["fourfold2"]=[O0O00O0O0OO00O00O ,O00000OOO0O00O0O0 ,OO000O00O0OO00OO0 ,OO0OO000O00OO00OO ]#line:723
        return O0000000OOO0O0OO0 ,O000000OOOO0O00OO #line:727
    def _verifynewact4ft (OO0O0O00OOOO000O0 ,_OO00O000OOOOOOOOO ):#line:729
        OO00OO0OO000O0O0O ={}#line:730
        for O0OO00O000OOO0OOO in OO0O0O00OOOO000O0 .task_actinfo ['cedents']:#line:731
            OO00OO0OO000O0O0O [O0OO00O000OOO0OOO ['cedent_type']]=O0OO00O000OOO0OOO ['filter_value']#line:733
        OOOOOO0OO00OOO0O0 =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond'])#line:735
        O000O0OO00OOOO000 =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond']&OO00OO0OO000O0O0O ['antv']&OO00OO0OO000O0O0O ['sucv'])#line:736
        OOOOO0OO0O0O000O0 =None #line:737
        OOO0OO0O00000OO00 =0 #line:738
        O0O00O0OO0OO00000 =0 #line:739
        if OOOOOO0OO00OOO0O0 >0 :#line:748
            OOO0OO0O00000OO00 =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond'])*1.0 /OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['cond'])#line:749
        if O000O0OO00OOOO000 >0 :#line:750
            O0O00O0OO0OO00000 =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond']&OO00OO0OO000O0O0O ['antv']&OO00OO0OO000O0O0O ['sucv'])*1.0 /OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['cond']&OO00OO0OO000O0O0O ['antv'])#line:752
        OO0O00OO00OOOOOOO =1 <<OO0O0O00OOOO000O0 .rows_count #line:754
        OOO0OO0O0OOOOO000 =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond'])#line:755
        OO00OOOOOO00OO00O =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&~(OO0O00OO00OOOOOOO |OO00OO0OO000O0O0O ['succ'])&OO00OO0OO000O0O0O ['cond'])#line:756
        O0O0OOO0O00OOO000 =OO0O0O00OOOO000O0 ._bitcount (~(OO0O00OO00OOOOOOO |OO00OO0OO000O0O0O ['ante'])&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond'])#line:757
        OO0O0OOOO0OOOOO00 =OO0O0O00OOOO000O0 ._bitcount (~(OO0O00OO00OOOOOOO |OO00OO0OO000O0O0O ['ante'])&~(OO0O00OO00OOOOOOO |OO00OO0OO000O0O0O ['succ'])&OO00OO0OO000O0O0O ['cond'])#line:758
        O00OOOOO0O00OO00O =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond']&OO00OO0OO000O0O0O ['antv']&OO00OO0OO000O0O0O ['sucv'])#line:759
        O0O0O0O00000O0OO0 =OO0O0O00OOOO000O0 ._bitcount (OO00OO0OO000O0O0O ['ante']&~(OO0O00OO00OOOOOOO |(OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['sucv']))&OO00OO0OO000O0O0O ['cond'])#line:760
        OOOO0000OOO00000O =OO0O0O00OOOO000O0 ._bitcount (~(OO0O00OO00OOOOOOO |(OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['antv']))&OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['cond']&OO00OO0OO000O0O0O ['sucv'])#line:761
        O0O00O00OOO00OOO0 =OO0O0O00OOOO000O0 ._bitcount (~(OO0O00OO00OOOOOOO |(OO00OO0OO000O0O0O ['ante']&OO00OO0OO000O0O0O ['antv']))&~(OO0O00OO00OOOOOOO |(OO00OO0OO000O0O0O ['succ']&OO00OO0OO000O0O0O ['sucv']))&OO00OO0OO000O0O0O ['cond'])#line:762
        O0OOOOO0OOO00000O =True #line:763
        for O0OO00O000O0O0OOO in OO0O0O00OOOO000O0 .quantifiers .keys ():#line:764
            if (O0OO00O000O0O0OOO =='PreBase')|(O0OO00O000O0O0OOO =='Base1'):#line:765
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=OOOOOO0OO00OOO0O0 )#line:766
            if (O0OO00O000O0O0OOO =='PostBase')|(O0OO00O000O0O0OOO =='Base2'):#line:767
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=O000O0OO00OOOO000 )#line:768
            if (O0OO00O000O0O0OOO =='PreRelBase')|(O0OO00O000O0O0OOO =='RelBase1'):#line:769
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=OOOOOO0OO00OOO0O0 *1.0 /OO0O0O00OOOO000O0 .data ["rows_count"])#line:770
            if (O0OO00O000O0O0OOO =='PostRelBase')|(O0OO00O000O0O0OOO =='RelBase2'):#line:771
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=O000O0OO00OOOO000 *1.0 /OO0O0O00OOOO000O0 .data ["rows_count"])#line:772
            if (O0OO00O000O0O0OOO =='Prepim')|(O0OO00O000O0O0OOO =='pim1')|(O0OO00O000O0O0OOO =='PreConf')|(O0OO00O000O0O0OOO =='conf1'):#line:773
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=OOO0OO0O00000OO00 )#line:774
            if (O0OO00O000O0O0OOO =='Postpim')|(O0OO00O000O0O0OOO =='pim2')|(O0OO00O000O0O0OOO =='PostConf')|(O0OO00O000O0O0OOO =='conf2'):#line:775
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=O0O00O0OO0OO00000 )#line:776
            if (O0OO00O000O0O0OOO =='Deltapim')|(O0OO00O000O0O0OOO =='DeltaConf'):#line:777
                O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=OOO0OO0O00000OO00 -O0O00O0OO0OO00000 )#line:778
            if (O0OO00O000O0O0OOO =='Ratiopim')|(O0OO00O000O0O0OOO =='RatioConf'):#line:781
                if (O0O00O0OO0OO00000 >0 ):#line:782
                    O0OOOOO0OOO00000O =O0OOOOO0OOO00000O and (OO0O0O00OOOO000O0 .quantifiers .get (O0OO00O000O0O0OOO )<=OOO0OO0O00000OO00 *1.0 /O0O00O0OO0OO00000 )#line:783
                else :#line:784
                    O0OOOOO0OOO00000O =False #line:785
        O00O000OOOO00O000 ={}#line:786
        if O0OOOOO0OOO00000O ==True :#line:787
            OO0O0O00OOOO000O0 .stats ['total_valid']+=1 #line:789
            O00O000OOOO00O000 ["base1"]=OOOOOO0OO00OOO0O0 #line:790
            O00O000OOOO00O000 ["base2"]=O000O0OO00OOOO000 #line:791
            O00O000OOOO00O000 ["rel_base1"]=OOOOOO0OO00OOO0O0 *1.0 /OO0O0O00OOOO000O0 .data ["rows_count"]#line:792
            O00O000OOOO00O000 ["rel_base2"]=O000O0OO00OOOO000 *1.0 /OO0O0O00OOOO000O0 .data ["rows_count"]#line:793
            O00O000OOOO00O000 ["conf1"]=OOO0OO0O00000OO00 #line:794
            O00O000OOOO00O000 ["conf2"]=O0O00O0OO0OO00000 #line:795
            O00O000OOOO00O000 ["deltaconf"]=OOO0OO0O00000OO00 -O0O00O0OO0OO00000 #line:796
            if (O0O00O0OO0OO00000 >0 ):#line:797
                O00O000OOOO00O000 ["ratioconf"]=OOO0OO0O00000OO00 *1.0 /O0O00O0OO0OO00000 #line:798
            else :#line:799
                O00O000OOOO00O000 ["ratioconf"]=None #line:800
            O00O000OOOO00O000 ["fourfoldpre"]=[OOO0OO0O0OOOOO000 ,OO00OOOOOO00OO00O ,O0O0OOO0O00OOO000 ,OO0O0OOOO0OOOOO00 ]#line:801
            O00O000OOOO00O000 ["fourfoldpost"]=[O00OOOOO0O00OO00O ,O0O0O0O00000O0OO0 ,OOOO0000OOO00000O ,O0O00O00OOO00OOO0 ]#line:802
        return O0OOOOO0OOO00000O ,O00O000OOOO00O000 #line:804
    def _verifyact4ft (OOOO0OO000OOO0O0O ,_OO00OO00OOO000OOO ):#line:806
        OO00OOO0OO00O0OOO ={}#line:807
        for O0O0OOOO00OOOOOO0 in OOOO0OO000OOO0O0O .task_actinfo ['cedents']:#line:808
            OO00OOO0OO00O0OOO [O0O0OOOO00OOOOOO0 ['cedent_type']]=O0O0OOOO00OOOOOO0 ['filter_value']#line:810
        O0OO00O000OO0O00O =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv-']&OO00OOO0OO00O0OOO ['sucv-'])#line:812
        OOO0O0OOO0O000OO0 =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv+']&OO00OOO0OO00O0OOO ['sucv+'])#line:813
        O0OOO000O000O00OO =None #line:814
        O0O0O0OO00O00OO0O =0 #line:815
        O0O0OOOO0O0O00O0O =0 #line:816
        if O0OO00O000OO0O00O >0 :#line:825
            O0O0O0OO00O00OO0O =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv-']&OO00OOO0OO00O0OOO ['sucv-'])*1.0 /OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv-'])#line:827
        if OOO0O0OOO0O000OO0 >0 :#line:828
            O0O0OOOO0O0O00O0O =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv+']&OO00OOO0OO00O0OOO ['sucv+'])*1.0 /OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv+'])#line:830
        OOO0000000OO0O0OO =1 <<OOOO0OO000OOO0O0O .data ["rows_count"]#line:832
        O00O00000O00OOO00 =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv-']&OO00OOO0OO00O0OOO ['sucv-'])#line:833
        OO00OOOOOOOOOO0OO =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['antv-']&~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['sucv-']))&OO00OOO0OO00O0OOO ['cond'])#line:834
        O00OOOO000OOOO0OO =OOOO0OO000OOO0O0O ._bitcount (~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['antv-']))&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['sucv-'])#line:835
        O0OOO0O00000O0000 =OOOO0OO000OOO0O0O ._bitcount (~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['antv-']))&~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['sucv-']))&OO00OOO0OO00O0OOO ['cond'])#line:836
        OOO000O00O0OOO000 =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['antv+']&OO00OOO0OO00O0OOO ['sucv+'])#line:837
        O0OO0OOO00O00OO0O =OOOO0OO000OOO0O0O ._bitcount (OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['antv+']&~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['sucv+']))&OO00OOO0OO00O0OOO ['cond'])#line:838
        OO00O000O0O0000OO =OOOO0OO000OOO0O0O ._bitcount (~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['antv+']))&OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['cond']&OO00OOO0OO00O0OOO ['sucv+'])#line:839
        O00O0O0OO000O00OO =OOOO0OO000OOO0O0O ._bitcount (~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['ante']&OO00OOO0OO00O0OOO ['antv+']))&~(OOO0000000OO0O0OO |(OO00OOO0OO00O0OOO ['succ']&OO00OOO0OO00O0OOO ['sucv+']))&OO00OOO0OO00O0OOO ['cond'])#line:840
        O0000OOO0OO0OOOO0 =True #line:841
        for OO0OO000OO0000O00 in OOOO0OO000OOO0O0O .quantifiers .keys ():#line:842
            if (OO0OO000OO0000O00 =='PreBase')|(OO0OO000OO0000O00 =='Base1'):#line:843
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=O0OO00O000OO0O00O )#line:844
            if (OO0OO000OO0000O00 =='PostBase')|(OO0OO000OO0000O00 =='Base2'):#line:845
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=OOO0O0OOO0O000OO0 )#line:846
            if (OO0OO000OO0000O00 =='PreRelBase')|(OO0OO000OO0000O00 =='RelBase1'):#line:847
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=O0OO00O000OO0O00O *1.0 /OOOO0OO000OOO0O0O .data ["rows_count"])#line:848
            if (OO0OO000OO0000O00 =='PostRelBase')|(OO0OO000OO0000O00 =='RelBase2'):#line:849
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=OOO0O0OOO0O000OO0 *1.0 /OOOO0OO000OOO0O0O .data ["rows_count"])#line:850
            if (OO0OO000OO0000O00 =='Prepim')|(OO0OO000OO0000O00 =='pim1')|(OO0OO000OO0000O00 =='PreConf')|(OO0OO000OO0000O00 =='conf1'):#line:851
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=O0O0O0OO00O00OO0O )#line:852
            if (OO0OO000OO0000O00 =='Postpim')|(OO0OO000OO0000O00 =='pim2')|(OO0OO000OO0000O00 =='PostConf')|(OO0OO000OO0000O00 =='conf2'):#line:853
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=O0O0OOOO0O0O00O0O )#line:854
            if (OO0OO000OO0000O00 =='Deltapim')|(OO0OO000OO0000O00 =='DeltaConf'):#line:855
                O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=O0O0O0OO00O00OO0O -O0O0OOOO0O0O00O0O )#line:856
            if (OO0OO000OO0000O00 =='Ratiopim')|(OO0OO000OO0000O00 =='RatioConf'):#line:859
                if (O0O0O0OO00O00OO0O >0 ):#line:860
                    O0000OOO0OO0OOOO0 =O0000OOO0OO0OOOO0 and (OOOO0OO000OOO0O0O .quantifiers .get (OO0OO000OO0000O00 )<=O0O0OOOO0O0O00O0O *1.0 /O0O0O0OO00O00OO0O )#line:861
                else :#line:862
                    O0000OOO0OO0OOOO0 =False #line:863
        OOO0O0OO0000O00OO ={}#line:864
        if O0000OOO0OO0OOOO0 ==True :#line:865
            OOOO0OO000OOO0O0O .stats ['total_valid']+=1 #line:867
            OOO0O0OO0000O00OO ["base1"]=O0OO00O000OO0O00O #line:868
            OOO0O0OO0000O00OO ["base2"]=OOO0O0OOO0O000OO0 #line:869
            OOO0O0OO0000O00OO ["rel_base1"]=O0OO00O000OO0O00O *1.0 /OOOO0OO000OOO0O0O .data ["rows_count"]#line:870
            OOO0O0OO0000O00OO ["rel_base2"]=OOO0O0OOO0O000OO0 *1.0 /OOOO0OO000OOO0O0O .data ["rows_count"]#line:871
            OOO0O0OO0000O00OO ["conf1"]=O0O0O0OO00O00OO0O #line:872
            OOO0O0OO0000O00OO ["conf2"]=O0O0OOOO0O0O00O0O #line:873
            OOO0O0OO0000O00OO ["deltaconf"]=O0O0O0OO00O00OO0O -O0O0OOOO0O0O00O0O #line:874
            if (O0O0O0OO00O00OO0O >0 ):#line:875
                OOO0O0OO0000O00OO ["ratioconf"]=O0O0OOOO0O0O00O0O *1.0 /O0O0O0OO00O00OO0O #line:876
            else :#line:877
                OOO0O0OO0000O00OO ["ratioconf"]=None #line:878
            OOO0O0OO0000O00OO ["fourfoldpre"]=[O00O00000O00OOO00 ,OO00OOOOOOOOOO0OO ,O00OOOO000OOOO0OO ,O0OOO0O00000O0000 ]#line:879
            OOO0O0OO0000O00OO ["fourfoldpost"]=[OOO000O00O0OOO000 ,O0OO0OOO00O00OO0O ,OO00O000O0O0000OO ,O00O0O0OO000O00OO ]#line:880
        return O0000OOO0OO0OOOO0 ,OOO0O0OO0000O00OO #line:882
    def _verify_opt (OO0OO00000O00OOOO ,O00OOOOO0O0O000O0 ,OO0O0OO0OOOOOOO00 ):#line:884
        OO0OO00000O00OOOO .stats ['total_ver']+=1 #line:885
        OOO0OOOO0O00000OO =False #line:886
        if not (O00OOOOO0O0O000O0 ['optim'].get ('only_con')):#line:889
            return False #line:890
        if not (OO0OO00000O00OOOO .options ['optimizations']):#line:893
            return False #line:895
        OOOOOOOO0000OO000 ={}#line:897
        for O0O0OOO0OOO0OO00O in OO0OO00000O00OOOO .task_actinfo ['cedents']:#line:898
            OOOOOOOO0000OO000 [O0O0OOO0OOO0OO00O ['cedent_type']]=O0O0OOO0OOO0OO00O ['filter_value']#line:900
        O000OOOO000OO0OO0 =1 <<OO0OO00000O00OOOO .data ["rows_count"]#line:902
        OOO0OOOO0000OO000 =O000OOOO000OO0OO0 -1 #line:903
        OOOOOO0OO0O0OO00O =""#line:904
        OOOO0O0O0OOOO0OO0 =0 #line:905
        if (OOOOOOOO0000OO000 .get ('ante')!=None ):#line:906
            OOO0OOOO0000OO000 =OOO0OOOO0000OO000 &OOOOOOOO0000OO000 ['ante']#line:907
        if (OOOOOOOO0000OO000 .get ('succ')!=None ):#line:908
            OOO0OOOO0000OO000 =OOO0OOOO0000OO000 &OOOOOOOO0000OO000 ['succ']#line:909
        if (OOOOOOOO0000OO000 .get ('cond')!=None ):#line:910
            OOO0OOOO0000OO000 =OOO0OOOO0000OO000 &OOOOOOOO0000OO000 ['cond']#line:911
        O0O0OO00OO0000OO0 =None #line:914
        if (OO0OO00000O00OOOO .proc =='CFMiner')|(OO0OO00000O00OOOO .proc =='4ftMiner')|(OO0OO00000O00OOOO .proc =='UICMiner'):#line:939
            OO0O00OOOOOOO0OO0 =OO0OO00000O00OOOO ._bitcount (OOO0OOOO0000OO000 )#line:940
            if not (OO0OO00000O00OOOO ._opt_base ==None ):#line:941
                if not (OO0OO00000O00OOOO ._opt_base <=OO0O00OOOOOOO0OO0 ):#line:942
                    OOO0OOOO0O00000OO =True #line:943
            if not (OO0OO00000O00OOOO ._opt_relbase ==None ):#line:945
                if not (OO0OO00000O00OOOO ._opt_relbase <=OO0O00OOOOOOO0OO0 *1.0 /OO0OO00000O00OOOO .data ["rows_count"]):#line:946
                    OOO0OOOO0O00000OO =True #line:947
        if (OO0OO00000O00OOOO .proc =='SD4ftMiner'):#line:949
            OO0O00OOOOOOO0OO0 =OO0OO00000O00OOOO ._bitcount (OOO0OOOO0000OO000 )#line:950
            if (not (OO0OO00000O00OOOO ._opt_base1 ==None ))&(not (OO0OO00000O00OOOO ._opt_base2 ==None )):#line:951
                if not (max (OO0OO00000O00OOOO ._opt_base1 ,OO0OO00000O00OOOO ._opt_base2 )<=OO0O00OOOOOOO0OO0 ):#line:952
                    OOO0OOOO0O00000OO =True #line:954
            if (not (OO0OO00000O00OOOO ._opt_relbase1 ==None ))&(not (OO0OO00000O00OOOO ._opt_relbase2 ==None )):#line:955
                if not (max (OO0OO00000O00OOOO ._opt_relbase1 ,OO0OO00000O00OOOO ._opt_relbase2 )<=OO0O00OOOOOOO0OO0 *1.0 /OO0OO00000O00OOOO .data ["rows_count"]):#line:956
                    OOO0OOOO0O00000OO =True #line:957
        return OOO0OOOO0O00000OO #line:959
        if OO0OO00000O00OOOO .proc =='CFMiner':#line:962
            if (OO0O0OO0OOOOOOO00 ['cedent_type']=='cond')&(OO0O0OO0OOOOOOO00 ['defi'].get ('type')=='con'):#line:963
                OO0O00OOOOOOO0OO0 =bin (OOOOOOOO0000OO000 ['cond']).count ("1")#line:964
                OO0OOOO0OOOO0O0O0 =True #line:965
                for OOO00OO0O0O0O00O0 in OO0OO00000O00OOOO .quantifiers .keys ():#line:966
                    if OOO00OO0O0O0O00O0 =='Base':#line:967
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OO0O00OOOOOOO0OO0 )#line:968
                        if not (OO0OOOO0OOOO0O0O0 ):#line:969
                            print (f"...optimization : base is {OO0O00OOOOOOO0OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:970
                    if OOO00OO0O0O0O00O0 =='RelBase':#line:971
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OO0O00OOOOOOO0OO0 *1.0 /OO0OO00000O00OOOO .data ["rows_count"])#line:972
                        if not (OO0OOOO0OOOO0O0O0 ):#line:973
                            print (f"...optimization : base is {OO0O00OOOOOOO0OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:974
                OOO0OOOO0O00000OO =not (OO0OOOO0OOOO0O0O0 )#line:975
        elif OO0OO00000O00OOOO .proc =='4ftMiner':#line:976
            if (OO0O0OO0OOOOOOO00 ['cedent_type']=='cond')&(OO0O0OO0OOOOOOO00 ['defi'].get ('type')=='con'):#line:977
                OO0O00OOOOOOO0OO0 =bin (OOOOOOOO0000OO000 ['cond']).count ("1")#line:978
                OO0OOOO0OOOO0O0O0 =True #line:979
                for OOO00OO0O0O0O00O0 in OO0OO00000O00OOOO .quantifiers .keys ():#line:980
                    if OOO00OO0O0O0O00O0 =='Base':#line:981
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OO0O00OOOOOOO0OO0 )#line:982
                        if not (OO0OOOO0OOOO0O0O0 ):#line:983
                            print (f"...optimization : base is {OO0O00OOOOOOO0OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:984
                    if OOO00OO0O0O0O00O0 =='RelBase':#line:985
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OO0O00OOOOOOO0OO0 *1.0 /OO0OO00000O00OOOO .data ["rows_count"])#line:986
                        if not (OO0OOOO0OOOO0O0O0 ):#line:987
                            print (f"...optimization : base is {OO0O00OOOOOOO0OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:988
                OOO0OOOO0O00000OO =not (OO0OOOO0OOOO0O0O0 )#line:989
            if (OO0O0OO0OOOOOOO00 ['cedent_type']=='ante')&(OO0O0OO0OOOOOOO00 ['defi'].get ('type')=='con'):#line:990
                OO0O00OOOOOOO0OO0 =bin (OOOOOOOO0000OO000 ['ante']&OOOOOOOO0000OO000 ['cond']).count ("1")#line:991
                OO0OOOO0OOOO0O0O0 =True #line:992
                for OOO00OO0O0O0O00O0 in OO0OO00000O00OOOO .quantifiers .keys ():#line:993
                    if OOO00OO0O0O0O00O0 =='Base':#line:994
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OO0O00OOOOOOO0OO0 )#line:995
                        if not (OO0OOOO0OOOO0O0O0 ):#line:996
                            print (f"...optimization : ANTE: base is {OO0O00OOOOOOO0OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:997
                    if OOO00OO0O0O0O00O0 =='RelBase':#line:998
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OO0O00OOOOOOO0OO0 *1.0 /OO0OO00000O00OOOO .data ["rows_count"])#line:999
                        if not (OO0OOOO0OOOO0O0O0 ):#line:1000
                            print (f"...optimization : ANTE:  base is {OO0O00OOOOOOO0OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:1001
                OOO0OOOO0O00000OO =not (OO0OOOO0OOOO0O0O0 )#line:1002
            if (OO0O0OO0OOOOOOO00 ['cedent_type']=='succ')&(OO0O0OO0OOOOOOO00 ['defi'].get ('type')=='con'):#line:1003
                OO0O00OOOOOOO0OO0 =bin (OOOOOOOO0000OO000 ['ante']&OOOOOOOO0000OO000 ['cond']&OOOOOOOO0000OO000 ['succ']).count ("1")#line:1004
                O0O0OO00OO0000OO0 =0 #line:1005
                if OO0O00OOOOOOO0OO0 >0 :#line:1006
                    O0O0OO00OO0000OO0 =bin (OOOOOOOO0000OO000 ['ante']&OOOOOOOO0000OO000 ['succ']&OOOOOOOO0000OO000 ['cond']).count ("1")*1.0 /bin (OOOOOOOO0000OO000 ['ante']&OOOOOOOO0000OO000 ['cond']).count ("1")#line:1007
                O000OOOO000OO0OO0 =1 <<OO0OO00000O00OOOO .data ["rows_count"]#line:1008
                OOOO0O0OOOOOO00O0 =bin (OOOOOOOO0000OO000 ['ante']&OOOOOOOO0000OO000 ['succ']&OOOOOOOO0000OO000 ['cond']).count ("1")#line:1009
                OOOOOOOO000O0OOO0 =bin (OOOOOOOO0000OO000 ['ante']&~(O000OOOO000OO0OO0 |OOOOOOOO0000OO000 ['succ'])&OOOOOOOO0000OO000 ['cond']).count ("1")#line:1010
                O0O0OOO0OOO0OO00O =bin (~(O000OOOO000OO0OO0 |OOOOOOOO0000OO000 ['ante'])&OOOOOOOO0000OO000 ['succ']&OOOOOOOO0000OO000 ['cond']).count ("1")#line:1011
                O0O000O0000O0OO00 =bin (~(O000OOOO000OO0OO0 |OOOOOOOO0000OO000 ['ante'])&~(O000OOOO000OO0OO0 |OOOOOOOO0000OO000 ['succ'])&OOOOOOOO0000OO000 ['cond']).count ("1")#line:1012
                OO0OOOO0OOOO0O0O0 =True #line:1013
                for OOO00OO0O0O0O00O0 in OO0OO00000O00OOOO .quantifiers .keys ():#line:1014
                    if OOO00OO0O0O0O00O0 =='pim':#line:1015
                        OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=O0O0OO00OO0000OO0 )#line:1016
                    if not (OO0OOOO0OOOO0O0O0 ):#line:1017
                        print (f"...optimization : SUCC:  pim is {O0O0OO00OO0000OO0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:1018
                    if OOO00OO0O0O0O00O0 =='aad':#line:1020
                        if (OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 )*(OOOO0O0OOOOOO00O0 +O0O0OOO0OOO0OO00O )>0 :#line:1021
                            OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=OOOO0O0OOOOOO00O0 *(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 +O0O0OOO0OOO0OO00O +O0O000O0000O0OO00 )/(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 )/(OOOO0O0OOOOOO00O0 +O0O0OOO0OOO0OO00O )-1 )#line:1022
                        else :#line:1023
                            OO0OOOO0OOOO0O0O0 =False #line:1024
                        if not (OO0OOOO0OOOO0O0O0 ):#line:1025
                            OOOOO0O0O000OO0O0 =OOOO0O0OOOOOO00O0 *(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 +O0O0OOO0OOO0OO00O +O0O000O0000O0OO00 )/(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 )/(OOOO0O0OOOOOO00O0 +O0O0OOO0OOO0OO00O )-1 #line:1026
                            print (f"...optimization : SUCC:  aad is {OOOOO0O0O000OO0O0} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:1027
                    if OOO00OO0O0O0O00O0 =='bad':#line:1028
                        if (OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 )*(OOOO0O0OOOOOO00O0 +O0O0OOO0OOO0OO00O )>0 :#line:1029
                            OO0OOOO0OOOO0O0O0 =OO0OOOO0OOOO0O0O0 and (OO0OO00000O00OOOO .quantifiers .get (OOO00OO0O0O0O00O0 )<=1 -OOOO0O0OOOOOO00O0 *(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 +O0O0OOO0OOO0OO00O +O0O000O0000O0OO00 )/(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 )/(OOOO0O0OOOOOO00O0 +O0O0OOO0OOO0OO00O ))#line:1030
                        else :#line:1031
                            OO0OOOO0OOOO0O0O0 =False #line:1032
                        if not (OO0OOOO0OOOO0O0O0 ):#line:1033
                            O00OO0OOOOO0OO000 =1 -OOOO0O0OOOOOO00O0 *(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 +O0O0OOO0OOO0OO00O +O0O000O0000O0OO00 )/(OOOO0O0OOOOOO00O0 +OOOOOOOO000O0OOO0 )/(OOOO0O0OOOOOO00O0 +O0O0OOO0OOO0OO00O )#line:1034
                            print (f"...optimization : SUCC:  bad is {O00OO0OOOOO0OO000} for {OO0O0OO0OOOOOOO00['generated_string']}")#line:1035
                OOO0OOOO0O00000OO =not (OO0OOOO0OOOO0O0O0 )#line:1036
        if (OOO0OOOO0O00000OO ):#line:1037
            print (f"... OPTIMALIZATION - SKIPPING BRANCH at cedent {OO0O0OO0OOOOOOO00['cedent_type']}")#line:1038
        return OOO0OOOO0O00000OO #line:1039
    def _print (O000O0OO00OO0O000 ,OO0OO0O000O000O00 ,_OOO000OOO00O0OO0O ,_O0OOOOOO000O0OO0O ):#line:1042
        if (len (_OOO000OOO00O0OO0O ))!=len (_O0OOOOOO000O0OO0O ):#line:1043
            print ("DIFF IN LEN for following cedent : "+str (len (_OOO000OOO00O0OO0O ))+" vs "+str (len (_O0OOOOOO000O0OO0O )))#line:1044
            print ("trace cedent : "+str (_OOO000OOO00O0OO0O )+", traces "+str (_O0OOOOOO000O0OO0O ))#line:1045
        O0OO0O0O0O00000O0 =''#line:1046
        OOO00000O000O00OO ={}#line:1047
        OO00OOOO00OOO0000 =[]#line:1048
        for OOO0OOOOOOOO00O0O in range (len (_OOO000OOO00O0OO0O )):#line:1049
            O0O00OOOO0OO000OO =O000O0OO00OO0O000 .data ["varname"].index (OO0OO0O000O000O00 ['defi'].get ('attributes')[_OOO000OOO00O0OO0O [OOO0OOOOOOOO00O0O ]].get ('name'))#line:1050
            O0OO0O0O0O00000O0 =O0OO0O0O0O00000O0 +O000O0OO00OO0O000 .data ["varname"][O0O00OOOO0OO000OO ]+'('#line:1052
            OO00OOOO00OOO0000 .append (O0O00OOOO0OO000OO )#line:1053
            O0OOOOOOO000OO00O =[]#line:1054
            for O00OO0O0O0O00000O in _O0OOOOOO000O0OO0O [OOO0OOOOOOOO00O0O ]:#line:1055
                O0OO0O0O0O00000O0 =O0OO0O0O0O00000O0 +str (O000O0OO00OO0O000 .data ["catnames"][O0O00OOOO0OO000OO ][O00OO0O0O0O00000O ])+" "#line:1056
                O0OOOOOOO000OO00O .append (str (O000O0OO00OO0O000 .data ["catnames"][O0O00OOOO0OO000OO ][O00OO0O0O0O00000O ]))#line:1057
            O0OO0O0O0O00000O0 =O0OO0O0O0O00000O0 [:-1 ]+')'#line:1058
            OOO00000O000O00OO [O000O0OO00OO0O000 .data ["varname"][O0O00OOOO0OO000OO ]]=O0OOOOOOO000OO00O #line:1059
            if OOO0OOOOOOOO00O0O +1 <len (_OOO000OOO00O0OO0O ):#line:1060
                O0OO0O0O0O00000O0 =O0OO0O0O0O00000O0 +' & '#line:1061
        return O0OO0O0O0O00000O0 ,OOO00000O000O00OO ,OO00OOOO00OOO0000 #line:1065
    def _print_hypo (OOO0O0O0O00000OO0 ,OOOO0OOOO000O0O00 ):#line:1067
        OOO0O0O0O00000OO0 .print_rule (OOOO0OOOO000O0O00 )#line:1068
    def _print_rule (O0O000OOO00O0OO0O ,O000000O0OOO00OOO ):#line:1070
        if O0O000OOO00O0OO0O .verbosity ['print_rules']:#line:1071
            print ('Rules info : '+str (O000000O0OOO00OOO ['params']))#line:1072
            for O0OO0OO00000O0OO0 in O0O000OOO00O0OO0O .task_actinfo ['cedents']:#line:1073
                print (O0OO0OO00000O0OO0 ['cedent_type']+' = '+O0OO0OO00000O0OO0 ['generated_string'])#line:1074
    def _genvar (O0OOOOO0OO0000O0O ,O00O00O0OOO00O000 ,OO0O0O0OOO0OOOOO0 ,_O00OO000000OOO0OO ,_O00OO0O00O00O0OO0 ,_OO000O0OOO00OO0O0 ,_OO0OOO0OO0OO0O000 ,_OOO0O0OOOOOOOOO0O ,_OO0OOO0O0O000O00O ,_OO00OO00O0O0OO000 ):#line:1076
        _O00OOO00000O00O0O =0 #line:1077
        if OO0O0O0OOO0OOOOO0 ['num_cedent']>0 :#line:1078
            _O00OOO00000O00O0O =(_OO00OO00O0O0OO000 -_OO0OOO0O0O000O00O )/OO0O0O0OOO0OOOOO0 ['num_cedent']#line:1079
        for O00O0O000000OOO00 in range (OO0O0O0OOO0OOOOO0 ['num_cedent']):#line:1080
            if len (_O00OO000000OOO0OO )==0 or O00O0O000000OOO00 >_O00OO000000OOO0OO [-1 ]:#line:1081
                _O00OO000000OOO0OO .append (O00O0O000000OOO00 )#line:1082
                OOO0O00OO0O000000 =O0OOOOO0OO0000O0O .data ["varname"].index (OO0O0O0OOO0OOOOO0 ['defi'].get ('attributes')[O00O0O000000OOO00 ].get ('name'))#line:1083
                _OOOO0OOOO0OO00O00 =OO0O0O0OOO0OOOOO0 ['defi'].get ('attributes')[O00O0O000000OOO00 ].get ('minlen')#line:1084
                _O00O000O0OOO0O0OO =OO0O0O0OOO0OOOOO0 ['defi'].get ('attributes')[O00O0O000000OOO00 ].get ('maxlen')#line:1085
                _O000O0OO00OO0OOO0 =OO0O0O0OOO0OOOOO0 ['defi'].get ('attributes')[O00O0O000000OOO00 ].get ('type')#line:1086
                O00OOOO0OOO0O0000 =len (O0OOOOO0OO0000O0O .data ["dm"][OOO0O00OO0O000000 ])#line:1087
                _OOO000O0O000O0OOO =[]#line:1088
                _O00OO0O00O00O0OO0 .append (_OOO000O0O000O0OOO )#line:1089
                _OOO0O0O0OOO0O00O0 =int (0 )#line:1090
                O0OOOOO0OO0000O0O ._gencomb (O00O00O0OOO00O000 ,OO0O0O0OOO0OOOOO0 ,_O00OO000000OOO0OO ,_O00OO0O00O00O0OO0 ,_OOO000O0O000O0OOO ,_OO000O0OOO00OO0O0 ,_OOO0O0O0OOO0O00O0 ,O00OOOO0OOO0O0000 ,_O000O0OO00OO0OOO0 ,_OO0OOO0OO0OO0O000 ,_OOO0O0OOOOOOOOO0O ,_OOOO0OOOO0OO00O00 ,_O00O000O0OOO0O0OO ,_OO0OOO0O0O000O00O +O00O0O000000OOO00 *_O00OOO00000O00O0O ,_OO0OOO0O0O000O00O +(O00O0O000000OOO00 +1 )*_O00OOO00000O00O0O )#line:1091
                _O00OO0O00O00O0OO0 .pop ()#line:1092
                _O00OO000000OOO0OO .pop ()#line:1093
    def _gencomb (OO00O0OOO0O0O00OO ,OOOO00O0O00O00O0O ,OO0OO00O0OOOO0OO0 ,_O0OO000OO0OO00OO0 ,_O000O000O00O000OO ,_OOO0O00O0OOO00OOO ,_O0000OOOOO000O000 ,_OOO0000O0O0O00OO0 ,OOOO00OO00O0O0O00 ,_O00000O0000O0O00O ,_OO0OO0000O000O0OO ,_O0O0O0OO00OO00O0O ,_O0OOO00O00O0O000O ,_O0OOO00O0O00O0OO0 ,_OOOOOOOO0O0OOO000 ,_O000O00OO00000O00 ):#line:1095
        _OOOO00OO00O0O0000 =[]#line:1096
        if _O00000O0000O0O00O =="subset":#line:1097
            if len (_OOO0O00O0OOO00OOO )==0 :#line:1098
                _OOOO00OO00O0O0000 =range (OOOO00OO00O0O0O00 )#line:1099
            else :#line:1100
                _OOOO00OO00O0O0000 =range (_OOO0O00O0OOO00OOO [-1 ]+1 ,OOOO00OO00O0O0O00 )#line:1101
        elif _O00000O0000O0O00O =="seq":#line:1102
            if len (_OOO0O00O0OOO00OOO )==0 :#line:1103
                _OOOO00OO00O0O0000 =range (OOOO00OO00O0O0O00 -_O0OOO00O00O0O000O +1 )#line:1104
            else :#line:1105
                if _OOO0O00O0OOO00OOO [-1 ]+1 ==OOOO00OO00O0O0O00 :#line:1106
                    return #line:1107
                O00O000O00O000000 =_OOO0O00O0OOO00OOO [-1 ]+1 #line:1108
                _OOOO00OO00O0O0000 .append (O00O000O00O000000 )#line:1109
        elif _O00000O0000O0O00O =="lcut":#line:1110
            if len (_OOO0O00O0OOO00OOO )==0 :#line:1111
                O00O000O00O000000 =0 ;#line:1112
            else :#line:1113
                if _OOO0O00O0OOO00OOO [-1 ]+1 ==OOOO00OO00O0O0O00 :#line:1114
                    return #line:1115
                O00O000O00O000000 =_OOO0O00O0OOO00OOO [-1 ]+1 #line:1116
            _OOOO00OO00O0O0000 .append (O00O000O00O000000 )#line:1117
        elif _O00000O0000O0O00O =="rcut":#line:1118
            if len (_OOO0O00O0OOO00OOO )==0 :#line:1119
                O00O000O00O000000 =OOOO00OO00O0O0O00 -1 ;#line:1120
            else :#line:1121
                if _OOO0O00O0OOO00OOO [-1 ]==0 :#line:1122
                    return #line:1123
                O00O000O00O000000 =_OOO0O00O0OOO00OOO [-1 ]-1 #line:1124
            _OOOO00OO00O0O0000 .append (O00O000O00O000000 )#line:1126
        elif _O00000O0000O0O00O =="one":#line:1127
            if len (_OOO0O00O0OOO00OOO )==0 :#line:1128
                O000O0OOO0OOOOOOO =OO00O0OOO0O0O00OO .data ["varname"].index (OO0OO00O0OOOO0OO0 ['defi'].get ('attributes')[_O0OO000OO0OO00OO0 [-1 ]].get ('name'))#line:1129
                try :#line:1130
                    O00O000O00O000000 =OO00O0OOO0O0O00OO .data ["catnames"][O000O0OOO0OOOOOOO ].index (OO0OO00O0OOOO0OO0 ['defi'].get ('attributes')[_O0OO000OO0OO00OO0 [-1 ]].get ('value'))#line:1131
                except :#line:1132
                    print (f"ERROR: attribute '{OO0OO00O0OOOO0OO0['defi'].get('attributes')[_O0OO000OO0OO00OO0[-1]].get('name')}' has not value '{OO0OO00O0OOOO0OO0['defi'].get('attributes')[_O0OO000OO0OO00OO0[-1]].get('value')}'")#line:1133
                    exit (1 )#line:1134
                _OOOO00OO00O0O0000 .append (O00O000O00O000000 )#line:1135
                _O0OOO00O00O0O000O =1 #line:1136
                _O0OOO00O0O00O0OO0 =1 #line:1137
            else :#line:1138
                print ("DEBUG: one category should not have more categories")#line:1139
                return #line:1140
        else :#line:1141
            print ("Attribute type "+_O00000O0000O0O00O +" not supported.")#line:1142
            return #line:1143
        if len (_OOOO00OO00O0O0000 )>0 :#line:1145
            _OOO0OO0OO0OOOO000 =(_O000O00OO00000O00 -_OOOOOOOO0O0OOO000 )/len (_OOOO00OO00O0O0000 )#line:1146
        else :#line:1147
            _OOO0OO0OO0OOOO000 =0 #line:1148
        _OOO00O0OOO000O0OO =0 #line:1150
        for O00OOO000OOO00O0O in _OOOO00OO00O0O0000 :#line:1152
                _OOO0O00O0OOO00OOO .append (O00OOO000OOO00O0O )#line:1154
                _O000O000O00O000OO .pop ()#line:1155
                _O000O000O00O000OO .append (_OOO0O00O0OOO00OOO )#line:1156
                _O0O0OOO0OOO0OOO00 =_OOO0000O0O0O00OO0 |OO00O0OOO0O0O00OO .data ["dm"][OO00O0OOO0O0O00OO .data ["varname"].index (OO0OO00O0OOOO0OO0 ['defi'].get ('attributes')[_O0OO000OO0OO00OO0 [-1 ]].get ('name'))][O00OOO000OOO00O0O ]#line:1160
                _O0O000O00O000O000 =1 #line:1162
                if (len (_O0OO000OO0OO00OO0 )<_OO0OO0000O000O0OO ):#line:1163
                    _O0O000O00O000O000 =-1 #line:1164
                if (len (_O000O000O00O000OO [-1 ])<_O0OOO00O00O0O000O ):#line:1166
                    _O0O000O00O000O000 =0 #line:1167
                _O000O0O0O000O00OO =0 #line:1169
                if OO0OO00O0OOOO0OO0 ['defi'].get ('type')=='con':#line:1170
                    _O000O0O0O000O00OO =_O0000OOOOO000O000 &_O0O0OOO0OOO0OOO00 #line:1171
                else :#line:1172
                    _O000O0O0O000O00OO =_O0000OOOOO000O000 |_O0O0OOO0OOO0OOO00 #line:1173
                OO0OO00O0OOOO0OO0 ['trace_cedent']=_O0OO000OO0OO00OO0 #line:1174
                OO0OO00O0OOOO0OO0 ['traces']=_O000O000O00O000OO #line:1175
                O00OOOO00000O0OOO ,OO0O0OO00O00O00O0 ,OOOOO0OOO00OOOO00 =OO00O0OOO0O0O00OO ._print (OO0OO00O0OOOO0OO0 ,_O0OO000OO0OO00OO0 ,_O000O000O00O000OO )#line:1176
                OO0OO00O0OOOO0OO0 ['generated_string']=O00OOOO00000O0OOO #line:1177
                OO0OO00O0OOOO0OO0 ['rule']=OO0O0OO00O00O00O0 #line:1178
                OO0OO00O0OOOO0OO0 ['filter_value']=_O000O0O0O000O00OO #line:1179
                OO0OO00O0OOOO0OO0 ['traces']=copy .deepcopy (_O000O000O00O000OO )#line:1180
                OO0OO00O0OOOO0OO0 ['trace_cedent']=copy .deepcopy (_O0OO000OO0OO00OO0 )#line:1181
                OO0OO00O0OOOO0OO0 ['trace_cedent_asindata']=copy .deepcopy (OOOOO0OOO00OOOO00 )#line:1182
                OOOO00O0O00O00O0O ['cedents'].append (OO0OO00O0OOOO0OO0 )#line:1184
                O00OOO00O00000OOO =OO00O0OOO0O0O00OO ._verify_opt (OOOO00O0O00O00O0O ,OO0OO00O0OOOO0OO0 )#line:1185
                if not (O00OOO00O00000OOO ):#line:1191
                    if _O0O000O00O000O000 ==1 :#line:1192
                        if len (OOOO00O0O00O00O0O ['cedents_to_do'])==len (OOOO00O0O00O00O0O ['cedents']):#line:1194
                            if OO00O0OOO0O0O00OO .proc =='CFMiner':#line:1195
                                OOO00O0O000OO0OO0 ,O0O0O0OO000O0000O =OO00O0OOO0O0O00OO ._verifyCF (_O000O0O0O000O00OO )#line:1196
                            elif OO00O0OOO0O0O00OO .proc =='UICMiner':#line:1197
                                OOO00O0O000OO0OO0 ,O0O0O0OO000O0000O =OO00O0OOO0O0O00OO ._verifyUIC (_O000O0O0O000O00OO )#line:1198
                            elif OO00O0OOO0O0O00OO .proc =='4ftMiner':#line:1199
                                OOO00O0O000OO0OO0 ,O0O0O0OO000O0000O =OO00O0OOO0O0O00OO ._verify4ft (_O0O0OOO0OOO0OOO00 )#line:1200
                            elif OO00O0OOO0O0O00OO .proc =='SD4ftMiner':#line:1201
                                OOO00O0O000OO0OO0 ,O0O0O0OO000O0000O =OO00O0OOO0O0O00OO ._verifysd4ft (_O0O0OOO0OOO0OOO00 )#line:1202
                            elif OO00O0OOO0O0O00OO .proc =='NewAct4ftMiner':#line:1203
                                OOO00O0O000OO0OO0 ,O0O0O0OO000O0000O =OO00O0OOO0O0O00OO ._verifynewact4ft (_O0O0OOO0OOO0OOO00 )#line:1204
                            elif OO00O0OOO0O0O00OO .proc =='Act4ftMiner':#line:1205
                                OOO00O0O000OO0OO0 ,O0O0O0OO000O0000O =OO00O0OOO0O0O00OO ._verifyact4ft (_O0O0OOO0OOO0OOO00 )#line:1206
                            else :#line:1207
                                print ("Unsupported procedure : "+OO00O0OOO0O0O00OO .proc )#line:1208
                                exit (0 )#line:1209
                            if OOO00O0O000OO0OO0 ==True :#line:1210
                                O00O0O00O0O00OOO0 ={}#line:1211
                                O00O0O00O0O00OOO0 ["rule_id"]=OO00O0OOO0O0O00OO .stats ['total_valid']#line:1212
                                O00O0O00O0O00OOO0 ["cedents_str"]={}#line:1213
                                O00O0O00O0O00OOO0 ["cedents_struct"]={}#line:1214
                                O00O0O00O0O00OOO0 ['traces']={}#line:1215
                                O00O0O00O0O00OOO0 ['trace_cedent_taskorder']={}#line:1216
                                O00O0O00O0O00OOO0 ['trace_cedent_dataorder']={}#line:1217
                                for O0O0O0OOOO00O00O0 in OOOO00O0O00O00O0O ['cedents']:#line:1218
                                    O00O0O00O0O00OOO0 ['cedents_str'][O0O0O0OOOO00O00O0 ['cedent_type']]=O0O0O0OOOO00O00O0 ['generated_string']#line:1220
                                    O00O0O00O0O00OOO0 ['cedents_struct'][O0O0O0OOOO00O00O0 ['cedent_type']]=O0O0O0OOOO00O00O0 ['rule']#line:1221
                                    O00O0O00O0O00OOO0 ['traces'][O0O0O0OOOO00O00O0 ['cedent_type']]=O0O0O0OOOO00O00O0 ['traces']#line:1222
                                    O00O0O00O0O00OOO0 ['trace_cedent_taskorder'][O0O0O0OOOO00O00O0 ['cedent_type']]=O0O0O0OOOO00O00O0 ['trace_cedent']#line:1223
                                    O00O0O00O0O00OOO0 ['trace_cedent_dataorder'][O0O0O0OOOO00O00O0 ['cedent_type']]=O0O0O0OOOO00O00O0 ['trace_cedent_asindata']#line:1224
                                O00O0O00O0O00OOO0 ["params"]=O0O0O0OO000O0000O #line:1226
                                OO00O0OOO0O0O00OO ._print_rule (O00O0O00O0O00OOO0 )#line:1228
                                OO00O0OOO0O0O00OO .rulelist .append (O00O0O00O0O00OOO0 )#line:1234
                            OO00O0OOO0O0O00OO .stats ['total_cnt']+=1 #line:1236
                            OO00O0OOO0O0O00OO .stats ['total_ver']+=1 #line:1237
                    if _O0O000O00O000O000 >=0 :#line:1238
                        if len (OOOO00O0O00O00O0O ['cedents_to_do'])>len (OOOO00O0O00O00O0O ['cedents']):#line:1239
                            OO00O0OOO0O0O00OO ._start_cedent (OOOO00O0O00O00O0O ,_OOOOOOOO0O0OOO000 +_OOO00O0OOO000O0OO *_OOO0OO0OO0OOOO000 ,_OOOOOOOO0O0OOO000 +(_OOO00O0OOO000O0OO +0.33 )*_OOO0OO0OO0OOOO000 )#line:1240
                    OOOO00O0O00O00O0O ['cedents'].pop ()#line:1241
                    if (len (_O0OO000OO0OO00OO0 )<_O0O0O0OO00OO00O0O ):#line:1242
                        OO00O0OOO0O0O00OO ._genvar (OOOO00O0O00O00O0O ,OO0OO00O0OOOO0OO0 ,_O0OO000OO0OO00OO0 ,_O000O000O00O000OO ,_O000O0O0O000O00OO ,_OO0OO0000O000O0OO ,_O0O0O0OO00OO00O0O ,_OOOOOOOO0O0OOO000 +(_OOO00O0OOO000O0OO +0.33 )*_OOO0OO0OO0OOOO000 ,_OOOOOOOO0O0OOO000 +(_OOO00O0OOO000O0OO +0.66 )*_OOO0OO0OO0OOOO000 )#line:1243
                else :#line:1244
                    OOOO00O0O00O00O0O ['cedents'].pop ()#line:1245
                if len (_OOO0O00O0OOO00OOO )<_O0OOO00O0O00O0OO0 :#line:1246
                    OO00O0OOO0O0O00OO ._gencomb (OOOO00O0O00O00O0O ,OO0OO00O0OOOO0OO0 ,_O0OO000OO0OO00OO0 ,_O000O000O00O000OO ,_OOO0O00O0OOO00OOO ,_O0000OOOOO000O000 ,_O0O0OOO0OOO0OOO00 ,OOOO00OO00O0O0O00 ,_O00000O0000O0O00O ,_OO0OO0000O000O0OO ,_O0O0O0OO00OO00O0O ,_O0OOO00O00O0O000O ,_O0OOO00O0O00O0OO0 ,_OOOOOOOO0O0OOO000 +_OOO0OO0OO0OOOO000 *(_OOO00O0OOO000O0OO +0.66 ),_OOOOOOOO0O0OOO000 +_OOO0OO0OO0OOOO000 *(_OOO00O0OOO000O0OO +1 ))#line:1247
                _OOO0O00O0OOO00OOO .pop ()#line:1248
                _OOO00O0OOO000O0OO +=1 #line:1249
                if OO00O0OOO0O0O00OO .options ['progressbar']:#line:1250
                    OO00O0OOO0O0O00OO .bar .update (min (100 ,_OOOOOOOO0O0OOO000 +_OOO0OO0OO0OOOO000 *_OOO00O0OOO000O0OO ))#line:1251
    def _start_cedent (OOOOOO00OOOOOO0O0 ,O00OOO0OO00O0OO00 ,_O000O0O0000000O0O ,_OO00OO00OOO0O000O ):#line:1254
        if len (O00OOO0OO00O0OO00 ['cedents_to_do'])>len (O00OOO0OO00O0OO00 ['cedents']):#line:1255
            _O00O0OO0000O0O000 =[]#line:1256
            _O0OO000OO00O0000O =[]#line:1257
            OOOOO00OO0OOOOOO0 ={}#line:1258
            OOOOO00OO0OOOOOO0 ['cedent_type']=O00OOO0OO00O0OO00 ['cedents_to_do'][len (O00OOO0OO00O0OO00 ['cedents'])]#line:1259
            O00O0OOOO000OOOOO =OOOOO00OO0OOOOOO0 ['cedent_type']#line:1260
            if ((O00O0OOOO000OOOOO [-1 ]=='-')|(O00O0OOOO000OOOOO [-1 ]=='+')):#line:1261
                O00O0OOOO000OOOOO =O00O0OOOO000OOOOO [:-1 ]#line:1262
            OOOOO00OO0OOOOOO0 ['defi']=OOOOOO00OOOOOO0O0 .kwargs .get (O00O0OOOO000OOOOO )#line:1264
            if (OOOOO00OO0OOOOOO0 ['defi']==None ):#line:1265
                print ("Error getting cedent ",OOOOO00OO0OOOOOO0 ['cedent_type'])#line:1266
            _O0O0OOO0OOOOOOO00 =int (0 )#line:1267
            OOOOO00OO0OOOOOO0 ['num_cedent']=len (OOOOO00OO0OOOOOO0 ['defi'].get ('attributes'))#line:1274
            if (OOOOO00OO0OOOOOO0 ['defi'].get ('type')=='con'):#line:1275
                _O0O0OOO0OOOOOOO00 =(1 <<OOOOOO00OOOOOO0O0 .data ["rows_count"])-1 #line:1276
            OOOOOO00OOOOOO0O0 ._genvar (O00OOO0OO00O0OO00 ,OOOOO00OO0OOOOOO0 ,_O00O0OO0000O0O000 ,_O0OO000OO00O0000O ,_O0O0OOO0OOOOOOO00 ,OOOOO00OO0OOOOOO0 ['defi'].get ('minlen'),OOOOO00OO0OOOOOO0 ['defi'].get ('maxlen'),_O000O0O0000000O0O ,_OO00OO00OOO0O000O )#line:1277
    def _calc_all (OOO0OO000OOOO0000 ,**O000OO0000OOOOO0O ):#line:1280
        if "df"in O000OO0000OOOOO0O :#line:1281
            OOO0OO000OOOO0000 ._prep_data (OOO0OO000OOOO0000 .kwargs .get ("df"))#line:1282
        if not (OOO0OO000OOOO0000 ._initialized ):#line:1283
            print ("ERROR: dataframe is missing and not initialized with dataframe")#line:1284
        else :#line:1285
            OOO0OO000OOOO0000 ._calculate (**O000OO0000OOOOO0O )#line:1286
    def _check_cedents (OO0OO0OOO00OOOOOO ,O00OO0000000OO0OO ,**OO0O0000O000000OO ):#line:1288
        O0O0OOOOO0O00OO0O =True #line:1289
        if (OO0O0000O000000OO .get ('quantifiers',None )==None ):#line:1290
            print (f"Error: missing quantifiers.")#line:1291
            O0O0OOOOO0O00OO0O =False #line:1292
            return O0O0OOOOO0O00OO0O #line:1293
        if (type (OO0O0000O000000OO .get ('quantifiers'))!=dict ):#line:1294
            print (f"Error: quantifiers are not dictionary type.")#line:1295
            O0O0OOOOO0O00OO0O =False #line:1296
            return O0O0OOOOO0O00OO0O #line:1297
        for O00O00OO0O0000000 in O00OO0000000OO0OO :#line:1299
            if (OO0O0000O000000OO .get (O00O00OO0O0000000 ,None )==None ):#line:1300
                print (f"Error: cedent {O00O00OO0O0000000} is missing in parameters.")#line:1301
                O0O0OOOOO0O00OO0O =False #line:1302
                return O0O0OOOOO0O00OO0O #line:1303
            O0O00OO00O0OOOO00 =OO0O0000O000000OO .get (O00O00OO0O0000000 )#line:1304
            if (O0O00OO00O0OOOO00 .get ('minlen'),None )==None :#line:1305
                print (f"Error: cedent {O00O00OO0O0000000} has no minimal length specified.")#line:1306
                O0O0OOOOO0O00OO0O =False #line:1307
                return O0O0OOOOO0O00OO0O #line:1308
            if not (type (O0O00OO00O0OOOO00 .get ('minlen'))is int ):#line:1309
                print (f"Error: cedent {O00O00OO0O0000000} has invalid type of minimal length ({type(O0O00OO00O0OOOO00.get('minlen'))}).")#line:1310
                O0O0OOOOO0O00OO0O =False #line:1311
                return O0O0OOOOO0O00OO0O #line:1312
            if (O0O00OO00O0OOOO00 .get ('maxlen'),None )==None :#line:1313
                print (f"Error: cedent {O00O00OO0O0000000} has no maximal length specified.")#line:1314
                O0O0OOOOO0O00OO0O =False #line:1315
                return O0O0OOOOO0O00OO0O #line:1316
            if not (type (O0O00OO00O0OOOO00 .get ('maxlen'))is int ):#line:1317
                print (f"Error: cedent {O00O00OO0O0000000} has invalid type of maximal length.")#line:1318
                O0O0OOOOO0O00OO0O =False #line:1319
                return O0O0OOOOO0O00OO0O #line:1320
            if (O0O00OO00O0OOOO00 .get ('type'),None )==None :#line:1321
                print (f"Error: cedent {O00O00OO0O0000000} has no type specified.")#line:1322
                O0O0OOOOO0O00OO0O =False #line:1323
                return O0O0OOOOO0O00OO0O #line:1324
            if not ((O0O00OO00O0OOOO00 .get ('type'))in (['con','dis'])):#line:1325
                print (f"Error: cedent {O00O00OO0O0000000} has invalid type. Allowed values are 'con' and 'dis'.")#line:1326
                O0O0OOOOO0O00OO0O =False #line:1327
                return O0O0OOOOO0O00OO0O #line:1328
            if (O0O00OO00O0OOOO00 .get ('attributes'),None )==None :#line:1329
                print (f"Error: cedent {O00O00OO0O0000000} has no attributes specified.")#line:1330
                O0O0OOOOO0O00OO0O =False #line:1331
                return O0O0OOOOO0O00OO0O #line:1332
            for O0O00OOOOO000O0OO in O0O00OO00O0OOOO00 .get ('attributes'):#line:1333
                if (O0O00OOOOO000O0OO .get ('name'),None )==None :#line:1334
                    print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO} has no 'name' attribute specified.")#line:1335
                    O0O0OOOOO0O00OO0O =False #line:1336
                    return O0O0OOOOO0O00OO0O #line:1337
                if not ((O0O00OOOOO000O0OO .get ('name'))in OO0OO0OOO00OOOOOO .data ["varname"]):#line:1338
                    print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} not in variable list. Please check spelling.")#line:1339
                    O0O0OOOOO0O00OO0O =False #line:1340
                    return O0O0OOOOO0O00OO0O #line:1341
                if (O0O00OOOOO000O0OO .get ('type'),None )==None :#line:1342
                    print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} has no 'type' attribute specified.")#line:1343
                    O0O0OOOOO0O00OO0O =False #line:1344
                    return O0O0OOOOO0O00OO0O #line:1345
                if not ((O0O00OOOOO000O0OO .get ('type'))in (['rcut','lcut','seq','subset','one'])):#line:1346
                    print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} has unsupported type {O0O00OOOOO000O0OO.get('type')}. Supported types are 'subset','seq','lcut','rcut','one'.")#line:1347
                    O0O0OOOOO0O00OO0O =False #line:1348
                    return O0O0OOOOO0O00OO0O #line:1349
                if (O0O00OOOOO000O0OO .get ('minlen'),None )==None :#line:1350
                    print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} has no minimal length specified.")#line:1351
                    O0O0OOOOO0O00OO0O =False #line:1352
                    return O0O0OOOOO0O00OO0O #line:1353
                if not (type (O0O00OOOOO000O0OO .get ('minlen'))is int ):#line:1354
                    if not (O0O00OOOOO000O0OO .get ('type')=='one'):#line:1355
                        print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} has invalid type of minimal length.")#line:1356
                        O0O0OOOOO0O00OO0O =False #line:1357
                        return O0O0OOOOO0O00OO0O #line:1358
                if (O0O00OOOOO000O0OO .get ('maxlen'),None )==None :#line:1359
                    print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} has no maximal length specified.")#line:1360
                    O0O0OOOOO0O00OO0O =False #line:1361
                    return O0O0OOOOO0O00OO0O #line:1362
                if not (type (O0O00OOOOO000O0OO .get ('maxlen'))is int ):#line:1363
                    if not (O0O00OOOOO000O0OO .get ('type')=='one'):#line:1364
                        print (f"Error: cedent {O00O00OO0O0000000} / attribute {O0O00OOOOO000O0OO.get('name')} has invalid type of maximal length.")#line:1365
                        O0O0OOOOO0O00OO0O =False #line:1366
                        return O0O0OOOOO0O00OO0O #line:1367
        return O0O0OOOOO0O00OO0O #line:1368
    def _calculate (OOOO0000O0O00O0OO ,**OOO0O000O00OOOOOO ):#line:1370
        if OOOO0000O0O00O0OO .data ["data_prepared"]==0 :#line:1371
            print ("Error: data not prepared")#line:1372
            return #line:1373
        OOOO0000O0O00O0OO .kwargs =OOO0O000O00OOOOOO #line:1374
        OOOO0000O0O00O0OO .proc =OOO0O000O00OOOOOO .get ('proc')#line:1375
        OOOO0000O0O00O0OO .quantifiers =OOO0O000O00OOOOOO .get ('quantifiers')#line:1376
        OOOO0000O0O00O0OO ._init_task ()#line:1378
        OOOO0000O0O00O0OO .stats ['start_proc_time']=time .time ()#line:1379
        OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do']=[]#line:1380
        OOOO0000O0O00O0OO .task_actinfo ['cedents']=[]#line:1381
        if OOO0O000O00OOOOOO .get ("proc")=='UICMiner':#line:1384
            if not (OOOO0000O0O00O0OO ._check_cedents (['ante'],**OOO0O000O00OOOOOO )):#line:1385
                return #line:1386
            _O0O00O00O0O00OOOO =OOO0O000O00OOOOOO .get ("cond")#line:1388
            if _O0O00O00O0O00OOOO !=None :#line:1389
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1390
            else :#line:1391
                O00O00O0OO0OO0O00 =OOOO0000O0O00O0OO .cedent #line:1392
                O00O00O0OO0OO0O00 ['cedent_type']='cond'#line:1393
                O00O00O0OO0OO0O00 ['filter_value']=(1 <<OOOO0000O0O00O0OO .data ["rows_count"])-1 #line:1394
                O00O00O0OO0OO0O00 ['generated_string']='---'#line:1395
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1397
                OOOO0000O0O00O0OO .task_actinfo ['cedents'].append (O00O00O0OO0OO0O00 )#line:1398
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1399
            if OOO0O000O00OOOOOO .get ('target',None )==None :#line:1400
                print ("ERROR: no succedent/target variable defined for UIC Miner")#line:1401
                return #line:1402
            if not (OOO0O000O00OOOOOO .get ('target')in OOOO0000O0O00O0OO .data ["varname"]):#line:1403
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1404
                return #line:1405
            if ("aad_score"in OOOO0000O0O00O0OO .quantifiers ):#line:1406
                if not ("aad_weights"in OOOO0000O0O00O0OO .quantifiers ):#line:1407
                    print ("ERROR: for aad quantifier you need to specify aad weights.")#line:1408
                    return #line:1409
                if not (len (OOOO0000O0O00O0OO .quantifiers .get ("aad_weights"))==len (OOOO0000O0O00O0OO .data ["dm"][OOOO0000O0O00O0OO .data ["varname"].index (OOOO0000O0O00O0OO .kwargs .get ('target'))])):#line:1410
                    print ("ERROR: aad weights has different number of weights than classes of target variable.")#line:1411
                    return #line:1412
        elif OOO0O000O00OOOOOO .get ("proc")=='CFMiner':#line:1413
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do']=['cond']#line:1414
            if OOO0O000O00OOOOOO .get ('target',None )==None :#line:1415
                print ("ERROR: no target variable defined for CF Miner")#line:1416
                return #line:1417
            if not (OOOO0000O0O00O0OO ._check_cedents (['cond'],**OOO0O000O00OOOOOO )):#line:1418
                return #line:1419
            if not (OOO0O000O00OOOOOO .get ('target')in OOOO0000O0O00O0OO .data ["varname"]):#line:1420
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1421
                return #line:1422
            if ("aad"in OOOO0000O0O00O0OO .quantifiers ):#line:1423
                if not ("aad_weights"in OOOO0000O0O00O0OO .quantifiers ):#line:1424
                    print ("ERROR: for aad quantifier you need to specify aad weights.")#line:1425
                    return #line:1426
                if not (len (OOOO0000O0O00O0OO .quantifiers .get ("aad_weights"))==len (OOOO0000O0O00O0OO .data ["dm"][OOOO0000O0O00O0OO .data ["varname"].index (OOOO0000O0O00O0OO .kwargs .get ('target'))])):#line:1427
                    print ("ERROR: aad weights has different number of weights than classes of target variable.")#line:1428
                    return #line:1429
        elif OOO0O000O00OOOOOO .get ("proc")=='4ftMiner':#line:1432
            if not (OOOO0000O0O00O0OO ._check_cedents (['ante','succ'],**OOO0O000O00OOOOOO )):#line:1433
                return #line:1434
            _O0O00O00O0O00OOOO =OOO0O000O00OOOOOO .get ("cond")#line:1436
            if _O0O00O00O0O00OOOO !=None :#line:1437
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1438
            else :#line:1439
                O00O00O0OO0OO0O00 =OOOO0000O0O00O0OO .cedent #line:1440
                O00O00O0OO0OO0O00 ['cedent_type']='cond'#line:1441
                O00O00O0OO0OO0O00 ['filter_value']=(1 <<OOOO0000O0O00O0OO .data ["rows_count"])-1 #line:1442
                O00O00O0OO0OO0O00 ['generated_string']='---'#line:1443
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1445
                OOOO0000O0O00O0OO .task_actinfo ['cedents'].append (O00O00O0OO0OO0O00 )#line:1446
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1450
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1451
        elif OOO0O000O00OOOOOO .get ("proc")=='NewAct4ftMiner':#line:1452
            _O0O00O00O0O00OOOO =OOO0O000O00OOOOOO .get ("cond")#line:1455
            if _O0O00O00O0O00OOOO !=None :#line:1456
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1457
            else :#line:1458
                O00O00O0OO0OO0O00 =OOOO0000O0O00O0OO .cedent #line:1459
                O00O00O0OO0OO0O00 ['cedent_type']='cond'#line:1460
                O00O00O0OO0OO0O00 ['filter_value']=(1 <<OOOO0000O0O00O0OO .data ["rows_count"])-1 #line:1461
                O00O00O0OO0OO0O00 ['generated_string']='---'#line:1462
                print (O00O00O0OO0OO0O00 ['filter_value'])#line:1463
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1464
                OOOO0000O0O00O0OO .task_actinfo ['cedents'].append (O00O00O0OO0OO0O00 )#line:1465
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('antv')#line:1466
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('sucv')#line:1467
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1468
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1469
        elif OOO0O000O00OOOOOO .get ("proc")=='Act4ftMiner':#line:1470
            _O0O00O00O0O00OOOO =OOO0O000O00OOOOOO .get ("cond")#line:1473
            if _O0O00O00O0O00OOOO !=None :#line:1474
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1475
            else :#line:1476
                O00O00O0OO0OO0O00 =OOOO0000O0O00O0OO .cedent #line:1477
                O00O00O0OO0OO0O00 ['cedent_type']='cond'#line:1478
                O00O00O0OO0OO0O00 ['filter_value']=(1 <<OOOO0000O0O00O0OO .data ["rows_count"])-1 #line:1479
                O00O00O0OO0OO0O00 ['generated_string']='---'#line:1480
                print (O00O00O0OO0OO0O00 ['filter_value'])#line:1481
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1482
                OOOO0000O0O00O0OO .task_actinfo ['cedents'].append (O00O00O0OO0OO0O00 )#line:1483
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('antv-')#line:1484
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('antv+')#line:1485
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('sucv-')#line:1486
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('sucv+')#line:1487
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1488
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1489
        elif OOO0O000O00OOOOOO .get ("proc")=='SD4ftMiner':#line:1490
            if not (OOOO0000O0O00O0OO ._check_cedents (['ante','succ','frst','scnd'],**OOO0O000O00OOOOOO )):#line:1493
                return #line:1494
            _O0O00O00O0O00OOOO =OOO0O000O00OOOOOO .get ("cond")#line:1495
            if _O0O00O00O0O00OOOO !=None :#line:1496
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1497
            else :#line:1498
                O00O00O0OO0OO0O00 =OOOO0000O0O00O0OO .cedent #line:1499
                O00O00O0OO0OO0O00 ['cedent_type']='cond'#line:1500
                O00O00O0OO0OO0O00 ['filter_value']=(1 <<OOOO0000O0O00O0OO .data ["rows_count"])-1 #line:1501
                O00O00O0OO0OO0O00 ['generated_string']='---'#line:1502
                OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1504
                OOOO0000O0O00O0OO .task_actinfo ['cedents'].append (O00O00O0OO0OO0O00 )#line:1505
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('frst')#line:1506
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('scnd')#line:1507
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1508
            OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1509
        else :#line:1510
            print ("Unsupported procedure")#line:1511
            return #line:1512
        print ("Will go for ",OOO0O000O00OOOOOO .get ("proc"))#line:1513
        OOOO0000O0O00O0OO .task_actinfo ['optim']={}#line:1516
        OOOO000O0OO0000OO =True #line:1517
        for O0OO000OOOOOO0000 in OOOO0000O0O00O0OO .task_actinfo ['cedents_to_do']:#line:1518
            try :#line:1519
                OOOOO0O0OOO0O0O00 =OOOO0000O0O00O0OO .kwargs .get (O0OO000OOOOOO0000 )#line:1520
                if OOOOO0O0OOO0O0O00 .get ('type')!='con':#line:1524
                    OOOO000O0OO0000OO =False #line:1525
            except :#line:1527
                OO0O0O0O00OO00O00 =1 <2 #line:1528
        if OOOO0000O0O00O0OO .options ['optimizations']==False :#line:1530
            OOOO000O0OO0000OO =False #line:1531
        OOOO00O00OOOOOOOO ={}#line:1532
        OOOO00O00OOOOOOOO ['only_con']=OOOO000O0OO0000OO #line:1533
        OOOO0000O0O00O0OO .task_actinfo ['optim']=OOOO00O00OOOOOOOO #line:1534
        print ("Starting to mine rules.")#line:1542
        sys .stdout .flush ()#line:1543
        time .sleep (0.01 )#line:1544
        if OOOO0000O0O00O0OO .options ['progressbar']:#line:1545
            OOO000000O000O0OO =[progressbar .Percentage (),progressbar .Bar (),progressbar .Timer ()]#line:1546
            OOOO0000O0O00O0OO .bar =progressbar .ProgressBar (widgets =OOO000000O000O0OO ,max_value =100 ,fd =sys .stdout ).start ()#line:1547
            OOOO0000O0O00O0OO .bar .update (0 )#line:1548
        OOOO0000O0O00O0OO .progress_lower =0 #line:1549
        OOOO0000O0O00O0OO .progress_upper =100 #line:1550
        OOOO0000O0O00O0OO ._start_cedent (OOOO0000O0O00O0OO .task_actinfo ,OOOO0000O0O00O0OO .progress_lower ,OOOO0000O0O00O0OO .progress_upper )#line:1551
        if OOOO0000O0O00O0OO .options ['progressbar']:#line:1552
            OOOO0000O0O00O0OO .bar .update (100 )#line:1553
            OOOO0000O0O00O0OO .bar .finish ()#line:1554
        OOOO0000O0O00O0OO .stats ['end_proc_time']=time .time ()#line:1556
        print ("Done. Total verifications : "+str (OOOO0000O0O00O0OO .stats ['total_cnt'])+", rules "+str (OOOO0000O0O00O0OO .stats ['total_valid'])+", times: prep "+"{:.2f}".format (OOOO0000O0O00O0OO .stats ['end_prep_time']-OOOO0000O0O00O0OO .stats ['start_prep_time'])+"sec, processing "+"{:.2f}".format (OOOO0000O0O00O0OO .stats ['end_proc_time']-OOOO0000O0O00O0OO .stats ['start_proc_time'])+"sec")#line:1560
        O00000O0OO0OOO00O ={}#line:1561
        OOO0OOOOO0OO0000O ={}#line:1562
        OOO0OOOOO0OO0000O ["task_type"]=OOO0O000O00OOOOOO .get ('proc')#line:1563
        OOO0OOOOO0OO0000O ["target"]=OOO0O000O00OOOOOO .get ('target')#line:1565
        OOO0OOOOO0OO0000O ["self.quantifiers"]=OOOO0000O0O00O0OO .quantifiers #line:1566
        if OOO0O000O00OOOOOO .get ('cond')!=None :#line:1568
            OOO0OOOOO0OO0000O ['cond']=OOO0O000O00OOOOOO .get ('cond')#line:1569
        if OOO0O000O00OOOOOO .get ('ante')!=None :#line:1570
            OOO0OOOOO0OO0000O ['ante']=OOO0O000O00OOOOOO .get ('ante')#line:1571
        if OOO0O000O00OOOOOO .get ('succ')!=None :#line:1572
            OOO0OOOOO0OO0000O ['succ']=OOO0O000O00OOOOOO .get ('succ')#line:1573
        if OOO0O000O00OOOOOO .get ('opts')!=None :#line:1574
            OOO0OOOOO0OO0000O ['opts']=OOO0O000O00OOOOOO .get ('opts')#line:1575
        O00000O0OO0OOO00O ["taskinfo"]=OOO0OOOOO0OO0000O #line:1576
        O00OO00000OO000O0 ={}#line:1577
        O00OO00000OO000O0 ["total_verifications"]=OOOO0000O0O00O0OO .stats ['total_cnt']#line:1578
        O00OO00000OO000O0 ["valid_rules"]=OOOO0000O0O00O0OO .stats ['total_valid']#line:1579
        O00OO00000OO000O0 ["total_verifications_with_opt"]=OOOO0000O0O00O0OO .stats ['total_ver']#line:1580
        O00OO00000OO000O0 ["time_prep"]=OOOO0000O0O00O0OO .stats ['end_prep_time']-OOOO0000O0O00O0OO .stats ['start_prep_time']#line:1581
        O00OO00000OO000O0 ["time_processing"]=OOOO0000O0O00O0OO .stats ['end_proc_time']-OOOO0000O0O00O0OO .stats ['start_proc_time']#line:1582
        O00OO00000OO000O0 ["time_total"]=OOOO0000O0O00O0OO .stats ['end_prep_time']-OOOO0000O0O00O0OO .stats ['start_prep_time']+OOOO0000O0O00O0OO .stats ['end_proc_time']-OOOO0000O0O00O0OO .stats ['start_proc_time']#line:1583
        O00000O0OO0OOO00O ["summary_statistics"]=O00OO00000OO000O0 #line:1584
        O00000O0OO0OOO00O ["rules"]=OOOO0000O0O00O0OO .rulelist #line:1585
        O000OOOO0O00O0OO0 ={}#line:1586
        O000OOOO0O00O0OO0 ["varname"]=OOOO0000O0O00O0OO .data ["varname"]#line:1587
        O000OOOO0O00O0OO0 ["catnames"]=OOOO0000O0O00O0OO .data ["catnames"]#line:1588
        O00000O0OO0OOO00O ["datalabels"]=O000OOOO0O00O0OO0 #line:1589
        OOOO0000O0O00O0OO .result =O00000O0OO0OOO00O #line:1592
    def print_summary (O00O000O0O00OO000 ):#line:1594
        print ("")#line:1595
        print ("CleverMiner task processing summary:")#line:1596
        print ("")#line:1597
        print (f"Task type : {O00O000O0O00OO000.result['taskinfo']['task_type']}")#line:1598
        print (f"Number of verifications : {O00O000O0O00OO000.result['summary_statistics']['total_verifications']}")#line:1599
        print (f"Number of rules : {O00O000O0O00OO000.result['summary_statistics']['valid_rules']}")#line:1600
        print (f"Total time needed : {strftime('%Hh %Mm %Ss', gmtime(O00O000O0O00OO000.result['summary_statistics']['time_total']))}")#line:1601
        print (f"Time of data preparation : {strftime('%Hh %Mm %Ss', gmtime(O00O000O0O00OO000.result['summary_statistics']['time_prep']))}")#line:1603
        print (f"Time of rule mining : {strftime('%Hh %Mm %Ss', gmtime(O00O000O0O00OO000.result['summary_statistics']['time_processing']))}")#line:1604
        print ("")#line:1605
    def print_hypolist (O00O000O00OO00O0O ):#line:1607
        O00O000O00OO00O0O .print_rulelist ();#line:1608
    def print_rulelist (O0O0OO0O0OO00OO00 ,sortby =None ,storesorted =False ):#line:1610
        def O000O0OO000O0000O (O00000OOOOO0OOOOO ):#line:1611
            O00O0OOOOOOO00O00 =O00000OOOOO0OOOOO ["params"]#line:1612
            return O00O0OOOOOOO00O00 .get (sortby ,0 )#line:1613
        print ("")#line:1615
        print ("List of rules:")#line:1616
        if O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="4ftMiner":#line:1617
            print ("RULEID BASE  CONF  AAD    Rule")#line:1618
        elif O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="UICMiner":#line:1619
            print ("RULEID BASE  AAD_SCORE  Rule")#line:1620
        elif O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="CFMiner":#line:1621
            print ("RULEID BASE  S_UP  S_DOWN Condition")#line:1622
        elif O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1623
            print ("RULEID BASE1 BASE2 RatioConf DeltaConf Rule")#line:1624
        else :#line:1625
            print ("Unsupported task type for rulelist")#line:1626
            return #line:1627
        OO0O0O00OO000OO00 =O0O0OO0O0OO00OO00 .result ["rules"]#line:1628
        if sortby is not None :#line:1629
            OO0O0O00OO000OO00 =sorted (OO0O0O00OO000OO00 ,key =O000O0OO000O0000O ,reverse =True )#line:1630
            if storesorted :#line:1631
                O0O0OO0O0OO00OO00 .result ["rules"]=OO0O0O00OO000OO00 #line:1632
        for OOO00O0OOO00000O0 in OO0O0O00OO000OO00 :#line:1634
            O0O0O0000O000O000 ="{:6d}".format (OOO00O0OOO00000O0 ["rule_id"])#line:1635
            if O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="4ftMiner":#line:1636
                O0O0O0000O000O000 =O0O0O0000O000O000 +" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["base"])+" "+"{:.3f}".format (OOO00O0OOO00000O0 ["params"]["conf"])+" "+"{:+.3f}".format (OOO00O0OOO00000O0 ["params"]["aad"])#line:1638
                O0O0O0000O000O000 =O0O0O0000O000O000 +" "+OOO00O0OOO00000O0 ["cedents_str"]["ante"]+" => "+OOO00O0OOO00000O0 ["cedents_str"]["succ"]+" | "+OOO00O0OOO00000O0 ["cedents_str"]["cond"]#line:1639
            elif O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="UICMiner":#line:1640
                O0O0O0000O000O000 =O0O0O0000O000O000 +" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["base"])+" "+"{:.3f}".format (OOO00O0OOO00000O0 ["params"]["aad_score"])#line:1641
                O0O0O0000O000O000 =O0O0O0000O000O000 +"     "+OOO00O0OOO00000O0 ["cedents_str"]["ante"]+" => "+O0O0OO0O0OO00OO00 .result ['taskinfo']['target']+"(*) | "+OOO00O0OOO00000O0 ["cedents_str"]["cond"]#line:1642
            elif O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="CFMiner":#line:1643
                O0O0O0000O000O000 =O0O0O0000O000O000 +" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["base"])+" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["s_up"])+" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["s_down"])#line:1644
                O0O0O0000O000O000 =O0O0O0000O000O000 +" "+OOO00O0OOO00000O0 ["cedents_str"]["cond"]#line:1645
            elif O0O0OO0O0OO00OO00 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1646
                O0O0O0000O000O000 =O0O0O0000O000O000 +" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["base1"])+" "+"{:5d}".format (OOO00O0OOO00000O0 ["params"]["base2"])+"    "+"{:.3f}".format (OOO00O0OOO00000O0 ["params"]["ratioconf"])+"    "+"{:+.3f}".format (OOO00O0OOO00000O0 ["params"]["deltaconf"])#line:1647
                O0O0O0000O000O000 =O0O0O0000O000O000 +"  "+OOO00O0OOO00000O0 ["cedents_str"]["ante"]+" => "+OOO00O0OOO00000O0 ["cedents_str"]["succ"]+" | "+OOO00O0OOO00000O0 ["cedents_str"]["cond"]+" : "+OOO00O0OOO00000O0 ["cedents_str"]["frst"]+" x "+OOO00O0OOO00000O0 ["cedents_str"]["scnd"]#line:1648
            print (O0O0O0000O000O000 )#line:1650
        print ("")#line:1651
    def print_hypo (OOO0OO00O00O00O0O ,O000000OOOO0OO00O ):#line:1653
        OOO0OO00O00O00O0O .print_rule (O000000OOOO0OO00O )#line:1654
    def print_rule (OO0O0O0000000OO00 ,OO0O0O00O0000OOOO ):#line:1657
        print ("")#line:1658
        if (OO0O0O00O0000OOOO <=len (OO0O0O0000000OO00 .result ["rules"])):#line:1659
            if OO0O0O0000000OO00 .result ['taskinfo']['task_type']=="4ftMiner":#line:1660
                print ("")#line:1661
                OO0000O000OOO0O0O =OO0O0O0000000OO00 .result ["rules"][OO0O0O00O0000OOOO -1 ]#line:1662
                print (f"Rule id : {OO0000O000OOO0O0O['rule_id']}")#line:1663
                print ("")#line:1664
                print (f"Base : {'{:5d}'.format(OO0000O000OOO0O0O['params']['base'])}  Relative base : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_base'])}  CONF : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['conf'])}  AAD : {'{:+.3f}'.format(OO0000O000OOO0O0O['params']['aad'])}  BAD : {'{:+.3f}'.format(OO0000O000OOO0O0O['params']['bad'])}")#line:1665
                print ("")#line:1666
                print ("Cedents:")#line:1667
                print (f"  antecedent : {OO0000O000OOO0O0O['cedents_str']['ante']}")#line:1668
                print (f"  succcedent : {OO0000O000OOO0O0O['cedents_str']['succ']}")#line:1669
                print (f"  condition  : {OO0000O000OOO0O0O['cedents_str']['cond']}")#line:1670
                print ("")#line:1671
                print ("Fourfold table")#line:1672
                print (f"    |  S  |  ¬S |")#line:1673
                print (f"----|-----|-----|")#line:1674
                print (f" A  |{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold'][0])}|{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold'][1])}|")#line:1675
                print (f"----|-----|-----|")#line:1676
                print (f"¬A  |{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold'][2])}|{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold'][3])}|")#line:1677
                print (f"----|-----|-----|")#line:1678
            elif OO0O0O0000000OO00 .result ['taskinfo']['task_type']=="CFMiner":#line:1679
                print ("")#line:1680
                OO0000O000OOO0O0O =OO0O0O0000000OO00 .result ["rules"][OO0O0O00O0000OOOO -1 ]#line:1681
                print (f"Rule id : {OO0000O000OOO0O0O['rule_id']}")#line:1682
                print ("")#line:1683
                OO0O0O0O0000O0OOO =""#line:1684
                if ('aad'in OO0000O000OOO0O0O ['params']):#line:1685
                    OO0O0O0O0000O0OOO ="aad : "+str (OO0000O000OOO0O0O ['params']['aad'])#line:1686
                print (f"Base : {'{:5d}'.format(OO0000O000OOO0O0O['params']['base'])}  Relative base : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_base'])}  Steps UP (consecutive) : {'{:5d}'.format(OO0000O000OOO0O0O['params']['s_up'])}  Steps DOWN (consecutive) : {'{:5d}'.format(OO0000O000OOO0O0O['params']['s_down'])}  Steps UP (any) : {'{:5d}'.format(OO0000O000OOO0O0O['params']['s_any_up'])}  Steps DOWN (any) : {'{:5d}'.format(OO0000O000OOO0O0O['params']['s_any_down'])}  Histogram maximum : {'{:5d}'.format(OO0000O000OOO0O0O['params']['max'])}  Histogram minimum : {'{:5d}'.format(OO0000O000OOO0O0O['params']['min'])}  Histogram relative maximum : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_max'])} Histogram relative minimum : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_min'])} {OO0O0O0O0000O0OOO}")#line:1688
                print ("")#line:1689
                print (f"Condition  : {OO0000O000OOO0O0O['cedents_str']['cond']}")#line:1690
                print ("")#line:1691
                print (f"Histogram                      {OO0000O000OOO0O0O['params']['hist']}")#line:1692
                if ('aad'in OO0000O000OOO0O0O ['params']):#line:1693
                    print (f"Histogram on full set          {OO0000O000OOO0O0O['params']['hist_full']}")#line:1694
                    print (f"Relative histogram             {OO0000O000OOO0O0O['params']['rel_hist']}")#line:1695
                    print (f"Relative histogram on full set {OO0000O000OOO0O0O['params']['rel_hist_full']}")#line:1696
            elif OO0O0O0000000OO00 .result ['taskinfo']['task_type']=="UICMiner":#line:1697
                print ("")#line:1698
                OO0000O000OOO0O0O =OO0O0O0000000OO00 .result ["rules"][OO0O0O00O0000OOOO -1 ]#line:1699
                print (f"Rule id : {OO0000O000OOO0O0O['rule_id']}")#line:1700
                print ("")#line:1701
                OO0O0O0O0000O0OOO =""#line:1702
                if ('aad_score'in OO0000O000OOO0O0O ['params']):#line:1703
                    OO0O0O0O0000O0OOO ="aad score : "+str (OO0000O000OOO0O0O ['params']['aad_score'])#line:1704
                print (f"Base : {'{:5d}'.format(OO0000O000OOO0O0O['params']['base'])}  Relative base : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_base'])}   {OO0O0O0O0000O0OOO}")#line:1706
                print ("")#line:1707
                print (f"Condition  : {OO0000O000OOO0O0O['cedents_str']['cond']}")#line:1708
                print (f"Antecedent : {OO0000O000OOO0O0O['cedents_str']['ante']}")#line:1709
                print ("")#line:1710
                print (f"Histogram                                        {OO0000O000OOO0O0O['params']['hist']}")#line:1711
                if ('aad_score'in OO0000O000OOO0O0O ['params']):#line:1712
                    print (f"Histogram on full set with condition             {OO0000O000OOO0O0O['params']['hist_cond']}")#line:1713
                    print (f"Relative histogram                               {OO0000O000OOO0O0O['params']['rel_hist']}")#line:1714
                    print (f"Relative histogram on full set with condition    {OO0000O000OOO0O0O['params']['rel_hist_cond']}")#line:1715
                OO0O0O0O0OO000OOO =OO0O0O0000000OO00 .result ['datalabels']['catnames'][OO0O0O0000000OO00 .result ['datalabels']['varname'].index (OO0O0O0000000OO00 .result ['taskinfo']['target'])]#line:1716
                print (" ")#line:1718
                print ("Interpretation:")#line:1719
                for O0OOOO0OO00000OOO in range (len (OO0O0O0O0OO000OOO )):#line:1720
                  O00O0000OOOOO00O0 =0 #line:1721
                  if OO0000O000OOO0O0O ['params']['rel_hist'][O0OOOO0OO00000OOO ]>0 :#line:1722
                      O00O0000OOOOO00O0 =OO0000O000OOO0O0O ['params']['rel_hist'][O0OOOO0OO00000OOO ]/OO0000O000OOO0O0O ['params']['rel_hist_cond'][O0OOOO0OO00000OOO ]#line:1723
                  O0000OO0OO0O0O000 =''#line:1724
                  if not (OO0000O000OOO0O0O ['cedents_str']['cond']=='---'):#line:1725
                      O0000OO0OO0O0O000 ="For "+OO0000O000OOO0O0O ['cedents_str']['cond']+": "#line:1726
                  print (f"    {O0000OO0OO0O0O000}{OO0O0O0000000OO00.result['taskinfo']['target']}({OO0O0O0O0OO000OOO[O0OOOO0OO00000OOO]}) has occurence {'{:.1%}'.format(OO0000O000OOO0O0O['params']['rel_hist_cond'][O0OOOO0OO00000OOO])}, with antecedent it has occurence {'{:.1%}'.format(OO0000O000OOO0O0O['params']['rel_hist'][O0OOOO0OO00000OOO])}, that is {'{:.3f}'.format(O00O0000OOOOO00O0)} times more.")#line:1728
            elif OO0O0O0000000OO00 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1729
                print ("")#line:1730
                OO0000O000OOO0O0O =OO0O0O0000000OO00 .result ["rules"][OO0O0O00O0000OOOO -1 ]#line:1731
                print (f"Rule id : {OO0000O000OOO0O0O['rule_id']}")#line:1732
                print ("")#line:1733
                print (f"Base1 : {'{:5d}'.format(OO0000O000OOO0O0O['params']['base1'])} Base2 : {'{:5d}'.format(OO0000O000OOO0O0O['params']['base2'])}  Relative base 1 : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_base1'])} Relative base 2 : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['rel_base2'])} CONF1 : {'{:.3f}'.format(OO0000O000OOO0O0O['params']['conf1'])}  CONF2 : {'{:+.3f}'.format(OO0000O000OOO0O0O['params']['conf2'])}  Delta Conf : {'{:+.3f}'.format(OO0000O000OOO0O0O['params']['deltaconf'])} Ratio Conf : {'{:+.3f}'.format(OO0000O000OOO0O0O['params']['ratioconf'])}")#line:1734
                print ("")#line:1735
                print ("Cedents:")#line:1736
                print (f"  antecedent : {OO0000O000OOO0O0O['cedents_str']['ante']}")#line:1737
                print (f"  succcedent : {OO0000O000OOO0O0O['cedents_str']['succ']}")#line:1738
                print (f"  condition  : {OO0000O000OOO0O0O['cedents_str']['cond']}")#line:1739
                print (f"  first set  : {OO0000O000OOO0O0O['cedents_str']['frst']}")#line:1740
                print (f"  second set : {OO0000O000OOO0O0O['cedents_str']['scnd']}")#line:1741
                print ("")#line:1742
                print ("Fourfold tables:")#line:1743
                print (f"FRST|  S  |  ¬S |  SCND|  S  |  ¬S |");#line:1744
                print (f"----|-----|-----|  ----|-----|-----| ")#line:1745
                print (f" A  |{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold1'][0])}|{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold1'][1])}|   A  |{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold2'][0])}|{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold2'][1])}|")#line:1746
                print (f"----|-----|-----|  ----|-----|-----|")#line:1747
                print (f"¬A  |{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold1'][2])}|{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold1'][3])}|  ¬A  |{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold2'][2])}|{'{:5d}'.format(OO0000O000OOO0O0O['params']['fourfold2'][3])}|")#line:1748
                print (f"----|-----|-----|  ----|-----|-----|")#line:1749
            else :#line:1750
                print ("Unsupported task type for rule details")#line:1751
            print ("")#line:1755
        else :#line:1756
            print ("No such rule.")#line:1757
    def get_rulecount (O0O00O0O0O0O000OO ):#line:1759
        return len (O0O00O0O0O0O000OO .result ["rules"])#line:1760
    def get_fourfold (OO0O0OOOOOOOOO0OO ,O00OOO0OOOO0O00OO ,order =0 ):#line:1762
        if (O00OOO0OOOO0O00OO <=len (OO0O0OOOOOOOOO0OO .result ["rules"])):#line:1764
            if OO0O0OOOOOOOOO0OO .result ['taskinfo']['task_type']=="4ftMiner":#line:1765
                O000O00000OO0OOO0 =OO0O0OOOOOOOOO0OO .result ["rules"][O00OOO0OOOO0O00OO -1 ]#line:1766
                return O000O00000OO0OOO0 ['params']['fourfold']#line:1767
            elif OO0O0OOOOOOOOO0OO .result ['taskinfo']['task_type']=="CFMiner":#line:1768
                print ("Error: fourfold for CFMiner is not defined")#line:1769
                return None #line:1770
            elif OO0O0OOOOOOOOO0OO .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1771
                O000O00000OO0OOO0 =OO0O0OOOOOOOOO0OO .result ["rules"][O00OOO0OOOO0O00OO -1 ]#line:1772
                if order ==1 :#line:1773
                    return O000O00000OO0OOO0 ['params']['fourfold1']#line:1774
                if order ==2 :#line:1775
                    return O000O00000OO0OOO0 ['params']['fourfold2']#line:1776
                print ("Error: for SD4ft-Miner, you need to provide order of fourfold table in order= parameter (valid values are 1,2).")#line:1777
                return None #line:1778
            else :#line:1779
                print ("Unsupported task type for rule details")#line:1780
        else :#line:1781
            print ("No such rule.")#line:1782
    def get_hist (OO00O0OO00O0O00OO ,O0OOOOO0O0O00O000 ):#line:1784
        if (O0OOOOO0O0O00O000 <=len (OO00O0OO00O0O00OO .result ["rules"])):#line:1786
            if OO00O0OO00O0O00OO .result ['taskinfo']['task_type']=="CFMiner":#line:1787
                OOOO0OO0000O000OO =OO00O0OO00O0O00OO .result ["rules"][O0OOOOO0O0O00O000 -1 ]#line:1788
                return OOOO0OO0000O000OO ['params']['hist']#line:1789
            elif OO00O0OO00O0O00OO .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1790
                print ("Error: SD4ft-Miner has no histogram")#line:1791
                return None #line:1792
            elif OO00O0OO00O0O00OO .result ['taskinfo']['task_type']=="4ftMiner":#line:1793
                print ("Error: 4ft-Miner has no histogram")#line:1794
                return None #line:1795
            else :#line:1796
                print ("Unsupported task type for rule details")#line:1797
        else :#line:1798
            print ("No such rule.")#line:1799
    def get_hist_cond (OOO000OO0O00O0OOO ,OO0OO00000OO00000 ):#line:1802
        if (OO0OO00000OO00000 <=len (OOO000OO0O00O0OOO .result ["rules"])):#line:1804
            if OOO000OO0O00O0OOO .result ['taskinfo']['task_type']=="UICMiner":#line:1805
                OOO0OOOO0O00O0OOO =OOO000OO0O00O0OOO .result ["rules"][OO0OO00000OO00000 -1 ]#line:1806
                return OOO0OOOO0O00O0OOO ['params']['hist_cond']#line:1807
            elif OOO000OO0O00O0OOO .result ['taskinfo']['task_type']=="CFMiner":#line:1808
                OOO0OOOO0O00O0OOO =OOO000OO0O00O0OOO .result ["rules"][OO0OO00000OO00000 -1 ]#line:1809
                return OOO0OOOO0O00O0OOO ['params']['hist']#line:1810
            elif OOO000OO0O00O0OOO .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1811
                print ("Error: SD4ft-Miner has no histogram")#line:1812
                return None #line:1813
            elif OOO000OO0O00O0OOO .result ['taskinfo']['task_type']=="4ftMiner":#line:1814
                print ("Error: 4ft-Miner has no histogram")#line:1815
                return None #line:1816
            else :#line:1817
                print ("Unsupported task type for rule details")#line:1818
        else :#line:1819
            print ("No such rule.")#line:1820
    def get_quantifiers (O0OOO000000O0O0OO ,O00O00OOOOOOO00O0 ,order =0 ):#line:1822
        if (O00O00OOOOOOO00O0 <=len (O0OOO000000O0O0OO .result ["rules"])):#line:1824
            O0O0OOOO00O0OO0O0 =O0OOO000000O0O0OO .result ["rules"][O00O00OOOOOOO00O0 -1 ]#line:1825
            if O0OOO000000O0O0OO .result ['taskinfo']['task_type']=="4ftMiner":#line:1826
                return O0O0OOOO00O0OO0O0 ['params']#line:1827
            elif O0OOO000000O0O0OO .result ['taskinfo']['task_type']=="CFMiner":#line:1828
                return O0O0OOOO00O0OO0O0 ['params']#line:1829
            elif O0OOO000000O0O0OO .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1830
                return O0O0OOOO00O0OO0O0 ['params']#line:1831
            else :#line:1832
                print ("Unsupported task type for rule details")#line:1833
        else :#line:1834
            print ("No such rule.")#line:1835
    def get_varlist (OOOOO00O00O0O000O ):#line:1837
        return OOOOO00O00O0O000O .result ["datalabels"]["varname"]#line:1838
    def get_category_names (O00OOOO0O0O00OO0O ,varname =None ,varindex =None ):#line:1840
        OOO0000O0OOOOOO00 =0 #line:1841
        if varindex is not None :#line:1842
            if OOO0000O0OOOOOO00 >=0 &OOO0000O0OOOOOO00 <len (O00OOOO0O0O00OO0O .get_varlist ()):#line:1843
                OOO0000O0OOOOOO00 =varindex #line:1844
            else :#line:1845
                print ("Error: no such variable.")#line:1846
                return #line:1847
        if (varname is not None ):#line:1848
            O00OOOO00O00000OO =O00OOOO0O0O00OO0O .get_varlist ()#line:1849
            OOO0000O0OOOOOO00 =O00OOOO00O00000OO .index (varname )#line:1850
            if OOO0000O0OOOOOO00 ==-1 |OOO0000O0OOOOOO00 <0 |OOO0000O0OOOOOO00 >=len (O00OOOO0O0O00OO0O .get_varlist ()):#line:1851
                print ("Error: no such variable.")#line:1852
                return #line:1853
        return O00OOOO0O0O00OO0O .result ["datalabels"]["catnames"][OOO0000O0OOOOOO00 ]#line:1854
    def print_data_definition (OOO00OO00OO0OOO0O ):#line:1856
        O0O0O0O0000OOOOO0 =OOO00OO00OO0OOO0O .get_varlist ()#line:1857
        for OO00OOO00OOOO00O0 in O0O0O0O0000OOOOO0 :#line:1858
            OO00OO000000OOOOO =OOO00OO00OO0OOO0O .get_category_names (OO00OOO00OOOO00O0 )#line:1859
            O00OO0OO000O0OO00 =""#line:1860
            for O000OO00O00O0OO0O in OO00OO000000OOOOO :#line:1861
                O00OO0OO000O0OO00 =O00OO0OO000O0OO00 +str (O000OO00O00O0OO0O )+" "#line:1862
            O00OO0OO000O0OO00 =O00OO0OO000O0OO00 [:-1 ]#line:1863
            print (f"Variable {OO00OOO00OOOO00O0} has {len(O0O0O0O0000OOOOO0)} categories: {O00OO0OO000O0OO00}")#line:1864
