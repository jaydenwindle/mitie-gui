# -*- coding: utf-8 -*-
import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
print parent
sys.path.append('/home/jayden/Documents/Hackathon/McHacks2017/MITIE/mitielib')

from mitie import *

# Dataset: Full Stack Developer - Canada

# Data: Web Designer and Developer @ QUMA Construction Inc
# URL: http:#ca.indeed.com/viewjob?jk=36541294275d553d&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample0 = ner_training_instance(["QUMA","Construction","Inc",",","located","in","1124","Lonsdale","Avenue",",","North","Vancouver",",","BC","is","looking","for","a","Permanent","Full","Time","(","full-stack",")","Web","Developer","who","is","experienced","in","building","dynamic","websites","and","applications",".","They","must","have","experience","in","building","complete","websites","from","concept","to","final","hosting","with","a","Canadian","web","service",".","The","candidate","must","also","be","able","to","build","an","in-house","Construction","Management","Application","capable","of","expanding","with","our","growth",".","Testing","and","post","project","support","is","also","required",".","Job","Description","–","Terms","and","Conditions",":","(","please","read","it","carefully","before","applying",")","Full","time","position",",","Convert","all","psd","provided","into","front-end","development","(","HTML5,","CSS3,","JS",")","keeping","in","mind","the","latest","web","2.0","trends",",","Back-end","development","(","PHP","(","zend","framework",")","+","mysql","+","memcache",")",",","Complete","testing","of","website","and","construction","software","(","white","&","black","box","testing",",","cosmetic","bug","test",",","etc",".",")",",","Ensure","website","is","responsive","(","working","on","all","devices","including",":","mobile",",","tablet",",","PC","and","Mac","screens",")",".","Set","up","Jenkins","for","Automatic","Testing","with","using","Capybara","and","Cucumber",",","Setup","of","full","administration","panel","to","control","entire","website","for","administrative","team","(","Job","Management",",","General","Management",",","Content","Management",",","FAQ","Management",",","etc",".",")",",","Setup","of","website","administrative","Emails","(","Admin","@","[","url","removed",",","login","to","view","]",",","support","@","[","url","removed",",","login","to","view","]",",","etc",".",")",",","Ensure","that","the","website","is","fast","and","user","friendly",".","Maximize","speed","as","much","as","possible","to","industry","acceptable","standards","and","ensure","cross","browser","compatibility","with","latest","stable","versions","of","most","popular","web","browsers","(","IE",",","safari",",","chrome",",","Firefox",",","opera",")","+","all","code","is","w3c","compliant",",","Write","clean",",","organized","and","authentic","code",".","No","code","generation","allowed",",","Ensure","anti-hacking","proof","coding","structure",",","database","indexing",",","on-page","optimization","and","[","url","removed",",","login","to","view","]","setup","(","Yahoo","(","text",")","&","Google","(","xml",")","sitemap",",","optimization","of","html","source","code",",","etc",".",")",",","Website","is","search","engine","crawler","friendly","(","sitemap",",","h1","tag","for","each","website",",","slice","images","to","reduce","loading","time",",","etc",".",")","and","projects","can","be","searched","using","Google","All","copyrights","to","website","will","be","held","by","us","(","[","url","removed",",","login","to","view","]",")","owners",".","Full","details","will","be","given","during","job","interview",".","We","don","'t","care","about","time",",","we","care","of","quality","so","please",",","if","you","are","beginner","programmer","don","'t","apply","'","Employment","Requirements",":","Bachelor","'s","degree","in","computer","science",",","communications","or","business","or","completion","of","a","college","program","in","computer","science",",","graphic","arts",",","web","design","or","business",",","Three","years","of","experience","in","the","field","of","web","developing",",","One","year","experience","in","making","costruction","management","applications","Highly","motivated","professional","with","strong","work","ethic",".","Good","listener","with","ability","to","motivate","others",".","Capable","of","setting","priorities","and","delegating","responsibilities",".","Fast","learner","able","to","assess","situations","and","quickly","find","solutions","with","respect","to","quality","standards","of","the","company",".","Able","to","work","as","a","team","member",".","Able","to","work","under","pressure",".","Programmer","must","have","good","English","communication","skills","The","successful","candidate","must","convert","one","page","of","psd","into","front-end","development","(","html",",","css",",","js",")","to","ensure","eligibility",",","Only","candidates","who","meet","these","requirements","will","be","contacted","for","further","consideration",".","All","applicants","to","apply","via","email","only",".","No","walk-ins",",","telephone","inquiries","or","faxes",".","Email","address","is","qumaemployment@gmail",".","com","Remuneration","will","vary","with","experience","but","wage","offered","is","$25","per","hour",",","30","hours","per","week",",","15","days","payed","vacation","+","benefits","package"])

sample0.add_entity(xrange(111,114), "language")
sample0.add_entity(xrange(127,128), "language")
sample0.add_entity(xrange(133,134), "language")
sample0.add_entity(xrange(354,355), "language")
sample0.add_entity(xrange(574,575), "language")
sample0.add_entity(xrange(576,577), "language")
sample0.add_entity(xrange(578,579), "language")
sample0.add_entity(xrange(129,131), "tool")
sample0.add_entity(xrange(135,136), "tool")
sample0.add_entity(xrange(183,184), "tool")
sample0.add_entity(xrange(189,190), "tool")
sample0.add_entity(xrange(191,192), "tool")

# Data: Full Stack Developer @ TAL Group
# URL: http:#ca.indeed.com/viewjob?jk=4e7106f0fd86ae71&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample1 = ner_training_instance(["Hiring","Full","Stack","Developers","(","Full-time",")","in","Mississauga",",","ON","!","As","an","Full","Stack","Developer","you","'ll","be","tasked","with","working","on","both","the","front","end","and","back","end","of","our","client","'s","web","applications",".","Working","within","the","software","development","team",",","your","duties","will","require","you","to","assist","in","the","development","and","architecture","of","enterprise","applications",".","This","role","is","ideal","for","ambitious","developers","who","feel","confident","in","their","technical","ability","and","want","to","be","a","part","of","the","highly-skilled","development","team",".","Perks","You","'ll","Love","•","Competitive","salary","and","benefits","•","Great","culture","that","is","facilitative","to","learning","•","Internal","Hackathons",",","Team","and","Training","Events","Main","Requirements","•","A","web","developer","at","heart","–","excited","about","modern","web","development","•","Personable",",","enthusiastic",",","a","strong","communicator",",","and","are","detail","oriented","•","Computer","Science","degree","or","equivalent","•","At","least","3+","years","Web","Development","experience","•","At","least","3+","years","full-stack","development","experience","•","Strong","CS","and","development","fundamentals",",","including","OOP","•","Strong","expertise","in","HTML5,","CSS",",","JavaScript","across","multiple","libraries","•","Single","Page","Application","design","with","Angular",".","js","•",".","Net","development","experience","preferred","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample1.add_entity(xrange(174,176), "language")
sample1.add_entity(xrange(177,178), "language")
sample1.add_entity(xrange(191,193), "language")
sample1.add_entity(xrange(187,190), "tool")

# Data: Full Stack Developer @ Step by Step Professional Services Inc.
# URL: http:#ca.indeed.com/viewjob?jk=75599c4da037e155&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample2 = ner_training_instance(["We","are","currently","looking","for","a","Full","Stack","Developer","with","React",",","Python","and","HTML",",","Javascript","and","CSS",".","Must","have","3","years","experience","with","each","skillset",".","This","is","a","contract","engagement","to","work","on","a","team","of","4","full","stack","web","developers",".","While","we","appreciate","all","interest",",","only","those","candidates","selected","for","an","interview","will","be","contacted","."])

sample2.add_entity(xrange(10,11), "tool")
sample2.add_entity(xrange(12,13), "language")
sample2.add_entity(xrange(14,15), "language")
sample2.add_entity(xrange(16,17), "language")
sample2.add_entity(xrange(18,19), "language")

# Data: Full-stack .NET Developer @ TAL Group
# URL: http:#ca.indeed.com/viewjob?jk=cd93d43260ed1233&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample3 = ner_training_instance(["Hiring","Full-stack",".","NET","Developers","(","Full-time",")","in","Toronto",",","ON","!","This","is","an","opportunity","to","work","in","a","complex","environment","as","part","of","a","fast-paced","and","talented","dev","team","on","a","cloud-","based","SaaS","solutions","environment",".","To","fill","this","role",",","you","must","have","strong","passion","and","skill","for",".","NET","web","development",".","Perks","You","'ll","Love","•","Collaborative","work","culture","•","Flex","hours","•","Fun","team","activities",",","such","as","lunch","parties",",","bowling",",","and","archery","Required","Skills","&","Experience","•","You","must","be","an","expert","at",":","•","C#","6.0","&",".","NET","4.6.","•","ASP",".","NET","4.5","(","ASP",".","NET","MVC",",","WebAPI",")",".","•","JavaScript-5","and","AngularJS",".","•","T-SQL","skills","targeting","SQL","Server","2016.","•","Links","to","code","samples","(","ex",".","Github","profile",")","are","a","plus","!","!","!","•","Communication","skills","(","written","and","verbal",")","•","University","Degree","in","Computer","Sciences","(","or","similar",")","Other","Experience","Pluses","•","Practical","skills","with","DOM",",","HTML5,","and","CSS","•","Any","ORM","or","micro-ORM","experience","•","Other","front-end","frameworks","(","React",",","KnockoutJS",",","Backbone",",","etc",")","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample3.add_entity(xrange(2,4), "language")
sample3.add_entity(xrange(53,55), "language")
sample3.add_entity(xrange(96,97), "language")
sample3.add_entity(xrange(99,101), "language")
sample3.add_entity(xrange(103,106), "language")
sample3.add_entity(xrange(117,118), "language")
sample3.add_entity(xrange(125,126), "language")
sample3.add_entity(xrange(172,173), "language")
sample3.add_entity(xrange(174,175), "language")
sample3.add_entity(xrange(119,120), "tool")
sample3.add_entity(xrange(177,178), "tool")
sample3.add_entity(xrange(186,187), "tool")
sample3.add_entity(xrange(188,189), "tool")
sample3.add_entity(xrange(190,191), "tool")

