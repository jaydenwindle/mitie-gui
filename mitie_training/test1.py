# -*- coding: utf-8 -*-
import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
print parent
sys.path.append('/home/jayden/Documents/Hackathon/McHacks2017/MITIE/mitielib')

from mitie import *
# DatasetWeb Dev Montreal

# Data: Front-end Developer @ Phuse
# URL: http:#ca.indeed.com/viewjob?jk=f5d674a6128d53cb&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample0 = ner_training_instance(["Posted","Today","–","Accepting","applications","We","'re","looking","for","an","experienced","front-end","developer","to","join","our","remote","team",".","We","work","with","all","sorts","of","clients—from","startups","to","government","agencies—to","build","engaging","sites","and","applications",".","We","love","to","work","with","people","who","are","as","excited","to","create","clean",",","functional","user","experiences","as","we","are",".","Our","ideal","colleague","can","help","us","bring","everything","from","brochure","site","designs","to","end-to-end","JavaScript","applications","to","life",".","Who","Is","Phuse","?","Phuse","is","a","remote","team","of","creatives","who","craft","websites",",","interfaces","and","brands",",","from","concept","to","completion",".","The","person","who","fills","this","position","will",":","have","excellent","communication","skills","be","motivated","to","learn","and","constantly","improve","have","plenty","of","web","development","industry","experience","be","adept","at","HTML",",","CSS","and","JavaScript","know","their","way","around","Git",",","Slack","and","Trello","be","able","to","meet","deadlines","and","interface","with","clients","be","considered","more","seriously","based","on","experience","with","server","side","languages","Job","Perks","This","position","pays","$49,000","-","$52,000","annually",".","At","Phuse",",","everyone","enjoys",":","30","hour","work","weeks","a","flexible","schedule","annual","Phuser","gathering","company-supported","growth","and","learning","opportunities","an","open","vacation","policy","home","office","stipend"])

sample0.add_entity(xrange(71,72), "language")
sample0.add_entity(xrange(129,130), "language")
sample0.add_entity(xrange(131,132), "language")
sample0.add_entity(xrange(133,134), "language")

# Data: Web developer @ Inorbital Inc.
# URL: http:#ca.indeed.com/viewjob?jk=e13766ec520cab8d&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample1 = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","or","equivalent","experience","Experience","2","years","to","less","than","3","years","Applications","Adobe","Illustrator",",","Adobe","Photoshop","Work","Setting","Computer","hardware","or","software","retailer/wholesaler","Programming","Languages","XML",",","Visual","Basic",",","Object-Oriented","programming","languages",",","MySQL",",","Java",",","JavaScript",",","HTML",",","CSS",",","ASP",",","JQuery","Own","Tools/Equipment","Computer","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Attention","to","detail",",","Ability","to","distinguish","between","colours",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Spreadsheet",",","Internet",",","Database","software",",","JavaOS",",","File","management","software",",","Image","editing","software",",","Project","management","software",",","Programming","software",",","HTML","editing","software",",","Software","development",",","Mapping","and","data","visualization","software",",","Website","creation","and","management","software",",","MS","Office",",","Desktop","applications",",","C#",",",".","NET","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Client","focus",",","Dependability",",","Organized"])

sample1.add_entity(xrange(32,33), "language")
sample1.add_entity(xrange(34,36), "language")
sample1.add_entity(xrange(41,42), "language")
sample1.add_entity(xrange(43,44), "language")
sample1.add_entity(xrange(45,46), "language")
sample1.add_entity(xrange(47,48), "language")
sample1.add_entity(xrange(49,50), "language")
sample1.add_entity(xrange(51,52), "language")
sample1.add_entity(xrange(53,54), "language")
sample1.add_entity(xrange(136,137), "language")
sample1.add_entity(xrange(138,140), "language")

# Data: Web developer @ Evertz Microsystems Ltd.
# URL: http:#ca.indeed.com/viewjob?jk=bd991bbdc2e25add&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample2 = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","or","equivalent","experience","Experience","Experience","an","asset","Programming","Languages","JQuery","Transportation/Travel","Information","Own","transportation",",","Valid","driver","'s","licence","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Attention","to","detail",",","Tight","deadlines","Computer","and","Technology","Knowledge","Unix",",","Linux",",","JavaOS",",","Networking","software",",","Networking","hardware",",","Programming","software",",","Website","creation","and","management","software","Personal","Suitability","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Dependability",",","Organized"])

sample2.add_entity(xrange(15,16), "language")

# Data: Web developer @ Newcom Business Media Inc.
# URL: http:#ca.indeed.com/viewjob?jk=5ff08c06c6b33feb&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample3 = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","3","years","to","less","than","5","years","Specific","Skills","Research","and","evaluate","a","variety","of","interactive","media","software","products",",","Prepare","mock-ups","and","storyboards",",","Consult","with","clients","to","develop","and","document","Website","requirements",",","Lead","and","co-ordinate","multidisciplinary","teams","to","develop","Website","graphics",",","content",",","capacity","and","interactivity",",","Source",",","select","and","organize","information","for","inclusion","and","design","the","appearance",",","layout","and","flow","of","the","Website",",","Create","and","optimize","content","for","Website","using","a","variety","of","graphics",",","database",",","animation","and","other","software",",","Develop","Website","architecture","and","determine","hardware","and","software","requirements",",","Plan",",","design",",","write",",","modify",",","integrate","and","test","Web-site","related","code",",","Conduct","tests","and","perform","security","and","quality","controls","Programming","Languages","MySQL",",","Java",",","HTML",",","DHTML","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Organized"])

