# -*- coding: utf-8 -*-
import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
print parent
sys.path.append('/home/jayden/Documents/Hackathon/McHacks2017/MITIE/mitielib')

from mitie import *

# training on: Developer - Toronto, ON

sample = range(25);

sample[0] = ner_training_instance(["Posted","Today","–","Accepting","applications","We","'re","looking","for","an","experienced","front-end","developer","to","join","our","remote","team",".","We","work","with","all","sorts","of","clients—from","startups","to","government","agencies—to","build","engaging","sites","and","applications",".","We","love","to","work","with","people","who","are","as","excited","to","create","clean",",","functional","user","experiences","as","we","are",".","Our","ideal","colleague","can","help","us","bring","everything","from","brochure","site","designs","to","end-to-end","JavaScript","applications","to","life",".","Who","Is","Phuse","?","Phuse","is","a","remote","team","of","creatives","who","craft","websites",",","interfaces","and","brands",",","from","concept","to","completion",".","The","person","who","fills","this","position","will",":","have","excellent","communication","skills","be","motivated","to","learn","and","constantly","improve","have","plenty","of","web","development","industry","experience","be","adept","at","HTML",",","CSS","and","JavaScript","know","their","way","around","Git",",","Slack","and","Trello","be","able","to","meet","deadlines","and","interface","with","clients","be","considered","more","seriously","based","on","experience","with","server","side","languages","Job","Perks","This","position","pays","$49,000","-","$52,000","annually",".","At","Phuse",",","everyone","enjoys",":","30","hour","work","weeks","a","flexible","schedule","annual","Phuser","gathering","company-supported","growth","and","learning","opportunities","an","open","vacation","policy","home","office","stipend"])

sample[0].add_entity(xrange(71,72), "tech_skill") # JavaScript 
sample[0].add_entity(xrange(129,130), "tech_skill") # HTML 
sample[0].add_entity(xrange(131,132), "tech_skill") # CSS 
sample[0].add_entity(xrange(133,134), "tech_skill") # JavaScript 
sample[0].add_entity(xrange(138,139), "tech_skill") # Git 
sample[0].add_entity(xrange(140,141), "tech_skill") # Slack 
sample[0].add_entity(xrange(142,143), "tech_skill") # Trello 

sample[1] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","5","years","or","more","Work","Setting","Manufacture",",","Research","and","development","institution","Programming","Languages","MySQL",",","JavaScript",",","C++",",","Perl",",","Soap","Security","and","Safety","Criminal","record","check","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Repetitive","tasks",",","Handling","heavy","loads",",","Physically","demanding",",","Manual","dexterity",",","Attention","to","detail",",","Ability","to","distinguish","between","colours",",","Sound","discrimination",",","Sitting",",","Combination","of","sitting",",","standing",",","walking",",","Standing","for","extended","periods",",","Bending",",","crouching",",","kneeling",",","Tight","deadlines","Computer","and","Technology","Knowledge","Unix",",","Linux",",","Intranet",",","Programming","software",",","Software","development",",","Multimedia","software","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Accurate",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Judgement",",","Organized"])

sample[1].add_entity(xrange(21,22), "tech_skill") # MySQL 
sample[1].add_entity(xrange(23,24), "tech_skill") # JavaScript 
sample[1].add_entity(xrange(25,26), "tech_skill") # C++ 
sample[1].add_entity(xrange(27,28), "tech_skill") # Perl 
sample[1].add_entity(xrange(101,102), "tech_skill") # Unix 
sample[1].add_entity(xrange(103,104), "tech_skill") # Linux 

sample[2] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","or","equivalent","experience","Credentials","(","certificates",",","licences",",","memberships",",","courses",",","etc",".",")","Not","required",",","Not","applicable","Experience","5","years","or","more","Work","Setting","Computer","hardware","or","software","retailer",",","wholesaler","Specific","Skills","Write",",","modify",",","integrate","and","test","software","code",",","Identify","and","communicate","technical","problems",",","processes","and","solutions",",","Prepare","reports",",","manuals","and","other","documentation","on","the","status",",","operation","and","maintenance","of","software",",","Assist","in","the","collection","and","documentation","of","user","'s","requirements",",","Assist","in","the","development","of","logical","and","physical","specifications",",","Research","and","evaluate","a","variety","of","software","products",",","Program","special","effects","software","for","film","and","video","applications",",","Maintain","existing","computer","programs","by","making","modifications","as","required",",","Write",",","modify",",","integrate","and","test","software","code","for","e-commerce","and","other","Internet","applications","Programming","Languages","XML",",","XSL",",","Object-Oriented","programming","languages",",","MySQL",",","Java",",","JavaScript",",","JSP",",","HTML",",","CSS",",","XML","Technology","(","XSL",",","XSD",",","DTD",")",",","SQL",",","Soap",",","Ajax",",","JQuery",",","React",".","js",",","Angular",".","js",",","CoffeeScript",",","Git",",","Groovy",",","Grunt",".","js",",","Gulp",",","Hadoop","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Repetitive","tasks",",","Attention","to","detail",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Word","processing","software",",","Unix",",","Linux",",","Internet",",","Database","software",",","MAC",",","JavaOS",",","Extranet",",","Intranet",",","Security","software",",","Programming","software",",","Software","development",",","Data","analysis","software",",","Mapping","and","data","visualization","software",",","Website","creation","and","management","software",",","Enterprise","Applications","Integration","(","EAI",")","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Accurate",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Judgement",",","Organized"])

# sample[2].add_entity(xrange(147,148), "tech_skill") # XML 
# sample[2].add_entity(xrange(149,150), "tech_skill") # XSL 
# sample[2].add_entity(xrange(151,153), "tech_skill") # Object-Oriented programming 
sample[2].add_entity(xrange(155,156), "tech_skill") # MySQL 
sample[2].add_entity(xrange(157,158), "tech_skill") # Java 
sample[2].add_entity(xrange(159,160), "tech_skill") # JavaScript 
sample[2].add_entity(xrange(161,162), "tech_skill") # JSP 
sample[2].add_entity(xrange(163,164), "tech_skill") # HTML 
sample[2].add_entity(xrange(165,166), "tech_skill") # CSS 
# sample[2].add_entity(xrange(167,168), "tech_skill") # XML 
# sample[2].add_entity(xrange(170,171), "tech_skill") # XSL 
# sample[2].add_entity(xrange(172,173), "tech_skill") # XSD 
# sample[2].add_entity(xrange(174,175), "tech_skill") # DTD 
sample[2].add_entity(xrange(177,178), "tech_skill") # SQL 
sample[2].add_entity(xrange(179,180), "tech_skill") # Soap 
sample[2].add_entity(xrange(181,182), "tech_skill") # Ajax 
sample[2].add_entity(xrange(183,184), "tech_skill") # JQuery 
sample[2].add_entity(xrange(185,186), "tech_skill") # React . js 
sample[2].add_entity(xrange(189,190), "tech_skill") # Angular . js 
sample[2].add_entity(xrange(193,194), "tech_skill") # CoffeeScript 
sample[2].add_entity(xrange(195,196), "tech_skill") # Git 
sample[2].add_entity(xrange(197,198), "tech_skill") # Groovy 
sample[2].add_entity(xrange(199,200), "tech_skill") # Grunt . js 
sample[2].add_entity(xrange(203,204), "tech_skill") # Gulp 
sample[2].add_entity(xrange(205,206), "tech_skill") # Hadoop 
sample[2].add_entity(xrange(237,238), "tech_skill") # Unix 
sample[2].add_entity(xrange(239,240), "tech_skill") # Linux 
# sample[2].add_entity(xrange(243,245), "tech_skill") # Database software 
sample[2].add_entity(xrange(246,247), "tech_skill") # MAC 
sample[2].add_entity(xrange(248,249), "tech_skill") # JavaOS 