# Data: Angular Full Stack Developer @ TAL Group
# URL: http:#ca.indeed.com/viewjob?jk=6063ce79c540868f&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample4 = ner_training_instance(["Hiring","an","Angular","Full","Stack","Developer","(","Full-time",")","in","Toronto",",","ON","!","As","an","Angular","Developer","you","'ll","be","tasked","with","working","on","both","the","front","end","and","back","end","of","our","client","'s","web","applications",".","Working","within","the","software","development","team",",","your","duties","will","require","you","to","assist","in","the","development","and","architecture","of","enterprise","applications",".","This","role","is","ideal","for","ambitious","developers","who","feel","confident","in","their","technical","ability","and","want","to","be","a","part","of","the","highly-skilled","development","team",".","Perks","You","'ll","Love","•","Competitive","salary","and","benefits","•","Great","culture","that","is","facilitative","to","learning","•","Internal","Hackathons",",","Team","and","Training","Events","Main","Requirements","&","Responsibilities","•","Degree","in","Computer","Science",",","Computer","Engineering",",","or","equivalent","life","experience","•","Minimum","3-5","years","in","enterprise","web","development",",","specifically","NodeJS","•","Strong","foundation","in","JavaScript",",","and","min","1-2","years","experience","with","AngularJS/ReactJS","•","Strong","knowledge","of","HTML","5","and","web","fundamentals","(","CSS",",","HTTP",",","security",",","performance",",","etc",".",")","•","Strong","knowledge","of","Java","and/or",".","NET","is","an","asset","•","Experience","in","consulting","onsite","with","clients","is","an","asset","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample4.add_entity(xrange(2,3), "tool")
sample4.add_entity(xrange(16,17), "tool")
sample4.add_entity(xrange(153,154), "tool")
sample4.add_entity(xrange(140,141), "language")
sample4.add_entity(xrange(145,146), "language")
sample4.add_entity(xrange(158,160), "language")
sample4.add_entity(xrange(164,165), "language")
sample4.add_entity(xrange(166,167), "language")
sample4.add_entity(xrange(179,180), "language")
sample4.add_entity(xrange(181,183), "language")

# Data: Full Stack Rails Developer @ TAL Group
# URL: http:#ca.indeed.com/viewjob?jk=932c12a0cc4637bc&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample5 = ner_training_instance(["Hiring","Full","Stack","Rails","Developer","(","Full-time",")","in","Toronto",",","ON","!","As","an","experienced","Full","Stack","Rails","Developer",",","you","will","assist","our","client","in","revolutionizing","its","growing","industry",".","Have","you","worked","on","large","scale","SaaS","applications","?","Do","you","find","it","tough","to","sleep","at","night","without","proper","test","coverage","?","Do","you","grow","software","through","Agile","Methodologies","such","as","TDD",",","continuous","integration",",","and","MVP","?","This","role","is","ideal","for","ambitious","developers","who","feel","confident","in","their","technical","ability","and","want","to","be","a","part","of","the","highly-skilled","development","team",".","Perks","You","'ll","Love","Competitive","salary","and","full","benefits","Great","culture","that","is","facilitative","to","learning","Internal","Hackathons",",","Team","and","Training","Events","Required","Skills","&","Background","Ruby","on","Rails","Javascript","Test","Driven","Development","Experience","with","dev-ops","(","AWS/Linode/etc",")","Exceptional","communication","skills","Skills","We","'d","Love","To","See","Angular","Mobile","application","development","Data","Warehouse","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample5.add_entity(xrange(3,4), "tool")
sample5.add_entity(xrange(18,19), "tool")
sample5.add_entity(xrange(125,128), "tool")
sample5.add_entity(xrange(147,148), "tool")
sample5.add_entity(xrange(128,129), "language")

# Data: Full Stack Developer @ Dynamic Leap Technology Inc.
# URL: http:#ca.indeed.com/viewjob?jk=78a8cf00ac07b5e8&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample6 = ner_training_instance(["Dynamic","Leap","is","a","Vancouver","based","software","development","shop","focusing","on","the","mobile","application","space",".","We","have","a","strong","team","consisting","of","a","cross","section","of","outstanding","people","who","focus","on","quality",",","performance","and","delivery",".","We","are","experiencing","a","rapid","growth","and","are","looking","for","new","talent","to","join","our","team",".","We","are","looking","for","a","Full","Stack","Developer","to","join","our","team",",","learn","and","grow","with","us",".","We","like","challenging","ourselves","to","solve","new","and","difficult","problems","and","to","create","beautiful","and","innovative","websites","and","apps","that","can","be","used","and","appreciated","by","millions","of","people",".","If","you","are","like","us","you","'ll","love","working","and","playing","at","Dynamic","Leap",".","Skills","&","Qualifications",":","Experience","using","web","services","APIs","in","mobile","applications","Experience","with","responsive","Web","development","Experience","working","with","back","end","and/or","front","end","technologies","such","as",":","PHP",",","Node",".","js",",","Java","(","Spring",")",",","MySQL",",","Angular",",","React",",","HTML",",","JS",",","JSON",",","CSS","Knowledge","of","various","CMS","such","as","WordPress",",","Drupal",",","Joomla",",","etc",".",",","a","bonus","A","minimum","of","three","years","work","experience","in","the","industry","A","positive","attitude","and","enthusiasm","Quick","learning","curve","Attention","to","detail"])

sample6.add_entity(xrange(127,128), "language")
sample6.add_entity(xrange(148,149), "language")
sample6.add_entity(xrange(150,153), "language")
sample6.add_entity(xrange(154,155), "language")
sample6.add_entity(xrange(159,160), "language")
sample6.add_entity(xrange(165,166), "language")
sample6.add_entity(xrange(167,168), "language")
sample6.add_entity(xrange(169,170), "language")
sample6.add_entity(xrange(171,172), "language")
sample6.add_entity(xrange(156,157), "tool")
sample6.add_entity(xrange(161,162), "tool")
sample6.add_entity(xrange(163,164), "tool")
sample6.add_entity(xrange(175,176), "tool")
sample6.add_entity(xrange(178,179), "tool")
sample6.add_entity(xrange(180,181), "tool")
sample6.add_entity(xrange(182,183), "tool")

# Data: Full Stack Software Developer @ TAL Group
# URL: http:#ca.indeed.com/viewjob?jk=53d548f37e744e6d&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample7 = ner_training_instance(["Hiring","a","Full","Stack","Software","Developer","(","Full-time",")","in","Toronto",",","ON","!","Our","client","is","looking","for","a","change","agent","to","join","its","growing","team","who","is","able","to","clearly","understand","business","requirements","and","provide","strategic","options",".","Hot","Job","Facts",":","•","Comprehensive","health","&","dental","benefits","•","Opportunity","to","join","a","collaborative","team","within","the","insurance","space","•","Free","parking","available","on-site","Responsibilities","&","Required","Skills","•","You","have","at","least","3+","years","advanced","experience","and","technical","skills","in","the","following","areas",":","o","HTML5","&","CSS3","o","ASP",".","NET","o","VB",".","NET","o","JavaScript",",","jQuery","o",".","NET","Framework","o","WCF","o","SQL","•","Prior","knowledge","of","the","following","technologies","(","asset",")","o","Entity","Framework","o","LINQ","o","KnockoutJS","o","TFS","o","Mobile","web","application","development","•","Knowledge","of","lending","and/or","insurance","(","i.e.","at","least","have","a","mortgage","or","car","loan",",","car","insurance",")","•","Passion","and","commitment","to","deliver","high","quality","code",",","on","time","and","to","specification","•","Excellent","diagnostic","skills","•","Good","written","and","verbal","communication","skills","•","Solid","understanding","of","MS","SQL","Server","relational","database","•","Experience","working","in","a","structured","software","development","environment","with","established","SDLC","•","You","are","a","strong","learner","who","supports","continuous","learning","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample7.add_entity(xrange(88,89), "language")
sample7.add_entity(xrange(90,91), "language")
sample7.add_entity(xrange(92,95), "language")
sample7.add_entity(xrange(96,99), "language")
sample7.add_entity(xrange(100,101), "language")
sample7.add_entity(xrange(102,103), "language")
sample7.add_entity(xrange(104,106), "language")
sample7.add_entity(xrange(108,109), "language")
sample7.add_entity(xrange(110,111), "language")
sample7.add_entity(xrange(185,187), "language")
sample7.add_entity(xrange(122,124), "tool")
sample7.add_entity(xrange(125,126), "tool")
sample7.add_entity(xrange(127,128), "tool")
sample7.add_entity(xrange(129,130), "tool")

