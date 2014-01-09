################################################################
####menu########################################################
################################################################

################################
####title#######################
################################
if request.function == 'index':
    response.title = 'troverman'
elif request.function == 'posts':
    if request.args(0) == 'tag':
        response.title = 'tag' + ' - ' + str(request.args(1))
    else:
        response.title = 'posts'  
elif request.function == 'post':
    response.title = str(request.args(0).replace('-',' '))
else:
    response.title = str(request.function.replace('_',' '))

################################
####meta########################
################################        
response.meta.author = 'Trevor Overman'
response.meta.description = 'troverman'
response.meta.keywords = 'troverman, development, giving'
response.meta.generator = 'troverman'