sample[3] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","3","years","to","less","than","5","years","Applications","Adobe","Illustrator",",","Adobe","Photoshop",",","Flash","Work","Setting","Consulting","firm","Specific","Skills","Write",",","modify",",","integrate","and","test","software","code",",","Identify","and","communicate","technical","problems",",","processes","and","solutions",",","Prepare","reports",",","manuals","and","other","documentation","on","the","status",",","operation","and","maintenance","of","software",",","Assist","in","the","collection","and","documentation","of","user","'s","requirements",",","Research","and","evaluate","a","variety","of","software","products",",","Maintain","existing","computer","programs","by","making","modifications","as","required",",","Write",",","modify",",","integrate","and","test","software","code","for","e-commerce","and","other","Internet","applications",",","Program","animation","software","to","predefined","specifications","for","interactive","CDs",",","DVDs",",","video","game","cartridges","and","Internet-based","applications","Programming","Languages","XML",",","PHP",",","Object-Oriented","programming","languages",",","JavaScript",",","HTML",",","CSS",",","Ajax",",","JQuery",",","React",".","js",",","SASS",",","Angular",".","js",",","CoffeeScript",",","D3",",","Git",",","Grunt",".","js",",","Gulp","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Repetitive","tasks",",","Attention","to","detail",",","Combination","of","sitting",",","standing",",","walking",",","Tight","deadlines","Work","Location","Information","Relocation","costs","not","covered","by","employer","Computer","and","Technology","Knowledge","Word","processing","software",",","Unix",",","MS","Windows",",","Linux",",","Internet",",","MAC",",","Intranet",",","Servers",",","File","management","software",",","Presentation","software",",","Mail","server","software",",","Communication","software",",","Image","editing","software",",","Programming","software",",","HTML","editing","software",",","Web","service","design",",","Desktop","publishing","software",",","Software","development",",","Website","creation","and","management","software",",","MS","Office",",","Business","diagram","software",",","Multimedia","software",",","API","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Accurate",",","Team","player",",","Excellent","oral","communication",",","Client","focus",",","Judgement",",","Organized"])

sample[3].add_entity(xrange(15,17), "tech_skill") # Adobe Illustrator 
sample[3].add_entity(xrange(18,20), "tech_skill") # Adobe Photoshop 
sample[3].add_entity(xrange(21,22), "tech_skill") # Flash 
# sample[3].add_entity(xrange(131,132), "tech_skill") # XML 
sample[3].add_entity(xrange(133,134), "tech_skill") # PHP 
# sample[3].add_entity(xrange(135,137), "tech_skill") # Object-Oriented programming 
sample[3].add_entity(xrange(139,140), "tech_skill") # JavaScript 
sample[3].add_entity(xrange(141,142), "tech_skill") # HTML 
sample[3].add_entity(xrange(143,144), "tech_skill") # CSS 
sample[3].add_entity(xrange(145,146), "tech_skill") # Ajax 
sample[3].add_entity(xrange(147,148), "tech_skill") # JQuery 
sample[3].add_entity(xrange(149,150), "tech_skill") # React . js 
sample[3].add_entity(xrange(153,154), "tech_skill") # SASS 
sample[3].add_entity(xrange(155,156), "tech_skill") # Angular . js 
sample[3].add_entity(xrange(159,160), "tech_skill") # CoffeeScript 
sample[3].add_entity(xrange(161,162), "tech_skill") # D3 
sample[3].add_entity(xrange(163,164), "tech_skill") # Git 
sample[3].add_entity(xrange(165,166), "tech_skill") # Grunt . js 
sample[3].add_entity(xrange(169,170), "tech_skill") # Gulp 
sample[3].add_entity(xrange(216,217), "tech_skill") # Unix 
sample[3].add_entity(xrange(219,220), "tech_skill") # Windows 
sample[3].add_entity(xrange(221,222), "tech_skill") # Linux 
sample[3].add_entity(xrange(225,226), "tech_skill") # MAC 
sample[3].add_entity(xrange(252,253), "tech_skill") # HTML 

sample[4] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","or","equivalent","experience","Experience","2","years","to","less","than","3","years","Applications","Adobe","Illustrator",",","Adobe","Photoshop","Work","Setting","Computer","hardware","or","software","retailer",",","wholesaler","Programming","Languages","XML",",","Visual","Basic",",","Object-Oriented","programming","languages",",","MySQL",",","Java",",","JavaScript",",","HTML",",","CSS",",","ASP",",","JQuery","Own","Tools",",","Equipment","Computer","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Attention","to","detail",",","Ability","to","distinguish","between","colours",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Spreadsheet",",","Internet",",","Database","software",",","JavaOS",",","File","management","software",",","Image","editing","software",",","Project","management","software",",","Programming","software",",","HTML","editing","software",",","Software","development",",","Mapping","and","data","visualization","software",",","Website","creation","and","management","software",",","MS","Office",",","Desktop","applications",",","C#",",",".","NET","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Client","focus",",","Dependability",",","Organized"])

sample[4].add_entity(xrange(18,20), "tech_skill") # Adobe Illustrator 
sample[4].add_entity(xrange(21,23), "tech_skill") # Adobe Photoshop 
# sample[4].add_entity(xrange(34,35), "tech_skill") # XML 
sample[4].add_entity(xrange(36,38), "tech_skill") # Visual Basic 
# sample[4].add_entity(xrange(39,41), "tech_skill") # Object-Oriented programming 
sample[4].add_entity(xrange(43,44), "tech_skill") # MySQL 
sample[4].add_entity(xrange(45,46), "tech_skill") # Java 
sample[4].add_entity(xrange(47,48), "tech_skill") # JavaScript 
sample[4].add_entity(xrange(49,50), "tech_skill") # HTML 
sample[4].add_entity(xrange(51,52), "tech_skill") # CSS 
sample[4].add_entity(xrange(53,54), "tech_skill") # ASP 
sample[4].add_entity(xrange(55,56), "tech_skill") # JQuery 
sample[4].add_entity(xrange(98,99), "tech_skill") # JavaOS 
sample[4].add_entity(xrange(115,116), "tech_skill") # HTML 
sample[4].add_entity(xrange(140,141), "tech_skill") # C# 
sample[4].add_entity(xrange(142,144), "tech_skill") # . NET 