sample3.add_entity(xrange(132,133), "language")
sample3.add_entity(xrange(134,135), "language")
sample3.add_entity(xrange(136,137), "language")
sample3.add_entity(xrange(138,139), "language")

# Data: Web developer @ Tian Bao Travel Ltd.
# URL: http:#ca.indeed.com/viewjob?jk=803ae8d7b5549587&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample4 = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","2","years","to","less","than","3","years","Applications","Adobe","Acrobat","Reader",",","Adobe","Illustrator",",","Adobe","Photoshop",",","Shockwave",",","Flash",",","Corel","Draw",",","Adobe","Dreamweaver",",","Adobe","Premiere","Pro","Specific","Skills","Research","and","evaluate","a","variety","of","interactive","media","software","products",",","Prepare","mock-ups","and","storyboards",",","Consult","with","clients","to","develop","and","document","Website","requirements",",","Lead","and","co-ordinate","multidisciplinary","teams","to","develop","Website","graphics",",","content",",","capacity","and","interactivity",",","Source",",","select","and","organize","information","for","inclusion","and","design","the","appearance",",","layout","and","flow","of","the","Website",",","Create","and","optimize","content","for","Website","using","a","variety","of","graphics",",","database",",","animation","and","other","software",",","Develop","Website","architecture","and","determine","hardware","and","software","requirements",",","Plan",",","design",",","write",",","modify",",","integrate","and","test","Web-site","related","code",",","Conduct","tests","and","perform","security","and","quality","controls","Programming","Languages","PHP",",","MySQL","Computer","and","Technology","Knowledge","Word","processing","software",",","Unix",",","Spreadsheet",",","MS","Windows",",","Linux",",","Internet",",","Database","software",",","MAC",",","JavaOS",",","Device","drivers",",","Networking","software",",","Networking","hardware",",","Networking","security",",","Intranet",",","Servers",",","File","management","software",",","Security","software",",","Presentation","software",",","Mail","server","software",",","Communication","software",",","3D","graphic","software",",","Image","editing","software",",","Project","management","software",",","Programming","software",",","HTML","editing","software",",","Web","service","design",",","Programming","languages",",","Software","development",",","Mapping","and","data","visualization","software",",","Website","creation","and","management","software",",","MS","Office",",","Desktop","applications",",","Multimedia","software",",","Computer-aided","design","(","CAD",")",",","C#",",",".","NET",",","API","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Dependability",",","Judgement",",","Organized"])

sample4.add_entity(xrange(156,157), "language")
sample4.add_entity(xrange(158,159), "language")
sample4.add_entity(xrange(274,275), "language")
sample4.add_entity(xrange(276,278), "language")

# Data: Web developer @ Horizon Quest/Your Local Flyer
# URL: http:#ca.indeed.com/viewjob?jk=c4126c158ea353ec&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample5 = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","1","year","to","less","than","2","years","Additional","Skills","Website","developer","Applications","Adobe","Photoshop",",","Adobe","Dreamweaver","Specific","Skills","Research","and","evaluate","a","variety","of","interactive","media","software","products",",","Prepare","mock-ups","and","storyboards",",","Consult","with","clients","to","develop","and","document","Website","requirements",",","Lead","and","co-ordinate","multidisciplinary","teams","to","develop","Website","graphics",",","content",",","capacity","and","interactivity",",","Source",",","select","and","organize","information","for","inclusion","and","design","the","appearance",",","layout","and","flow","of","the","Website",",","Create","and","optimize","content","for","Website","using","a","variety","of","graphics",",","database",",","animation","and","other","software",",","Develop","Website","architecture","and","determine","hardware","and","software","requirements",",","Plan",",","design",",","write",",","modify",",","integrate","and","test","Web-site","related","code",",","Conduct","tests","and","perform","security","and","quality","controls","Programming","Languages","Visual","Basic",",","PHP",",","JavaScript",",","HTML",",","CSS",",","JQuery","Transportation/Travel","Information","Own","transportation",",","Own","vehicle",",","Public","transportation","is","not","available","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Attention","to","detail",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Spreadsheet",",","MS","Windows",",","Internet",",","HTML","editing","software",",","MS","Office","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Dependability",",","Judgement",",","Organized"])

sample5.add_entity(xrange(142,144), "language")
sample5.add_entity(xrange(145,146), "language")
sample5.add_entity(xrange(147,148), "language")
sample5.add_entity(xrange(149,150), "language")
sample5.add_entity(xrange(151,152), "language")
sample5.add_entity(xrange(153,154), "language")

