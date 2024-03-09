# cookie cutter url
# cookiecutter  https://github.com/audreyfeldroy/cookiecutter-pypackage
# import nesessary libraries like
# os => For Making the folder structure
# pathlib => For path control
# Logging => For handling any type of log
import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

project_name='End_To_End_DataScience'
list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingetion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_traning.py",
    f"src/{project_name}/components/model_monetring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    'requirements.txt',
    'setup.py',
    'Dockerfile'
]

# Read the list of file for creating the file and folders
# If file/folder not exists create the file/folder
# If file exists simple write pass inside the if block
# else write file already exists
for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if(file_dir and not os.path.isdir(file_dir)):
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating files directory {file_dir} for the file name {file_name}")

    elif((not os.path.isfile(file_path)) or (os.path.getsize(file_path))==0):
        with open (file_path,"w") as f:
            pass
            logging.info(f"Creating Empty file {file_name}")

    else:
        logging.info(f"File already exists: {file_path}")