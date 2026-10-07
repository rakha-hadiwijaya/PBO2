<?php

namespace App\Models;

use Database\Factories\ProduksiFactory;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Produksi extends Model
{
    /** @use HasFactory<ProduksiFactory> */
    use HasFactory;

    protected $guarded = [];
}