# Data: Temporary Database/Web Developer @ Registered Nurses Association of Ontario
# URL: http:#ca.indeed.com/viewjob?jk=90ad40e813f9367d&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample6 = ner_training_instance(["Temporary","Database/Web","Developer","(","6","months",")"])

# Data: Web Developer (HTML / CSS / Bootstrap / Angular) @ Step by Step Professional Services Inc.
# URL: http:#ca.indeed.com/viewjob?jk=4c811937180f9e60&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample7 = ner_training_instance(["We","are","seeking","a","Web","Developer","with","HTML","/","CSS","/","Bootstrap","/","&","Angular",".","2","years","of","HTML","&","CSS","exp","is","expected","and","knowledge","of","Angular",",","Bootstrap","&","Javascript","an","asset",".","Skill","Years","Experience","Level","HTML","2","Intermediate","CSS","2","Intermediate","bootstrap",".","js","0.5","Novice","angular",".","js","Javascript","0.5","0.5","Novice","Novice","Able","to","work","in","the","following","location","(","s",")","Toronto","***Thank","you","to","all","applicants","for","your","interest","in","this","role",",","please","note","that","only","those","deemed","most","suitable","for","the","position","will","be","contacted","for","interviews","***"])

sample7.add_entity(xrange(7,8), "language")
sample7.add_entity(xrange(9,10), "language")
sample7.add_entity(xrange(11,12), "language")
sample7.add_entity(xrange(14,15), "language")
sample7.add_entity(xrange(19,20), "language")
sample7.add_entity(xrange(21,22), "language")
sample7.add_entity(xrange(28,29), "language")
sample7.add_entity(xrange(30,31), "language")
sample7.add_entity(xrange(32,33), "language")
sample7.add_entity(xrange(40,41), "language")
sample7.add_entity(xrange(43,44), "language")
sample7.add_entity(xrange(46,47), "language")
sample7.add_entity(xrange(51,52), "language")
sample7.add_entity(xrange(54,55), "language")

# Data: Web Developer (Internship) @ Reizt Inc.
# URL: http:#ca.indeed.com/viewjob?jk=64ecb0c376555bda&qd=xm-IJviY22GES7GDmn3WuVxzvCZu5RIYT4_Md3LBlUP2Ke5r5apWRFdse3qvrrkN2lKYITTZy2bTVvphuNyAKjqLdRH0sqYkMDqTdxwos5SDBfhE8IgzO_q_LQgY-_NZ&indpubnum=9978236252243350&atk=1b84t1bsaaepkfkq
sample8 = ner_training_instance(["Reizt","Inc",".","is","a","professional","recruitment","agency","based","in","Toronto",".","Our","client","is","a","IT","consulting","and","training","company",",","which","provides","training","and","internship","opportunities","for","people","who","need","entry","level","training","and","work","experience","in","Web","Development",",","QA","Analyst","and","IT","administration","fields",".","This","non-paid","internship","is","starting","from","January","2017","to","April","2017.","Reference","letter","will","be","provided","after","finishing","the","internship",".","Open","source","projects/codes","can","be","used","as","demonstration","to","your","next","job","hunting",".","Referral","to","employers","for","full-time","job","opportunities","or","transfer","to","direct","hire","are","subject","to","availability","for","top","performers",".","May","not","be","eligible","as","credits","at","colleges/universities","internship","program",".","Responsibilities","-","Finish","practice","assignments","after","training","-","Work","on","real","past","projects","to","develop","skills","accordingly","-","Test","fixes","to","ensure","problem","has","been","adequately","resolved","-","Identify","and","learn","appropriate","software","and","hardware","used","and","supported","by","the","organization","-","Perform","routine","management/reporting","tasks","-","Monitor","activities","of","IT","systems","and","applications","Requirement","-","No","formal","experience","is","required","Some","degree","of","Web","Development","experience","to","include","any","or","all","of","the","following",":","-Java/J2EE",",","JavaScript",",","Python",",","HTML",",","PHP-Basic","knowledge","of","the","Software","Development","Lifecycle","-","Familiarity","with","Web/Portal","architecture/technologies",":","Web","Server","(","IIS",",","Apache",")",",","LDAP",",","Web","Application","Server","-","Proficient","in","Microsoft","Office","Applications","(","Excel",",","PowerPoint",",","Word",")","-Basic","knowledge","of","the","IT","industry"])

sample8.add_entity(xrange(191,192), "language")
sample8.add_entity(xrange(193,194), "language")
sample8.add_entity(xrange(195,196), "language")
sample8.add_entity(xrange(197,198), "language")
sample8.add_entity(xrange(199,200), "language")


# do training
trainer = ner_trainer("../MITIE/MITIE-models/english/total_word_feature_extractor.dat")

trainer.add(sample1)
trainer.add(sample2)
trainer.add(sample3)
trainer.add(sample4)
trainer.add(sample5)
trainer.add(sample6)
trainer.add(sample7)
trainer.add(sample8)

trainer.num_threads = 4

ner = trainer.train()
ner.save_to_disk("testmodel.dat")
print ("tags:", ner.get_possible_ner_tags())