sample[5] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","3","years","to","less","than","5","years","Specific","Skills","Research","and","evaluate","a","variety","of","interactive","media","software","products",",","Prepare","mock-ups","and","storyboards",",","Consult","with","clients","to","develop","and","document","Website","requirements",",","Lead","and","co-ordinate","multidisciplinary","teams","to","develop","Website","graphics",",","content",",","capacity","and","interactivity",",","Source",",","select","and","organize","information","for","inclusion","and","design","the","appearance",",","layout","and","flow","of","the","Website",",","Create","and","optimize","content","for","Website","using","a","variety","of","graphics",",","database",",","animation","and","other","software",",","Develop","Website","architecture","and","determine","hardware","and","software","requirements",",","Plan",",","design",",","write",",","modify",",","integrate","and","test","Web-site","related","code",",","Conduct","tests","and","perform","security","and","quality","controls","Programming","Languages","MySQL",",","Java",",","HTML",",","DHTML","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Organized"])

sample[5].add_entity(xrange(132,133), "tech_skill") # MySQL 
sample[5].add_entity(xrange(134,135), "tech_skill") # Java 
sample[5].add_entity(xrange(136,137), "tech_skill") # HTML 

sample[6] = ner_training_instance(["Temporary","Database",",","Web","Developer","(","6","months",")"])


sample[7] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","3","years","to","less","than","5","years","Work","Setting","Consulting","firm","Specific","Skills","Write",",","modify",",","integrate","and","test","software","code",",","Identify","and","communicate","technical","problems",",","processes","and","solutions",",","Prepare","reports",",","manuals","and","other","documentation","on","the","status",",","operation","and","maintenance","of","software",",","Assist","in","the","collection","and","documentation","of","user","'s","requirements",",","Assist","in","the","development","of","logical","and","physical","specifications",",","Research","and","evaluate","a","variety","of","software","products",",","Maintain","existing","computer","programs","by","making","modifications","as","required",",","Write",",","modify",",","integrate","and","test","software","code","for","e-commerce","and","other","Internet","applications","Programming","Languages","Java","Security","and","Safety","Basic","security","clearance","Own","Tools",",","Equipment","Cellular","phone","Transportation",",","Travel","Information","Willing","to","travel","regularly",",","Willing","to","travel","for","extended","periods",",","Travel","expenses","paid","by","employer",",","Public","transportation","is","available","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Repetitive","tasks",",","Attention","to","detail",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Unix",",","MS","Windows",",","Linux",",","JavaOS",",","MS","Office","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Accurate",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Judgement",",","Organized"])

sample[7].add_entity(xrange(114,115), "tech_skill") # Java 
sample[7].add_entity(xrange(180,181), "tech_skill") # Unix 
sample[7].add_entity(xrange(183,184), "tech_skill") # Windows 
sample[7].add_entity(xrange(185,186), "tech_skill") # Linux 
sample[7].add_entity(xrange(187,188), "tech_skill") # JavaOS 

sample[8] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","3","years","to","less","than","5","years","Additional","Skills","Oracle","Work","Setting","Consulting","firm","Specific","Skills","Write",",","modify",",","integrate","and","test","software","code",",","Identify","and","communicate","technical","problems",",","processes","and","solutions",",","Prepare","reports",",","manuals","and","other","documentation","on","the","status",",","operation","and","maintenance","of","software",",","Assist","in","the","collection","and","documentation","of","user","'s","requirements",",","Assist","in","the","development","of","logical","and","physical","specifications",",","Research","and","evaluate","a","variety","of","software","products",",","Maintain","existing","computer","programs","by","making","modifications","as","required",",","Write",",","modify",",","integrate","and","test","software","code","for","e-commerce","and","other","Internet","applications","Programming","Languages","Java",",","JavaScript",",","JSP",",","SQL",",","Soap","Security","and","Safety","Basic","security","clearance","Own","Tools",",","Equipment","Cellular","phone","Transportation",",","Travel","Information","Willing","to","travel","regularly",",","Willing","to","travel","for","extended","periods",",","Travel","expenses","paid","by","employer",",","Public","transportation","is","available","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Repetitive","tasks",",","Attention","to","detail",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Unix",",","MS","Windows",",","JavaOS",",","MS","Office","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Accurate",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Judgement",",","Organized"])

sample[8].add_entity(xrange(117,118), "tech_skill") # Java 
sample[8].add_entity(xrange(119,120), "tech_skill") # JavaScript 
sample[8].add_entity(xrange(121,122), "tech_skill") # JSP 
sample[8].add_entity(xrange(123,124), "tech_skill") # SQL 
sample[8].add_entity(xrange(125,126), "tech_skill") # Soap 
sample[8].add_entity(xrange(191,192), "tech_skill") # Unix 
sample[8].add_entity(xrange(194,195), "tech_skill") # Windows 

sample[9] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","3","years","to","less","than","5","years","Work","Setting","Telecommunications","industry","Specific","Skills","Write",",","modify",",","integrate","and","test","software","code",",","Identify","and","communicate","technical","problems",",","processes","and","solutions",",","Prepare","reports",",","manuals","and","other","documentation","on","the","status",",","operation","and","maintenance","of","software",",","Assist","in","the","collection","and","documentation","of","user","'s","requirements",",","Assist","in","the","development","of","logical","and","physical","specifications",",","Maintain","existing","computer","programs","by","making","modifications","as","required","Programming","Languages","Visual","Basic",",","Visual","C++",",","MFC",",","VB","Script",",","Object-Oriented","programming","languages",",","Java",",","JavaScript",",","HTML",",","C",",","C++",",","XML","Technology","(","XSL",",","XSD",",","DTD",")",",","SQL","Transportation",",","Travel","Information","Own","transportation",",","Own","vehicle",",","Willing","to","travel","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Attention","to","detail",",","Sitting",",","Tight","deadlines","Computer","and","Technology","Knowledge","Linux",",","JavaOS",",","Device","drivers",",","Networking","software",",","Networking","hardware",",","Networking","security",",","Intranet",",","Servers",",","Communication","software",",","Software","development","Personal","Suitability","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus"])

sample[9].add_entity(xrange(89,91), "tech_skill") # Visual Basic 
sample[9].add_entity(xrange(93,94), "tech_skill") # C++ 
sample[9].add_entity(xrange(95,96), "tech_skill") # MFC 
sample[9].add_entity(xrange(97,99), "tech_skill") # VB Script 
# sample[9].add_entity(xrange(100,102), "tech_skill") # Object-Oriented programming 
sample[9].add_entity(xrange(104,105), "tech_skill") # Java 
sample[9].add_entity(xrange(106,107), "tech_skill") # JavaScript 
sample[9].add_entity(xrange(108,109), "tech_skill") # HTML 
sample[9].add_entity(xrange(110,111), "tech_skill") # C 
sample[9].add_entity(xrange(112,113), "tech_skill") # C++ 
# sample[9].add_entity(xrange(114,115), "tech_skill") # XML 
# sample[9].add_entity(xrange(117,118), "tech_skill") # XSL 
# sample[9].add_entity(xrange(119,120), "tech_skill") # XSD 
# sample[9].add_entity(xrange(121,122), "tech_skill") # DTD 
sample[9].add_entity(xrange(124,125), "tech_skill") # SQL 
sample[9].add_entity(xrange(162,163), "tech_skill") # Linux 
sample[9].add_entity(xrange(164,165), "tech_skill") # JavaOS 

