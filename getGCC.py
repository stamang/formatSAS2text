#!python
from sas7bdat import SAS7BDAT
import datetime

#fname="gcc_steps_survey_2014_steps_c.sas7bdat"
fname="gcc_steps_survey_2014_member_c.sas7bdat"
#fname="gcc_steps_survey_2014_weight_c.sas7bdat" 
#fname = "oracle08_13_clean.sas7bdat"
#fname = "all_yearly_variables_pvor_v3.sas7bdat"
#fname = "risk_dataset.sas7bdat"
#fname = "pv9607_share.sas7bdat"
#fname = "plant_level.sas7bdat"
#fname = "all_yearly_variables_pvor_v3.sas7bdat"
#fname = "all_static_vars_pvor_96_12.sas7bdat"
#fname = "all_static_vars_new.sas7bdat"


with SAS7BDAT("/Users/stamang/alcoa/gcc/"+fname) as f:
#with SAS7BDAT("/Volumes/QSU/Datasets/Alcoa/HR Data/pv9607_share/"+fname) as f:
#with SAS7BDAT("/Volumes/QSU/Datasets/Alcoa/Alcoa Investigators/JK/Relational Tables/relational files/"+fname) as f:
#with SAS7BDAT('/Volumes/QSU/Datasets/Alcoa/Alcoa Investigators/JK/Relational Tables/'+fname) as f:
    tmpfname = fname.split(".")
    fout = open("/Users/stamang/alcoa/"+tmpfname[0]+".txt","w")
    lc = 0
    for row in f:
        #print row
        trow = []
        for i in range(len(row)):
            #print type(row[i])
            if type(row[i]) is unicode:
                #print type(row[i])
                row[i].encode('ascii', 'ignore')
                trow.append(row[i])
            else: 
                row[i]=str(row[i])
                trow.append(row[i])
        tmp = trow[0]
        if trow[0] == "": tmp = "BLANK"
        for i in range(1,len(trow)):
            if trow[i] == "": tmp = tmp +"|BLANK"
            else: 
                if type(trow[i]) is unicode: 
                    tmp = tmp +"|"+trow[i].encode('ascii', 'ignore')
                    #trow[i]=trow[i].replace("\u2013","2013")
                else: tmp = tmp +"|"+str(trow[i])
        #print tmp
        print >> fout, tmp
        lc += 1
#        print lc
    #[u'eessno', u'earliestdt', u'sex_new', u'ethnic_new', u'dob_new']
#        print "row:",row
        #print >> fout, tmp
# datetime.date(1942, 2, 7)
print "lines processed: ",lc