# Data: Full Stack Developer @ Traction On Demand
# URL: http:#ca.indeed.com/viewjob?jk=eeb8e7f729805ebd&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample8 = ner_training_instance(["Traction","is","among","the","fastest","growing","CRM","consulting","companies","in","North","America","and","a","strategic","partner","to","Salesforce",".","com",".","We","are","excited","about","our","growing","team","and","invite","top","caliber","people","like","you","to","join","us","in","this","adventure",".","We","are","definitely","a","one","of","a","kind","company","-","respectful","of","people","'s","personal","interests","and","aspirations",",","with","a","simple","mission",":","bend","web-based","technologies","to","meet","the","needs","of","sales","and","marketing","professionals",".","Our","clients","have","included","10","of","the","25","largest","global","technology","companies",",","local","start-ups","on","their","way","to","greatness",",","and","hundreds","of","other","companies","that","are","trying","to","make","CRM","easier",",","friendlier","and","more","valuable",".","You","love","a","challenge","and","are","eager","to","learn",".","You","understand","people",",","and","have","the","ability","to","hear","a","symptom",",","identify","the","problem","and","scribe","a","solution",".","You","work","well","in","a","casual","yet","fast-paced","team","environment",".","You","work","well","with","others",",","yet","have","the","independence","to","support","and","drive","projects",".","You","have","what","it","takes","to","grow","with","our","business",",","for","the","long","run",".","Maybe",",","you","even","like","wake-boarding",".",".",".","we","keep","a","boat","in","the","office","and","an","AirStream","!","As","a","Full","Stack","Developer","you","will","be","responsible","for","customizing",",","developing","and","supporting","solutions","on","the","Force",".","com","platform",".","What","you","will","be","doing",":","Build","client-specific","solutions","on","the","Force",".","com","platform","using","Apex/Visual","Force","(","Salesforce","proprietary","language",",","similar","to","Java","or","C#/","ASP",".","NET",")",",","HTML",",","JavaScript",",","AJAX",",","and","jQuery",".","Some","graphic","design","principles","capability","is","preferable",",","e.g.","experience","with","Photoshop","and","Illustrator","Experience","with","mobile","application","development","Builds","software","applications","–","Follows","coding","standards",",","builds","appropriate","unit","tests",",","integration","tests","and","deployment","scripts","Translates","designs","and","style","guides","provided","by","the","UI/UX","team","into","functional","user","interfaces",",","ensuring","cross","browser","compatibility","and","performance","Owns","success","–","Takes","responsibility","for","successful","delivery","of","the","solutions","Contributes","to","continual","improvement","by","suggesting","improvements","to","user","interface",",","software","architecture","or","new","technologies","Requirements","Computer","Science","Degree","or","equivalent","experience",",","3-5","years","development","experience","in","Java",",",".","NET","or","another","C-style","language","through","personal","or","work","experience","Web","development","experience","using","JSP","or","ASP",".","NET","is","a","strong","asset","Proficiency","in","HTML","and","JavaScript/AJAX","Strong","knowledge","of","relational","databases","and","SQL","Ability","to","effectively","communicate","technical","issues","in","laymen","'s","termsto","customers","Highly","motivated","with","the","ability","to","prioritize","what","'s","on","your","plate","Definite","Assets","Knowledge","of","CRM","and","ERP","systems","Salesforce",".","com","development","(","will","train",")","Not","afraid","to","ask","questions","Learning","new","things","Any","kind","of","client","facing","work","Minimum","of","5","years","development","experience","in","different","environments"])

sample8.add_entity(xrange(6,7), "tool")
sample8.add_entity(xrange(110,111), "tool")
sample8.add_entity(xrange(288,289), "tool")
sample8.add_entity(xrange(290,291), "tool")
sample8.add_entity(xrange(440,441), "tool")
sample8.add_entity(xrange(442,443), "tool")
sample8.add_entity(xrange(444,445), "tool")
sample8.add_entity(xrange(251,253), "language")
sample8.add_entity(xrange(260,261), "language")
sample8.add_entity(xrange(262,263), "language")
sample8.add_entity(xrange(264,266), "language")
sample8.add_entity(xrange(268,269), "language")
sample8.add_entity(xrange(270,271), "language")
sample8.add_entity(xrange(272,273), "language")
sample8.add_entity(xrange(275,276), "language")
sample8.add_entity(xrange(375,376), "language")
sample8.add_entity(xrange(377,379), "language")
sample8.add_entity(xrange(392,393), "language")
sample8.add_entity(xrange(394,397), "language")
sample8.add_entity(xrange(403,404), "language")
sample8.add_entity(xrange(405,406), "language")
sample8.add_entity(xrange(412,413), "language")

# Data: Software Developer (Full Stack) @ PinPoint Talent
# URL: http:#ca.indeed.com/viewjob?jk=4645fb9b23885d01&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample9 = ner_training_instance(["As","a","software","developer","you","will","design","complex","systems","and","lead","the","technical","solution","of","projects","in","an","environment","that","releases","weekly",",","in","a","highly","collaborative","and","empowering","environment","that","strives","to","see","each","individual","succeed",".","Our","client","has","built","a","massive","infrastructure","and","utilizes","modern","web","technologies","to","create","a","cutting","edge","product",".","If","you","enjoy","building","full","stack","applications","from","the","ground","up","and","have","previous","experience","with","web","development",",","UX/UI","and","in","an","environment","that","rapidly","iterates","and","deploys","this","may","be","a","role","for","you",".","Qualifications",":","-","3+","years","of","large","scale",",","full","life","cycle","development","experience","-","Solid","foundation","in","data","structures",",","algorithms",",","and","OO","design","-","Has","in-depth","technical","experience","with","full","stack","server","side","and","web","development","-","Solid","experience","with","at","least","2","of","the","following",":","HTML5,","JavaScript",",","AJAX",",","BackBoneJS",",","VueJS",",","CSS","-","Solid","experience","with","at","least","2","of","the","following",":","SQL",",","Postgres",",","PHP",",","Ruby",",","Coldfusion","Responsibilities",":","-","Design","complex","systems","and","lead","the","technical","solution","of","projects","-","Work","closely","with","our","product","and","design","teams","to","define","feature","specifications","-","Be","responsible","for","the","code","quality","on","your","team","-","Mentor","more","junior","developers","-","Be","responsible","for","all","aspects","of","software","development",",","from","design","to","implementation",",","testing","and","maintenance","."])

sample9.add_entity(xrange(144,146), "language")
sample9.add_entity(xrange(153,154), "language")
sample9.add_entity(xrange(165,166), "language")
sample9.add_entity(xrange(167,168), "language")
sample9.add_entity(xrange(171,172), "language")
sample9.add_entity(xrange(173,174), "language")
sample9.add_entity(xrange(147,148), "tool")
sample9.add_entity(xrange(149,150), "tool")
sample9.add_entity(xrange(151,152), "tool")

# Data: Full-Stack Developer @ Genetec Inc.
# URL: http:#ca.indeed.com/viewjob?jk=1ebf5f19b0224552&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample10 = ner_training_instance(["Genetec","'s","Custom","Solutions","team","is","looking","for","a","proficient","hands-on","Software","Developer","that","is","passionate","about","high-tech","systems","evolving","from","complex","networking","architecture","and","distributed","client-servers",".","We","are","looking","for","the","kind","of","person","that","thrives","in","a","changing","and","challenging","environment",".","Someone","who","steps","up","to","do","whatever","is","needed","without","waiting","to","be","asked",".","Custom","Solutions","Developement","is","a","team","of","full-stack","developers","who","are","exposed","to","all","parts","of","software","development","from","client","'s","requirements","definition","to","design",",","development",",","code","review",",","final","deployment",",","operation","and","support",".","Responsibilities",":","You","'ll","be","performing","tasks","such","as",":","•","Design","and","implement","distributed","applications","projects","for","multiple","clients","each","year",".","Projects","can","be","composed","of","Windows","desktop","applications",",","Web","applications","and","distributed","server","systems",".","•","Review","code",",","comment","on","and","accept","pull-requests","from","other","developers","in","our","GIT","source","control","environment",".","•","Collaborating","with","our","integrators","to","ensure","our","projects","are","meeting","our","client","'s","needs",".","Requirements",":","•","College","or","University","degree","in","Computer","Science",",","Software","Engineering","or","related","field",".","•","2+","years","relevant","work","experience","developing","distributed","software",",","Web","applications","or","desktop","applications",".","•","Bilingual","(","English","and","French",")",".","•","Stellar","interpersonal","skills","with","the","ability","to","coordinate","across","teams",".","Technical","Requirements",":","•","Experience","in","a","server-side","web","development","stack","(","e.g.","ASP",".","NET",",","Node",".","js",",","etc",")",".","•","Have","a","good","background","using","C#","and","JavaScript","language",".","•","Know","how","to","write","testable","code",".","•","Know","your","way","around","Windows","and","Linux","(","Ubuntu",")","servers",".","•","Experience","using","bug","tracking","and","source","control","tools",".","•","Excellent","technical","writing","skills","to","document","specifications","and","designs",".","Assets",":","•","Proficiency","with","Windows","Presentation","Framework","(","WPF",")",".","•","Knowledge","of","HTML5","and","CSS3.","•","Familiarity","of","web","frontend","framework","(","e.g.","AngularJS",",","React",",","Vue",".","js",")",".","•","Knowledge","of","search","and","data","analysis","engine","(","e.g.","Elasticsearch",")",".","•","Comfortable","using","No-SQL","database","(","e.g.","MongoDB",",","RethinkDB",",","Redis",")","and","using","SQL","relational","database","(","MSSQL",",","MySQL",")","environment","."])

