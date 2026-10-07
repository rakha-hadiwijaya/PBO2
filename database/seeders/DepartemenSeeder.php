<?php

namespace Database\Seeders;

use App\Models\Departemen;
use Illuminate\Database\Seeder;

class DepartemenSeeder extends Seeder
{
    public function run(): void
    {
        Departemen::create(['nama_departemen' => 'Human Resources', 'deskripsi' => 'HR Department']);
        Departemen::create(['nama_departemen' => 'Operations', 'deskripsi' => 'Mining Operations']);
        Departemen::create(['nama_departemen' => 'Maintenance', 'deskripsi' => 'Equipment Maintenance']);
    }
}
