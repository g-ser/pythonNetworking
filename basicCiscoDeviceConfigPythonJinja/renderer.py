from jinja2 import Environment, FileSystemLoader
import yaml

def get_interface_speed(iface_name):
    """it returns the expected speed in Mbps based on the name of the interface
    """

    if 'gigabit' in iface_name.lower():
        return 1000
    if 'fast' in iface_name.lower():
        return 100

#instantiate an Environment object and use the do extension to allow do tag in the template
jinja_env = Environment(loader=FileSystemLoader('.'),extensions=['jinja2.ext.do'])
#add filter to ENV object
jinja_env.filters['get_interface_speed'] = get_interface_speed
#instantiate a template object
template = jinja_env.get_template("complete_config_template.j2")

with open("data.yml") as f:
    # interfaces is a list with several dictionaries as its elements
    interfaces = yaml.load(f)
    print(template.render(interface_list=interfaces))