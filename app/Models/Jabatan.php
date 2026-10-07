<?php

namespace App\Models;

use Database\Factories\JabatanFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Jabatan extends Model
{
    /** @use HasFactory<JabatanFactory> */
    use HasFactory;

    protected $guarded = [];
}
