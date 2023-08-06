
from os import path
import json
import subprocess
from tempfile import gettempdir
import argparse
import yaml
from jsonschema import validate

SOURCE_PATH = path.dirname(__file__)
SCHEMA_PATH = path.join(SOURCE_PATH, "schemas")

class ExSource:
    """
    Class that stores and validates ExSource data.
    """

    def __init__(self):
        self._data = {}

    def load(self, filepath):
        """
        Load ExSource data from file.
        """
        file_format = get_exsource_format(filepath, "read")
        with open(filepath, 'r', encoding="utf-8") as file_obj:
            file_content = file_obj.read ()
            if file_format == "JSON":
                input_data = json.loads(file_content)
            else:
                #only other option is YAML
                input_data = yaml.safe_load(file_content)
        self.validate(input_data)
        self._data = input_data

    def save(self, filepath):
        """
        Save ExSource data to file.
        """
        file_format = get_exsource_format(filepath, "write")
        with open(filepath, 'w', encoding="utf-8") as file_obj:
            if file_format == "JSON":
                json.dump(self.data, file_obj, sort_keys=True, indent=4)
            else:
                #only other option is YAML
                file_obj.write(yaml.dump(self.data))

    def set_data(self, data):
        """
        Set data from dictionary
        """
        self.validate(data)
        self._data = data

    @property
    def data(self):
        """
        Read-only property. Wiith the data read from the ExSource file.
        """
        return self._data

    def load_schema(self):
        """
        Return the exsource schema.
        """
        schema_file = path.join(SCHEMA_PATH, "exsource.schema.json")
        with open(schema_file, 'r', encoding="utf-8") as file_obj:
            schema = json.loads(file_obj.read())
        return schema

    def validate(self, data):
        """
        Validate the exsource schema
        """
        validate(instance=data, schema=self.load_schema())

def get_exsource_format(filepath, mode="read"):
    """
    Return the format of an exsource file based on filename.

    This will error if the file type is not supported
    """
    if filepath.lower().endswith('.yml') or filepath.lower().endswith('.yaml'):
        file_format = "YAML"
    elif filepath.lower().endswith('.json'):
        file_format = "JSON"
    else:
        raise ValueError(f"Couldn't {mode} '{filepath}'. "
                         "Only YAML and JSON exsource files are supported.")
    return file_format

def get_make_parser():
    description = "Process exsource file to create inputs."
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("exsource_file", help="Path to exsource_file")
    return parser

def make():
    parser = get_make_parser()
    args = parser.parse_args()
    exsource = ExSource()
    exsource.load(args.exsource_file)
    processor = ExSourceProcessor(exsource)
    processor.make()

class ExSourceProcessor:

    def __init__(self, exsource):
        self.exsource = exsource

    @property
    def outputs(self):
        return self.exsource.data["outputs"]

    def make(self):
        for output_id in self.outputs:
            output = self.outputs[output_id]
            app = output["application"]
            if app.lower() == "openscad":
                self.process_openscad(output)
            elif app.lower() == "freecad":
                self.process_freecad(output)
            else:
                #TODO use logging
                print("Skipping {output_id} as no methods available process files with {app}")

    def process_openscad(self, output):
        #TODO: Tidy up
        outputs = output["output-files"]
        assert len(outputs)==1, "OpenSCAD expects only one output"
        sources = output["source-files"]
        assert len(sources)==1, "Openscad expects only one source file"
        if "app-options" in output:
            options = output["app-options"]
        else:
            options = []
        params = []
        if "parameters" in output:
            parameters = output["parameters"]
            for parameter in parameters:
                if isinstance(parameters[parameter], (float, int)):
                    par = str(parameters[parameter])
                elif isinstance(parameters[parameter], bool):
                    #ensure lowercase for booleans
                    par = str(parameters[parameter]).lower()
                elif isinstance(parameters[parameter], str):
                    par = parameters[parameter]
                else:
                    print("Can only process string, numerical or boolean arguments for OpenSCAD. "
                          f"Skipping parameter {parameter}")
                    continue
                params.append("-D")
                params.append(f"{parameter}={par}")

        executable = "openscad"
        openscad_args = options + params + ["-o", outputs[0], sources[0]]
        try:
            ret = subprocess.run([executable] + openscad_args, check=True, capture_output=True)
            #print std_err as OpenSCAD uses it to print rather than std_out
            std_err = ret.stderr.decode('UTF-8')
            print(std_err)
        except subprocess.CalledProcessError as error:
            std_err = error.stderr.decode('UTF-8')
            raise RuntimeError(f"\n\nOpenSCAD failed create file: {outputs[0]} with error:\n\n"
                               f"{std_err}") from error


    def process_freecad(self, output):
        #TODO: Tidy up

        outputs = output["output-files"]
        sources = output["source-files"]
        assert len(sources)==1, "Openscad expects only one source file"
        sourcefile = sources[0]
        if "app-options" in output:
            assert len(output["app-options"])==0, "Cannot apply options to freecad"
        if "parameters" in output:
            parameters = output["parameters"]
            for parameter in parameters:
                print("Cannot process parameters for FreeCAD "
                      f"Skipping parameter {parameter}")
                continue

        for outfile in outputs:
            if outfile.lower().endswith('.stp') or outfile.lower().endswith('.step'):
                macro = (f"doc = FreeCAD.openDocument('{sourcefile}')\n"
                         "body = doc.getObject('Body')\n"
                         f"body.Shape.exportStep('{outfile}')\n")
            elif outfile.lower().endswith('.stl'):
                macro = ("from FreeCAD import Mesh\n"
                         f"doc = FreeCAD.openDocument('{sourcefile}')\n"
                         "body = doc.getObject('Body')\n"
                         f"Mesh.export([body], '{outfile}')\n")
            tmpdir = gettempdir()
            macropath = path.join(tmpdir, "export.FCMacro")
            with open(macropath, 'w', encoding="utf-8") as file_obj:
                file_obj.write(macro)
            subprocess.run(["freecadcmd", macropath], check=True)
