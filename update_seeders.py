import os
import re

base_path = r"c:\Kuliah\Semester 5\tugas\PBO 2\pbo2-tugas\database\seeders"

seeders = {
    "UserSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\User;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    public function run(): void
    {
        User::create([
            'name' => 'Admin System',
            'email' => 'admin@company.com',
            'password' => Hash::make('password'),
            'role' => 'admin'
        ]);
        User::create([
            'name' => 'Manager HR',
            'email' => 'manager1@company.com',
            'password' => Hash::make('password'),
            'role' => 'manager'
        ]);
        User::create([
            'name' => 'Manager Ops',
            'email' => 'manager2@company.com',
            'password' => Hash::make('password'),
            'role' => 'manager'
        ]);
    }
}""",
    "DepartemenSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Departemen;

class DepartemenSeeder extends Seeder
{
    public function run(): void
    {
        Departemen::create(['nama_departemen' => 'Human Resources', 'deskripsi' => 'HR Department']);
        Departemen::create(['nama_departemen' => 'Operations', 'deskripsi' => 'Mining Operations']);
        Departemen::create(['nama_departemen' => 'Maintenance', 'deskripsi' => 'Equipment Maintenance']);
    }
}""",
    "JabatanSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Jabatan;

class JabatanSeeder extends Seeder
{
    public function run(): void
    {
        Jabatan::create(['nama_jabatan' => 'Manager', 'level' => 1, 'deskripsi' => 'Department Manager']);
        Jabatan::create(['nama_jabatan' => 'Supervisor', 'level' => 2, 'deskripsi' => 'Site Supervisor']);
        Jabatan::create(['nama_jabatan' => 'Operator', 'level' => 3, 'deskripsi' => 'Heavy Equipment Operator']);
    }
}""",
    "SiteSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Site;

class SiteSeeder extends Seeder
{
    public function run(): void
    {
        Site::create(['kode_site' => 'ST001', 'nama_site' => 'Site Alpha', 'lokasi' => 'North Zone', 'kabupaten' => 'Kutai Kartanegara', 'status' => 'Aktif', 'deskripsi' => 'Main mining site']);
        Site::create(['kode_site' => 'ST002', 'nama_site' => 'Site Beta', 'lokasi' => 'South Zone', 'kabupaten' => 'Kutai Timur', 'status' => 'Aktif', 'deskripsi' => 'Secondary mining site']);
        Site::create(['kode_site' => 'ST003', 'nama_site' => 'Site Gamma', 'lokasi' => 'East Zone', 'kabupaten' => 'Berau', 'status' => 'Nonaktif', 'deskripsi' => 'Exploration site']);
    }
}""",
    "PegawaiSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Pegawai;

class PegawaiSeeder extends Seeder
{
    public function run(): void
    {
        Pegawai::create(['nik' => 'EMP001', 'nama' => 'Budi Santoso', 'jenis_kelamin' => 'Laki-laki', 'tanggal_lahir' => '1985-05-15', 'alamat' => 'Jl. Merdeka No. 10', 'no_hp' => '081234567890', 'status_kepegawaian' => 'Tetap', 'tanggal_masuk' => '2010-01-10', 'departemen_id' => 1, 'jabatan_id' => 1, 'site_id' => 1, 'status' => 'Aktif']);
        Pegawai::create(['nik' => 'EMP002', 'nama' => 'Siti Aminah', 'jenis_kelamin' => 'Perempuan', 'tanggal_lahir' => '1990-08-20', 'alamat' => 'Jl. Sudirman No. 25', 'no_hp' => '082345678901', 'status_kepegawaian' => 'Kontrak', 'tanggal_masuk' => '2015-06-01', 'departemen_id' => 2, 'jabatan_id' => 2, 'site_id' => 2, 'status' => 'Aktif']);
        Pegawai::create(['nik' => 'EMP003', 'nama' => 'Andi Darmawan', 'jenis_kelamin' => 'Laki-laki', 'tanggal_lahir' => '1995-12-05', 'alamat' => 'Jl. Gatot Subroto No. 5', 'no_hp' => '083456789012', 'status_kepegawaian' => 'Outsourcing', 'tanggal_masuk' => '2020-03-15', 'departemen_id' => 3, 'jabatan_id' => 3, 'site_id' => 1, 'status' => 'Aktif']);
    }
}""",
    "ProduksiSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Produksi;

class ProduksiSeeder extends Seeder
{
    public function run(): void
    {
        Produksi::create(['site_id' => 1, 'tanggal' => '2023-10-01', 'jenis_material' => 'Batubara', 'target_produksi' => 1000.00, 'realisasi_produksi' => 950.50, 'satuan' => 'Ton', 'keterangan' => 'Produksi harian shift 1']);
        Produksi::create(['site_id' => 2, 'tanggal' => '2023-10-01', 'jenis_material' => 'Overburden', 'target_produksi' => 5000.00, 'realisasi_produksi' => 5200.00, 'satuan' => 'BCM', 'keterangan' => 'Pengupasan tanah']);
        Produksi::create(['site_id' => 1, 'tanggal' => '2023-10-02', 'jenis_material' => 'Batubara', 'target_produksi' => 1000.00, 'realisasi_produksi' => 1050.00, 'satuan' => 'Ton', 'keterangan' => 'Produksi harian shift 1']);
    }
}""",
    "AlatSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Alat;