sample10.add_entity(xrange(151,152), "tool")
sample10.add_entity(xrange(273,274), "tool")
sample10.add_entity(xrange(275,276), "tool")
sample10.add_entity(xrange(277,278), "tool")
sample10.add_entity(xrange(328,329), "tool")
sample10.add_entity(xrange(330,331), "tool")
sample10.add_entity(xrange(332,335), "tool")
sample10.add_entity(xrange(347,348), "tool")
sample10.add_entity(xrange(357,358), "tool")
sample10.add_entity(xrange(359,360), "tool")
sample10.add_entity(xrange(361,362), "tool")
sample10.add_entity(xrange(238,241), "language")
sample10.add_entity(xrange(242,245), "language")
sample10.add_entity(xrange(255,256), "language")
sample10.add_entity(xrange(257,258), "language")
sample10.add_entity(xrange(311,312), "language")
sample10.add_entity(xrange(317,318), "language")
sample10.add_entity(xrange(319,320), "language")
sample10.add_entity(xrange(353,354), "language")
sample10.add_entity(xrange(365,366), "language")
sample10.add_entity(xrange(369,370), "language")
sample10.add_entity(xrange(371,372), "language")

# Data: Full Stack C# Developer @ IT/IQ TECH RECRUITERS
# URL: http:#ca.indeed.com/viewjob?jk=4eb834aeed120c23&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample11 = ner_training_instance(["IT/IQ","Tech","Recruiters"])


# Data: Full Stack Java / Js Developer @ Lawpoint
# URL: http:#ca.indeed.com/viewjob?jk=910873c60622fc61&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample12 = ner_training_instance(["DIGI117","Ltd",".","has","the","open","full-time","permanent","position","of","a","Full","Stack","Java","/","JS","developer",".","Successful","candidate","must","have",":","Two","(","2",")","or","more","years","of","strong","Java","experience","(","in-depth","knowledge","of","classes",")",".","Strong","knowledge","of","Spring","(","Spring","Boot",",","Security",",","Spring","Cloud",",","Spring","Data",",","etc",")",",","Hibernate",",","Maven",".","Strong","knowledge","of","OOP/OOD",",","architecture",",","and","design","patterns",".","Solid","experience","in","MySQL","/","Postgres","/","MongoDB",".","Understanding","of","TDD","values","and","experience","in","applying","them","to","real","projects",".","Extensive","experience","with","JavaScript","programming","and","frameworks","e.g.","Angular",",","React","and","Backbone",".","Extensive","experience","in","writing","semantic","HTML5,","CSS3","and","CSS","preprocessors","like","Sass","and","Less",".","Excellent","knowledge","of","HTTP",",","REST","API",".","Experience","with","microservice","architecture",".","Working","experience","with","Linux","+","Continuous","Integration","(","Jenkins",",","Team","City",",","Code","Coverage","Reporting",",","Continuous","Deployment",",","etc",")",".","Real","life","experience","with","distributed","Agile","projects","as","a","part","of","a","multi-skilled","team",".","Ability","to","provide","realistic","time","estimates","for","assigned","work","tasks","and","meet","the","deadlines",".","Candidate","must","be","fluent","in","verbal/written","English","as","the","position","involves","communication","with","customers",".","Preference","will","be","given","to","candidates","with","leadership","experience","within","a","software","development","team",".","Duties","on","the","job","will","include","but","not","be","limited","to",":","Develop","and","maintain","the","front-end","/","back-end","portions","of","the","system",".","Identify","and","execute","performance","optimization",".","Multi-platform","and","cross-browser","development","and","debugging",".","DIGI117","Ltd",".","is","an","IT","consulting","and","software","development","company","with","focus","on","innovative","technology","and","product","development",",","located","at","220-145","Chadwick","Court",",","Vancouver",",","BC",",","V7M","3K1,","Canada",".","Work","location","is","at","the","same","address",".","The","position","is","compensated","at","$75,000","per","year",",","with","minimum","of","35","work","hours","per","week","and","a","possibility","of","overtime","when","needed",".","Paid","vacation",",","extended","medical",",","dental",",","long","term","disability",",","life/accidental","death","and","dismemberment","insurance","is","available","after","3","months","on","the","job",".","Please","apply","by","sending","your","resume","and","reference","letter","by","email",",","by","clicking","on","the","provided","\"","Apply","\"","button",",","or","by","faxing","to","416","273","2321."])

sample12.add_entity(xrange(13,14), "language")
sample12.add_entity(xrange(15,16), "language")
sample12.add_entity(xrange(32,33), "language")
sample12.add_entity(xrange(67,68), "language")
sample12.add_entity(xrange(78,79), "language")
sample12.add_entity(xrange(80,81), "language")
sample12.add_entity(xrange(82,83), "language")
sample12.add_entity(xrange(100,101), "language")
sample12.add_entity(xrange(116,118), "language")
sample12.add_entity(xrange(119,120), "language")
sample12.add_entity(xrange(122,123), "language")
sample12.add_entity(xrange(124,125), "language")
sample12.add_entity(xrange(129,130), "language")
sample12.add_entity(xrange(131,133), "language")
sample12.add_entity(xrange(44,45), "tool")
sample12.add_entity(xrange(46,47), "tool")
sample12.add_entity(xrange(51,52), "tool")
sample12.add_entity(xrange(54,55), "tool")
sample12.add_entity(xrange(105,106), "tool")
sample12.add_entity(xrange(107,108), "tool")
sample12.add_entity(xrange(109,110), "tool")
sample12.add_entity(xrange(142,143), "tool")
sample12.add_entity(xrange(147,148), "tool")

# Data: Full-Stack Software Developer @ Flinks.io
# URL: http:#ca.indeed.com/viewjob?jk=9e64e5114d4959d2&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample13 = ner_training_instance(["WE","ACCEPT","REMOTE","OR","ON-SITE","WORK",",","IT","'S","YOURS","TO","DECIDE","!"])


# Data: Programmeur-analyste.Net (full stack developer) @ TRANSIT
# URL: http:#ca.indeed.com/viewjob?jk=dfcbc7d8f788b1a9&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample14 = ner_training_instance(["Vous","rêvez","d","'avoir","un","impact","majeur","au","sein","d","'une","entreprise","?","Vous","voulez","intégrer","une","équipe","reconnue","et","respectée","par","l","'entreprise","?","Vous","voulez","travailler","sur","des","projets","stratégiques","à","partir","des","toutes","dernières","technologies","Microsoft","?","Rejoignez","notre","équipe",",","votre","place","est","avec","nous","!","Votre","mission",":","Vous","participerez","au","développement","de","notre","nouvelle","plateforme","à","partir","des","toutes","dernières","technologies","telles","que","ASP",".","NET",",","Core","et","git",".","Vous","participerez","activement","à","l","'analyse",",","à","l","'architecture",",","au","développement","et","au","déploiement","du","projet","au","sein","d","'une","organisation","LEAN",".","5otre","bagage","doit","contenir",":","DEC","et/ou","BAC","en","informatique","complété",",","au","moins","3","ans","d","'expérience","significative","en","C#",".","NET",",","avoir","déjà","travaillé","avec","Visual","Studio","et","SQL","Server",",","un","excellent","français","parlé","&","écrit",".","Atouts","importants",":","C#",",","ASP",".","NET","MVC",",","SQL","Server",",","JavaScript","Vous","devez","être",":","visionnaire",",","innovateur",",","autonome",",","consciencieux",",","dynamique",",","organisé",",","ouvert","d","'esprit","et","être","un","joueur","d","'équipe",".","Pourquoi","joindre","Transit",":","Horaire","vraiment","flexible",",","35h","à","40h/semaine",",","salaire","compétitif",",","assurances","collectives",",","environnement","sans","stress","et","vous","travaillerez","avec","les","meilleurs","outils","."])

sample14.add_entity(xrange(69,72), "language")
sample14.add_entity(xrange(122,125), "language")
sample14.add_entity(xrange(133,134), "language")
sample14.add_entity(xrange(146,147), "language")
sample14.add_entity(xrange(148,151), "language")
sample14.add_entity(xrange(153,154), "language")
sample14.add_entity(xrange(156,157), "language")

