<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    public function run(): void
    {
        User::create([
            'name' => 'Admin System',
            'email' => 'admin@company.com',
            'password' => Hash::make('password'),
            'role' => 'admin',
        ]);
        User::create([
            'name' => 'Manager HR',
            'email' => 'manager1@company.com',
            'password' => Hash::make('password'),
            'role' => 'manager',
        ]);
        User::create([
            'name' => 'Manager Ops',
            'email' => 'manager2@company.com',
            'password' => Hash::make('password'),
            'role' => 'manager',
        ]);
    }
}
