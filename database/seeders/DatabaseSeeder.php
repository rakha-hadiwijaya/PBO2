<?php

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
}
