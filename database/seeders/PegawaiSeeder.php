<?php

namespace Database\Seeders;

use App\Models\Pegawai;
use Illuminate\Database\Seeder;

class PegawaiSeeder extends Seeder
{
    public function run(): void
    {
        Pegawai::create(['nik' => 'EMP001', 'nama' => 'Budi Santoso', 'jenis_kelamin' => 'Laki-laki', 'tanggal_lahir' => '1985-05-15', 'alamat' => 'Jl. Merdeka No. 10', 'no_hp' => '081234567890', 'status_kepegawaian' => 'Tetap', 'tanggal_masuk' => '2010-01-10', 'departemen_id' => 1, 'jabatan_id' => 1, 'site_id' => 1, 'status' => 'Aktif']);
        Pegawai::create(['nik' => 'EMP002', 'nama' => 'Siti Aminah', 'jenis_kelamin' => 'Perempuan', 'tanggal_lahir' => '1990-08-20', 'alamat' => 'Jl. Sudirman No. 25', 'no_hp' => '082345678901', 'status_kepegawaian' => 'Kontrak', 'tanggal_masuk' => '2015-06-01', 'departemen_id' => 2, 'jabatan_id' => 2, 'site_id' => 2, 'status' => 'Aktif']);
        Pegawai::create(['nik' => 'EMP003', 'nama' => 'Andi Darmawan', 'jenis_kelamin' => 'Laki-laki', 'tanggal_lahir' => '1995-12-05', 'alamat' => 'Jl. Gatot Subroto No. 5', 'no_hp' => '083456789012', 'status_kepegawaian' => 'Outsourcing', 'tanggal_masuk' => '2020-03-15', 'departemen_id' => 3, 'jabatan_id' => 3, 'site_id' => 1, 'status' => 'Aktif']);
    }
}
