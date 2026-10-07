<?php

namespace Database\Seeders;

use App\Models\Site;
use Illuminate\Database\Seeder;

class SiteSeeder extends Seeder
{
    public function run(): void
    {
        Site::create(['kode_site' => 'ST001', 'nama_site' => 'Site Alpha', 'lokasi' => 'North Zone', 'kabupaten' => 'Kutai Kartanegara', 'status' => 'Aktif', 'deskripsi' => 'Main mining site']);
        Site::create(['kode_site' => 'ST002', 'nama_site' => 'Site Beta', 'lokasi' => 'South Zone', 'kabupaten' => 'Kutai Timur', 'status' => 'Aktif', 'deskripsi' => 'Secondary mining site']);
        Site::create(['kode_site' => 'ST003', 'nama_site' => 'Site Gamma', 'lokasi' => 'East Zone', 'kabupaten' => 'Berau', 'status' => 'Nonaktif', 'deskripsi' => 'Exploration site']);
    }
}
