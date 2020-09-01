'''
exportstl
===
Demos 307 redirects with the Onshape API
'''

from onshape_client import OnshapeElement, Client

# variables
config_filename = '.onshape_client_config.yaml'
did = '4106f8fea9cf4607edeba1db'
wid = 'c11cf0ae6ab5e6297d09562d'
eid = '3340d6f3b50b6e32e22d9a3b'


# do things
client = Client( config_filename ) # create client


'''
print( 'https://cad.onshape.com/documents/{}/w/{}/e/{}'.format(did,wid,eid) )
element = OnshapeElement('https://cad.onshape.com/documents/{}/w/{}/e/{}'.format(did,wid,eid)) # create onshape element

#headers={}
headers={"Accept": "application/vnd.onshape.v1+json;charset=utf-8;qs=0.1, application/json;charset=utf-8; qs=0.09",
         "Authorization": "Bearer {}".format( client.get_client().configuration.access_token )}
query_params={}


response = client.api_client.request('GET',
                                     '{}/api/partstudios/d/{}/w/{}/e/{}/stl'.format(client.configuration.host,did,wid,eid),
                                     headers,
                                     query_params)

'''

'''
print( element.did, element.wvm, element.wvmid, element.eid )


response = client.part_studios_api.export_stl1(element.did,
                                    element.wvm,
                                    element.wvmid,
                                    element.eid,
                                    _preload_content=True)


'''
'''
file = 'out.stl'
with open(file, 'wb') as f:
    f.write(response.data)
#assert f.stat().st_size > 1000
'''
