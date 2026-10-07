<?php

namespace App\Models;

use Database\Factories\AlatFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Alat extends Model
{
    /** @use HasFactory<AlatFactory> */
    use HasFactory;

    protected $guarded = [];
}
