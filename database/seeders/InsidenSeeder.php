<?php

namespace Database\Seeders;

use App\Models\Insiden;
use Illuminate\Database\Seeder;

class InsidenSeeder extends Seeder
{
    public function run(): void
    {
        Insiden::create(['site_id' => 1, 'pegawai_id' => 3, 'tanggal' => '2023-09-10', 'jenis_insiden' => 'Near Miss', 'tingkat_keparahan' => 'Ringan', 'deskripsi' => 'Tergelincir di area tambang', 'tindakan' => 'Pemasangan rambu peringatan', 'status' => 'Selesai']);
        Insiden::create(['site_id' => 2, 'pegawai_id' => 2, 'tanggal' => '2023-09-20', 'jenis_insiden' => 'Kerusakan Alat', 'tingkat_keparahan' => 'Sedang', 'deskripsi' => 'Ban dump truck pecah', 'tindakan' => 'Penggantian ban dan pengecekan jalan', 'status' => 'Selesai']);
        Insiden::create(['site_id' => 1, 'pegawai_id' => 1, 'tanggal' => '2023-10-05', 'jenis_insiden' => 'Kecelakaan Kerja', 'tingkat_keparahan' => 'Ringan', 'deskripsi' => 'Terjepit pintu kabin', 'tindakan' => 'Perawatan medis ringan dan briefing K3', 'status' => 'Investigasi']);
    }
}
