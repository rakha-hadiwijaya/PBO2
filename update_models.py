import os
import re

base_path = r"c:\Kuliah\Semester 5\tugas\PBO 2\pbo2-tugas\app\Models"

models = ["Departemen", "Jabatan", "Site", "Pegawai", "Produksi", "Alat", "Maintenance", "Insiden", "User"]

for filename in os.listdir(base_path):
    name = filename.replace(".php", "")
    if name in models:
        filepath = os.path.join(base_path, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        if name == "User":
            # For user, it already has fillable. We just need to add 'role' to fillable.
            if "'role'" not in content:
                content = content.replace("'password',", "'password',\n        'role',")
        else:
            # Add protected $guarded = [];
            pattern = r"use HasFactory;"
            replacement = "use HasFactory;\n\n    protected $guarded = [];"
            if "protected $guarded" not in content:
                content = re.sub(pattern, replacement, content)
        
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filename}")