# Data: Software Developer @ Envysion, Inc
# URL: http:#ca.indeed.com/viewjob?jk=d74bbc1d60de841e&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample15 = ner_training_instance(["Software","Developer"])


# Data: Intermediate Front End Developer @ TAL Group
# URL: http:#ca.indeed.com/viewjob?jk=3386a7e291098b26&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample16 = ner_training_instance(["Hiring","an","Intermediate","Front","End","Developer","(","Full-time",")","in","Toronto",",","ON","!","Our","ideal","candidate","is","a","strong","self-starter",",","has","initiative","and","reacts","quickly","in","time","sensitive","situations",".","This","is","an","exciting","opportunity","to","work","with","the","world","'s","No","1","Travel/Adventure","company","!","Perks","You","'ll","Love","Work","with","the","world","'s","No","1","Travel/Adventure","company","Exciting","opportunities","for","travel","and","growth","An","environment","where","you","work","hard","and","have","so","much","fun","doing","it","-","So","rewarding","!","What","We","'re","Looking","For","Strong","self-starter",",","has","initiative","and","reacts","quickly","in","time","sensitive","situations","Expert","knowledge","of","JavaScript","(","and","it","'s","libraries",")","Understanding","of","the","full","web","stack","–","from","server","to","browser","Evangelize","and","improve","tools","for","responsive","development","Required","Background","&","Skills","At","least","3+","years","experience","with","Front","End","Technologies","and","Development","experience","At","least","1+","year","of","experience","with","React","You","are","a","people","person","!","Personality","is","super","important","for","their","culture","!","Our","client","wants","a","fun",",","collaborative","and","passionate","individual","who","wants","to","an","integral","part","of","a","growing","team","BA","in","Computer","Science","or","related","field","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample16.add_entity(xrange(104,105), "language")
sample16.add_entity(xrange(152,153), "tool")

# Data: Intermediate Web Application Developer @ IT MindFinders
# URL: http:#ca.indeed.com/viewjob?jk=4cda984c919d7892&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample17 = ner_training_instance(["This","job","is","posted","by","an","employment","agency","or","third","party","on","behalf","of","the","employer",".","Employer","Name",":","N/A","Industry","Title",":","Data","Processing",",","Hosting",",","and","Related","Services","(","5182",")","IT","MindFinders","is","conducting","a","search","for","an","Intermedate","Web","Application","Developer","on","behalf","of","a","client","in","Vancouver",",","BC",".","The","Web","Application","Developer","wil","work","to","develop","and","augment","our","client","'s","site",",","enhance","the","application","'s","reputation",",","and","evolve","it","to","the","'next","level","'.","This","position","will","work","with","a","variety","of","technologies","from","all","parts","of","the","web","stack",".","Our","client","is","looking","for","someone","who","is","a","motivated","self-starter",",","a","great","communicator",",","able","to","multitask",",","adheres","to","development","best","practices","and","existing","coding","conventions",".","Responsibilities",":","Maintain","and","develop","new","features","for","our","client","'s","site","Research","latest","web","performance","trends","and","tools","Make","improvements","and","recommendations","to","tools","developed","by","the","client","Provide","support","for","site","users","Requirements",":","2+","years","of","experience","in","full","web","stack","development","A","scripting","language","(","eg",".","Perl",",","Python",")","MySQL","(","or","other","relational","database",")","HTML5,","CSS3,","and","CSS","Pre-processors","(","eg",".","Sass",")","JavaScript","and","JS","frameworks","(","eg",".","jQuery",")","Git","Solid","understanding","of","front-end","web","performance","Comfortable","working","in","Lunux","(","or","other","*nix","OS",")","Familiar","with","Agile/Scrum","development","methodology","Experience","with","Perl","and/or","C++","is","an","asset","Experience","developing","Firefox","and","Chrome","extensions","is","an","asset","Benefits",":","Our","client","recognizes","the","importance","of","balancing","careers","with","other","aspects","of","life",",","and","their","office","culture","and","benefits","reflect","this","-","from","flexible","work","hours","to","health","and","wellness","incentives",",","rooftop","barbeques","and","staff","garden",",","open","space","and","a","casual","vibe",".","They","also","encourage","and","support","sustainable","lifestyle","habits","and","invest","in","company","green","practices","such","as","their","green","roof","and","living","wall",".","In","addition","to","all","of","this",",","they","offer","a","competitive","salary",",","extended","health","and","dental",",","flexible","hours",",","training",",","education",",","and","an","opportunity","to","grown","and","advance","with","a","top","IT","company","located","within","steps","of","the","Skytrain",",","Seabus","and","West","Coast","Express","."])

sample17.add_entity(xrange(184,185), "language")
sample17.add_entity(xrange(186,187), "language")
sample17.add_entity(xrange(188,189), "language")
sample17.add_entity(xrange(195,197), "language")
sample17.add_entity(xrange(198,199), "language")
sample17.add_entity(xrange(203,204), "language")
sample17.add_entity(xrange(205,206), "language")
sample17.add_entity(xrange(207,208), "language")
sample17.add_entity(xrange(212,213), "language")
sample17.add_entity(xrange(238,239), "language")
sample17.add_entity(xrange(240,241), "language")
sample17.add_entity(xrange(214,215), "tool")
sample17.add_entity(xrange(224,225), "tool")
sample17.add_entity(xrange(228,229), "tool")
sample17.add_entity(xrange(233,234), "tool")

# Data: Intermediate Web Application Developer @ IT MindFinders Search Consultants Inc.
# URL: http:#ca.indeed.com/viewjob?jk=6d143c6bc5db973c&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample18 = ner_training_instance(["IT","MindFinders","is","conducting","a","search","for","an","Intermediate","Web","Application","Developer","on","behalf","of","a","client",".","The","Web","Application","Developer","will","work","to","develop","and","augment","our","client","'s","site",",","enhance","the","application","'s","reputation",",","and","evolve","it","to","the","'next","level","'.","This","position","will","work","with","a","variety","of","technologies","from","all","parts","of","the","web","stack",".","Our","client","is","looking","for","someone","who","is","a","motivated","self-starter",",","a","great","communicator",",","able","to","multi-task",",","adheres","to","development","best","practices","and","existing","coding","conventions",".","Responsibilities",":","Maintain","and","develop","new","features","for","our","client","'s","site","Research","latest","web","performance","trends","and","tools","Make","improvements","and","recommendations","to","tools","developed","by","the","client","Provide","support","for","site","users","Requirements",":","2+","years","of","experience","in","full","web","stack","development","A","scripting","language","(","eg",".","Perl",",","Python",")","MySQL","(","or","other","relational","database",")","HTML5,","CSS3,","and","CSS","Pre-processors","(","eg",".","Sass",")","JavaScript","and","JS","frameworks","(","eg",".","jQuery",")","Git","Solid","understanding","of","front-end","web","performance","Comfortable","working","in","Linux","(","or","other","*nix","OS",")","Familiar","with","Agile/Scrum","development","methodology","Experience","with","Perl","and/or","C++","is","an","asset","Experience","developing","Firefox","and","Chrome","extensions","is","an","asset","Benefits",":","Our","client","recognizes","the","importance","of","balancing","careers","with","other","aspects","of","life",",","and","their","office","culture","and","benefits","reflect","this","-","from","flexible","work","hours","to","health","and","wellness","incentives",",","rooftop","barbeques","and","staff","garden",",","open","space","and","a","casual","vibe",".","They","also","encourage","and","support","sustainable","lifestyle","habits","and","invest","in","company","green","practices","such","as","their","green","roof","and","living","wall",".","In","addition","to","all","of","this",",","they","offer","a","competitive","salary",",","extended","health","and","dental",",","flexible","hours",",","training",",","education",",","and","an","opportunity","to","grow","and","advance","with","a","top","IT","company","located","within","steps","of","the","Skytrain",",","Seabus","and","West","Coast","Express","."])

sample18.add_entity(xrange(145,146), "language")
sample18.add_entity(xrange(147,148), "language")
sample18.add_entity(xrange(149,150), "language")
sample18.add_entity(xrange(156,158), "language")
sample18.add_entity(xrange(159,160), "language")
sample18.add_entity(xrange(164,165), "language")
sample18.add_entity(xrange(166,167), "language")
sample18.add_entity(xrange(168,169), "language")
sample18.add_entity(xrange(173,174), "language")
sample18.add_entity(xrange(199,200), "language")
sample18.add_entity(xrange(201,202), "language")
sample18.add_entity(xrange(175,176), "tool")
sample18.add_entity(xrange(185,186), "tool")
sample18.add_entity(xrange(189,190), "tool")
sample18.add_entity(xrange(194,195), "tool")

