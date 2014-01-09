################################################################
####controllers#################################################
################################################################

################################
####about#######################
################################
def about():
    return dict()
    
################################
####bankingfor##################
################################
def bankingfor():
    return dict()    
    
################################
####conexus#####################
################################    
def conexus(): 
    return dict() 
     
################################
####contact#####################
################################
def contact():
    return dict()  
    
################################
####deliveryfor#################
################################    
def deliveryfor():
    image_array = db(db.project_pictures.project_name == 'deliveryfor').select() 
    complete_picture_array=[]
    for image in image_array:
        complete_picture_array.append([image['project_name'],image['picture']]) 
    import random
    random_picture_array = random.sample(complete_picture_array, random.randint(1,len(complete_picture_array)))
    image_array=random_picture_array
    return dict(image_array=image_array)

################################
####epointme####################
################################       
def epointme():
    return dict()  
    
################################
####evolvedus###################
################################ 
def evolvedus():
    return dict()
      
################################
####givingfor###################
################################     
def givingfor():
    return dict()
    
################################
####hospitalityfor##############
################################    
def hospitalityfor():
    return dict()
    
################################
####inlrn#######################
################################           
def inlrn(): 
    image_array = db(db.project_pictures.project_name == 'inlrn').select()  
    complete_picture_array=[]
    for image in image_array:
        complete_picture_array.append([image['project_name'],image['picture']])   
    import random
    random_picture_array = random.sample(complete_picture_array, random.randint(1,len(complete_picture_array)))
    image_array=random_picture_array
    return dict(image_array=image_array)

################################
####insuringfor#################
################################     
def insuringfor():
    return dict()
    
################################
####investingfor################
################################         
def investingfor():
    return dict()
    
################################
####lealr#######################
################################     
def lealr():
    return dict()    
    
################################
####mission#####################
################################    
def mission():
    return dict() 
           
################################
####index#######################
################################
def index():
    project_image_list = db(db.project_pictures).select().as_list()
    complete_picture_array = []
    for image in project_image_list:
        complete_picture_array.append([image['project_name'],image['picture']])    
    import random
    random_picture_array = random.sample(complete_picture_array, random.randint(7,len(complete_picture_array)))
    post_list =  db(db.post).select()
    
    html_block_list =  db(db.html_block.html_type=='quote').select()
    complete_html_block_array = []
    for html in html_block_list:
        complete_html_block_array.append(html['html_content'])    
    random_html_block_array = random.sample(complete_html_block_array, random.randint(7,len(complete_html_block_array)))
    
    index_block_list =  db(db.html_block.html_type=='index').select()
    complete_index_block_array = []
    for html in index_block_list:
        complete_index_block_array.append(html['html_content'])    
    random_index_block_array = random.sample(complete_index_block_array, random.randint(2,len(complete_index_block_array)))
    return dict(
        random_index_block_array=random_index_block_array,
        random_html_block_array=random_html_block_array,
        project_image_list=project_image_list,
        random_picture_array=random_picture_array,
        complete_picture_array=complete_picture_array,
        post_list=post_list,
    )
    
################################
####post########################
################################     
def post():
    post = db(db.post.url_title == request.args(0)).select()
    post_id = db(db.post.url_title == request.args(0)).select()[0]['id']
    tag_list = db(db.post_tag.post_id == post_id).select()
    return dict(
        post=post,
        tag_list=tag_list,
    )
    
################################
####posts#######################
################################     
def posts():
    post_array=''
    sorted_combined_count_and_tag_array = ''
    create_post = SQLFORM(db.post)
    posts_list = db(db.post).select()
    complete_tag_array = []
    post_tags = db(db.post_tag).select()          
    for tag in post_tags:
        complete_tag_array.append(tag['tag'])
    set_complete_tag_array = set(complete_tag_array)
    complete_tag_array_unsorted = list(set_complete_tag_array)
    combined_count_and_tag_array=[]
    for tag in complete_tag_array_unsorted:
        combined_count_and_tag_array.append([tag, complete_tag_array.count(tag)])                           
    from operator import itemgetter
    tag_thread_list_sorted_by_total_count = sorted(combined_count_and_tag_array, key=itemgetter(1))            
    if request.args(0) == 'tag':    
        url_tag_array = request.args(1).split(',')
        tag_list_array = []
        for tags in url_tag_array:
            tag_list_array.append(db(db.post_tag.tag == tags).select())
        total_tag_array=[]     
        for tag in tag_list_array:
            for t in tag:
                tag_array=db(db.post_tag.post_id == t['post_id']).select()
                for a_tag in tag_array:
                    total_tag_array.append(a_tag['tag'])
        set_total_tag_array = set(total_tag_array)
        total_tag_array_unsorted = list(set_total_tag_array)
        combined_count_and_tag_array=[]
        for tag in total_tag_array_unsorted:
            combined_count_and_tag_array.append([tag, total_tag_array.count(tag)])
        from operator import itemgetter
        sorted_combined_count_and_tag_array = sorted(combined_count_and_tag_array, key=itemgetter(1))            
        post_array = []
        for tag in tag_list_array:
            for t in tag:
                posts=db(db.post.id == t['post_id']).select()
                post_array.append(posts[0])
    return dict(
        post_array=post_array,
        sorted_combined_count_and_tag_array=sorted_combined_count_and_tag_array,
        posts_list=posts_list,
        post_tags=post_tags,
        tag_thread_list_sorted_by_total_count=tag_thread_list_sorted_by_total_count,
    )
        
################################
####projects####################
################################                  
def projects():
    project_image_list = db(db.project_pictures).select().as_list()
    complete_picture_array = []
    for image in project_image_list:
        complete_picture_array.append([image['project_name'],image['picture']])
    import random
    random_picture_array = random.sample(complete_picture_array, random.randint(len(complete_picture_array),len(complete_picture_array))) 
    return dict(complete_picture_array=complete_picture_array,random_picture_array=random_picture_array)

def troverman():
    image_array = db(db.project_pictures.project_name == 'troverman').select() 
    complete_picture_array=[]
    for image in image_array:
        complete_picture_array.append([image['project_name'],image['picture']])
    import random
    random_picture_array = random.sample(complete_picture_array, random.randint(1,len(complete_picture_array)))
    image_array=random_picture_array
    return dict(image_array=image_array)   
     
def voetr():
    image_array = db(db.project_pictures.project_name == 'voetr').select()
    complete_picture_array=[]
    for image in image_array:
        complete_picture_array.append([image['project_name'],image['picture']])  
    import random
    random_picture_array = random.sample(complete_picture_array, random.randint(1,len(complete_picture_array)))
    image_array=random_picture_array
    return dict(image_array=image_array)
          
################################################################
##helpers#######################################################
################################################################
    
@cache.action()
def download():
    return response.download(request, db)
def call():
    return service()
