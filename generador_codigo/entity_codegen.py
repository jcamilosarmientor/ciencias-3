"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm

projectName = raw_input('Nombre del proyecto: ')


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

    def htmltype(s):
        return {
                'float': 'number',
                'integer': 'number',
                'string': 'text',
                'bool': 'checkbox',
                'time': 'date'
        }.get(s.name)

    def mongotype(s):
        return {
                'float': 'Number',
                'integer': 'Number',
                'string': 'String',
                'bool': 'Bool',
                'time': 'Time'
        }.get(s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)
    srcgen_folder_api = join(this_folder, 'srcgen/api')
    if not exists(srcgen_folder_api):
        mkdir(srcgen_folder_api)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    jinja_env.tests['entity'] = is_entity
    jinja_env.filters['reacttype'] = reacttype
    jinja_env.filters['htmltype'] = htmltype
    jinja_env.filters['mongotype'] = mongotype

    # Crea el index.html
    template = jinja_env.get_template('index.template')
    with open(join(srcgen_folder, "index.html"), 'w') as f:
            f.write(template.render(entity=projectName))

    # Crea package.json
    template = jinja_env.get_template('package_json.template')
    with open(join(srcgen_folder, "package.json"), 'w') as f:
            f.write(template.render(entity=projectName.replace(" ", "_")))

    # Controlladores template
    template = jinja_env.get_template('controller.template')
    controllers = []
    for entity in person_model.entities:
        controllers.append(entity)
        # For each entity generate js file
        with open(join(srcgen_folder,
                       entity.name.lower()+"_controller.js"), 'w') as f:
            f.write(template.render(entity=entity))

    # Crea el index.js
    template = jinja_env.get_template('index_controller.template')
    with open(join(srcgen_folder, "index.js"), 'w') as f:
            f.write(template.render(entity=controllers, projectName=projectName))

    # Crea el index.css
    template = jinja_env.get_template('styles.template')
    with open(join(srcgen_folder, "index.css"), 'w') as f:
            f.write(template.render())

    # server.js template
    template = jinja_env.get_template('server.template')        
    with open(join(srcgen_folder_api,"index.js"), 'w') as f:
            f.write(template.render(entity=controllers))

    # database.js template
    template = jinja_env.get_template('database.template')        
    with open(join(srcgen_folder_api,"database.js"), 'w') as f:
            f.write(template.render(projectName=projectName))
    
    # modelos para el api 
    template = jinja_env.get_template('schemas.template')        
    for entity in person_model.entities:
        with open(join(srcgen_folder_api,
                entity.name.lower()+".model.js"), 'w') as f:
            f.write(template.render(entity=entity))

    # rutas para el api 
    template = jinja_env.get_template('route.template')        
    for entity in person_model.entities:
        with open(join(srcgen_folder_api,
                entity.name.lower()+".route.js"), 'w') as f:
            f.write(template.render(entity=entity))

if __name__ == "__main__":
    main()
