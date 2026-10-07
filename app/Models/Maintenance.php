<?php

namespace App\Models;

use Database\Factories\MaintenanceFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Maintenance extends Model
{
    /** @use HasFactory<MaintenanceFactory> */
    use HasFactory;

    protected $guarded = [];
}
