'''
    Test
'''
from onshape_client import OnshapeElement, Client
from pathlib import Path


config_filename = '.onshape_client_config.yaml'

client = Client( config_filename )
new_doc = OnshapeElement.create("Engine")
print('here')
translated_geometry = Path().cwd() / "test" / "assets"/ "translated_geometry"
imported_part_studio = new_doc.import_file(translated_geometry / "Cube.x_t", allow_faulty_parts=True)
