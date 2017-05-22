from xml.dom import minidom
import csv
from collections import defaultdict 

xmldoc = minidom.parse('datascience/Posts.xml')    
data = defaultdict() 

itemlist = xmldoc.getElementsByTagName('row')       

for node in itemlist:
    row_id = node.getAttribute('Id')

    tag = node.getAttribute('Tags')                   
    tag.encode('ascii','ignore')          

    post_type_id = node.getAttribute('PostTypeId') 

    if(int(post_type_id) == 1):                                                                                           
        parent_id = -1
        if(node.hasAttribute('AcceptedAnswerId') == True):
            accepted_answer_id = node.getAttribute('AcceptedAnswerId')  
        else:
            accepted_answer_id = -1    
    # elif(int(post_type_id) == 2):
    #     accepted_answer_id = -1
    #     parent_id = node.getAttribute('ParentId')

    # try:
    #   if(int(post_type_id) == 1):
    #       accepted_answer_id = node.getAttribute('AcceptedAnswerId')
    #   elif(int(post_type_id) == 2):
    #       parent_id = node.getAttribute('ParentId')
    # except Exception as e:
    #   print 'No answer exist for this title ',e

    title = node.getAttribute('Title')
    title.encode('ascii','ignore')

    body = node.getAttribute('Body')
    body.encode('ascii','ignore')

    data[row_id] = [post_type_id, parent_id, accepted_answer_id, tag, title, body]  
    # data[row_id] = (tag,body)  

# print 'size of dictionary (data): ',len(data)
# print
# for i in data.items():
#     print i[0] , ':', ''.join(i[1][3].split('<')[:]).split('>')[:-1], ' ', i[1][4].encode('utf8')       

with open('datascience_datasets_for_doc_similarity.csv','wb') as csv_data:   
    writer = csv.writer(csv_data)
    for i in data.values(): 
        file = str(i[3])
        if(int(i[0])==1 and int(i[1])==-1 and int(i[2])!=-1):   
        		writer.writerow([''.join(file.split('<')[:]).split('>')[:-1],i[4].encode('utf8'),data[i[2]][5].encode('utf8')])         