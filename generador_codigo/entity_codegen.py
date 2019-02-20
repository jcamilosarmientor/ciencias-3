"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm

projectName=raw_input('Nombre del proyecto: ')

def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'person.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    def reacttype(s):
        return {
                'float': 'var',
                'integer': 'var',
                'string': 'var',
                'bool': 'var',
                'time': 'var'
        }.get(s.name)

    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
                'integer': 'int',
                'string': 'String'
        }.get(s.name, s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['javatype'] = javatype
    jinja_env.filters['reacttype'] = reacttype

    # Crea el index.html
    template = jinja_env.get_template('index.template')
    with open(join(srcgen_folder,"index.html"), 'w') as f:
            f.write(template.render(entity=projectName))
    
    # Crea package.json 
    template = jinja_env.get_template('package_json.template')
    with open(join(srcgen_folder,"package.json"), 'w') as f:
            f.write(template.render(entity=projectName.replace(" ", "_")))

    # Controlladores template
    template = jinja_env.get_template('controller.template')
    controllers=[]
    for entity in person_model.entities:
        controllers.append(entity)
        # For each entity generate js file
        with open(join(srcgen_folder,
                       entity.name.lower()+"_controller.js"), 'w') as f:
            f.write(template.render(entity=entity))

    # Crea el index.js       
    template = jinja_env.get_template('index_controller.template')        
    with open(join(srcgen_folder,"index.js"), 'w') as f:
            f.write(template.render(entity=controllers, projectName=projectName))
    
    # Crea el index.jcss       
    template = jinja_env.get_template('styles.template')        
    with open(join(srcgen_folder,"index.css"), 'w') as f:
            f.write(template.render())

if __name__ == "__main__":
    main()