# Data: Software Developer, Co-op @ Clio
# URL: http:#ca.indeed.com/viewjob?jk=e95bf6d052c2fe49&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample19 = ner_training_instance(["Clio","is","one","of","the","fastest-growing","technology","startups","in","Canada","consistently","included","in","Deloitte","'s","Technology","Fast","50","ranking","and","has","been","named","in","the","as","Canada","'s","10","Most","Admired","Corporate","Cultures","of","2016","by","Waterstone","Human","Capital",".","We","are","a","cloud-based","practice","management","solution","for","lawyers","that","makes","their","lives","simpler","and","helps","them","build","a","better","practice",".","Learn","more","about","us","at","teamclio",".","tumblr",".","com","or","check","us","out","on","GlassDoor",".","As","a","Software","Developer",",","Co-op",",","you","will","be","working","on","a","revolutionary","SaaS","product","with","a","tech","stack","running","off","of","a","Rails","backend",".","You","will","be","coached","and","mentored","by","some","of","the","best","developers","in","the","business","and","working","on","some","of","the","most","challenging","problems","that","a","rapid","growth","venture-backed","company","can","face",".","We","are","proud","to","say","that","100%","of","our","2016","Co-op","students","are","returning","to","us","in","2017","either","for","another","co-op","term","or","full","time","employment","!","You","are","team-oriented","and","have","successfully","completed","one",",","if","not","two",",","previous","software","development","co-ops",".","You","embrace","new","challenges","with","gusto","and","problems","are","the","tasty","seasoning","sprinkled","on","your","fries",".","You","like","to","lose","yourself","in","complex","yet","interesting","riddles","and","have","fun","while","doing","it",".","We","are","looking","for","the","next","wave","of","Clions","to","be","part","of","our","success","story","!","Applicants","should","be","available","for","an","8","month","co-op","period","from","May","2017","to","December","2017.","We","will","be","accepting","applications","throughout","the","Spring",".","You","should","have",":","Completed","your","second","year","coursework","and","be","a","3rd","or","4th","year","Computer","Science/Engineering","student",",","Excellent","computer","science","fundamentals",":","data","structures",",","algorithms",",","programming","languages",",","SQL",",","Strong","understanding","for","networking","and","concurrency",",","Superb","communication","skills","written",",","verbal",",","and","spoken",",","and",",","Great","team","skills","--","lone","wolves","aren","'t","a","great","fit","for","us",".","It","'s","nice","if","you",":","Bring","new","ideas","to","the","table","to","help","make","our","environment","better",".","Be","constantly","experimenting","and","learning","outside","school","curriculum",".","Help","contribute","to","our","culture",".","Board","Game","nights",",","Ping","Pong",",","Street","Fighter","2,","beach","volleyball","league","(","on-premise",")",",","dodgeball","team",",","whatever","!","Your","contributions","are","welcome",".","We","offer","a","great","compensation","package",",","3","weeks","vacation","(","or","pay","in","lieu","of",")",",","a","fun","work","environment",",","a","killer","benefits","plan",",","and","an","opportunity","to","be","part","of","a","great","growth","story","with","unlimited","potential",".","We","value","excellence",",","transparency",",","initiative","and","offer","a","work","culture","and","environment","that","people","rave","about","!","Career","movement",",","advancement",",","and","growth","opportunities","are","around","every","corner",".","If","you","want","to","accelerate","yourself","and","maybe","even","try","things","you","never","dreamed","of",",","Clio","is","the","place","for","you","!","Diversity","and","Inclusion","We","believe","that","ensuring","diversity","and","inclusion","will","produce","a","better","place","to","work","and","a","better","product",".","We","encourage","all","candidates","to","apply",".","You","must","be","eligible","to","work","in","Canada","."])

sample19.add_entity(xrange(103,104), "tool")
sample19.add_entity(xrange(294,295), "language")

# Data: Developer Support @ Astucemedia
# URL: http:#ca.indeed.com/viewjob?jk=1ef03e5edfae2e71&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample20 = ner_training_instance(["We","are","seeking","a","Full-stack","Developer","with","technical","support","skills","to","work","(","remotely","or","at","our","office",")","with","our","creative","and","technically","innovative","team",".","The","right","candidate","will","have","to",":","PRIMARY","RESPONSIBILITIES","1.","Technical","support","Assist","customers","via","phone",",","email",",","and","remote","connection","tools","Troubleshoot","hardware","and","software","issues","Ticket","end-user","interaction","Quickly","and","adequately","resolve","problems","the","customer","is","facing","and","report","to","Software","Team","2.","Operations","support","Execute","test","plans","with","a","critical","eye","Be","an","active","part","of","support","relating","to","the","use","of","operational","systems","Be","part","of","the","process","leading","to","the","production","of","internal","tools/process","within","the","department","Develop","useful","tools","for","the","customer-service","department","3.","Work","closely","with","the","Software","team","Write","stable",",","clean","JavaScript",",","HTML","and","CSS","Work","with","Software","Team","to","translate","business","requirements","into","practical","software","solutions","Ensure","that","the","problems","be","correctly","identified","and","resolved","Update","the","team","on","the","quality","of","the","project","and","communicate","technical","and","creative","ideas",",","Execute","test","plans","with","a","critical","eye","4.","Documentation","Perform","administrative","duties","such","as","e-mail","management","and","support","documentation","Accurately","report","findings","through","our","databases","Update","technical","procedures","and","materials","that","can","be","used","to","inform","and/or","coach","users","or","that","could","be","used","as","technical","support","for","various","applications","and","data","bases","Revise","and/or","write","projects","operations","manuals","when","required","5.","Technological","watch","Ensure","that","the","best","new","technologies","are","investigated","and","selected","for","use","Must","be","constantly","on","the","watch","for","new","technologies","and","what","is","being","done","in","the","field","of","web","development","and","multimedia",".","REQUIRED","EXPERIENCE","2+","years","of","experience","as","technical","support","Strong","experience","with","scripting","Excellent","communication","skills","and","the","ability","to","work","in","a","team","setting","Ability","to","handle","multiple","tasks","and","the","flexibility","to","respond","to","changing","priorities","and","timelines","and","demands","Advanced","technical","level","REQUIRED","SKILLS","These","are","considered","a","strong","asset",":","Javascript",",","Bootstrap",",","C++",",","C#","-","preferably","in","relation","to","developing","RESTful","APIs",".","ServiceStack","and","ORM","frameworks","Second-Screen","or","other","interactive","touch-screen","development","Strong","knowledge","of","sports","(","Soccer",",","Football",",","Baseball",",","Hockey",",","etc",".",")","Strong","computer","skills","(","file","structure",",","databases",",","word","processing",",","text","editors",")",".","Experience","with","social","media","APIs","(","Twitter",",","Facebook",",","Instagram",",","etc",".",")","Passion","about","how","data","can","enrich","the","television","viewing","experience","Good","analytical","skills",",","quickly","identify","a","problem","and","suggest","efficient","solutions","Communicate","effectively","with","both","engineers","and","non","technical","people","These","are","considered","a","strong","assets",":","Javascript",",","Bootstrap",",","C++",",","C#","-","preferably","in","relation","to","developing","RESTful","APIs",".","ServiceStack","and","ORM","frameworks","Second-Screen","or","other","interactive","touch-screen","development","Strong","knowledge","of","sports","(","Soccer",",","Football",",","Baseball",",","Hockey",",","etc",".",")","Strong","computer","skills","(","file","structure",",","databases",",","word","processing",",","text","editors",")",".","Experience","with","social","media","APIs","(","Twitter",",","Facebook",",","Instagram",",","etc",".",")","Passion","about","how","data","can","enrich","the","television","viewing","experience","Good","analytical","skills",",","quickly","identify","a","problem","and","suggest","efficient","solutions","Communicates","effectively","with","both","engineers","and","non","technical","people"])

sample20.add_entity(xrange(128,129), "language")
sample20.add_entity(xrange(130,131), "language")
sample20.add_entity(xrange(132,133), "language")
sample20.add_entity(xrange(323,324), "language")
sample20.add_entity(xrange(327,328), "language")
sample20.add_entity(xrange(329,330), "language")
sample20.add_entity(xrange(434,435), "language")
sample20.add_entity(xrange(436,437), "language")
sample20.add_entity(xrange(438,439), "language")
sample20.add_entity(xrange(440,441), "language")
sample20.add_entity(xrange(325,326), "tool")
sample20.add_entity(xrange(336,338), "tool")
sample20.add_entity(xrange(339,340), "tool")
sample20.add_entity(xrange(341,342), "tool")
sample20.add_entity(xrange(343,344), "tool")
sample20.add_entity(xrange(447,449), "tool")
sample20.add_entity(xrange(450,451), "tool")
sample20.add_entity(xrange(452,453), "tool")
sample20.add_entity(xrange(454,455), "tool")

