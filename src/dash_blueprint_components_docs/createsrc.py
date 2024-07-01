import frontmatter
import importlib
from pathlib import Path
import json

path = Path('pages')
dirs = [d for d in sorted(path.iterdir()) if d.is_dir()]
sidebar = list()
count = 0

for d in dirs:
    md = d / f'{d.name}.md'
    dir_content = frontmatter.load(md)
    section = {
        'route': str('/' / d.relative_to(d.parts[0])),
        'path': str(d / f'{d.name}').replace('/', '.'),
        'level': 1,
        'title': dir_content['title'],
        'isSection': dir_content['isSection'],
    }
    subdirs = [d for d in sorted(d.iterdir()) if d.is_dir()]
    subsections = list()
    for subdir in subdirs:
        subdir_md =  subdir / f'{subdir.name}.md'
        subdir_content= frontmatter.load(subdir_md)

        subsubdirs = [d for d in subdir.iterdir() if d.is_dir()]
        subsubsections = list()
        if subsubdirs:
            for subsubdir in subsubdirs:
                subsubdir_md =  subsubdir / f'{subsubdir.name}.md'
                subsubdir_content= frontmatter.load(subsubdir_md)
                subsubsection = {
                    'route': str('/' / subsubdir.relative_to(subsubdir.parts[0])),
                    'path': str(subsubdir / f'{subsubdir.name}').replace('/', '.'),
                    'level': 2,
                    'title': subsubdir_content['title'],
                    'isSection': subsubdir_content['isSection'],
                    'module': '',
                    'description': '',
                    'section': '',
                    'name': '',
                    'content': [],
                }
                
                # get layout
                subsubsections.append(subsubsection)

        subsection = {
            'route': str('/' / subdir.relative_to(subdir.parts[0])),
            'path': str(subdir / f'{subdir.name}').replace('/', '.'),
            'level': 2,
            'title': subdir_content['title'],
            'isSection': subdir_content['isSection'],
            'module': '',
            'description': '',
            'section': '',
            'name': '',
            'content': subsubsections,
        }

        subsections.append(subsection)
    
    section['module'] = ''
    section['description'] = ''
    section['section'] = ''
    section['name'] = ''
    
    section['content'] = subsections
    sidebar.append(section)


with open('src.json', 'w') as fid:
    json.dump(sidebar, fid, indent=2)
