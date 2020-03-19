import ruamel.yaml
# from ruamel.yaml import YAML


yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True
# yaml.default_style = "'"


def my_represent_none(self, data):
    return self.represent_scalar(u'tag:yaml.org,2002:null', u'~')


def my_represent_str(self, data):
    data = data.encode('unicode_escape').decode()
    return self.represent_str("'" + data + "'")


yaml.representer.add_representer(type(None), my_represent_none)
# yaml.representer.add_representer(str, my_represent_str)