# Data: Software Developer – Web @ Yocale
# URL: http:#ca.indeed.com/viewjob?jk=17c0e24a62cf6fe5&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample21 = ner_training_instance(["Fantastic","opportunity","to","work","for","one","of","the","fastest","growing","start-ups","in","Vancouver",".","We","are","looking","for","a","self-motivated",",","passionate",",","creative",",","and","experienced","Full","Stack","Software","Developer","for","Web","to","join","our","team","building","the","cutting","age","web","and","multimedia","applications",".","What","you","will","be","doing","Work","with","a","small","team","(","10-15","people",")","in","a","scrum","environment","Build","high-quality","software","and","adapt","to","a","rapidly","growing","start-up","environment","Design","and","develop","new","code","as","well","and","maintain","existing","code","in","full","stack","Work","with","quality","assurance","to","test","software","code",",","troubleshoot","and","fix","issues","Assist","other","junior","team","members","with","your","technical","knowledge","Maintain","your","time","and","track","your","work","in","a","Microsoft","TFS","(","Team","Foundation","Server","What","you","will","need","3+","years","of","experience","as","a","web","developer","using","full","stack","Microsoft",".","Net","technologies","Expert","with","C#",",","ASP",".","Net","MVC","and","EF","Expert","with","HTML5/CSS3/LESS/JavaScript","Experience","with","JQuery","and","Bootstrap","Deep","understanding","of","object","oriented","programming","and","design","patterns","Deep","understanding","of","relational","databases","specially","Microsoft","SQL","Server","Nice","to","Have","Skills","Experience","of","developing","applications","using","C#",".","Net/WPF","Experience","with","e-Commerce","web","applications","Familiar","with","mobile","application","development","Familiar","with","NoSQL","Databases","concept","Compensation","80K-110K","based","on","experience","Great","benefits","and","stock","options","in","our","rapidly","growing","company","Flexible","working","hours"])

sample21.add_entity(xrange(121,122), "tool")
sample21.add_entity(xrange(142,144), "language")
sample21.add_entity(xrange(147,148), "language")
sample21.add_entity(xrange(149,152), "language")
sample21.add_entity(xrange(157,158), "language")
sample21.add_entity(xrange(160,162), "language")
sample21.add_entity(xrange(179,180), "language")
sample21.add_entity(xrange(190,191), "language")
sample21.add_entity(xrange(192,193), "language")
sample21.add_entity(xrange(205,206), "language")

# Data: Senior Full Stack Developer @ GenXys Health Care Systems
# URL: http:#ca.indeed.com/viewjob?jk=225f9d8ddaf9cd2e&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample22 = ner_training_instance(["GenXys","provides","smart","tools","for","patients","and","health-care","professionals","enabling","personalized","care",".","We","offer","pharmacogenetic","testing","(","myPGx",")","and","a","medication","decision","support","system","(","TreatGx",")","to","provide","safe",",","effective","and","personalized","treatment","options","for","patients","and","health","care","professionals",".","Every","GenXys","employee","contributes","to","our","vision","-","Leading","Personalized","Health","Care","for","All",".","You","will","collaborate","on","the","products","and","solutions","that","help","us","carry","out","our","mission","of","providing","smart","tools","for","patients","and","health","care","professionals","enabling","personalized","care",".","We","are","a","start-up","company",",","a","spin-off","from","the","University","of","British","Columbia",".","We","want","to","move","from","our","current","heuristic","system","to","AI",".","Join","our","team","for","a","rewarding","career",".","We","have","an","immediate","opening","for","a","full-time","Senior","Full","Stack","Developer","at","our","office","within","the","University","of","British","Columbia",",","BC",".","This","position","will","work","in","a","team","environment","and","will","deliver","high","quality","software","for","a","medication","decision","support","system",".","In","addition","to","new","software","development",",","this","role","will","also","debug","problems","reported","by","customers","and","implement","intelligent","fixes","to","resolve","these","problems",".","Primary","Responsibilities",":","Perform","architectural","analysis","and","defining","software","architecture",".","Design","and","develop","and","implement","software","in","all","layers","(","front-end",",","mid-tier",",","server","side",")","as","needed",".","Perform","logical/algorithmic","design","independently","and","with","others",",","and","generalize","knowledge","to","new","environments",".","Develop",",","document",",","debug","and","maintain","software","in","accordance","with","requirements","and","design",".","Provide","the","technical","contents","of","Product","Documentation",".","Work","closely","with","others","to","investigate","and","fix","complex","product","defects",",","and","issue","timely","HotFixes","as","required",".","Experience","Minimum","Requirements","3+","years","experience","in","software","engineering","Critical","Skills","Proven","track","record","in","designing","and","developing","Web-based","enterprise","software",".","Experience","with","all","stages","of","the","software","development","life","cycle",".","Experience","in","secure","web","development","and","implementation","of","application","security","measures",".","Experience","in","GUI","design","specializing","in","simple","human/machine","interfacing",".","Experience","in","UI","design","for","non-experts","operating","complex","systems","on","omni-platform",".","Knowledge","of","the","following","products",",","frameworks","and","languages",":","Microsoft","SQL","Server",".","Microsoft","C#",".","Node",".","js",".","React",".","Bootstrap",".","Additional","Knowledge","&","Skills","Familiarity","with","healthcare",",","such","as","SNOMED","codes","Familiarity","with","clinical","data","exchange","standards",",","such","as","HL7","Familiarity","with","one","of","the","secure","Framework","in","Web","Service","Excellent","verbal","and","written","communication","skills","Education","4-year","degree","in","computer","science","or","related","field","or","equivalent","experience","Skills","and","Competency",":","Self-motivated","developer","who","can","work","independently","on","projects","and","come","up","with","new","ideas","and","concepts","Logical","thinker","with","proactive","troubleshooting","and","critical","problem","solving","skills","Self-motivated","with","ability","to","work","in","a","close","team","environment","Some","reasons","why","you","'d","want","to","work","with","us",":","Competitive","salary","Our","office","is","a","bright","open","space",",","located","at","UBC","close","to","public","transit",".","You","'ll","get","to","enjoy","snacks",",","coffee/tea",",","and","happy","hours","with","the","team",".","You","want","to","play","a","big","part","in","growing",",","young","company","while","working","alongside","people","who","are","smart",",","easy-going",",","and","helpful",".","You","do","your","best","in","a","setting","where","excellent","work","is","valued",".","You","'re","looking","for","a","big","challenge","that","involves","lots","of","variety",",","collaboration",",","inventiveness",",","and","on","your","toes","thinking","."])

sample22.add_entity(xrange(360,362), "language")
sample22.add_entity(xrange(364,365), "language")
sample22.add_entity(xrange(366,369), "language")
sample22.add_entity(xrange(372,373), "language")
sample22.add_entity(xrange(370,371), "tool")

# Data: Senior Full Stack Developer @ Filament Creative inc.
# URL: http:#ca.indeed.com/viewjob?jk=450a156a81782655&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample23 = ner_training_instance(["Posted","Dec","7","–","Accepting","applications","Opportunity","We","have","an","opportunity","for","a","Senior","Full","Stack","Developer","with","top-shelf","skills","to","join","our","tight","and","talented","team","in","Toronto","(","no","remote—sorry",")",".","You","'ll","be","collaborating","closely","with","strategy",",","design",",","and","contributing","your","skills","with","the","Dev","team",".","We","are","a","fast-paced","agency","with","a","full","pipeline",".","You","'ll","be","bringing","your","existing","skill","set","and","helping","us","evolve","our","stack","on","a","wide","range","of","projects",".","We","'re","currently","a","very","heavy","LAMP","stack","shop","but","have","a","number","of","projects","that","fall","outside","this","wheelhouse",".","You","'ll","be","working","with","clients","like","Fitbit",",","eHealth","Ontario",",","City","of","Toronto","(","GreenP",")",",","and","Toshiba","(","to","name","a","few",")","to","push","unexpectedly","clever","features","and","functionality","to","existing","and","new","web","properties","and","applications",".","We","'d","like","you","to","be","curious","and","courageous","enough","to","bring","new","technologies","into","the","fold",".","You","have","a","chance","to","be","part","of","a","small","team","and","make","a","huge","impact","on","how","things","are","done",".","Your","Personality","The","kind","of","personality","we","'re","looking","for","is","someone","who","is","both","detail","oriented","but","also","sees","the","big","picture",".","You","'re","interested","in","supporting","your","team","and","you","enjoy","growing","your","skills","by","rising","to","challenges",".","You","'re","flexible","and","open","and","understand","that","clients","aren","'t","an","impediment","to","doing","great","work",",","rather",",","they","are","an","opportunity","to","do","your","best","work",".","You","'re","a","great","communicator","who","strives","to","create","context","and","visibility","for","everyone","involved","on","a","project",".","You","use","We","more","than","I.","You","have","contributed","to","the","dev","community","and","your","passion","for","technology","is","clearly","demonstrated","through","development","related","networks","(","Codepen",",","Git",")","and","commentary/opinion","channels","(","Medium",",","your","own","blog",",","Twitter",",","Instagram",")",".","Requirements","3-5+","years","of","agency","or","product","team","experience",".","Front","End","Extensive","experience","with","jQuery","and","jQuery","plugins","In-depth","knowledge","of","“vanilla”","JavaScript","Frontend","Frameworks","like","Bootstrap","and","Foundation","are","a","must","Extensive","experience","with","responsive","SCSS","Experience","with","Bower",",","NPM",",","Grunt",",","and/or","Gulp","Git","and","GitHub","knowledge","is","essential","A","knack","for","writing","semantically","meaningful",",","object","orientated","and","reusable","code","You","can","show","us","your","work","with","CSS","animations","and","transitions","Familiarity","with","building","for","accessibility","and","AODA","Compliance","Working","with","payment","gateways","and","commerce","platforms","like","Stripe",",","PayPal",",","Shopify",",","and","Magento","A","good","understanding","of","client-side","performance","tuning",",","security","and","optimization","(","caching",",","CDNs",",","request","management",",","cookies",",","http",",","https",",","etc",".",")","Back","End","PHP","frameworks",",","specifically","Laravel","Ruby","on","Rails","Write/maintain","applications","using","PHP","Frameworks","and","ORMs",":","Wordpress","Expertise","Deployment","and","maintenance","of","core","WP","and","plugins",".","WP-CLI","and","Composer","for","updates","Roll","own","plugins","Use","Wordpress","best","practices","for","JS","and","CSS","management","Performance","tuning","with","caching","plugins","and","CDNs","Security","monitoring","and","hardening","(","Wordfence",",","etc",")","Ability","to","work","with","third-party","APIs","Input","and","output","CSV",",","Excel","and","PDF","documents","Server","Management","Maintain","Ubuntu","and","CentOS","servers",".","Provision","new","VMs","on","DigitalOcean",",","Linode","and","Peer1","AWS",":","S3","and","Cloudfront","are","musts",".","DNS","management","Monitoring","Backups","SSL","Configuration","(","A+","scores","in","SSLLabs","earn","extra","points",")","SSH","Key","access","control","for","the","team",".","Job","Perks","Full","benefits","package",",","Hardware","Credit",",","Professional","Development","Credit",",","Flexible","PTO",",","Beautiful","dog","friendly","office",",","Monthly","team","building","activities","(","indoor","sky","diving","etc",")",",","Team","lunches","on","Friday",",","Small","team","environment"])

