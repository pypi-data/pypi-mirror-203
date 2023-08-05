from __future__ import annotations
from functools import cached_property

class Script():
    
    def __init__(self, source):
        self.refs : dict[str, SplinterRef] = dict()
        self.source : str = source
        self.splinters_params = 0
    
    @cached_property
    def splinter_blocks(self):
        return len(self.refs.keys())
    
    def imports_handler(self):
        # does not return nothing special since this is called only during 
        # the preload and compile phases.
        # the imports nad rendered by a Renderer class
        return ""
    
    def splinter_handler(self, ref_name, splinter_tasks, ident=0, **kwargs):
        """Stores the dependency of the script with a Splinter"""
        
        if ref_name in self.refs:
            raise SyntaxError(f"Script alread has a ref with name {ref_name}")

        self.refs[ref_name] = SplinterRef(ref_name, splinter_tasks, ident, dict(**kwargs))


class SplinterRef():
    
    def __init__(self, name, tasks, ident, vars):
        self.name = name
        self.tasks = tasks
        self.vars = vars
        self.ident = ident
        self.splinters = set()
        self.max_param_size = 0

