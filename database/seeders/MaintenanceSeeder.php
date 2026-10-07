<?php

namespace Database\Seeders;

use App\Models\Maintenance;
use Illuminate\Database\Seeder;

class MaintenanceSeeder extends Seeder
{
    public function run(): void
    {
        Maintenance::create(['alat_id' => 2, 'tanggal' => '2023-10-05', 'jenis_maintenance' => 'Preventive', 'deskripsi' => 'Ganti oli dan filter', 'biaya' => 5000000.00, 'status' => 'Selesai', 'tanggal_selesai' => '2023-10-06']);
        Maintenance::create(['alat_id' => 1, 'tanggal' => '2023-10-10', 'jenis_maintenance' => 'Corrective', 'deskripsi' => 'Perbaikan sistem hidrolik', 'biaya' => 15000000.00, 'status' => 'Sedang Proses', 'tanggal_selesai' => null]);
        Maintenance::create(['alat_id' => 3, 'tanggal' => '2023-10-15', 'jenis_maintenance' => 'Preventive', 'deskripsi' => 'Inspeksi undercarriage', 'biaya' => 2000000.00, 'status' => 'Direncanakan', 'tanggal_selesai' => null]);
    }
}
