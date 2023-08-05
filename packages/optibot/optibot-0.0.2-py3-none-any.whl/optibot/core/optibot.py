import os
import logging
from glob import glob
from jinja2 import Environment, BaseLoader
from .splinter import Splinter
from .script import Script
from .renderer import Renderer
from .errors import DuplicateIdError, MissingIdError, MissingMetaError
from .constants import MAX_SIZE
from random import randint


class OptiBot:
    def __init__(self):
        self.splinter_registry : dict[str, Splinter] = dict()
        self.script_registry : dict[str, Script] = dict()
        self.splinters_params = 0
        self.splinter_blocks = 0

    def preload_splinters_from_path(self, base_path):
        splinters_paths = glob(base_path)

        for splinter_path in splinters_paths:
            with open(splinter_path, "r") as fp:
                try:
                    splinter = self.prepload_splinters_from_string(fp.read())
                    self._register_splinter(splinter)
                except MissingMetaError:
                    logging.error(f"Missing meta splinter in {splinter_path}")
                except MissingIdError:
                    logging.error(f"Splinter id not defined in '{splinter_path}'")
                except DuplicateIdError:
                    logging.error(f"Splinter id {splinter.id} already exists. Duplicate found in {splinter_path}")
                
                    
    def prepload_splinters_from_string(self, splinter_source) -> Splinter:
        splinter_parts = splinter_source.split("---")
                
        if len(splinter_parts) < 2:
            raise MissingMetaError()

        meta, source = splinter_parts[0], splinter_parts[1]
        splinter = self._build_splinter(meta, source)
        
        return splinter

    
    def _register_splinter(self, splinter: Splinter) -> None:

        if splinter.id is None:
            raise MissingIdError()

        if splinter.id in self.splinter_registry:
            raise DuplicateIdError()

        self.splinter_registry[splinter.id] = splinter

    
    def _build_splinter(self, splinter_meta, splinter_source) -> Splinter:
        splinter = Splinter()
        splinter.source = splinter_source
        env = Environment(loader=BaseLoader)
                
        env.globals['optiid'] = splinter.optiid_handler
        env.globals['optidesc'] = splinter.optidesc_handler
        env.globals['optitask'] = splinter.optitask_handler
        env.globals['optiimport'] = splinter.optiimport_handler
        env.globals['optivar'] = splinter.optivar_handler
        env.globals['optiparam'] = splinter.optiparam_handler

        rtemplate = env.from_string(splinter_meta)
        rtemplate.render()
        
        return splinter

    
    def preload_scripts_from_path(self, base_path):
        scripts_path = glob(base_path)

        for script_path in scripts_path:
            with open(script_path, "r") as fp:
                try:
                    script_id = os.path.basename(script_path)
                    script = self.preload_templates_from_string(fp.read())
                
                    self._register_script(script_id, script)                
                except DuplicateIdError:
                    logging.error(f"Script id {script_id} already exists. Duplicate found in {script_path}")

                
    def preload_templates_from_string(self, script_source: str) -> Script:
        script = self._build_script(script_source)
        return script
    

    def _register_script(self, script_id: str, script: Script) -> None:
        if script_id in self.script_registry:
            raise DuplicateIdError()

        self.script_registry[script_id] = script


    def _build_script(self, script_source):
        script = Script(script_source)

        env = Environment(loader=BaseLoader)
                
        env.globals['splinter'] = script.splinter_handler
        env.globals['imports'] = script.imports_handler
        
        rtemplate = env.from_string(script_source)   
        rtemplate.render()

        return script


    def compile(self) -> None:
        """
        Compiles the script registry by finding the most suitable splinters 
        for each script reference by signature and task.
        Raises ValueError if no suitable splinter is found
        """

        # Initialize two variables to keep track of total splinter params and blocks
        self.splinters_params = 0
        self.splinter_blocks = 0

        # Iterate over each script in the script registry
        for script_id, script in self.script_registry.items():
            
            # Iterate over each reference in the script
            for ref in script.refs.values():
                # Initialize some variables for each reference
                is_workable = False
                max_param_size = 0
                tasks = set(ref.tasks.split("."))
                signature = set(ref.vars.keys())

                # Iterate over each splinter in the splinter registry
                for splinter_id, splinter in self.splinter_registry.items():
                    # Check if the tasks of the reference are a subset of the tasks of the splinter
                    if not tasks.issubset(splinter.tasks):
                        continue

                    # Check if the signature of the reference matches the signature of the splinter
                    if signature != splinter.signature:
                        continue

                    # If we've found a suitable splinter, update some variables for the reference
                    is_workable = True
                    max_param_size = max(max_param_size, splinter.param_size)
                    ref.splinters.add(splinter_id)

                # Set the maximum parameter size for the reference
                ref.max_param_size = max_param_size

                # If we couldn't find a suitable splinter for the reference, raise a ValueError
                if not is_workable:
                    raise ValueError(f"No suitable splinters for script '{script_id}'. task: '{ref.tasks}'. signature: '{signature}'")

                # Update the total splinter params for each script
                script.splinters_params += max_param_size
            
            self.splinters_params = max(self.splinters_params, script.splinters_params)
            self.splinter_blocks = max(self.splinter_blocks, script.splinter_blocks)


    def _generate_script(self):
        for x in range(self.splinter_blocks):
            yield randint(0, MAX_SIZE)
        for x in range(self.splinters_params):
            yield randint(-MAX_SIZE, MAX_SIZE)
    
    def generate_script(self) -> list[int]:
        return list(self._generate_script())
    
    def render(self, script_id: str, sequence: list[int]):

        renderer = Renderer(self.script_registry[script_id], sequence, self.splinter_registry)
        return renderer.render()