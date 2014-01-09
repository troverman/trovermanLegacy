################################################################
####db##########################################################
################################################################
if not request.env.web2py_runtime_gae:
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    db = DAL('google:datastore')
    session.connect(request, response, db=db)
response.generic_patterns = ['*'] if request.is_local else []

################################################################
####database_tables#############################################
################################################################

################################
####html_block##################
################################
db.define_table('html_block',
    Field('html_content','text'),
    Field('html_type','string'),
)

################################
####post########################
################################
db.define_table('post',
    Field('title','string'),
    Field('url_title', readable=False, writable=False),
    Field('post_content','text'),
)

################################
####site_files##################
################################
db.define_table('site_files', 
    Field('file_type','string'),
    Field('f_file', 'upload', uploadfield='f_file_blob'),
    Field('f_file_blob', 'blob')  
)

################################
####post_tag####################
################################
db.define_table('post_tag',
    Field('post_id','reference post'),
    Field('tag','string'),
)

################################
####project_pictures############
################################
db.define_table('project_pictures', 
    Field('project_name', 'string'),
    Field('picture', 'upload', uploadfield='picture_file'),
    Field('picture_file', 'blob')  
)