sample23.add_entity(xrange(307,308), "tool")
sample23.add_entity(xrange(460,463), "tool")
sample23.add_entity(xrange(469,470), "tool")
sample23.add_entity(xrange(471,472), "tool")
sample23.add_entity(xrange(478,479), "tool")
sample23.add_entity(xrange(482,483), "tool")
sample23.add_entity(xrange(484,485), "tool")
sample23.add_entity(xrange(491,492), "tool")
sample23.add_entity(xrange(533,534), "tool")
sample23.add_entity(xrange(535,536), "tool")
sample23.add_entity(xrange(339,340), "language")
sample23.add_entity(xrange(341,342), "language")
sample23.add_entity(xrange(347,348), "language")
sample23.add_entity(xrange(351,352), "language")
sample23.add_entity(xrange(353,354), "language")
sample23.add_entity(xrange(361,362), "language")
sample23.add_entity(xrange(364,365), "language")
sample23.add_entity(xrange(366,367), "language")
sample23.add_entity(xrange(368,369), "language")
sample23.add_entity(xrange(371,373), "language")
sample23.add_entity(xrange(374,375), "language")
sample23.add_entity(xrange(495,496), "language")
sample23.add_entity(xrange(497,498), "language")
sample23.add_entity(xrange(520,521), "language")

# Data: Programmeur web Full Stack @ Groupe Marcelle
# URL: http:#ca.indeed.com/viewjob?jk=a45deaad72ad85c3&qd=xm-IJviY22GES7GDmn3WuXuCJ_aqYWAPn-lSt_f61w72oVtYPrSA2Pv8Q0qxbIwJm6fq9c5yEpJyzeUS7EDVQBwSQD4_FSYxr4CyE9FLpJSQhwggWUZEvHtN5OcDtAPb&indpubnum=9978236252243350&atk=1b85946klavd29p7
sample24 = ner_training_instance(["Isarta",":","www",".","isarta",".","com","Groupe","Marcelle","cherche","un","Programmeur","web","Full","Stack","Leader","au","Canada","dans","le","domaine","des","cosmétiques","et","démontrant","une","croissance","constante","depuis","les","dernières","années",",","Groupe","Marcelle","est","présentement","à","la","recherche","d","'un","Programmeur","web","Full","Stack","possédant","une","expérience","d","'au","moins","3","ans","en","développement","front-end","et","back-end",",","pour","aider","l","'équipe","d","'E-Commerce","à","maintenir","et","à","améliorer","l","'expérience","sur","nos","sites","web",",","basés","sur","Magento",".","Cette","personne","sera","responsable","des","projets","de","développements","numériques","(","nouvelles","fonctionnalités","et","debugging",")",":","évaluation",",","écriture","des","spécifications","techniques",",","développements",",","tests",",","mise","en","production",".","Le","Programmeur","web","Full","Stack","–","E-Commerce","est","rattaché","à","l","'équipe","web",",","sa","participation","est","requise","dès","le","début","des","projets","et","contribue","activement","en","collaboration","avec","les","spécialistes","web","à","la","création","des","spécifications","fonctionnelles",".","Il","joue","un","rôle","stratégique","dans","l","'orientation","et","les","choix","de","technologie","en","marketing","digital",".","RESPONSABILITÉS","Effectuer","le","développement","du","front-end","et","du","back-end","des","sites","et","des","applications","web",",","Conseiller","et","recommander","différentes","technologies","à","l","'équipe","en","fonction","des","besoins",",","Optimiser","le","code","afin","de","simplifier","le","produit","final","et","la","maintenance","future",",","Effectuer","le","contrôle","qualité","par","des","tests",",","Déployer","et","gérer","le","code","sur","différents","environnements","(","développement",",","tests",",","production",")",",","Assurer","une","maintenance","pour","résoudre","les","bugs","sur","les","installations","existantes",",","Effectuer","les","mises","à","jour","des","sites","web",",","Effectuer","le","développement","de","nouvelles","intégrations","et","modules",",","Mettre","en","place","des","APIs","entre","différents","systèmes",",","Intégrer","Magento","à","des","systèmes","de","tierces","parties",",","Travailler","en","étroite","collaboration","avec","le","graphiste","web","lors","de","la","création","de","pages",",","fonctionnalités","ou","autres",",","Travailler","en","étroite","collaboration","avec","les","équipes","à","l","'interne",",","participer","à","la","planification","de","projets","et","à","l","'amélioration","des","sites","web",".","QUALIFICATIONS","Diplôme","de","1er","cycle","informatique","ou","autre","formation","pertinente",",","Minimum","de","4","ans","d","'expérience","sur","Magento","1.x",",","Maitrise","de","PHP",",","Expertise","dans","la","mise","en","place","de","modules","Magento","personnalisables",",","Expertise","dans","la","personnalisation","de","stores","Magento","et","dans","l","'utilisation","de","thème",",","Maitrise","des","langages","HTML",",","CSS",",","JS",",","Possède","une","expérience","pertinente","dans","l","'intégration","de","Magento","avec","d","'autres","systèmes","tels","qu","'ERP",",","Logistics",",","APIs","etc",".",",","Connaissance","des","environnements","de","serveur","Linux",",","Connaissance","de","Git","et","du","système","de","mise","en","place","de","versions",",","Soucieux",")","de","livrer","une","solution","solide",",","sécuritaire",",","stable","et","performante",",","capable","de","piloter","un","projet","jusqu","'à","sa","livraison","en","respectant","des","délais",",","Curieux",",","autonome",",","débrouillard",",","Connaissance","de","Magento","Developer","Certification","(","un","atout",")",",","Experience","en","Magento","2.0","(","un","atout",")",",","A","déjà","travaillé","pour","des","entreprises","intégrant","des","solutions","certifiées","Magento","(","un","atout",")",".","Si","vous","voulez","joindre","une","équipe","dynamique","et","prospère",",","veuillez","nous","faire","parvenir","votre","curriculum","vitae","en","toute","confidentialité",".","Nous","remercions","à","l","'avance","tous","les","candidats",",","mais","seuls","les","candidats","sélectionnés","seront","contactés",".","Le","masculin","est","utilisé","dans","le","seul","but","d","'alléger","le","texte","."])

sample24.add_entity(xrange(270,271), "language")
sample24.add_entity(xrange(351,352), "language")
sample24.add_entity(xrange(361,362), "language")
sample24.add_entity(xrange(370,371), "language")
sample24.add_entity(xrange(381,382), "language")
sample24.add_entity(xrange(383,384), "language")
sample24.add_entity(xrange(385,386), "language")
sample24.add_entity(xrange(276,277), "tool")
sample24.add_entity(xrange(466,467), "tool")
sample24.add_entity(xrange(476,477), "tool")
sample24.add_entity(xrange(493,494), "tool")


# do training
trainer = ner_trainer("../MITIE/MITIE-models/english/total_word_feature_extractor.dat")

trainer.add(sample0)
trainer.add(sample1)
trainer.add(sample2)
trainer.add(sample3)
trainer.add(sample4)
trainer.add(sample5)
trainer.add(sample6)
trainer.add(sample7)
trainer.add(sample9)
trainer.add(sample10)
trainer.add(sample11)
trainer.add(sample12)
trainer.add(sample13)
trainer.add(sample14)
trainer.add(sample15)
trainer.add(sample16)
trainer.add(sample17)
trainer.add(sample18)
trainer.add(sample19)
trainer.add(sample20)
trainer.add(sample21)
trainer.add(sample22)
trainer.add(sample23)
trainer.add(sample24)

trainer.num_threads = 4

ner = trainer.train()
ner.save_to_disk("testmodel1.dat")
print ("tags:", ner.get_possible_ner_tags())