class AlatSeeder extends Seeder
{
    public function run(): void
    {
        Alat::create(['kode_alat' => 'EXC-01', 'nama_alat' => 'Excavator PC200', 'jenis_alat' => 'Excavator', 'merk' => 'Komatsu', 'tahun' => 2018, 'site_id' => 1, 'kondisi' => 'Baik', 'status_operasional' => 'Beroperasi']);
        Alat::create(['kode_alat' => 'DT-05', 'nama_alat' => 'Dump Truck HD465', 'jenis_alat' => 'Dump Truck', 'merk' => 'Komatsu', 'tahun' => 2019, 'site_id' => 1, 'kondisi' => 'Rusak Ringan', 'status_operasional' => 'Maintenance']);
        Alat::create(['kode_alat' => 'DZ-02', 'nama_alat' => 'Dozer D85ESS', 'jenis_alat' => 'Bulldozer', 'merk' => 'Komatsu', 'tahun' => 2015, 'site_id' => 2, 'kondisi' => 'Baik', 'status_operasional' => 'Beroperasi']);
    }
}""",
    "MaintenanceSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Maintenance;

class MaintenanceSeeder extends Seeder
{
    public function run(): void
    {
        Maintenance::create(['alat_id' => 2, 'tanggal' => '2023-10-05', 'jenis_maintenance' => 'Preventive', 'deskripsi' => 'Ganti oli dan filter', 'biaya' => 5000000.00, 'status' => 'Selesai', 'tanggal_selesai' => '2023-10-06']);
        Maintenance::create(['alat_id' => 1, 'tanggal' => '2023-10-10', 'jenis_maintenance' => 'Corrective', 'deskripsi' => 'Perbaikan sistem hidrolik', 'biaya' => 15000000.00, 'status' => 'Sedang Proses', 'tanggal_selesai' => null]);
        Maintenance::create(['alat_id' => 3, 'tanggal' => '2023-10-15', 'jenis_maintenance' => 'Preventive', 'deskripsi' => 'Inspeksi undercarriage', 'biaya' => 2000000.00, 'status' => 'Direncanakan', 'tanggal_selesai' => null]);
    }
}""",
    "InsidenSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Insiden;

class InsidenSeeder extends Seeder
{
    public function run(): void
    {
        Insiden::create(['site_id' => 1, 'pegawai_id' => 3, 'tanggal' => '2023-09-10', 'jenis_insiden' => 'Near Miss', 'tingkat_keparahan' => 'Ringan', 'deskripsi' => 'Tergelincir di area tambang', 'tindakan' => 'Pemasangan rambu peringatan', 'status' => 'Selesai']);
        Insiden::create(['site_id' => 2, 'pegawai_id' => 2, 'tanggal' => '2023-09-20', 'jenis_insiden' => 'Kerusakan Alat', 'tingkat_keparahan' => 'Sedang', 'deskripsi' => 'Ban dump truck pecah', 'tindakan' => 'Penggantian ban dan pengecekan jalan', 'status' => 'Selesai']);
        Insiden::create(['site_id' => 1, 'pegawai_id' => 1, 'tanggal' => '2023-10-05', 'jenis_insiden' => 'Kecelakaan Kerja', 'tingkat_keparahan' => 'Ringan', 'deskripsi' => 'Terjepit pintu kabin', 'tindakan' => 'Perawatan medis ringan dan briefing K3', 'status' => 'Investigasi']);
    }
}""",
    "DatabaseSeeder.php": r"""<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        $this->call([
            UserSeeder::class,
            DepartemenSeeder::class,
            JabatanSeeder::class,
            SiteSeeder::class,
            PegawaiSeeder::class,
            ProduksiSeeder::class,
            AlatSeeder::class,
            MaintenanceSeeder::class,
            InsidenSeeder::class,
        ]);
    }
}"""
}

for filename, content in seeders.items():
    filepath = os.path.join(base_path, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated {filename}")
