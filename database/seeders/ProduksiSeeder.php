<?php

namespace Database\Seeders;

use App\Models\Produksi;
use Illuminate\Database\Seeder;

class ProduksiSeeder extends Seeder
{
    public function run(): void
    {
        Produksi::create(['site_id' => 1, 'tanggal' => '2023-10-01', 'jenis_material' => 'Batubara', 'target_produksi' => 1000.00, 'realisasi_produksi' => 950.50, 'satuan' => 'Ton', 'keterangan' => 'Produksi harian shift 1']);
        Produksi::create(['site_id' => 2, 'tanggal' => '2023-10-01', 'jenis_material' => 'Overburden', 'target_produksi' => 5000.00, 'realisasi_produksi' => 5200.00, 'satuan' => 'BCM', 'keterangan' => 'Pengupasan tanah']);
        Produksi::create(['site_id' => 1, 'tanggal' => '2023-10-02', 'jenis_material' => 'Batubara', 'target_produksi' => 1000.00, 'realisasi_produksi' => 1050.00, 'satuan' => 'Ton', 'keterangan' => 'Produksi harian shift 1']);
    }
}
