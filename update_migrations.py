import os
import re

base_path = r"c:\Kuliah\Semester 5\tugas\PBO 2\pbo2-tugas\database\migrations"

migrations = {
    "departemens": """            $table->id();
            $table->string('nama_departemen');
            $table->text('deskripsi')->nullable();
            $table->timestamps();""",
    "jabatans": """            $table->id();
            $table->string('nama_jabatan');
            $table->integer('level')->nullable();
            $table->text('deskripsi')->nullable();
            $table->timestamps();""",
    "sites": """            $table->id();
            $table->string('kode_site')->unique();
            $table->string('nama_site');
            $table->string('lokasi');
            $table->string('kabupaten')->nullable();
            $table->enum('status', ['Aktif', 'Nonaktif'])->default('Aktif');
            $table->text('deskripsi')->nullable();
            $table->timestamps();""",
    "pegawais": """            $table->id();
            $table->string('nik')->unique();
            $table->string('nama');
            $table->enum('jenis_kelamin', ['Laki-laki', 'Perempuan']);
            $table->date('tanggal_lahir');
            $table->text('alamat')->nullable();
            $table->string('no_hp')->nullable();
            $table->enum('status_kepegawaian', ['Tetap', 'Kontrak', 'Outsourcing']);
            $table->date('tanggal_masuk');
            $table->foreignId('departemen_id')->constrained()->cascadeOnDelete();
            $table->foreignId('jabatan_id')->constrained()->cascadeOnDelete();
            $table->foreignId('site_id')->constrained()->cascadeOnDelete();
            $table->enum('status', ['Aktif', 'Nonaktif'])->default('Aktif');
            $table->timestamps();""",
    "produksis": """            $table->id();
            $table->foreignId('site_id')->constrained()->cascadeOnDelete();
            $table->date('tanggal');
            $table->string('jenis_material');
            $table->decimal('target_produksi', 10, 2);
            $table->decimal('realisasi_produksi', 10, 2);
            $table->string('satuan');
            $table->text('keterangan')->nullable();
            $table->timestamps();""",
    "alats": """            $table->id();
            $table->string('kode_alat')->unique();
            $table->string('nama_alat');
            $table->string('jenis_alat');
            $table->string('merk')->nullable();
            $table->integer('tahun')->nullable();
            $table->foreignId('site_id')->constrained()->cascadeOnDelete();
            $table->enum('kondisi', ['Baik', 'Rusak Ringan', 'Rusak Berat']);
            $table->enum('status_operasional', ['Beroperasi', 'Maintenance', 'Tidak Aktif']);
            $table->timestamps();""",
    "maintenances": """            $table->id();
            $table->foreignId('alat_id')->constrained()->cascadeOnDelete();
            $table->date('tanggal');
            $table->string('jenis_maintenance');
            $table->text('deskripsi')->nullable();
            $table->decimal('biaya', 15, 2)->nullable();
            $table->enum('status', ['Direncanakan', 'Sedang Proses', 'Selesai']);
            $table->date('tanggal_selesai')->nullable();
            $table->timestamps();""",
    "insidens": """            $table->id();
            $table->foreignId('site_id')->constrained()->cascadeOnDelete();
            $table->foreignId('pegawai_id')->nullable()->constrained()->nullOnDelete();
            $table->date('tanggal');
            $table->enum('jenis_insiden', ['Near Miss', 'Kecelakaan Kerja', 'Kerusakan Alat']);
            $table->enum('tingkat_keparahan', ['Ringan', 'Sedang', 'Berat', 'Fatal']);
            $table->text('deskripsi')->nullable();
            $table->text('tindakan')->nullable();
            $table->enum('status', ['Terbuka', 'Investigasi', 'Selesai']);
            $table->timestamps();"""
}

for filename in os.listdir(base_path):
    for key, replacement in migrations.items():
        if key in filename and filename.endswith(".php"):
            filepath = os.path.join(base_path, filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            pattern = r"\$table->id\(\);\n\s*\$table->timestamps\(\);"
            new_content = re.sub(pattern, replacement, content)
            
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filename}")
