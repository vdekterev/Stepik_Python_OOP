class RenderList:
    def __init__(self, type_list='ul'):
        if type_list not in ('ul', 'ol'):
            self.type_list = 'ul'
        else:
            self.type_list = type_list

    def __call__(self, lst, *args, **kwargs):
        template = [f'<{self.type_list}>', f'</{self.type_list}>']
        template.insert(1, '\n'.join([f'<li>{l}</li>' for l in lst]))
        return '\n'.join(template)
