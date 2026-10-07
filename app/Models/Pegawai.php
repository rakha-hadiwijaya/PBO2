<?php

namespace App\Models;

use Database\Factories\PegawaiFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Pegawai extends Model
{
    /** @use HasFactory<PegawaiFactory> */
    use HasFactory;

    protected $guarded = [];
}
