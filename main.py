import yaml
from jinja2 import Template

def generate_yaml(template_file, values_file, output_file):
    # Load the Jinja2 template
    with open(template_file, 'r') as f:
        template_content = f.read()
    template = Template(template_content)

    # Load the values from the values file
    with open(values_file, 'r') as f:
        values = yaml.safe_load(f)

    # Convert keys to strings in the values dictionary
    values = {str(key): value for key, value in values.items()}

    # Render the template with the values
    rendered = template.render(values)

    # Write the rendered output to the output file
    with open(output_file, 'w') as f:
        f.write(rendered)

if __name__ == "__main__":
    template_file = r"D:\Python\Task\templates\values.j2"
    values_file = r"D:\Python\Task\data.yaml"
    output_file = r"D:\Python\Task\values.yaml"

    generate_yaml(template_file, values_file, output_file)
















































# import yaml
# from jinja2 import Template

# def generate_yaml(template_file, values_file, output_file):
#     # Load the Jinja2 template
#     with open(template_file, 'r') as f:
#         template_content = f.read()
#     template = Template(template_content)

#     # Load the values from the values file
#     with open(values_file, 'r') as f:
#         values = yaml.safe_load(f)

#     # Render the template with the values
#     rendered = template.render(values)

#     # Write the rendered output to the output file
#     with open(output_file, 'w') as f:
#         f.write(rendered)

# if __name__ == "__main__":
#     template_file = r"D:\Python\Task\templates\values.j2"
#     values_file = r"D:\Python\Task\values.yaml"
#     output_file = r"D:\Python\Task\values-Helm.yaml"

#     generate_yaml(template_file, values_file, output_file)









# # import os
# # import yaml
# # from jinja2 import Environment, FileSystemLoader

# # def generate_service_yaml(values_file, template_file, output_file):
# #     # Load values from the values.yaml file
# #     with open(values_file, 'r') as f:
# #         values = yaml.safe_load(f)

# #     # Load the Jinja2 template
# #     env = Environment(loader=FileSystemLoader(searchpath=os.path.dirname(template_file)))
# #     template = env.get_template(os.path.basename(template_file))

# #     # Render the template with the values
# #     rendered = template.render(values=values)

# #     # Write the rendered output to the service YAML file
# #     with open(output_file, 'w') as f:
# #         f.write(rendered)

# # if __name__ == "__main__":
# #     values_file = r'D:\Python\Task\values.yaml'
# #     template_file = r'D:\Python\Task\templates\values.j2'
# #     output_file = r'D:\Python\Task\values-helm.yaml'

# #     generate_service_yaml(values_file, template_file, output_file)
