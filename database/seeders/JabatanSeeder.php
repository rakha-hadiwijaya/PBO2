<?php

namespace Database\Seeders;

use App\Models\Jabatan;
use Illuminate\Database\Seeder;

class JabatanSeeder extends Seeder
{
    public function run(): void
    {
        Jabatan::create(['nama_jabatan' => 'Manager', 'level' => 1, 'deskripsi' => 'Department Manager']);
        Jabatan::create(['nama_jabatan' => 'Supervisor', 'level' => 2, 'deskripsi' => 'Site Supervisor']);
        Jabatan::create(['nama_jabatan' => 'Operator', 'level' => 3, 'deskripsi' => 'Heavy Equipment Operator']);
    }
}
