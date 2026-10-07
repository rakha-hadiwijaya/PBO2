<?php

namespace Database\Seeders;

use App\Models\Alat;
use Illuminate\Database\Seeder;

class AlatSeeder extends Seeder
{
    public function run(): void
    {
        Alat::create(['kode_alat' => 'EXC-01', 'nama_alat' => 'Excavator PC200', 'jenis_alat' => 'Excavator', 'merk' => 'Komatsu', 'tahun' => 2018, 'site_id' => 1, 'kondisi' => 'Baik', 'status_operasional' => 'Beroperasi']);
        Alat::create(['kode_alat' => 'DT-05', 'nama_alat' => 'Dump Truck HD465', 'jenis_alat' => 'Dump Truck', 'merk' => 'Komatsu', 'tahun' => 2019, 'site_id' => 1, 'kondisi' => 'Rusak Ringan', 'status_operasional' => 'Maintenance']);
        Alat::create(['kode_alat' => 'DZ-02', 'nama_alat' => 'Dozer D85ESS', 'jenis_alat' => 'Bulldozer', 'merk' => 'Komatsu', 'tahun' => 2015, 'site_id' => 2, 'kondisi' => 'Baik', 'status_operasional' => 'Beroperasi']);
    }
}
