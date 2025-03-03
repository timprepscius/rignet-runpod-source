from datetime import datetime

print(f"SETUP ---- A {datetime.now()}");

import os
import sys

print(f"SETUP ---- B {datetime.now()}");

import subprocess
import base64

print(f"SETUP ---- C {datetime.now()}");

def b64to(b64_string, file_path):
    with open(file_path, "wb") as file:
        file.write(base64.b64decode(b64_string))

def process(job_id, job_input):
    print(f"RUN ---- A {datetime.now()}");

    glb_input_b64 = job_input['glb']
    glb_input_name = f"/tmp/input_{job_id}.glb"
    glb_output_name = f"/tmp/output_{job_id}.glb"
    b64to(glb_input_b64, glb_input_name);

    subprocess.run(["/bin/bash", "process", glb_input_name, glb_output_name], stdout=sys.stdout, stderr=sys.stderr);
#    os.system(f"./process {glb_input_name} {glb_output_name}")

    return glb_output_name


