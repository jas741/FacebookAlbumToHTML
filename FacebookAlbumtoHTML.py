

import facebook



#input your access code, in quotes. (get this from https://developers.facebook.com/tools/explorer/). Codes expire after two hours. You can use an app code instead of a user code if you need a longer duration.
token = "your code"

# set this to what you want the title of the html page to be, in quotes
pagetitle = "My Album"

# This is the text at the top of the page, eg "Photos from My Summer Abroad". In quotes.
pagedescription = "Photos from My Summer Abroad"

# This is the name of the album, eg, "Summer2016", if the pic folder is "Summer2016@@".
albumname = "Summer2016" 



albumnumber = "album_number"
#To get albumnumber its the numerical string following the a ,
# but only before the first dot, so if the whole thing is
 # #media_set?set=a.10291136899892709.6736476374
                             #then its:
                             #10291136899892709


graph = facebook.GraphAPI(access_token=token, version=2.7)


htmlstring = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<HTML>
<HEAD>
<meta charset="utf-8">
   <TITLE>""" + pagetitle + """</TITLE>
</HEAD>
<BODY TEXT="#000000" BGCOLOR="#FFFFF" LINK="#0000EE" VLINK="#551A8B" ALINK="#FF0000">


<h3>""" + pagedescription +  """</h3>

<b>

"""



photodict = graph.get_object(id=albumnumber, fields="photos")

photolist = [x['id'] for x in photodict['photos']['data']]


for photo in photolist:


    photocapt = graph.get_object(id=photo, fields="tags,name")

    if "name" in photocapt:
        caption = photocapt['name']
        
        if "tags" in photocapt:
     
            tagslist = [x["name"] for x in photocapt['tags']['data']]
            tagstring = ", ".join(tagslist)
    
            htmlstring += """
            <img src=\"""" + albumname + """@@/""" + str(photolist.index(photo)+1) + """.jpg">
            <p>""" + caption + """</p>
            <!-- """ + tagstring + """ -->
            """

        else:

            htmlstring += """
            <img src=\"""" + albumname + """@@/""" + str(photolist.index(photo)+1) + """.jpg">
            <p>""" + caption + """</p>
            <!-- -->
            """

    else:
        
        if "tags" in photocapt:
     
            tagslist = [x["name"] for x in photocapt['tags']['data']]
            tagstring = ", ".join(tagslist)
    
            htmlstring += """
            <img src=\"""" + albumname + """@@/""" + str(photolist.index(photo)+1) + """.jpg">
            <p>""" + tagstring + """</p>
            <!--  -->
            """

        else:

            htmlstring += """
            <img src=\"""" + albumname + """@@/""" + str(photolist.index(photo)+1) + """.jpg">
            <p></p>
            <!-- -->
            """
        
htmlstring += """

</b>

<hr>

Go to:
<ul>
<li><a href="">My Photo
    Gallery</a></li>
<li><a href="">My Home Page</a></li>
</ul>
</BODY>
</HTML>
"""
#The above assumes you want to situate this page within a larger website with a main photo galleries page and a home page

Html_file = open(albumname + ".html","w")
Html_file.write(htmlstring)
Html_file.close()




# guide to facebook-sdk python package at http://facebook-sdk.readthedocs.io/en/latest/api.html