sample[10] = ner_training_instance(["Hiring","Full-stack",".","NET","Developers","(","Full-time",")","in","Toronto",",","ON","!","This","is","an","opportunity","to","work","in","a","complex","environment","as","part","of","a","fast-paced","and","talented","dev","team","on","a","cloud-","based","SaaS","solutions","environment",".","To","fill","this","role",",","you","must","have","strong","passion","and","skill","for",".","NET","web","development",".","Perks","You","'ll","Love","•","Collaborative","work","culture","•","Flex","hours","•","Fun","team","activities",",","such","as","lunch","parties",",","bowling",",","and","archery","Required","Skills","&","Experience","•","You","must","be","an","expert","at",":","•","C#","6.0","&",".","NET","4.6.","•","ASP",".","NET","4.5","(","ASP",".","NET","MVC",",","WebAPI",")",".","•","JavaScript-5","and","AngularJS",".","•","T-SQL","skills","targeting","SQL","Server","2016.","•","Links","to","code","samples","(","ex",".","Github","profile",")","are","a","plus","!","!","!","•","Communication","skills","(","written","and","verbal",")","•","University","Degree","in","Computer","Sciences","(","or","similar",")","Other","Experience","Pluses","•","Practical","skills","with","DOM",",","HTML5,","and","CSS","•","Any","ORM","or","micro-ORM","experience","•","Other","front-end","frameworks","(","React",",","KnockoutJS",",","Backbone",",","etc",")","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample[10].add_entity(xrange(2,4), "tech_skill") # . NET 
sample[10].add_entity(xrange(53,55), "tech_skill") # . NET 
sample[10].add_entity(xrange(96,97), "tech_skill") # C# 
sample[10].add_entity(xrange(99,101), "tech_skill") # . NET 
sample[10].add_entity(xrange(103,106), "tech_skill") # ASP . NET 
sample[10].add_entity(xrange(108,112), "tech_skill") # ASP . NET MVC 
sample[10].add_entity(xrange(113,114), "tech_skill") # WebAPI 
sample[10].add_entity(xrange(117,118), "tech_skill") # JavaScript-5 
sample[10].add_entity(xrange(119,120), "tech_skill") # AngularJS 
# sample[10].add_entity(xrange(122,123), "tech_skill") # T-SQL 
sample[10].add_entity(xrange(125,126), "tech_skill") # SQL 
sample[10].add_entity(xrange(136,137), "tech_skill") # Github 
sample[10].add_entity(xrange(172,173), "tech_skill") # HTML5, 
sample[10].add_entity(xrange(174,175), "tech_skill") # CSS 
sample[10].add_entity(xrange(177,178), "tech_skill") # ORM 
sample[10].add_entity(xrange(186,187), "tech_skill") # React 
sample[10].add_entity(xrange(188,189), "tech_skill") # KnockoutJS 
sample[10].add_entity(xrange(190,191), "tech_skill") # Backbone 

sample[11] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","5","years","or","more","Additional","Skills","JDBC",",","Database","development",",","Computer","science","Work","Setting","Computer","hardware","or","software","retailer",",","wholesaler","Specific","Skills","Write",",","modify",",","integrate","and","test","software","code",",","Identify","and","communicate","technical","problems",",","processes","and","solutions",",","Assist","in","the","collection","and","documentation","of","user","'s","requirements",",","Assist","in","the","development","of","logical","and","physical","specifications",",","Research","and","evaluate","a","variety","of","software","products",",","Maintain","existing","computer","programs","by","making","modifications","as","required","Programming","Languages","Servlet",",","Object-Oriented","programming","languages",",","Java",",","JavaScript",",","JSP",",","CSS",",","COM",",","COM+",",","DCOM",",","MTS",",","ActiveX",",","C",",","C++",",","Applet",",","XML","Technology","(","XSL",",","XSD",",","DTD",")",",","SQL",",","Coldfusion",",","Soap",",","Ajax",",","JQuery",",","C#",",","Groovy","Own","Tools",",","Equipment","Internet","access",",","Cellular","phone","Transportation",",","Travel","Information","Willing","to","travel",",","Willing","to","travel","cross-border",",","Willing","to","travel","overnight",",","Travel","expenses","paid","by","employer","Work","Conditions","and","Physical","Capabilities","Fast-paced","environment",",","Work","under","pressure",",","Attention","to","detail",",","Combination","of","sitting",",","standing",",","walking",",","Tight","deadlines","Computer","and","Technology","Knowledge","Word","processing","software",",","Unix",",","Spreadsheet",",","MS","Windows",",","Linux",",","Internet",",","MAC",",","JavaOS",",","Device","drivers",",","Networking","software",",","Networking","hardware",",","Networking","security",",","Extranet",",","Intranet",",","Servers",",","File","management","software",",","Presentation","software",",","Project","management","software",",","Programming","software",",","HTML","editing","software",",","Web","service","design",",","Software","development",",","Data","analysis","software",",","Mapping","and","data","visualization","software",",","Website","creation","and","management","software",",","MS","Office",",","Business","diagram","software",",","API","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Judgement",",","Organized"])

sample[11].add_entity(xrange(94,96), "tech_skill") # Object-Oriented programming 
sample[11].add_entity(xrange(98,99), "tech_skill") # Java 
sample[11].add_entity(xrange(100,101), "tech_skill") # JavaScript 
sample[11].add_entity(xrange(102,103), "tech_skill") # JSP 
sample[11].add_entity(xrange(104,105), "tech_skill") # CSS 
# sample[11].add_entity(xrange(106,107), "tech_skill") # COM 
# sample[11].add_entity(xrange(108,109), "tech_skill") # COM+ 
# sample[11].add_entity(xrange(110,111), "tech_skill") # DCOM 
# sample[11].add_entity(xrange(112,113), "tech_skill") # MTS 
# sample[11].add_entity(xrange(114,115), "tech_skill") # ActiveX 
sample[11].add_entity(xrange(116,117), "tech_skill") # C 
sample[11].add_entity(xrange(118,119), "tech_skill") # C++ 
# sample[11].add_entity(xrange(120,121), "tech_skill") # Applet 
# sample[11].add_entity(xrange(122,123), "tech_skill") # XML 
# sample[11].add_entity(xrange(125,126), "tech_skill") # XSL 
# sample[11].add_entity(xrange(127,128), "tech_skill") # XSD 
# sample[11].add_entity(xrange(129,130), "tech_skill") # DTD 
sample[11].add_entity(xrange(132,133), "tech_skill") # SQL 
sample[11].add_entity(xrange(134,135), "tech_skill") # Coldfusion 
sample[11].add_entity(xrange(136,137), "tech_skill") # Soap 
sample[11].add_entity(xrange(138,139), "tech_skill") # Ajax 
sample[11].add_entity(xrange(140,141), "tech_skill") # JQuery 
sample[11].add_entity(xrange(142,143), "tech_skill") # C# 
sample[11].add_entity(xrange(144,145), "tech_skill") # Groovy 
sample[11].add_entity(xrange(211,212), "tech_skill") # Unix 
sample[11].add_entity(xrange(216,217), "tech_skill") # Windows 
sample[11].add_entity(xrange(218,219), "tech_skill") # Linux 
sample[11].add_entity(xrange(222,223), "tech_skill") # MAC 
sample[11].add_entity(xrange(224,225), "tech_skill") # JavaOS 
sample[11].add_entity(xrange(292,293), "tech_skill") # API 

sample[12] = ner_training_instance(["Hiring","an","Angular","Full","Stack","Developer","(","Full-time",")","in","Toronto",",","ON","!","As","an","Angular","Developer","you","'ll","be","tasked","with","working","on","both","the","front","end","and","back","end","of","our","client","'s","web","applications",".","Working","within","the","software","development","team",",","your","duties","will","require","you","to","assist","in","the","development","and","architecture","of","enterprise","applications",".","This","role","is","ideal","for","ambitious","developers","who","feel","confident","in","their","technical","ability","and","want","to","be","a","part","of","the","highly-skilled","development","team",".","Perks","You","'ll","Love","•","Competitive","salary","and","benefits","•","Great","culture","that","is","facilitative","to","learning","•","Internal","Hackathons",",","Team","and","Training","Events","Main","Requirements","&","Responsibilities","•","Degree","in","Computer","Science",",","Computer","Engineering",",","or","equivalent","life","experience","•","Minimum","3-5","years","in","enterprise","web","development",",","specifically","NodeJS","•","Strong","foundation","in","JavaScript",",","and","min","1-2","years","experience","with","AngularJS",",","ReactJS","•","Strong","knowledge","of","HTML","5","and","web","fundamentals","(","CSS",",","HTTP",",","security",",","performance",",","etc",".",")","•","Strong","knowledge","of","Java","and",",","or",".","NET","is","an","asset","•","Experience","in","consulting","onsite","with","clients","is","an","asset","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample[12].add_entity(xrange(2,3), "tech_skill") # Angular 
sample[12].add_entity(xrange(16,17), "tech_skill") # Angular 
sample[12].add_entity(xrange(140,141), "tech_skill") # NodeJS 
sample[12].add_entity(xrange(145,146), "tech_skill") # JavaScript 
sample[12].add_entity(xrange(153,154), "tech_skill") # AngularJS 
sample[12].add_entity(xrange(155,156), "tech_skill") # ReactJS 
sample[12].add_entity(xrange(160,162), "tech_skill") # HTML 5 
sample[12].add_entity(xrange(166,167), "tech_skill") # CSS 
sample[12].add_entity(xrange(168,169), "tech_skill") # HTTP 
sample[12].add_entity(xrange(181,182), "tech_skill") # Java 
sample[12].add_entity(xrange(185,187), "tech_skill") # . NET 

sample[13] = ner_training_instance(["Our","client",",","a","rapidly","growing","start-up","here","in","Toronto",",","is","looking","for","talented","Mobile","Developers","to","join","their","team",".","You","will","work","alongside","people","who","are","innovative","and","passionate","about","what","they","do-","building","cutting-edge",",","applications","and","experiences",".","What","you","bring","to","the","table",":","•","You","are","very","smart",",","but","humble","•","You","thrive","in","an","environment","that","is","agile","and","challenging","•","Making","an","impact","on","projects","is","a","driving","force","for","you","•","Computer","Science","Degree","or","equivalent","experience","Technology","you","use",":","•","Experience","with","Objective-C","or","Java","•","Android","and",",","or","iOS","development","experience","•","Ability","to","debug","and","test","code","•","Previous","experience","with","C",",","C++","or","C#","is","an","asset","•","Great","communication","skills","Hot","Job","Facts",":","•","Work","on","next","generation","smart","products","•","Start-up","culture","•","Dynamic","team","with","leading","industry","experience","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample[13].add_entity(xrange(95,96), "tech_skill") # Objective-C 
sample[13].add_entity(xrange(97,98), "tech_skill") # Java 
sample[13].add_entity(xrange(99,100), "tech_skill") # Android 
sample[13].add_entity(xrange(103,104), "tech_skill") # iOS 
sample[13].add_entity(xrange(117,118), "tech_skill") # C 
sample[13].add_entity(xrange(119,120), "tech_skill") # C++ 
sample[13].add_entity(xrange(121,122), "tech_skill") # C# 

sample[14] = ner_training_instance(["We","are","currently","looking","for","a","Full","Stack","Developer","with","React",",","Python","and","HTML",",","Javascript","and","CSS",".","Must","have","3","years","experience","with","each","skillset",".","This","is","a","contract","engagement","to","work","on","a","team","of","4","full","stack","web","developers",".","While","we","appreciate","all","interest",",","only","those","candidates","selected","for","an","interview","will","be","contacted","."])

sample[14].add_entity(xrange(10,11), "tech_skill") # React 
sample[14].add_entity(xrange(12,13), "tech_skill") # Python 
sample[14].add_entity(xrange(14,15), "tech_skill") # HTML 
sample[14].add_entity(xrange(16,17), "tech_skill") # Javascript 
sample[14].add_entity(xrange(18,19), "tech_skill") # CSS 

sample[15] = ner_training_instance(["Hiring","Full","Stack","Rails","Developer","(","Full-time",")","in","Toronto",",","ON","!","As","an","experienced","Full","Stack","Rails","Developer",",","you","will","assist","our","client","in","revolutionizing","its","growing","industry",".","Have","you","worked","on","large","scale","SaaS","applications","?","Do","you","find","it","tough","to","sleep","at","night","without","proper","test","coverage","?","Do","you","grow","software","through","Agile","Methodologies","such","as","TDD",",","continuous","integration",",","and","MVP","?","This","role","is","ideal","for","ambitious","developers","who","feel","confident","in","their","technical","ability","and","want","to","be","a","part","of","the","highly-skilled","development","team",".","Perks","You","'ll","Love","Competitive","salary","and","full","benefits","Great","culture","that","is","facilitative","to","learning","Internal","Hackathons",",","Team","and","Training","Events","Required","Skills","&","Background","Ruby","on","Rails","Javascript","Test","Driven","Development","Experience","with","dev-ops","(","AWS",",","Linode",",","etc",")","Exceptional","communication","skills","Skills","We","'d","Love","To","See","Angular","Mobile","application","development","Data","Warehouse","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample[15].add_entity(xrange(3,4), "tech_skill") # Rails 
sample[15].add_entity(xrange(60,61), "tech_skill") # Agile 
# sample[15].add_entity(xrange(64,65), "tech_skill") # TDD 
sample[15].add_entity(xrange(125,128), "tech_skill") # Ruby on Rails 
sample[15].add_entity(xrange(128,129), "tech_skill") # Javascript 
sample[15].add_entity(xrange(136,137), "tech_skill") # AWS 
sample[15].add_entity(xrange(138,139), "tech_skill") # Linode 
sample[15].add_entity(xrange(151,152), "tech_skill") # Angular 

sample[16] = ner_training_instance(["Languages","English","Education","Bachelor","'s","degree","Experience","2","years","to","less","than","3","years","Applications","Adobe","Acrobat","Reader",",","Adobe","Illustrator",",","Adobe","Photoshop",",","Shockwave",",","Flash",",","Corel","Draw",",","Adobe","Dreamweaver",",","Adobe","Premiere","Pro","Specific","Skills","Research","and","evaluate","a","variety","of","interactive","media","software","products",",","Prepare","mock-ups","and","storyboards",",","Consult","with","clients","to","develop","and","document","Website","requirements",",","Lead","and","co-ordinate","multidisciplinary","teams","to","develop","Website","graphics",",","content",",","capacity","and","interactivity",",","Source",",","select","and","organize","information","for","inclusion","and","design","the","appearance",",","layout","and","flow","of","the","Website",",","Create","and","optimize","content","for","Website","using","a","variety","of","graphics",",","database",",","animation","and","other","software",",","Develop","Website","architecture","and","determine","hardware","and","software","requirements",",","Plan",",","design",",","write",",","modify",",","integrate","and","test","Web-site","related","code",",","Conduct","tests","and","perform","security","and","quality","controls","Programming","Languages","PHP",",","MySQL","Computer","and","Technology","Knowledge","Word","processing","software",",","Unix",",","Spreadsheet",",","MS","Windows",",","Linux",",","Internet",",","Database","software",",","MAC",",","JavaOS",",","Device","drivers",",","Networking","software",",","Networking","hardware",",","Networking","security",",","Intranet",",","Servers",",","File","management","software",",","Security","software",",","Presentation","software",",","Mail","server","software",",","Communication","software",",","3D","graphic","software",",","Image","editing","software",",","Project","management","software",",","Programming","software",",","HTML","editing","software",",","Web","service","design",",","Programming","languages",",","Software","development",",","Mapping","and","data","visualization","software",",","Website","creation","and","management","software",",","MS","Office",",","Desktop","applications",",","Multimedia","software",",","Computer-aided","design","(","CAD",")",",","C#",",",".","NET",",","API","Personal","Suitability","Initiative",",","Effective","interpersonal","skills",",","Team","player",",","Excellent","oral","communication",",","Excellent","written","communication",",","Client","focus",",","Dependability",",","Judgement",",","Organized"])

# sample[16].add_entity(xrange(15,18), "tech_skill") # Adobe Acrobat Reader 
# sample[16].add_entity(xrange(19,21), "tech_skill") # Adobe Illustrator 
# sample[16].add_entity(xrange(22,24), "tech_skill") # Adobe Photoshop 
sample[16].add_entity(xrange(25,26), "tech_skill") # Shockwave 
sample[16].add_entity(xrange(27,28), "tech_skill") # Flash 
# sample[16].add_entity(xrange(29,31), "tech_skill") # Corel Draw 
# sample[16].add_entity(xrange(32,34), "tech_skill") # Adobe Dreamweaver 
# sample[16].add_entity(xrange(35,38), "tech_skill") # Adobe Premiere Pro 
sample[16].add_entity(xrange(156,157), "tech_skill") # PHP 
sample[16].add_entity(xrange(158,159), "tech_skill") # MySQL 
sample[16].add_entity(xrange(167,168), "tech_skill") # Unix 
sample[16].add_entity(xrange(172,173), "tech_skill") # Windows 
sample[16].add_entity(xrange(174,175), "tech_skill") # Linux 
sample[16].add_entity(xrange(181,182), "tech_skill") # MAC 
sample[16].add_entity(xrange(183,184), "tech_skill") # JavaOS 
sample[16].add_entity(xrange(233,234), "tech_skill") # HTML 
sample[16].add_entity(xrange(271,272), "tech_skill") # CAD 
sample[16].add_entity(xrange(274,275), "tech_skill") # C# 
sample[16].add_entity(xrange(276,278), "tech_skill") # . NET 
sample[16].add_entity(xrange(279,280), "tech_skill") # API 

sample[17] = ner_training_instance(["Hiring","a","Front","End","Developer","(","Full-time",")","in","Toronto",",","ON","!","Our","client","based","out","of","midtown","Toronto","is","looking","for","a","Front","End","Developer","that","passionate","about","emerging","platforms","and","technologies",".","This","role","will","execute","front-end","Javascript-based","interfaces","and","design","patterns",",","developing","them","into","packages","to","be","implemented","across","a","suite","of","SaaS","WiFi","offerings",".","Perks","You","'ll","Love","Join","a","creative","agile","environment","with","plenty","of","internal","growth","opportunities","Casual","office","environment","&","great","team","Enjoy","having","no","dress","code","and","the","free","beer","in","the","fridge","Responsibilities","&","Required","Experience","Expert","in","Javascript",",","preferably","with","either","major","framework","(","Angular",".","js","or","Backbone",".","js",")","Expert","knowledge","of","minimalist","interface","design","in","CSS",",","HTML","(","4+","years",")","Strong","knowledge","of","source","control","management","systems","(","Git",")","Advanced","knowledge","of","JQuery",",","WebSockets",",","Ajax",",","Web","Services","You","are","very","comfortable","within","a","Linux","Shell","environment","Familiarity","with","base","suite","of","Amazon","Web","Services","Familiarity","with","WiFi","Access","Systems","You","are","highly","organized","and","have","the","ability","to","self-manage","&","achieve","deadlines","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

# sample[17].add_entity(xrange(68,69), "tech_skill") # agile 
sample[17].add_entity(xrange(100,101), "tech_skill") # Javascript 
sample[17].add_entity(xrange(108,109), "tech_skill") # Angular . js 
sample[17].add_entity(xrange(112,113), "tech_skill") # Backbone . js 
sample[17].add_entity(xrange(123,124), "tech_skill") # CSS 
sample[17].add_entity(xrange(125,126), "tech_skill") # HTML 
sample[17].add_entity(xrange(138,139), "tech_skill") # Git 
sample[17].add_entity(xrange(143,144), "tech_skill") # JQuery 
sample[17].add_entity(xrange(145,146), "tech_skill") # WebSockets 
sample[17].add_entity(xrange(147,148), "tech_skill") # Ajax 
# sample[17].add_entity(xrange(149,151), "tech_skill") # Web Services 
# sample[17].add_entity(xrange(157,159), "tech_skill") # Linux Shell 
# sample[17].add_entity(xrange(165,168), "tech_skill") # Amazon Web Services 

sample[18] = ner_training_instance(["We","are","seeking","a","Web","Developer","with","HTML",",","CSS",",","Bootstrap",",","&","Angular",".","2","years","of","HTML","&","CSS","exp","is","expected","and","knowledge","of","Angular",",","Bootstrap","&","Javascript","an","asset",".","Skill","Years","Experience","Level","HTML","2","Intermediate","CSS","2","Intermediate","bootstrap",".","js","0.5","Novice","angular",".","js","Javascript","0.5","0.5","Novice","Novice","Able","to","work","in","the","following","location","(","s",")","Toronto","***Thank","you","to","all","applicants","for","your","interest","in","this","role",",","please","note","that","only","those","deemed","most","suitable","for","the","position","will","be","contacted","for","interviews","***"])

sample[18].add_entity(xrange(7,8), "tech_skill") # HTML 
sample[18].add_entity(xrange(9,10), "tech_skill") # CSS 
sample[18].add_entity(xrange(11,12), "tech_skill") # Bootstrap 
sample[18].add_entity(xrange(14,15), "tech_skill") # Angular 
sample[18].add_entity(xrange(19,20), "tech_skill") # HTML 
sample[18].add_entity(xrange(21,22), "tech_skill") # CSS 
sample[18].add_entity(xrange(28,29), "tech_skill") # Angular 
sample[18].add_entity(xrange(30,31), "tech_skill") # Bootstrap 
sample[18].add_entity(xrange(32,33), "tech_skill") # Javascript 
sample[18].add_entity(xrange(40,41), "tech_skill") # HTML 
sample[18].add_entity(xrange(43,44), "tech_skill") # CSS 
sample[18].add_entity(xrange(46,47), "tech_skill") # bootstrap 
sample[18].add_entity(xrange(51,52), "tech_skill") # angular . js 
sample[18].add_entity(xrange(54,55), "tech_skill") # Javascript 

sample[19] = ner_training_instance(["Hot","new","role","for","MEAN","Stack","Developers","!","Our","client","is","a","big","player","in","the","Toronto","FinTech","space","and","they","are","growing","the","team",".","This","is","an","exciting","opportunity","to","join","a","fun","and","hardworking","team","in","one","of","the","hottest","industries",".","This","is","a","permanent","opportunity","and","scheduled","to","start","immediately",".","The","MEAN","Stack","Developer","will","be","working","closely","with","the","rest","of","the","development","team",",","designers","and","Product","Manager","to","design",",","build","and","deploy","creative","solutions","to","business","needs","driven","by","their","customers","and","clients",".","This","is","an","incredible","opportunity","to","add","functionality","to","an","already","successful","application",",","in","order","to","extend","and","integrate","into","financial","institutions","and","clients",".","This","is","a","perfect","mix","of","start-up","culture","and","speed","of","delivery","with","executing","on","large","enterprise","initiatives",".","Sound","interesting","?","We","want","to","hear","from","you","!","Preference","will","be","given","to","candidates","with","exceptional","experience","with","MongoDB",",","Angular","and","Node",".","js",".","As","there","are","a","number","of","roles",",","having","expertise","on","the","front-end","is","great","as","is","having","more","experience","with","API","development","and","strong","Database","development","experience",".","Any","exposure","to","cloud","computing",",","AWS","specifically",",","running","and","deploying","code","or","experience","with","DevOps","tools","is","highly","desirable",".","We","look","forward","to","hearing","from","you","!"])

sample[19].add_entity(xrange(4,5), "tech_skill") # MEAN 
sample[19].add_entity(xrange(57,58), "tech_skill") # MEAN 
sample[19].add_entity(xrange(159,160), "tech_skill") # MongoDB 
sample[19].add_entity(xrange(161,162), "tech_skill") # Angular 
sample[19].add_entity(xrange(163,164), "tech_skill") # Node . js 
sample[19].add_entity(xrange(188,189), "tech_skill") # API 
sample[19].add_entity(xrange(202,203), "tech_skill") # AWS 
sample[19].add_entity(xrange(212,213), "tech_skill") # DevOps 

sample[20] = ner_training_instance(["ATS","is","the","industry","leader","in","using","technology","to","revolutionize","engineering","and","design","processes",".","We","create","tools","to","help","engineers","and","architects","to","integrate","complex","systems","quickly","and","accurately","for","North","America","'s","most","exciting","building","projects",".","ATS","is",",","first","and","foremost",",","about","delighting","our","clients","and","we","are","deeply","committed","to","providing","them","with","exceptional","service",".","We","are","recognized","for","our","technical","expertise","and","experience",",","which","we","apply","to","help","our","clients","succeed",".","We","have","a","strong","work","ethic","and","will","do","all","that","we","can","to","assist","our","clients","complete","their","projects","efficiently",".","Our","thriving","and","motivated","culture","is","the","heartbeat","of","our","organization",".","We","hope","you","will","become","a","part","of","it","!","We","are","currently","a","seeking","dynamic","Software","Developer","to","join","our","IT","Team",".","If","you","enjoy","the","mix","of","coding",",","architecting","enterprise","level","solutions","whilst","growing","and","mentoring","your","team","then","this","role","is","perfect","for","you","!","Our","head","office","in","Toronto",",","Ontario","Canada","is","near","Morningside","Avenue","and","Highway","401","in","the","north","east","GTA",".","We","are","conveniently","located","near","transit","(","TTC",")","and","a","variety","of","restaurants",",","shops","and","a","bank",".","Our","office","offers","an","open","and","spacious","work","environment","with","free","parking",",","an","onsite","gym",",","games","(","table","tennis",",","air","hockey",",","foosball",",","outdoor","basketball","net",")",",","outdoor","patio","and","BBQ",".","These","great","amenities","along","with","fun","quarterly","employee","events",",","promote","friendship","and","camaraderie","among","our","team",",","which","are","mutually","beneficial","for","our","employees","'","well-being","at","work","and","our","company","'s","success",".","As","our","Software","Developer","you","will",":","Develop","of","web","applications","from","planning","to","design",",","coding",",","testing","and","deployment",",","Determine","functionality","that","the","application","must","support","and","develop","content","based","on","practical","approved","layout",",","Test","and","maintain","web","applications",",","identifying","and","solving","any","technical","problems","and","glitches",",","Display","strong","analytical","and","time","management","skills",",","plus","balance","competing","priorities","and","client","'s","needs",",","Offer","solid","interpersonal","and","communication","skills","with","excellent","fluency","in","English",",","Be","a","detail-oriented",",","self-starter","while","working","independently","or","collaboratively","in","a","fast-paced","environment",",","Possess","exceptional","organization","and","leadership","skills","to","effectively","collaborate","with","a","multi-functional","team",",","Grasp","new","techniques","and","technologies","to","continuously","improve","the","performance","of","our","platforms",",","As","our","Software","Developer","you","must","have",":","A","Bachelor","'s","Degree","or","diploma",",","certificate","in","related","program",",","3+","years","experience","with","Software","Development","using","PHP","and","RelationalDatabase","Solid","experience","with","MVC","frameworks","(","Zend",",","Laravel",",","Symfony",")","Solid","knowledge","in","Object","Oriented","Programming","and","Design","Patterns","isrequiredStrong","knowledge","in","Relationship","database","design","(","MySQL",",","PostgreSQL",",","MariaDB",")","Experience","with","database","query","(","SQL",")","optimization","is","requiredExperience","with","Web","API",",","Microservice","development","using","REST",",","RabbitMQ-","Knowledge","of","Doctrine","and","ORM","is","big","asset","Experience","with","Zend","Expressive",",","PSR-7","is","plus","Working","knowledge","in","following","additional","tools",",","techniques","such","as","-","Git",",","Docker",",","Unit","Testing",",","automated","testing",".","Experience","working","within","an","agile",",","scrum","environment",".","You","must","have","excellent","communication","skills",",","be","a","fast","learner",".","COMPENSATION","Salary",":","Based","on","experience",".","Private","Health","Services","Plan","and","yearly","target","based","bonus",".","Please","email","careers@atsspec",".","ca","including","your","resume",",","and","either","a","link","to","your","Git","Hub","or","Bit","Bucket",".","To","learn","more","about","ATS","'","Companies",",","please","visit","our","promotional","video",":","http",":",",",",","youtu",".","be",",","MPyk3BdN-8o","And","our","websites",":","atsspec",".","ca",",","ats-sales",".","ca",",","visualspecbuilder",".","com",",","spectrumlockers",".","com","Allied","Technical","Sales","Inc",".","values","diversity",",","and","is","proud","to","be","an","Equal","Opportunity","Employer",".","We","are","committed","to","the","principles","and","practices","of","employment","equity",",","and","encourage","all","qualified","individuals",",","including","women",",","persons","with","disabilities",",","visible","minorities",",","and","Aboriginal","Peoples","to","apply",".","If","you","are","contacted","for","a","job","opportunity",",","please","advise","us","of","any","accommodations","needed","to","ensure","you","have","access","to","a","fair","and","equitable","process",".","Any","information","received","relating","to","accommodation","will","be","addressed","confidentially","."])

sample[20].add_entity(xrange(430,431), "tech_skill") # PHP 
sample[20].add_entity(xrange(436,437), "tech_skill") # MVC 
sample[20].add_entity(xrange(439,440), "tech_skill") # Zend 
sample[20].add_entity(xrange(441,442), "tech_skill") # Laravel 
sample[20].add_entity(xrange(443,444), "tech_skill") # Symfony 
# sample[20].add_entity(xrange(448,451), "tech_skill") # Object Oriented Programming 
sample[20].add_entity(xrange(461,462), "tech_skill") # MySQL 
sample[20].add_entity(xrange(463,464), "tech_skill") # PostgreSQL 
sample[20].add_entity(xrange(465,466), "tech_skill") # MariaDB 
sample[20].add_entity(xrange(472,473), "tech_skill") # SQL 
sample[20].add_entity(xrange(479,480), "tech_skill") # API 
# sample[20].add_entity(xrange(481,482), "tech_skill") # Microservice 
sample[20].add_entity(xrange(484,485), "tech_skill") # REST 
# sample[20].add_entity(xrange(486,487), "tech_skill") # RabbitMQ- 
sample[20].add_entity(xrange(489,490), "tech_skill") # Doctrine 
sample[20].add_entity(xrange(491,492), "tech_skill") # ORM 
sample[20].add_entity(xrange(497,498), "tech_skill") # Zend 
# sample[20].add_entity(xrange(500,501), "tech_skill") # PSR-7 
sample[20].add_entity(xrange(514,515), "tech_skill") # Git 
sample[20].add_entity(xrange(516,517), "tech_skill") # Docker 
# sample[20].add_entity(xrange(528,529), "tech_skill") # agile 
# sample[20].add_entity(xrange(530,531), "tech_skill") # scrum 
sample[20].add_entity(xrange(577,578), "tech_skill") # Git 

sample[21] = ner_training_instance(["We","'re","seeking","Python","Developers","for","contract","opportunities","with","several","of","our","Clients","we","'re","anticipating","over","the","next","several","weeks","of","Summer","2016.","Criteria","is","completely","open",",","however",",","must","have","3-4","experience","as","a","Python","Developer","at","a","minimum","."])

sample[21].add_entity(xrange(3,4), "tech_skill") # Python 
sample[21].add_entity(xrange(37,38), "tech_skill") # Python 

sample[22] = ner_training_instance(["Desired","Education","or","Background",":","Degree","or","diploma","in","Computer","Science","or","a","related","discipline","PROGRESS","experience",",","at","least","two","years","(","asset",")","Brokerage","or","financial","industry","experience","(","asset",")","Familiarity","with","the","Dataphile","database","and","application","will","be","considered","an","asset",".","Experience","designing","and","building","web-based","applications"])

# sample[22].add_entity(xrange(36,38), "tech_skill") # Dataphile database 

sample[23] = ner_training_instance(["Responsibilities","Architect",",","Design",",","Develop","SOA","framework","and","services","Mentoring","and","Coaching","other","members","of","our","development","team","with","SOA",",",".","NET",",","SharePoint","BizTalk","knowledge","Work","extensively","with","other","members","of","our","development","team",",","using","your","analytical","and","problem-solving","abilities","to","push","the","boundaries","and","create","new","solutions","Analyze","business","and","technical","requirements",".","Maintain","and","enhance","existing","applications","Description","of","the","work","required","and","deliverables","Required","an","understanding","current","applications","and","migrating","to","SOA","platforms","Required","innovative","and","creative","solutions","for","creating","IT","agility","Required","accountability","for","any","SOA","related","or","assigned","technical","issues","Required","quality","and","accuracy","of","the","work","deliverables","."])

# sample[23].add_entity(xrange(6,7), "tech_skill") # SOA 
# sample[23].add_entity(xrange(20,21), "tech_skill") # SOA 
sample[23].add_entity(xrange(22,24), "tech_skill") # . NET 
sample[23].add_entity(xrange(25,26), "tech_skill") # SharePoint 
# sample[23].add_entity(xrange(78,79), "tech_skill") # SOA 
# sample[23].add_entity(xrange(93,94), "tech_skill") # SOA 

sample[24] = ner_training_instance(["Hiring","an","Intermediate","Front","End","Developer","(","Full-time",")","in","Toronto",",","ON","!","Our","ideal","candidate","is","a","strong","self-starter",",","has","initiative","and","reacts","quickly","in","time","sensitive","situations",".","This","is","an","exciting","opportunity","to","work","with","the","world","'s","No","1","Travel",",","Adventure","company","!","Perks","You","'ll","Love","Work","with","the","world","'s","No","1","Travel",",","Adventure","company","Exciting","opportunities","for","travel","and","growth","An","environment","where","you","work","hard","and","have","so","much","fun","doing","it","-","So","rewarding","!","What","We","'re","Looking","For","Strong","self-starter",",","has","initiative","and","reacts","quickly","in","time","sensitive","situations","Expert","knowledge","of","JavaScript","(","and","it","'s","libraries",")","Understanding","of","the","full","web","stack","–","from","server","to","browser","Evangelize","and","improve","tools","for","responsive","development","Required","Background","&","Skills","At","least","3+","years","experience","with","Front","End","Technologies","and","Development","experience","At","least","1+","year","of","experience","with","React","You","are","a","people","person","!","Personality","is","super","important","for","their","culture","!","Our","client","wants","a","fun",",","collaborative","and","passionate","individual","who","wants","to","an","integral","part","of","a","growing","team","BA","in","Computer","Science","or","related","field","***NOTE",":","All","applicants","MUST","be","authorized","to","work","in","Canada",".","Any","applicants","not","meeting","this","criteria","will","not","be","notified","and","will","not","be","considered","eligible","for","the","position",".","***"])

sample[24].add_entity(xrange(108,109), "tech_skill") # JavaScript 
sample[24].add_entity(xrange(156,157), "tech_skill") # React

# do training
trainer = ner_trainer("../MITIE/MITIE-models/english/total_word_feature_extractor.dat")

for entity in sample:
    trainer.add(entity)

trainer.num_threads = 4

ner = trainer.train()
ner.save_to_disk("25_dev_no_js.dat")
print ("tags:", ner.get_possible_ner_tags())
